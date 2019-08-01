from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import sqlalchemy
from flask import Flask, jsonify
import datetime as dt

app = Flask(__name__)


engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


@app.route("/")
def home():
    return("Welcome! <br> <br>  Here are the available routes: <br> <br> \
        /api/v1.0/precipitation <br>  \
        /api/v1.0/stations <br> \
        /api/v1.0/tobs <br> \
        /api/v1.0/< start > <br> \
        /api/v1.0/< start > / < end >")


@app.route("/api/v1.0/precipitation")
def get_prcp():
    prcp_dict = {}
    measurements_list = session.query(
        Measurement.date, Measurement.station, Measurement.prcp).all()
    for measurement in measurements_list:
        date = measurement[0]
        station = measurement[1]
        prcp = measurement[2]
        if date not in prcp_dict:
            prcp_dict[date] = {station: prcp}
        else:
            prcp_dict[date][station] = prcp
    return jsonify(prcp_dict)


@app.route("/api/v1.0/stations")
def get_stations():
    station_list = []
    stations = session.query(Station.station).all()
    for station in stations:
        station_list.append(station[0])
    return jsonify(station_list)


@app.route("/api/v1.0/tobs")
def get_tobs():
    last_date = max(session.query(Measurement.date))[0]
    year_before = dt.datetime.strptime(
        last_date, "%Y-%m-%d") - dt.timedelta(days=366)
    tobs_list = session.query(Measurement.tobs).filter(
        Measurement.date >= year_before).all()
    return jsonify([s[0] for s in tobs_list])


@app.route("/api/v1.0/<start>")
def get_min_avg_max_temp_from_start_date(start):
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    min_max_avg = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).all()[0]
    return jsonify(min_max_avg)


@app.route("/api/v1.0/<start>/<end>")
def get_min_avg_max_temp(start, end):
    start_date = dt.datetime.strptime(start, "%Y-%m-%d")
    end_date = dt.datetime.strptime(end, "%Y-%m-%d")
    min_max_avg = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(
            Measurement.date <= end_date).all()[0]
    return jsonify(min_max_avg)


if __name__ == "__main__":
    app.run(debug=True)
