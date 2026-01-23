def prediction(stock, n_days, theme):
    import yfinance as yf
    import pandas as pd
    import numpy as np
    import plotly.graph_objs as go
    from sklearn.model_selection import train_test_split, GridSearchCV
    from sklearn.svm import SVR
    from datetime import date, timedelta

    df = yf.download(stock, period="60d")

    if df.empty:
        raise Exception("No data")

    df.reset_index(inplace=True)
    df["Day"] = np.arange(len(df))

    X = df[["Day"]].values
    y = df["Close"].values

    x_train, x_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, shuffle=False
    )

    gsc = GridSearchCV(
        SVR(kernel="rbf"),
        param_grid={
            "C": [0.1, 1, 10, 100],
            "epsilon": [0.001, 0.01, 0.1],
            "gamma": [0.001, 0.01, 0.1, 1],
        },
        cv=5,
        scoring="neg_mean_absolute_error",
        n_jobs=-1,
    )

    gsc.fit(x_train, y_train)
    best = gsc.best_params_

    model = SVR(
        kernel="rbf",
        C=best["C"],
        epsilon=best["epsilon"],
        gamma=best["gamma"],
    )

    model.fit(x_train, y_train)

    last_day = X[-1][0]
    future_days = np.array([[last_day + i] for i in range(1, n_days)])

    future_prices = model.predict(future_days)

    future_dates = []
    current = date.today()
    for _ in range(len(future_prices)):
        current += timedelta(days=1)
        future_dates.append(current)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=future_dates,
            y=future_prices,
            mode="lines+markers",
            name="Forecast",
        )
    )

    fig.update_layout(
        title=f"Predicted Close Price for Next {n_days - 1} Days",
        template="plotly_dark" if theme == "dark" else "plotly_white",
        height=500,
        xaxis_title="Date",
        yaxis_title="Close Price",
        margin=dict(l=40, r=60, t=50, b=40),
        modebar={
            "bgcolor": "rgba(0,0,0,0)",
            "color": "#198754" if theme == "light" else "#c3ff00",
            "orientation": "h",
        },
    )

    return fig
