#!/usr/bin/python3
"""Init"""
from flask import Blueprint


<<<<<<< HEAD
<<<<<<< HEAD
=======
"""import flask views"""
>>>>>>> 46f23fea41f33a85f87da087253bd28dee886eb1
=======
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")


>>>>>>> 48e2fad36f78c5f49a35dd454129d9ca4aa65bb2
from api.v1.views.index import *
<<<<<<< HEAD
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
=======

>>>>>>> 48e2fad36f78c5f49a35dd454129d9ca4aa65bb2