## simulation_system

The system is comprised of a clock and three identical processors.

"simulation_data.py" randomly generates a simulation data, according to certain criterias. A simulation dataset contains 100 tasks. The code stores the dataset in sqlite3.

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Design](#design)

## General info

Each task is characterised by the following properties.

<strong>ID</strong> : A string of six characters. Each character is randomly chosen (uniform probability) from letters (’a’-’z’ and ’A’-’Z’), digits (’0’-’9’) and some special characters (’@’, ’ ’, ’#’, ’*’, ’-’, and ’&’). ``The message displayed ** Task [TASK ID] accepted.``

	Example:
	■ JoGY6A
	■ l*@1D*
	■ FJUBT4 
	■ *17hu-

``If the ID does not satisfy at least 3 of the following rules, the task is automatically discarded, the following message is displayed ** Task [TASK ID] unfeasible and discarded.``

<strong>Arrival</strong> : A random real value generated by a uniform distribution from 0 to 100.

	Example:
	■ 47.847
	■ 0.12434545 
	■ 12.236673
	■ 85.18483830

<strong>Duration</strong> : A random value generated by an exponential distribution of parameter 1, rounded up.

	Example:
	■ This time, the result will be an integer number.

At the beginning, the clock is set to zero and the processors are not busy and are, therefore, available. The following message is displayed in the
console: <strong>** SYSTEM INITIALISED ** </strong>
	
At each step of the simulation, the simulation clock is updated to the next significant event, e.g., assigned ID, Arrival/task taken for processing, Duration/task completion time.

<img src="https://user-images.githubusercontent.com/47834415/97199763-497ff800-17a8-11eb-98f2-368bee0b55ae.png" alt="terminal" width="450" height="450"/>

In the rare eventuality of multiple tasks arriving at the same time and all of the processors are busy. The processing order is indifferent and the tasks are processed one at the time, ``the message displayed ** Task [TASK ID] on hold``

Finally, when all the tasks have been processed and completed, the simulation ends and the following message is displayed:
``** [CLOCK] : SIMULATION COMPLETED. **``

## Technologies

Project is created with:
* Python
* Sqlite 3

## Setup 

1. Open terminal shell, select simulation_system folder.

2. Run "simulation_data.py" first to generate a dataset that contains 100 tasks, (test2.db is created).

	To run "simulation_data.py". Terminal shell syntax: python3 simulation_data.py
	
	Optional: SQL viewer <link>http://inloop.github.io/sqlite-viewer/</link> to check if the data has been generated to (test2.db)

3. Run "simulation.py" to process the tasks.

## Design

Terminal shell:

<img src="https://user-images.githubusercontent.com/47834415/97178305-34e33600-178f-11eb-9e46-5f398346c9cd.png" alt="terminal" width="450" height="450"/>

SQL viewer (click to enlarge):

<img src="https://user-images.githubusercontent.com/47834415/97183330-8db5cd00-1795-11eb-914f-d1bba6f59776.png" alt="sql" width="250" height="175"/>
