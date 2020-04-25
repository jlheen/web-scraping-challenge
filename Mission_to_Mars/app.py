from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# a landing page (best practice to include, but not necessary)
@app.route('/')
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


# where we're going to scrape the data from
# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    # Find mongo database
    mars = mongo.db.mars 

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Update the Mongo database using update and upsert=True
    mars.replace_one({}, mars_data, upsert=True)

    # Redirect back to home page
    return 'successful'


if __name__ == "__main__":
    app.run(debug=True)
