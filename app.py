import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine('sqlite:///hawaii.sqlite')
base = automap_base()
base.prepare(engine, reflect = True)

Station = base.classes.station
Measurement = base.classes.measurement

app = Flask(__name__)

@app.route('/')
def home():
    '''List all availble routes'''

    return(
        f'Available Routes: </br>'
        f'/api/v1.0/precipitation </br>'
        f'/api/v1.0/stations </br>'
        f'/api/v1.0/tobs </br>'
        f'/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd] </br>'
        f'/api/v1.0/[start_date format:yyyy-mm-dd] </br>'
    )

@app.route('/api/v1.0/precipitation')
def prcp():
    '''Convert the query results to a dictionary using `date` as the key and `prcp` as the value'''

    session = Session(engine)
    results = session.query(
        Measurement.date, 
        Measurement.prcp).all()

    session.close()

    precipitation = []

    for date, prcp in results:
        prcp_dict = {}
        prcp_dict['date'] = date
        prcp_dict['precipitation'] = prcp
        precipitation.append(prcp_dict)
    
    return jsonify(precipitation)

@app.route('/api/v1.0/stations')
def stations():
    '''Return a JSON list of stations from the dataset'''

    session = Session(engine)
    results = session.query(Station.name)

    session.close()

    stations = []

    for station in results:
        stations.append(station)

    return jsonify(stations)

@app.route('/api/v1.0/tobs')
def temps():
    '''Query the dates and temperature observations of'''
    '''the most active station for the last year of data.'''

    session = Session(engine)
    results = session.query(
        Measurement.date, 
        Measurement.station, 
        Measurement.tobs
        ).filter(
            Measurement.station == 'USC00519281').filter(
                Measurement.date >= '2016-08-24').all()

    session.close()

    observe = []

    for date, station, temp in results:
        day = {}
        day['date'] = date
        day['station'] = station
        day['temp'] = temp
        observe.append(day)

    return jsonify(observe)

@app.route('/api/v1.0/<start_date>/<end_date>')
def start_end_stats(start_date, end_date):
    '''Return a JSON list of the minimum temperature,'''
    '''the average temperature, and the max temperature '''
    '''for a given start or start-end range.'''

    session = Session(engine)
    results = session.query(
        func.min(Measurement.tobs), 
        func.max(Measurement.tobs), 
        func.avg(Measurement.tobs)).filter(
            Measurement.date >= start_date).filter(
                Measurement.date <= end_date).all()

    session.close()

    temps = []

    for min_tobs, max_tobs, avg_tobs in results:
        stats = {}
        stats['min_temps'] = min_tobs
        stats['max_temps'] = max_tobs
        stats['avg_temps'] = avg_tobs
        temps.append(stats)

    return jsonify(temps)


@app.route('/api/v1.0/<start_date>')
def start_stats(start_date):
    '''Return a JSON list of the minimum temperature,'''
    '''the average temperature, and the max temperature '''
    '''for a given start or start-end range.'''

    session = Session(engine)
    results = session.query(
        func.min(Measurement.tobs), 
        func.max(Measurement.tobs), 
        func.avg(Measurement.tobs)).filter(
            Measurement.date >= start_date).all()

    session.close()

    temps = []

    for min_tobs, max_tobs, avg_tobs in results:
        stats = {}
        stats['min_temps'] = min_tobs
        stats['max_temps'] = max_tobs
        stats['avg_temps'] = avg_tobs
        temps.append(stats)

    return jsonify(temps)

if __name__ == "__main__":
    app.run(debug=True)