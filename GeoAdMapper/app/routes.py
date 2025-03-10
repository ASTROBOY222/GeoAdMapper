from flask import Blueprint, jsonify, render_template
from app.google_sheets import get_coordinates


main = Blueprint('main',__name__)

@main.route("/",methods=["GET","POST"])
def my_func():
    return render_template('index.html')

@main.route("/coordinates",methods=["GET","POST"])
def coordinates():
    data = get_coordinates()
    return jsonify({"coordinates": data})
