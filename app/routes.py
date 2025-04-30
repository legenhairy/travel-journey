from flask import Blueprint, render_template

# Create a Blueprint to separate and organzie the routes

main = Blueprint('app', __name__)

@main.route('/')
def home():
    return render_template('index.html')