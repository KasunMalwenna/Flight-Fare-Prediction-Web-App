# Flight Fare Prediction Web App: 

![](https://i.imgur.com/HroclkL.jpg)

## Overview
This repository contains a Flask web application which predicts the fare of flight tickets between the busiest cities in India. This is the deployment part of the capstone project undertaken at [BrainStation](https://brainstation.io/) Data Science Bootcamp. Dataset and the project notebooks can be accessed [here](https://github.com/KasunMalwenna/Flight-Fare-Prediction.git).


## Installation
The Code is written in Python 3.8.15. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 
First, you can clone this repository by running the following code in the terminal after navigating into the project directory:
```bash
git clone https://github.com/KasunMalwenna/Flight-Fare-Prediction-Web-App.git
```

 To install the required packages and libraries, run this command in the project directory after cloning the repository:
```bash
pip install -r requirements.txt
```
Now you can run the app using following commands in the terminal:
```bash
python app.py
```
or
```bash
flask run
```


## Directory Tree 
```
├── static 
│   ├── css
│   │   ├── styles.css
│   ├── images
│   │   ├── pic5.jpg
├── templates
│   ├── home.html
├── .gitattributes
├── Procfile
├── README.md
├── app.py
├── RanForest_tuned_gridSearch_model_Best.pkl
├── requirements.txt
```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 


