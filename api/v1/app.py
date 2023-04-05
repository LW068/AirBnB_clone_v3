#!/usr/bin/python3
""" Script that creates a Flask app """
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from os import getenv
from flasgger import Swagger
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

swagger = Swagger(app)

@app.teardown_appcontext
def teardown_session(exception):
    """ Closes storage session """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Returns JSON response with 404 status """
    return jsonify({"error": "Not found"}), 404


@app.route('/api/v1/status', strict_slashes=False)
def status():
    """Returns a JSON with the status"""
    return jsonify({"status": "OK"})


if __name__ == '__main__':
    HBNB_API_HOST = getenv('HBNB_API_HOST')
    HBNB_API_PORT = getenv('HBNB_API_PORT')

    host = '0.0.0.0' if not HBNB_API_HOST else HBNB_API_HOST
    port = 5000 if not HBNB_API_PORT else HBNB_API_PORT
    app.run(host=host, port=port, threaded=True)
