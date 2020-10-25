
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info

A simulation system processing 10000 tasks with 3 processors.

Features:
This system acquires tasks from the database and stores them in a queue which was built with linked list.

The system checks on the task IDs is carried out using Regular Expressions.

At each step of the simulation, the simulation clock is updated to the next significant event, e.g.,task arrival, task processing completion.

"simulation_data.py" randomly generates a simulation data, according to certain criterias. A simulation dataset contains 10000 tasks. The code stores the dataset in sqlite3.

## Technologies

Project is created with:
* Python

## Setup

Setup & Installation (run in terminal shell)
1.Run "simulation_data.py" first to generate a dataset that contains 10000 tasks, (test2.db is created).

2.Run "simulation.py" to process the tasks.


To run this project, install it locally using npm:

```
$ cd ../lorem
$ npm install
$ npm start
```

### static_website
Coursework Static & Responsive University Website Prototype (wireframe provided). Built on: HTML & CSS 

<h3>Includes title page:</h3>

<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="25" height="25"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="25" height="25"/>

<img class="uni" src="../style/pictures/7615945272_d16746ea81_o.jpg" alt="Image of University">
PontyBridge University - Homepage Design (desktop).pdf

A good README is for others to understand what our code includes, and why it's noteworthy

Make sure the file always includes the following elements:

Titles and internal titles
Introduction - the project's aim
Technologies
Launch







	


## Code Examples
To generate lorem ipsum use special shortcode: `put-your-code-here`

which will be displayed as:

<p>Examples of use In case of reusable code or your own library, providing a manual how to use our project might be necessary. It can work as a fragment of code: </p>

#########################
# STATIC-WEBISTE-ACCORDING-TO-WIRE-FRAME
Simple HTML5/CSS Static & Responsive 3 Webpages done according to <b>Designer's Wire Frame</b>

# Example

<img src="https://i.imgur.com/TlpBLnG.png" alt="Home page view Desktop" width="300" heigh="300"/>

<img src="https://i.imgur.com/iQmTSbm.png" alt="Home page view Desktop" width="400" heigh="100"/>

<img src="https://i.imgur.com/KBj5R4Y.png" alt="Home page view Desktop" width="300" heigh="300"/>




# Loading pages
Run the web pages in the development mode, inside folder STATIC-WEBISTE-ACCORDING-TO-WIRE-FRAME i.e.:

command line:

`python -m SimpleHTTPServer`

check if the app is running on `http://0.0.0.0:8000/`









