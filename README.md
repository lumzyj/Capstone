DESCRIPTION

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. The backend is designed to work for three type of users, Casting director, casting assistant and executive directors.


ROLES & PERMISSIONS 

Casting assistant can only get movies and actors
casting directors can do what casting assistant can do and also add or delete actors as well as modify actors and movives  
executive directors have the access to carry our the resposiblity of a casting director and also to delete and add actors. 

Authorization of users is enabled via Auth0.

***********************************************************************************************************

PROJECT DEPENDENCIES

The project depends on the latest version of Python 3.x which we recommend to download and install from their official website and use a virtual environment to install all dependencies.

***********************************************************************************************************

PIP dependencies

After having successfully installed Python, navigate to the root folder of the project (the project must be forked to your local machine) and run the following in a command line:

pip3 install -r requirements.txt

***********************************************************************************************************

DATA MODELING

The data model of the project is provided in models.py filr in the root folder. The following schema for the database are used for API behaviour:

- There are two tables created: movies and actors

***********************************************************************************************************

All necessary credential to run the project are provided in the setup.sh file.

To run the API server on a local development environmental the following commands must be additionally executed:

On MacOS: export
export FLASK_APP=app.py
export FLASK_ENV=development

***********************************************************************************************************

API Server
All accessable endpoints of the project are located in the app.py file.

Run the following command in the project root folder to start the local development server:

flask run

***********************************************************************************************************

API endpoints

Public endpoints

GET '/movies'
Fetches a dictionary with id and title of movies who posted their release date to the database.
Request Arguments: None
Returns: A JSON object with two keys: 'success' and 'success meessage' - a dictionary with company id and name.
Sample curl request: curl -X GET http://127.0.0.1:5000/movies 

Sample response:

{
    "movies": {
        "1": "Kyle XY",
        "2": "Black Panther",
        "3": "Bob"
    },
    "success": true
}

Sample curl request: curl -X GET http://127.0.0.1:5000/companies 

***********************************************************************************************************


Testing
The testing of all endpoints was implemented with unittest. Each endpoint can be tested with one success test case and one error test case. 

All test cases are soted in test_app.py file in the project rool folder.

Before running the test application, create jobportal_test database using Psql CLI:

create database capstone_test
Then in the command line interface run the test file:

python3 test_app.py

***********************************************************************************************************

Heroku Deployment and Base URL
The backend application has been deployed on Heroku and can be accessed live at

https://capstone-deployment-cv3o.onrender.com

TOKEN FOR EXECUTIVE DIRECTOR: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdlSHJJbjdvdjlqLW5CT1JjaVZSViJ9.eyJpc3MiOiJodHRwczovL2Rldi1vMXdkZ2xibWwzdHM4d2IyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDExNjkxODY1OTk5NzAzOTkyNzQ1NSIsImF1ZCI6ImNhcHN0b25lIiwiaWF0IjoxNjc3MDU2MDQwLCJleHAiOjE2NzcwNjMyNDAsImF6cCI6IjNLRlV0R2hlM0p6clFhVGNuTG1pUE5zcWdEbG42WEd0Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.IdzjmpwYNU0W5Ji9G7FykNILAtKEMKi2uW6fHADpXAYGGHWhJT2ouN4pDipMXrCaltR2Qe3o16XqqVd-FlX4lct64132rQTyTVRL2YSJWCQuzcdj9LqRJQJ9erJMKOxPfF9QlRvSCvgASX1_xXn2P1oE8MwDRLZRiBkzrKPekKMHt5PtFYQ0TfePJKl8B7i3dNMmEsntDap4tu1l9YozRFeRvsAUw6ot_DgDSfrNEbeN02IeRUS7HLfJNlEKe55DZ5oGJN2MGdMKJ-_vja9AyTFeM1QyLxzubY8pAD8VCV69yiPEMe2-yO_WA-h0pi5iqmSf_1ZTOlrsj10AEqrXwQ

