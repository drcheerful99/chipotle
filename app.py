from flask import Flask, render_template, jsonify, request, session, g, redirect, url_for, abort, flash, make_response
import pymongo
from bson import json_util
import json
import pandas 
accessToken="pk.eyJ1IjoibWVsaXNzYXNtYXNoZXkiLCJhIjoiY2tsazMyZjI3NjJmaDJvdWlydWo0dGVhaiJ9.T1g70t7acsLWiXm43ycHYg"
url="https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}"
app = Flask(__name__)
def transform(text_file_contents):
    return text_file_contents.replace("=", ",")
def parse_json(data):
    return json.loads(json_util.dumps(data))
def parse_json(datas):
    return json.loads(json_util.dumps(datas))
# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.Chipotle
chipotle_locations = db.chipotle_locations
restaurant_locations=db.restaurants

@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    # locations = list(chipotle_locations.find())
    # print(locations)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html")
@app.route("/data")
def data():
    locations = chipotle_locations.find()
    return jsonify(parse_json(locations))

@app.route("/data2")
def datas():
    res_locations = restaurant_locations.find()
    return jsonify(parse_json(res_locations))

@app.route("/chipotle")
def chipotle():
    # write a statement that finds all the items in the db and sets it to a variable
    locations = list(chipotle_locations.find())
    print(locations)    
    return render_template("chipotle.html", locations=locations)

@app.route("/restaurants")  
def restaruants(): 
    res_locations = list(restaurant_locations.find())
    print(res_locations)    
    return render_template("restaurants.html", restaurant_locations=restaurant_locations)
@app.route("/templates/map.html")  
def map(): 
    url="https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}"
    accessToken="pk.eyJ1IjoibWVsaXNzYXNtYXNoZXkiLCJhIjoiY2tsazMyZjI3NjJmaDJvdWlydWo0dGVhaiJ9.T1g70t7acsLWiXm43ycHYg"
    return render_template("map.html", access_token=accessToken, url=url)

@app.route("/templates/Stock.html")  
def stock(): 
    return render_template("Stock.html")
@app.route('/csv')
def weather_dashboard():
    filename = '/data/chipotle_stores.csv'
    data = pandas.read_csv(filename, header=0)
    data.columns=['state','location','address','latitude','longitude']
    data.to_html(open('chipotle_table.html', 'w'))
    return render_template('chipotle_table.html')
if __name__ == "__main__":
    app.run(debug=True)