# Reservation System
## Overview
This project is a technical challenge test for Realityna Inc. and provides a reservation system for multiple listings using a web application based on DRF. Reservations and room availability can be made via REST API endpoints, and owners can view their booked rooms through an HTML report.
## Get Started
In order to run this project, you must follow these steps first.

1 - Make sure you have PostgreSQL installed. Otherwise, you will have to change the database in the .env file. In order to do this, you have to change the 'DB_ENGINE' to either postgresql or sqlite according to your preference.

2 – Double-click on the sample_env file in the root directory and it will create the.env file. The purpose of this file is to maintain the safety and security of our secret key and other important settings.
## Installation and Usage
``` python
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```
At http://localhost:8000/api/, you can see the endpoints and the redoc file, which can be used by tools such as Postman to send requests to the relevant endpoints.
## Creating a Superuser
``` python
$ python manage.py createsuperuser
```
To access the admin site, visit http://localhost:8000/admin/and use the superuser credentials you created.

