# web-gates
A simple application to track quality of machined parts. A user inputs measurements on a form, some calculations are performed and the measurements are logged on a database.

The application also reads and displays the results on a data dashaboard. 


## Requirements
- Python 2.7
## Stack
- [Flask](http://flask.pocoo.org/) A python microframeworks
- [Bootstrap](http://getbootstrap.com/) For responsive css layout
- [Boostrap Keen.io Template](https://keen.github.io/dashboards/)
- [C3.js](http://c3js.org/) A javascript charting library based on d3.js
- [sqlite3](https://docs.python.org/2/library/sqlite3.html) A simple SQL database to store the measurements 
- [Bootstrap Form Generator](https://bootsnipp.com/forms) A bootstrap form generator



![](/Screenshot.png?raw=true)

## Getting started

Clone the repo and install dependencies: 
```
$ git clone https://github.com/msenejoa/web-gates web-gates
```
Open the directory, create and activate a virtual environment:
```
$ cd web-gates
$ virtualenv venv
$ source venv/bin/activate
```
Install required dependencies:
```
$ pip install -r requirements.txt
```
Run the app:
```
$ python app.py
```
Point your browser to [localhost:12345](http://localhost:12345/) or [localhost:12345/graph](http://localhost:12345/graph) to display the graphs


The javascript c3.js code is located in:
```
/static/assets/js/fud.js
```
