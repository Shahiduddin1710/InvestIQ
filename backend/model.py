import yfinance as yf
import pandas as pd
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_percentage_error
from functools import lru_cache
import hashlib

_model_cache = {}  # { ticker: (model, scaler_X, scaler_y, df, feature_cols) }


def _add_features(df: pd.DataFrame) -> pd.DataFrame:
    close = df["Close"]

    # Lag features
    for lag in [1, 2, 3, 5, 10, 21]:
        df[f"Lag_{lag}"] = close.shift(lag)

    # Rolling stats
    for w in [5, 10, 21, 50]:
        df[f"RollingMean_{w}"] = close.rolling(w).mean()
        df[f"RollingStd_{w}"]  = close.rolling(w).std()

    # Momentum
    df["Momentum_5"]  = close - close.shift(5)
    df["Momentum_21"] = close - close.shift(21)

    # RSI (14)
    delta = close.diff()
    gain  = delta.clip(lower=0).rolling(14).mean()
    loss  = (-delta.clip(upper=0)).rolling(14).mean()
    rs    = gain / (loss + 1e-9)
    df["RSI_14"] = 100 - (100 / (1 + rs))

    # MACD
    ema12 = close.ewm(span=12).mean()
    ema26 = close.ewm(span=26).mean()
    df["MACD"]        = ema12 - ema26
    df["MACD_Signal"] = df["MACD"].ewm(span=9).mean()

    # Bollinger Band width
    rm20 = close.rolling(20).mean()
    rs20 = close.rolling(20).std()
    df["BB_Width"] = (2 * rs20) / (rm20 + 1e-9)

    # Volume features
    if "Volume" in df.columns:
        df["Vol_Change"]     = df["Volume"].pct_change()
        df["Vol_Rolling5"]   = df["Volume"].rolling(5).mean()

    # Day of week / month (cyclical)
    df["DayOfWeek"] = df.index.dayofweek
    df["Month"]     = df.index.month

    # % returns
    df["Return_1d"] = close.pct_change(1)
    df["Return_5d"] = close.pct_change(5)

    return df


def prediction(stock: str, n_days: int, theme: str) -> dict:
    global _model_cache

    if stock not in _model_cache:
        print(f"[Model] Downloading data for {stock}...")
        df = yf.download(stock, period="5y", auto_adjust=True, progress=False, multi_level_index=False)

        if df.empty:
            raise ValueError(f"No data found for ticker: {stock}")

        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        df = df[["Close", "Volume"]].copy()
        df = _add_features(df)
        df.dropna(inplace=True)

        feature_cols = [c for c in df.columns if c != "Close"]
        X = df[feature_cols].values.astype(float)
        y = df["Close"].values.astype(float)

        scaler_X = MinMaxScaler()
        scaler_y = MinMaxScaler()
        X_scaled = scaler_X.fit_transform(X)
        y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).ravel()

        split = int(len(X_scaled) * 0.9)
        X_train, X_test = X_scaled[:split], X_scaled[split:]
        y_train, y_test = y_scaled[:split], y_scaled[split:]

        print(f"[Model] Training GradientBoosting on {len(X_train)} samples...")
        model = GradientBoostingRegressor(
            n_estimators=150,
            learning_rate=0.05,
            max_depth=3,
            subsample=0.8,
            min_samples_leaf=5,
            random_state=42
        )
        model.fit(X_train, y_train)

        _model_cache[stock] = (model, scaler_X, scaler_y, df, feature_cols, X_test, y_test)
        print(f"[Model] Cached model for {stock}")
    else:
        print(f"[Model] Using cached model for {stock}")

    model, scaler_X, scaler_y, df, feature_cols, X_test, y_test = _model_cache[stock]

    # MAPE on test set
    y_pred_test = scaler_y.inverse_transform(
        model.predict(X_test).reshape(-1, 1)
    ).ravel()
    y_true_test = scaler_y.inverse_transform(
        y_test.reshape(-1, 1)
    ).ravel()
    mape = mean_absolute_percentage_error(y_true_test, y_pred_test) * 100
    print(f"[Model] Test MAPE: {mape:.2f}%")

  # Forecast — recompute features fresh each step
    future_prices = []
    df_sim = df[["Close", "Volume"]].copy()

    for i in range(n_days):
        df_feat = _add_features(df_sim.copy())
        df_feat.dropna(inplace=True)

        if df_feat.empty:
            break

        last_row = df_feat[feature_cols].iloc[-1].values.astype(float)
        row_scaled = scaler_X.transform(last_row.reshape(1, -1))
        pred_scaled = model.predict(row_scaled)
        pred = float(scaler_y.inverse_transform(pred_scaled.reshape(-1, 1))[0][0])
        future_prices.append(pred)

        # Append predicted close as next row
        next_date = df_sim.index[-1] + pd.Timedelta(days=1)
        last_volume = float(df_sim["Volume"].iloc[-1])
        new_row = pd.DataFrame(
            {"Close": [pred], "Volume": [last_volume]},
            index=[next_date]
        )
        df_sim = pd.concat([df_sim, new_row])
    last_date    = df.index[-1]
    future_dates = pd.bdate_range(
        start=last_date + pd.Timedelta(days=1),
        periods=n_days
    )

    template     = "plotly_dark"  if theme == "dark"  else "plotly_white"
    accent_color = "#c3ff00"      if theme == "dark"  else "#198754"

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=future_dates.strftime("%Y-%m-%d").tolist(),
        y=future_prices,
        mode="lines+markers",
        name=f"Forecast (MAPE: {mape:.1f}%)",
        line=dict(color=accent_color, width=2),
        marker=dict(size=6)
    ))

    fig.update_layout(
        title=f"{stock} — {n_days}-Day Forecast (Test MAPE: {mape:.1f}%)",
        template=template,
        height=500,
        xaxis_title="Date",
        yaxis_title="Close Price",
        xaxis=dict(rangeslider=dict(visible=False)),
        margin=dict(l=40, r=40, t=50, b=40),
        modebar={"bgcolor": "rgba(0,0,0,0)", "color": accent_color},
        hovermode="x unified"
    )

    print(f"[Model] Forecast complete for {stock}")
    return fig.to_dict()