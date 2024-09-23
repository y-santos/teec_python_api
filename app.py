from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from os import environ
from main import modeloLM
import asyncio

PORT = environ.get('PORT', 5000)

app = Flask(__name__)
api = Api(app)
cors = CORS(app)

api.add_resource(modeloLM,
                '/modelo/Wind=<string:wind>&Temp=<string:temp>&Month=<string:month>')

@app.route('/')
def homepage():
    return "A API está sussa"

async def run_flask_app():
    app.run(host='0.0.0.0', debug= True, port = int(PORT))

if __name__ == "__main__":
    asyncio.run(run_flask_app())
