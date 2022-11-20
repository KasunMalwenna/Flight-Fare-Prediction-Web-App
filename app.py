
# Importing required packages
from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pandas as pd
import joblib

app = Flask(__name__)
# load the best model
model = joblib.load("RanForest_tuned_gridSearch_model_Best.pkl")



@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    """
      Takes user inputs and creats a list of values for all features in
      transformed datasent used to train a model and appy .predict on the 
      traind model and outputs predicted Air fare.
    
            Input:  User input from the web app
                    

            Output: Predicted air fare
                    
    """
    if request.method == "POST":

        # grabbing values form user inputs and creating features in dataframe
        # day month features
        date_dep = request.form["Dep_Time"]
        
        trip_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        
        trip_month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        
        # deaparture features
        dep_time_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        
        dep_time_minute = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)

        # arrival features
        date_arr = request.form["Arrival_Time"]
        
        arr_time_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
      
        arr_time_minute = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        

        # Duration features
        duration_hours = abs(dep_time_hour - arr_time_hour)
        duration_minutes = abs(dep_time_minute - arr_time_minute)

        # Stops feature
        stop = int(request.form["stops"])

        # airline feature
        # airline=='Air Asia'(1 in column)
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


        # origin freatures
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


        # Destination features
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

        # making prediction using created features
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
