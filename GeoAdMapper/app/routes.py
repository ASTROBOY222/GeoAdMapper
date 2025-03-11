from flask import Blueprint, jsonify, render_template
from app.google_sheets import get_coordinates
import os


main = Blueprint('main',__name__)

@main.route("/",methods=["GET","POST"])
def my_func():
    map_api = os.getenv("GOOGLE_MAPS_API_KEY")
    return render_template('index.html', map_api = map_api)

@main.route("/coordinates",methods=["GET","POST"])
def coordinates():
    data = get_coordinates()
    return jsonify({"coordinates": data})
