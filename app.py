#Import dependencies
import datetime as dt
import numpy as np
import pandas as pd

#Import SQLite dependencies
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base 
from sqlalchemy.orm import Session 
from sqlalchemy import create_engine, func  

#Import flask dependencies
from flask import Flask, jsonify 

#Create engine that allows for SQLite query 
engine = create_engine("sqlite:///hawaii.sqlite")

#Create Base-object to reflect database 
Base = automap_base()
Base.prepare(engine, reflect=True)  

#Save class references to database tables as variables
Measurement = Base.classes.measurement 
Station = Base.classes.station 

#Create session link
session = Session(engine) 

#Define our Flask app
app = Flask(__name__)
#Define our root 
@app.route("/")

#Define root contents
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!<br/>
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end
    ''')

#Now create a route for the precipitation data

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp). \
    filter(Measurement.date>=prev_year).all()
    #Loop through the dataset to create a dictionary
    precip = {date:prcp for date, prcp in precipitation}
    #Convert the dictionary into JSON format and return the result
    return jsonify(precip)

#Now we create a route for station data
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    #Convert the format to a simple one dimensional array (list)
    station_list = list(np.ravel(results))
    #Return the results in JSON format
    return jsonify(station_list=station_list) #In the parenthesis we specify a name in order to format as JSON 

#Now we create a route for temperature data
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017,8,23) - dt.timedelta(days=365)
    #Here we will only query one station (the one with the most obs)
    result = session.query(Measurement.tobs).filter(Measurement.station =='USC00519281') \
    .filter(Measurement.date >= prev_year).all()
    #Again convert to a one dimen array
    temps = list(np.ravel(result))
    return jsonify(temps=temps)

#Now we create a route for statistical data
#To get the stats we need to create a route for our start and end dates

@app.route("/api/v1.0/temp/<start>")  #Inequality symbols indicate that an argument can be input in url
@app.route("/api/v1.0/temp/<start>/<end>")

def stats(start=None, end=None):
    #Create our list
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end: #If end is not provided or end=None
        #The asterisk indicates there will be multiple results from our query
        results = session.query(*sel). \
        filter(Measurement.date >= start).all()  
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)

#To run the above we must provide the start/end dates in the url