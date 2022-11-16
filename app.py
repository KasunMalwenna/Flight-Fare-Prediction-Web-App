

from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("RanForest_tuned_gridSearch_model_Best.pkl")



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        trip_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        trip_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        dep_time_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        dep_time_minute = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        arr_time_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        arr_time_minute = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        duration_hours = abs(dep_time_hour - arr_time_hour)
        duration_minutes = abs(dep_time_minute - arr_time_minute)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        stop = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['airline']
        if(airline=='Trujet'):
            airline = 0

        elif (airline=='Air Asia'):
            airline = 1

        elif (airline=='Star Air'):
            airline = 2
            
        elif (airline=='IndiGo'):
            airline = 3
            
        elif (airline=='Go First'):
            airline = 4
            
        elif (airline=='SpiceJet'):
            airline = 5

        elif (airline=='Air India'):
            airline = 6

        elif (airline=='Vistara'):
            airline = 7

        elif (airline=='Air India Business'):
            airline = 8

        elif (airline=='Vistara Business'):
            airline = 9
            
        else:
            airline = None

        # print(Jet_Airways,
        #     IndiGo,
        #     Air_India,
        #     Multiple_carriers,
        #     SpiceJet,
        #     Vistara,
        #     GoAir,
        #     Multiple_carriers_Premium_economy,
        #     Jet_Airways_Business,
        #     Vistara_Premium_economy,
        #     Trujet)

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Bangalore'):
            Origin_Bangalore = 1
            Origin_Chennai = 0
            Origin_Delhi = 0
            Origin_Hyderabad = 0
            Origin_Kolkata = 0
            Origin_Mumbai = 0

        elif (Source == 'Chennai'):
            Origin_Bangalore = 0
            Origin_Chennai = 1
            Origin_Delhi = 0
            Origin_Hyderabad = 0
            Origin_Kolkata = 0
            Origin_Mumbai = 0

        elif (Source == 'Delhi'):
            Origin_Bangalore = 0
            Origin_Chennai = 0
            Origin_Delhi = 1
            Origin_Hyderabad = 0
            Origin_Kolkata = 0
            Origin_Mumbai = 0

        elif (Source == 'Hyderabad'):
            Origin_Bangalore = 0
            Origin_Chennai = 0
            Origin_Delhi = 0
            Origin_Hyderabad = 1
            Origin_Kolkata = 0
            Origin_Mumbai = 0

        elif (Source == 'Kolkata'):
            Origin_Bangalore = 0
            Origin_Chennai = 0
            Origin_Delhi = 0
            Origin_Hyderabad = 0
            Origin_Kolkata = 1
            Origin_Mumbai = 0

        elif (Source == 'Mumbai'):
            Origin_Bangalore = 0
            Origin_Chennai = 0
            Origin_Delhi = 0
            Origin_Hyderabad = 0
            Origin_Kolkata = 0
            Origin_Mumbai = 1

        else:
            Origin_Bangalore = 0
            Origin_Chennai = 0
            Origin_Delhi = 0
            Origin_Hyderabad = 0
            Origin_Kolkata = 0
            Origin_Mumbai = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Destination"]
        if (Source == 'Bangalore'):
            Destination_Bangalore = 1
            Destination_Chennai = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Mumbai = 0
        
        elif (Source == 'Chennai'):
            Destination_Bangalore = 0
            Destination_Chennai = 1
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Mumbai = 0

        elif (Source == 'Delhi'):
            Destination_Bangalore = 0
            Destination_Chennai = 0
            Destination_Delhi = 1
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Mumbai = 0

        elif (Source == 'Hyderabad'):
            Destination_Bangalore = 0
            Destination_Chennai = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 1
            Destination_Kolkata = 0
            Destination_Mumbai = 0

        elif (Source == 'Kolkata'):
            Destination_Bangalore = 0
            Destination_Chennai = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 1
            Destination_Mumbai = 0

        elif (Source == 'Mumbai'):
            Destination_Bangalore = 0
            Destination_Chennai = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Mumbai = 1

        else:
            Destination_Bangalore = 0
            Destination_Chennai = 0
            Destination_Delhi = 0
            Destination_Hyderabad = 0
            Destination_Kolkata = 0
            Destination_Mumbai = 0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']
        
        prediction=model.predict([[
            airline,
            stop,
            trip_month,
            trip_day,
            dep_time_hour,
            dep_time_minute,
            arr_time_hour,
            arr_time_minute,
            duration_hours,
            duration_minutes,
            Origin_Bangalore,
            Origin_Chennai,
            Origin_Delhi,
            Origin_Hyderabad,
            Origin_Kolkata,
            Origin_Mumbai,
            Destination_Bangalore,
            Destination_Chennai,
            Destination_Delhi,
            Destination_Hyderabad,
            Destination_Kolkata,
            Destination_Mumbai
        ]])

        output=int(round(prediction[0],0))

        return render_template('home.html',prediction_text="Your flight price is Rs. {}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
