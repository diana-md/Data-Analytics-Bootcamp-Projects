from flask import Flask, render_template, redirect, url_for
import pymongo

# Create MongoDB connection; Create database and collection if it does not exist.
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client["marsDB"]
collection = db["mars"]

app = Flask(__name__)


@app.route("/scrape")
def import_scrape():
    # Import scrape_mars py file that starts scrapping the webpages and returns
    # a disctionary with all the data scraped.
    import scrape_mars
    if len(db.list_collection_names()) != 0:
        for field in db["mars"].find():
            field.drop()
    collection.insert_one(scrape_mars.scrape())
    # return "Data was successfully scrapped."
    return redirect(url_for('show_scraped_data'))


@app.route("/")
def show_scraped_data():
    # Query the Mongo database and pass the mars data into an HTML template to
    # display the data.
    mars_dict = None
    if len(db.list_collection_names()) == 0:
        #import scrape_mars
        #mars_dict = scrape_mars.scrape()
        # collection.insert_one(mars_dict)
        return render_template("scrape.html")
    else:
        for field in db["mars"].find():
            mars_dict = field
            break
        return render_template("index.html", dict=mars_dict)


if __name__ == "__main__":
    app.run()
