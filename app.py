from flask import Flask, render_template, jsonify
import pymongo
from bson import json_util
import json

app = Flask(__name__)

def parse_json(data):
    return json.loads(json_util.dumps(data))

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# connect to mongo db and collection
db = client.Chipotle
chipotle_locations = db.chipotle_locations


@app.route("/")
def index():
    # write a statement that finds all the items in the db and sets it to a variable
    locations = list(chipotle_locations.find())
    print(locations)

    # render an index.html template and pass it the data you retrieved from the database
    return render_template("index.html", locations=locations)
@app.route("/data")
def data():
    locations = chipotle_locations.find()
    return jsonify(parse_json(locations))

if __name__ == "__main__":
    app.run(debug=True)