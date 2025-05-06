# Game Data Webapp

This repository contains files necessary to run a webapp that interacts with a local database of games. It utilizes python, html, css, and an sqlite3 database file.

## Requirements

This webapp utilizes the ```flask```, ```flask_sqlalchemy```, and ```datetime``` libraries. Use the following code to install these libraries if you don't have them already:

```
pip3 install flask
pip3 install flask_sqlalchemy
pip3 install datetime
```

## Components

The ```app.py``` file is the main file for this program. 

The ```templates``` folder contains the ```.html``` files used for the different webpages. 

The ```static``` folder contains the ```.css``` files for styling. 

The ```instance``` folder contains the ```sqlite3``` database file.

## Usage

With the correct libraries installed, simply run ```flask run``` on your command line while inside this directory. Then, in your browser, go to the url: ```http://localhost:5000/list```.