import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from datetime import datetime as dt
import yfinance as yf
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import base64
import re
from dash import no_update
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from model import prediction


with open("Assets/line.gif", "rb") as f:
    image_data = f.read()

with open("Assets/cover.png", "rb") as l:
    image_dat = l.read()

with open("Assets/bb.png", "rb") as n:
    image_da = n.read()

with open("Assets/name.png", "rb") as t:
    image_d = t.read()

with open("Assets/shahid.png", "rb") as s:
    ima_d = s.read()

with open("Assets/design.png", "rb") as o:
    ima = o.read()

with open("Assets/aditya.png", "rb") as w:
    im = w.read()

with open("Assets/pranav.jpg", "rb") as y:
    i = y.read()

with open("Assets/cmd.png", "rb") as b:
    l = b.read()

with open("Assets/port.jpg", "rb") as h:
    q = h.read()

with open("Assets/education.jpg", "rb") as z:
    x = z.read()

with open("Assets/risk.jpg", "rb") as zz:
    xx = zz.read()

with open("Assets/eng.jpg", "rb") as zzz:
    ll = zzz.read()

with open("Assets/nn.jpg", "rb") as z1:
    ll1 = z1.read()

with open("Assets/bb.png", "rb") as k1:
    n1 = k1.read()

encoded_image = base64.b64encode(image_data).decode()
encoded_imagee = base64.b64encode(image_dat).decode()
encoded_imageee = base64.b64encode(image_da).decode()
encoded_imageeee = base64.b64encode(image_d).decode()
encoded_image1 = base64.b64encode(ima_d).decode()
encoded_image11 = base64.b64encode(ima).decode()
encoded_image111 = base64.b64encode(im).decode()
encoded_image12 = base64.b64encode(i).decode()
encoded_image22 = base64.b64encode(l).decode()
encoded_image222 = base64.b64encode(q).decode()
encoded_imagee222 = base64.b64encode(x).decode()
encoded_imagee22 = base64.b64encode(xx).decode()
e = base64.b64encode(ll).decode()
e1 = base64.b64encode(ll1).decode()
e2 = base64.b64encode(n1).decode()

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)


app.index_string = """
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            /* Initial page hide to prevent flash */
            #page-content { opacity: 0; }
            
            body {
                overflow-x: hidden;
                scroll-behavior: smooth;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
"""

server = app.server

github_icon_url = "https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png"
email_icon_url = (
    "https://upload.wikimedia.org/wikipedia/commons/7/7e/Gmail_icon_%282020%29.svg"
)



def load_img(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


logo_img = load_img("Assets/name.png")
right_img = load_img("Assets/line.gif")


navbar = dbc.Navbar(
    [
        html.Img(
            src=f"data:image/png;base64,{logo_img}",
            style={"height": "45px"},
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/"),
                dbc.NavLink("AI Predictor", href="/AI-Predictor"),
                dbc.NavLink("Top 50 Stocks", href="/top-50-stocks"),
                dbc.NavLink("Why InvestIQ?", href="/why-investiq"),
                dbc.NavLink("About", href="/about"),
                # 🔥 YAHAN ADD KAR
                dbc.Button(
                    "🌙 Dark / ☀️ Light",
                    id="theme-toggle",
                    n_clicks=0,
                    color="secondary",
                    outline=True,
                    size="sm",
                    className="ms-3",  # thoda gap ke liye
                ),
            ],
            className="ms-auto",
            navbar=True,
        ),
        html.Img(
            src=f"data:image/gif;base64,{right_img}",
            style={"height": "40px"},
        ),
    ],
    dark=True,
    color="primary",
    className="px-4",
)

def about_page():
    return html.Div(
        [

            html.Div(
                [

                    html.H1("About Us", className="about-title"),

                    
                    html.Div(
                        [
                            html.P(
                                "InvestIQ is a modern financial analytics platform designed to help users "
                                "understand, analyze, and explore stock market data with clarity and confidence. "
                                "The platform focuses on transforming complex market information into meaningful, "
                                "easy-to-understand insights through intelligent visualization and data-driven analysis."
                            )
                        ],
                        className="about-card",
                    ),

                    html.Div(
                        [
                            html.H2("What We Do"),
                            html.P(
                                "InvestIQ provides tools for stock trend analysis, historical price visualization, "
                                "technical indicators, and AI-based forecasting. By integrating real-time market data "
                                "with machine learning models, the platform enables users to explore patterns, "
                                "evaluate market behavior, and make informed analytical decisions."
                            ),
                        ],
                        className="about-card",
                    ),

                    html.Div(
                        [
                            html.H2("Our Approach"),
                            html.P(
                                "Our approach is centered around simplicity, accuracy, and performance. Each feature "
                                "is designed with a user-first mindset, ensuring that insights are accessible without "
                                "unnecessary complexity."
                            ),
                        ],
                        className="about-card",
                    ),

                    html.Div(
                        [
                            html.H2("Our Mission"),
                            html.P(
                                "Our mission is to make stock market analysis more accessible through intelligent "
                                "technology and thoughtful design."
                            ),
                        ],
                        className="about-card",
                    ),

                    html.Div(
                        [
                            html.H2("Get in Touch"),
                            html.P("Have questions, feedback, or ideas? We'd love to hear from you."),

                            dcc.Input(id="contact-name", placeholder="Your Name", className="contact-input"),
                            dcc.Input(id="contact-email", placeholder="Your Email", className="contact-input"),
                            dcc.Textarea(id="contact-message", placeholder="Your Message", className="contact-textarea"),
                            html.Button("Send Message", id="contact-submit", className="contact-button"),
                            html.Div(id="contact-status"),
                        ],
                        className="about-card",
                    ),

                ],
                className="about-bg-container"  
            )
        ]
    )



def why_investiq_page():
    return html.Div(
        [
            html.H1("Why InvestIQ?", className="why-investiq-header"),
            html.H6(
                "InvestIQ is a cutting-edge investment platform designed to empower investors with powerful tools and insights to make informed investment decisions. Here are some reasons why you should choose InvestIQ:"
            ),
            html.Ul(
                [
                    html.Li(
                        "Comprehensive Market Analysis: InvestIQ provides comprehensive market analysis tools, including real-time data, advanced charting, and customizable indicators, to help you analyze market trends and make informed decisions."
                    ),
                    html.Li(
                        "Portfolio Management: With InvestIQ, you can easily manage your investment portfolio, track performance, and diversify your holdings across various asset classes."
                    ),
                    html.Li(
                        "Educational Resources: InvestIQ offers a wealth of educational resources, including tutorials, articles, and webinars, to help you enhance your investment knowledge and skills."
                    ),
                    html.Li(
                        "Risk Management: InvestIQ helps you manage investment risk effectively with risk assessment tools, portfolio optimization strategies, and dynamic asset allocation."
                    ),
                    html.Li(
                        "Community Engagement: Join a vibrant community of investors on InvestIQ to share insights, discuss investment strategies, and collaborate with like-minded individuals."
                    ),
                ],
                className="why-investiq-list",
            ),
        ],
        className="why-investiq-container",
        style={
            "background-image": f"url(data:image/png;base64,{e1})",
            "opacity": "1",
            "transition": "opacity 0.5s ease-in-out",
        },
    )


def home_page():
    return html.Div(
        [
            html.H1("Welcome to InvestIQ", className="home-header"),
         
            html.Div(
                [
                    html.H2("Features", className="features-header"),
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.Img(
                                        src=f"data:image/png;base64,{encoded_image22}",
                                        style={"width": "150px", "height": "100px"},
                                    ),
                                    html.H5("Comprehensive Market Analysis"),
                                    html.P(
                                        "InvestIQ provides comprehensive market analysis tools, including real-time data, advanced charting, and customizable indicators, to help you analyze market trends and make informed decisions."
                                    ),
                                ],
                                className="feature-box",
                            ),
                            html.Div(
                                [
                                    html.Img(
                                        src=f"data:image/png;base64,{encoded_image222}",
                                        style={"width": "150px", "height": "100px"},
                                    ),
                                    html.H5("Portfolio Management"),
                                    html.P(
                                        "With InvestIQ, you can easily manage your investment portfolio, track performance, and diversify your holdings across various asset classes."
                                    ),
                                ],
                                className="feature-box",
                            ),
                            html.Div(
                                [
                                    html.Img(
                                        src=f"data:image/png;base64,{encoded_imagee222}",
                                        style={"width": "150px", "height": "100px"},
                                    ),
                                    html.H5("Educational Resources"),
                                    html.P(
                                        "InvestIQ offers a wealth of educational resources, including tutorials, articles, and webinars, to help you enhance your investment knowledge and skills."
                                    ),
                                ],
                                className="feature-box",
                            ),
                            html.Div(
                                [
                                    html.Img(
                                        src=f"data:image/png;base64,{encoded_imagee22}",
                                        style={"width": "150px", "height": "100px"},
                                    ),
                                    html.H5("Risk Management"),
                                    html.P(
                                        "InvestIQ helps you manage investment risk effectively with risk assessment tools, portfolio optimization strategies, and dynamic asset allocation."
                                    ),
                                ],
                                className="feature-box",
                            ),
                            html.Div(
                                [
                                    html.Img(
                                        src=f"data:image/png;base64,{e}",
                                        style={"width": "150px", "height": "100px"},
                                    ),
                                    html.H5("Community Engagement"),
                                    html.P(
                                        "Join a vibrant community of investors on InvestIQ to share insights, discuss investment strategies, and collaborate with like-minded individuals."
                                    ),
                                ],
                                className="feature-box",
                            ),
                        ],
                        className="feature-container",
                    ),
                ],
                className="home-features",
            ),
            html.Div(
                [
                    html.H2("How to Use InvestIQ", className="how-to-use-header"),
                    html.Div(
                        [
                            html.P(
                                "1. Navigate to the 'Top 50 Stocks' page to view a list of the top 50 stocks in the market."
                            ),
                            html.P(
                                "2. Select any stock name to view detailed information and analysis for that stock."
                            ),
                            html.P(
                                "3. Visit the 'AI Predictor' page to predict future stock prices using advanced machine learning algorithms."
                            ),
                            html.P(
                                "4. Explore the 'Why InvestIQ?' page to learn about the features and benefits of using InvestIQ for your investment needs."
                            ),
                            html.P(
                                "5. Get to know more about us on the 'About Us' page, where you can learn about our team and mission."
                            ),
                        ],
                        className="how-to-use-steps",
                    ),
                ],
                className="how-to-use-container",
            ),
        ],
        className="home-container",
    )


def top50_page():
    stock_names = [
        ("AAPL", " - Apple Inc"),
        ("MSFT", " - Microsoft Corporation"),
        ("GOOGL", " - Alphabet Inc (Google)"),
        ("AMZN", " - Amazon.com Inc"),
        ("NVDA", " - NVIDIA Corporation"),
        ("META", " - Meta Platforms Inc"),
        ("TSLA", " - Tesla Inc"),
        ("BRK-B", " - Berkshire Hathaway Inc"),
        ("JPM", " - JPMorgan Chase & Co"),
        ("V", " - Visa Inc"),
        ("MA", " - Mastercard Inc"),
        ("UNH", " - UnitedHealth Group Inc"),
        ("XOM", " - Exxon Mobil Corporation"),
        ("PG", " - Procter & Gamble Co"),
        ("JNJ", " - Johnson & Johnson"),
        ("HD", " - Home Depot Inc"),
        ("LLY", " - Eli Lilly and Company"),
        ("AVGO", " - Broadcom Inc"),
        ("COST", " - Costco Wholesale Corporation"),
        ("PEP", " - PepsiCo Inc"),
        ("KO", " - Coca-Cola Company"),
        ("MRK", " - Merck & Co Inc"),
        ("ABBV", " - AbbVie Inc"),
        ("NFLX", " - Netflix Inc"),
        ("ORCL", " - Oracle Corporation"),
        ("CRM", " - Salesforce Inc"),
        ("INTC", " - Intel Corporation"),
        ("AMD", " - Advanced Micro Devices Inc"),
        ("IBM", " - International Business Machines Corp"),
        ("QCOM", " - Qualcomm Inc"),
        ("CSCO", " - Cisco Systems Inc"),
        ("ADBE", " - Adobe Inc"),
        ("TXN", " - Texas Instruments Inc"),
        ("AMAT", " - Applied Materials Inc"),
        ("GS", " - Goldman Sachs Group Inc"),
        ("MS", " - Morgan Stanley"),
        ("AXP", " - American Express Company"),
        ("WMT", " - Walmart Inc"),
        ("MCD", " - McDonald's Corporation"),
        ("NKE", " - Nike Inc"),
        ("DIS", " - Walt Disney Company"),
        ("BA", " - Boeing Company"),
        ("GE", " - General Electric Company"),
        ("T", " - AT&T Inc"),
        ("VZ", " - Verizon Communications Inc"),
        ("UBER", " - Uber Technologies Inc"),
        ("PYPL", " - PayPal Holdings Inc"),
        ("SNOW", " - Snowflake Inc"),
    ]

    stock_list_items = [
        html.Li(
            [
                html.B(code),
                html.Span(name),
            ]
        )
        for code, name in stock_names
    ]

    return html.Div(
        [
            html.H1("Top 50 Stocks", className="top-stocks-header"),
            html.P(
                "(Stock Code - Stock Name) ____ Hint: You can use Ctrl+F to search in the Top 50 Stock List.",
                className="top-stocks-description",
            ),
            html.Ul(stock_list_items, className="stock-list-items"),
        ],
        className="top-stocks-container",
    )



@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/about":
        return about_page()
    elif pathname == "/why-investiq":
        return why_investiq_page()
    elif pathname == "/top-50-stocks":
        return top50_page()
    elif pathname == "/AI-Predictor":
        return ai_predictor_layout()
    # Default condition ko home_page par set karein
    else:
        return home_page()


app.layout = html.Div(
    id="root",
    children=[
        dcc.Store(id="theme-store", data="dark"),
        dcc.Store(id="ai-state-store", storage_type="session", data={}),
        dcc.Store(id="ai-output-store", storage_type="session", data={}),  # ✅ NEW
        dcc.Location(id="url", refresh=False),
        navbar,
        html.Div(
            id="page-wrapper",
            children=html.Div(id="page-content"),
        ),
    ],
)


@app.callback(
    Output("ai-state-store", "data"),
    Input("submit", "n_clicks"),
    State("dropdown_tickers", "value"),
    State("ai-state-store", "data"),
    prevent_initial_call=True,
)
def save_ticker(n, ticker, store):
    if not ticker:
        raise PreventUpdate

    store["ticker"] = ticker
    return store


@app.callback(
    Output("dropdown_tickers", "value"),
    Input("url", "pathname"),
    State("ai-state-store", "data"),
)
def restore_ticker(pathname, store):

    if pathname != "/AI-Predictor":
        raise PreventUpdate

    if not store or "ticker" not in store:
        raise PreventUpdate

    return store["ticker"]



@app.callback(
    Output("theme-store", "data"),
    Input("theme-toggle", "n_clicks"),
    State("theme-store", "data"),
)
def toggle_theme(n, current):
    if n is None:
        return "dark"
    return "light" if current == "dark" else "dark"



@app.callback(
    Output("root", "className"),
    Input("theme-store", "data"),
)
def apply_theme(theme):
    return theme


def get_stock_price_fig(df, theme):
    fig = go.Figure(
        data=[
            go.Candlestick(
                x=df["Date"],
                open=df["Open"],
                high=df["High"],
                low=df["Low"],
                close=df["Close"],
                name="Price",
            )
        ]
    )

    fig.update_layout(
        title="Closing and Opening Price vs Date",
        height=500,
        template="plotly_dark" if theme == "dark" else "plotly_white",
        margin=dict(l=40, r=60, t=50, b=40),
        modebar={
            "bgcolor": "rgba(0,0,0,0)",
            "color": "#198754" if theme == "light" else "#c3ff00",
            "orientation": "h",  
        },
        hovermode="x unified",
    )
    return fig


def get_more(df, theme):
    df["EMA_20"] = df["Close"].ewm(span=20).mean()

    fig = go.Figure()


    fig.add_trace(
        go.Candlestick(
            x=df["Date"],
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="Price",
            increasing=dict(line=dict(color="#00ff9c")),  # green
            decreasing=dict(line=dict(color="#ff4d4d")),  # red
        )
    )


    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["EMA_20"],
            mode="lines",
            name="EMA 20",
            line=dict(color="#ffd500" if theme == "dark" else "#198754", width=2),
        )
    )

    fig.update_layout(
        title="Exponential Moving Average vs Date",
        height=500,
        template="plotly_dark" if theme == "dark" else "plotly_white",
        margin=dict(l=40, r=60, t=50, b=40),
        # 🔥 SAME MODEBAR LOOK
        modebar={
            "bgcolor": "rgba(0,0,0,0)",
            "color": "#198754" if theme == "light" else "#c3ff00",
            "orientation": "h",
        },
        hovermode="x unified",
    )

    return fig


def ai_predictor_layout():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Input(
                                id="dropdown_tickers",
                                placeholder="Ex: AAPL",
                                type="text",
                                className="mb-2",
                                persistence=True,
                                persistence_type="session",
                            ),
                            html.Button("Submit", id="submit"),
                            dcc.DatePickerRange(
                                id="my-date-picker-range",
                                min_date_allowed=dt(1995, 8, 5),
                                max_date_allowed=dt.now(),
                                start_date=None,
                                end_date=dt.now().date(),
                                initial_visible_month=dt.now(),
                                start_date_placeholder_text="Start Date",
                                end_date_placeholder_text="End Date",
                            ),
                            html.Button("Stock Price", id="stock"),
                            html.Button("Indicators", id="indicators"),
                            dcc.Input(
                                id="n_days", placeholder="Forecast days", type="number"
                            ),
                            html.Button("Forecast", id="forecast"),
                            html.Div(
                                id="forecast-error",
                                style={
                                    "color": "#ff4d4d",
                                    "margin-top": "8px",
                                    "font-size": "14px",
                                    "font-weight": "500",
                                },
                            ),
                        ],
                        width=3,
                    ),
                   
                    dbc.Col(
                        [
                            dcc.Loading(
                                type="dot",
                                children=[
                                    html.H3(id="ticker"),
                                    html.P(id="description"),
                                ],
                                color="var(--accent)",
                            ),
                            dcc.Loading(
                                id="loading-graphs",
                                type="default",
                                children=[
                                    html.Div(id="graphs-content"),
                                    html.Div(id="main-content"),
                                    html.Div(id="forecast-content"),
                                ],
                                color="var(--accent)",
                                overlay_style={
                                    "visibility": "visible",
                                    "opacity": "0.4",
                                },
                            ),
                        ],
                        width=9,
                    ),
                ]
            )
        ],
        className="ai-predictor",
    )


@app.callback(
    Output("forecast-error", "children"),
    Input("ai-output-store", "data"),
)
def show_forecast_error(store):
    if not store:
        return ""

    if store.get("last_action") != "forecast":
        return ""

    return store.get("forecast_error", "")


@app.callback(
    Output("ai-output-store", "data"),
    [
        Input("submit", "n_clicks"),
        Input("stock", "n_clicks"),
        Input("indicators", "n_clicks"),
        Input("forecast", "n_clicks"),
    ],
    [
        State("dropdown_tickers", "value"),
        State("my-date-picker-range", "start_date"),
        State("my-date-picker-range", "end_date"),
        State("n_days", "value"),
        State("theme-store", "data"),
        State("ai-output-store", "data"),
    ],
    prevent_initial_call=True,
)
def update_ai_store(
    n_sub, n_stk, n_ind, n_frc, ticker, start, end, n_days, theme, store
):
    if not ticker:
        raise PreventUpdate

    if store is None:
        store = {}

    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "submit":

        prev_ticker = store.get("last_ticker")

        if prev_ticker != ticker.upper():
            store.pop("stock_fig", None)
            store.pop("indicator_fig", None)
            store.pop("forecast_fig", None)

        t = yf.Ticker(ticker.upper())
        info = t.info or {}

        store["name"] = info.get("shortName", ticker.upper())
        store["desc"] = info.get("longBusinessSummary", "No description available.")
        store["last_ticker"] = ticker.upper()

        store["saved_start_date"] = start
        store["saved_end_date"] = end
        store["last_action"] = "submit"
        store.pop("forecast_error", None)
        return store
    store["saved_start_date"] = start
    store["saved_end_date"] = end

 
    if button_id == "stock":
        df = yf.download(ticker, start=start, end=end)
        if not df.empty:
            df.reset_index(inplace=True)
            df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
            store["stock_fig"] = get_stock_price_fig(df, theme).to_dict()
            store["last_action"] = "stock"
            store.pop("forecast_error", None)

    elif button_id == "indicators":
        df = yf.download(ticker, start=start, end=end)
        if not df.empty:
            df.reset_index(inplace=True)
            df.columns = [c[0] if isinstance(c, tuple) else c for c in df.columns]
            store["indicator_fig"] = get_more(df, theme).to_dict()
            store["last_action"] = "indicators"
            store.pop("forecast_error", None)

   
    elif button_id == "forecast":
        store["last_action"] = "forecast"

    if n_days is None:
        store["forecast_error"] = "Please enter number of future days"
        store.pop("forecast_fig", None)
        return store

    try:
        n_days = int(n_days)
    except (TypeError, ValueError):
        store["forecast_error"] = "Please enter valid number"
        store.pop("forecast_fig", None)
        return store

    if n_days == 0:
        store["forecast_error"] = "Please enter a number above 0"
        store.pop("forecast_fig", None)
        return store

    if n_days < 0:
        store["forecast_error"] = "Please enter positive number"
        store.pop("forecast_fig", None)
        return store

    store.pop("forecast_error", None)
    store["forecast_fig"] = prediction(ticker.upper(), n_days, theme).to_dict()

    return store


@app.callback(
    [
        Output("description", "children"),
        Output("ticker", "children"),
        Output("graphs-content", "children"),
        Output("main-content", "children"),
        Output("forecast-content", "children"),
    ],
    [
        Input("url", "pathname"),
        Input("ai-output-store", "data"),
    ],
)
def restore_all_ai_ui(pathname, store):
    if pathname != "/AI-Predictor":
        raise PreventUpdate

    desc, name, g_stk, g_ind, g_frc = "", "", "", "", ""

    
    if store:
        desc = store.get("desc", "")
        name = store.get("name", "")

        graph_config = {
            "displayModeBar": True,
            "displaylogo": False,
            "modeBarButtonsToRemove": [
                "lasso2d",
                "select2d",
                "autoScale2d",
                "hoverClosestCartesian",
                "hoverCompareCartesian",
                "toggleSpikelines",
            ],
            "toImageButtonOptions": {
                "format": "png",
                "filename": f"InvestIQ_{name}_Chart",
                "height": 600,
                "width": 1200,
                "scale": 2,
            },
        }

        if "stock_fig" in store and store["stock_fig"]:
            g_stk = dcc.Graph(
                figure=go.Figure(store["stock_fig"]),
                config=graph_config,
                style={"border-radius": "15px", "overflow": "hidden"},
            )

        if "indicator_fig" in store and store["indicator_fig"]:
            g_ind = dcc.Graph(
                figure=go.Figure(store["indicator_fig"]),
                config=graph_config,
                style={"border-radius": "15px", "overflow": "hidden"},
            )

        if "forecast_fig" in store and store["forecast_fig"]:
            g_frc = dcc.Graph(
                figure=go.Figure(store["forecast_fig"]),
                config=graph_config,
                style={"border-radius": "15px", "overflow": "hidden"},
            )

    return desc, name, g_stk, g_ind, g_frc

@app.callback(
    Output("contact-status", "children"),
    Output("contact-status", "style"),
    Input("contact-submit", "n_clicks"),
    State("contact-name", "value"),
    State("contact-email", "value"),
    State("contact-message", "value"),
    prevent_initial_call=True,
)
def handle_contact_form(n, name, email, message):

    if not name or not email or not message:
        return "❌ Please fill in all fields.", {"color": "#ff4d4d"}

    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_pattern, email):
        return "❌ Please enter a valid email address.", {"color": "#ff4d4d"}

    success = send_email(name, email, message)

    if success:
        return "✅ Message sent successfully! We'll get back to you soon.", {
            "color": "#22c55e"
        }
    else:
        return "❌ Failed to send message. Please try again later.", {
            "color": "#ff4d4d"
        }


def send_email(name, sender_email, message):
    receiver_email = "shahiduddin153@gmail.com"

    msg = MIMEMultipart()
    msg["From"] = "InvestIQ Contact <techshaho786@gmail.com>"
    msg["To"] = receiver_email
    msg["Reply-To"] = sender_email
    msg["Subject"] = "📩 New Contact Message - InvestIQ"

    body = f"""
New message received from InvestIQ Contact Form

Name: {name}
Email: {sender_email}

Message:
{message}
    """

    msg.attach(MIMEText(body, "plain"))

    try:
        print("🔹 Connecting to SMTP...")
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)
        server.set_debuglevel(1)  
        server.starttls()

        print("🔹 Logging in...")
        server.login(
            "techshaho786@gmail.com",
            "hydyyuhhuztezdub"  
        )

        print("🔹 Sending email...")
        server.sendmail(
            "techshaho786@gmail.com",
            receiver_email,
            msg.as_string()
        )

        server.quit()
        print("✅ Email SENT")
        return True

    except Exception as e:
        print("❌ Email FAILED:", e)
        return False


if __name__ == "__main__":
    app.run(debug=True)
