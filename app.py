from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# import [from directory or pkg].[filename] 


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
mongo = PyMongo(app)

# a landing page (best practice to include, but not necessary)
@app.route('/')
def index():
    mars = mongo.db.collection.find_one()
    return render_template("index.html", listings=mars)


# where we're going to scrape the data from
# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
