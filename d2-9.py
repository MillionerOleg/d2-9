import sentry_sdk
import os
from bottle import HTTPResponse, Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_dsn = ""
sentry_sdk.init(
    dsn = sentry_dsn,
    integrations=[BottleIntegration()]
)

app = Bottle()
@app.route('/success')  
def index():  
    return

@app.route('/fail')  
def index2():   
    raise RuntimeError("ошибка сервера")

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host='localhost', port=8080)
