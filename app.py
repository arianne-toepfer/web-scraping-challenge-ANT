from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraper

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/scaper"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scraper():
    data = mongo.db.mars_info
    scraped_data = scraper.scrape()
    data.update({}, scraped_data, upsert=True)
    return redirect("http://localhost:5000", code=302)


if __name__ == "__main__":
    app.run(debug=True)
