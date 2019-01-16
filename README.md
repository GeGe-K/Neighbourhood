# Neighbourhood Watch

## Author
### *Gloria Givondo* (11/01/2018)

## Description
This is a web application that allows you to be in the loop about everything happening in your neighborhood.
        
You can view the live link [here]()

## User Stories
These are the behaviours that the application implements for use by a user.

As a user, I would like to: 
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| The program should navigate to the login page on load | **On page load, click on get started** | Navigate to the login page|
| Display neibhbourhoods | **Miotoni** | Redirected to a page with alerts, messages, businesses from that naighbourhood |
| Display post a message | **Click button add** | The message/alert is displayed showing by whom and when |
| View profile | **Gloria** | Redirected to the profile page |

## Technologies Used
* Virtual environment
* Python version 3.6.7(Django framework)
* Bootstrap4
* Postgresql
* HTML5
* CSS
* Heroku
* Atom
* Visual Studio Editor (prefered text editor)

## Setup / Installation Requirements
* Web browser
* Virtual environment
* Django
* Python version 3.6
* Postgresql

### Cloning the Repo
* In your terminal run:

        $ git clone https://github.com/GeGe-K/Neighbourhood.git
        $ cd Neighbourhood

* Activate virtual environment

        $ source virtual/bin/activate

* Download the latest version of pip

        $ curl https:/bootstrap.pypa.io/get-pip.py | python

* Install application dependancies and other Modules

        $ pip install -r requirements.txt

* Create the database

        $ psql
        
        CREATE DATABASE hood;

* Create a .env file and add the following

        - SECRET_KEY = `rud-!ooyv()v7x=%)vy9%^b_!5_7bqxfzs3*)%d^xp#g4honjb`
        - DB_NAME = `hood`
        - DB_USER = `moringaschool`
        - DB_PASSWORD = `maroon5`
        - DEBUG = `True`

* Run initial migration

        $ python3.6 manage.py makemigrations <name of app>
        $ python3.6 manage.py migrate

* Run the application in your terminal:

        $ python3.6 manage.py runserver

### Django Admin
* Username: moringaschool 
* Password: <see_me>

## Testing the Application 
* To run the tests for the class files and check if they function well:

        $ python3.6 manage.py tests

## Known Bugs
There are no known bugs. Contact gloriagivondo@gmail.com in-case of any bugs.

## License
The content of this site is license under the MIT license
Copyright (c) 2018 **Gloria**
        
