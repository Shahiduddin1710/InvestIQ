from fastapi import APIRouter, HTTPException, Query
import yfinance as yf
import plotly.graph_objs as go
import traceback
from schemas import ForecastRequest
from model import prediction

router = APIRouter(prefix="/stock", tags=["stock"])


def _theme_colors(theme: str):
    return (
        "plotly_dark" if theme == "dark" else "plotly_white",
        "#c3ff00" if theme == "dark" else "#198754"
    )


@router.get("/info/{ticker}")
async def get_ticker_info(ticker: str):
    try:
        t = yf.Ticker(ticker.upper())
        info = t.info or {}
        return {
            "name": info.get("shortName", ticker.upper()),
            "description": info.get("longBusinessSummary", "No description available.")
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/price")
async def get_stock_price(
    ticker: str = Query(...),
    start_date: str = Query(...),
    end_date: str = Query(...),
    theme: str = Query("dark")
):
    try:
        df = yf.download(ticker.upper(), start=start_date, end=end_date, auto_adjust=False)
        if df.empty:
            raise HTTPException(status_code=404, detail="No data found")

        df.reset_index(inplace=True)
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]

        template, accent = _theme_colors(theme)

        fig = go.Figure(data=[go.Candlestick(
            x=df["Date"].astype(str).tolist(),
            open=df["Open"].tolist(),
            high=df["High"].tolist(),
            low=df["Low"].tolist(),
            close=df["Close"].tolist(),
            name="Price"
        )])

        fig.update_layout(
            title="Closing and Opening Price vs Date",
            height=500,
            template=template,
            margin=dict(l=40, r=40, t=50, b=40),
            modebar={"bgcolor": "rgba(0,0,0,0)", "color": accent},
            hovermode="x unified",
            xaxis=dict(rangeslider=dict(visible=False))
        )

        return {"figure": fig.to_dict()}
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/indicators")
async def get_indicators(
    ticker: str = Query(...),
    start_date: str = Query(...),
    end_date: str = Query(...),
    theme: str = Query("dark")
):
    try:
        df = yf.download(ticker.upper(), start=start_date, end=end_date, auto_adjust=False)
        if df.empty:
            raise HTTPException(status_code=404, detail="No data found")

        df.reset_index(inplace=True)
        df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
        df["EMA_20"] = df["Close"].ewm(span=20).mean()

        template, accent = _theme_colors(theme)

        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=df["Date"].astype(str).tolist(),
            open=df["Open"].tolist(),
            high=df["High"].tolist(),
            low=df["Low"].tolist(),
            close=df["Close"].tolist(),
            name="Price",
            increasing=dict(line=dict(color="#00ff9c")),
            decreasing=dict(line=dict(color="#ff4d4d"))
        ))
        fig.add_trace(go.Scatter(
            x=df["Date"].astype(str).tolist(),
            y=df["EMA_20"].tolist(),
            mode="lines",
            name="EMA 20",
            line=dict(color=accent, width=2)
        ))

        fig.update_layout(
            title="Exponential Moving Average vs Date",
            height=500,
            template=template,
            margin=dict(l=40, r=40, t=50, b=40),
            modebar={"bgcolor": "rgba(0,0,0,0)", "color": accent},
            hovermode="x unified",
            xaxis=dict(rangeslider=dict(visible=False))
        )

        return {"figure": fig.to_dict()}
    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/forecast")
async def get_forecast(req: ForecastRequest):
    try:
        if req.n_days <= 0:
            raise HTTPException(status_code=400, detail="n_days must be positive")
        if req.n_days > 365:
            raise HTTPException(status_code=400, detail="Max 365 days allowed")

        print(f"[Forecast] Starting: ticker={req.ticker}, days={req.n_days}, theme={req.theme}")
        fig_dict = prediction(req.ticker.upper(), req.n_days, req.theme)
        print(f"[Forecast] Completed: {req.ticker}")
        return {"figure": fig_dict}

    except HTTPException:
        raise
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
