import connexion
from waitress import serve

from swagger_server import encoder

def serve_api():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Credit Score Predictor'}, pythonic_params=True)
    serve(app, host="0.0.0.0", port=8080)