#!/usr/bin/python3
"""script to create routes"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns a JSON status"""
    return jsonify({"status": "OK"})

