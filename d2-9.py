import sentry_sdk
import os
from bottle import HTTPResponse, Bottle, request
from sentry_sdk.integrations.bottle import BottleIntegration
sentry_sdk.init(
    "https://40f676f3d47e46198be4e3472d7083cb@o577999.ingest.sentry.io/5733923",
    integrations=[BottleIntegration()]
)

app = Bottle()
@app.route('/success')  
def index():  
    raise HTTPResponse(status=200)
    return

@app.route('/fail')  
def index2():   
    raise RuntimeError("ошибка сервера")
    return
  
@app.route('/')  
def index3():  
    raise HTTPResponse(status=200)
    return

if os.environ.get("APP_LOCATION") == "heroku":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    app.run(host='localhost', port=8080)
