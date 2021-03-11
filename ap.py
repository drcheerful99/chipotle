import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from config import Password
from flask import Flask, jsonify

###Database Setup

engine = create_engine('postgresql://postgres:{Password}@localhost/Restaurants')

#reflect an exisiting database into a new model
Base = automap_base()

#relect the tables
Base.prepare(engine, reflect=True)

#Flask Setup
app = Flask(__name__, instance_relative_config=True)

@app.route("/")
def names():
    #return "did it work?"
    session=Session(engine)
    results=session.query(restaurant.name).all()
    session.close()
    return (jsonify(results))
        # f"/api/v1.0/Restaurants"
   

if __name__ == "__main__":
    app.run(debug=True)

#########################Random Notes
#connect to postgres is ap.py
#read data in postgres line 6
#return data instead of string

#read table in python to json 
#d3.json/
#put in command "python ap.py"