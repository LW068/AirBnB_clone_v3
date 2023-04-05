#!/usr/bin/python3
"""API module"""
from flask import Flask, jsonify
from os import getenv
from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')

@app.teardown_appcontext
def close_storage_db(error):
    """Closes the storage"""
    storage.close()

@app.route('/api/v1/status')
def status():
    """Returns the status of the API"""
    return jsonify(status="OK")

if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', default='0.0.0.0')
    port = getenv('HBNB_API_PORT', default=5000)
    app.run(host=host, port=port, threaded=True)
