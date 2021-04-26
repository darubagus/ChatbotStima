import os
from flask import *
import sqlite3 as sql

app = Flask(__name__)

# APP_ROUTE = os.path.dirname(os.path.abspath(__file__))

kataPenting = [
    'tucil' , 
    'tubes', 
    'kuis',
    'ujian',
    'praktikum',
    'mummu'
]

@app.route("/")
def index():
    return render_template("home.html")




# MAIN
if __name__ == "__main__":
    app.run(debug=True)