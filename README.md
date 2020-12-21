# The Mbari API 
> API for the resources used in mbari website and mobile app


## Release History

* v1
    * initialized API with djangorestframework to create endpoints overview with all available URLs to be consumed by the frontend


## Quickstart

* Start your virtual environment (pipenv/venv)
* Pip install the requirements.txt to get your dependancies up to date
* Start the django server
* Launch Postman and use the appropriate URLs in the collection to test the request-response endpoints


## To Do / Pending

* Authorization and authentication for access
* Database poulation with past and present issues, posts, products etc.
* CONSTANTLY CHECK AND UPDATE THE <strong> PROJECT SECTION </strong> OF THE REPO { TODOs, PENDING & DONE }.



## Issues
* All endpoints are vulnerable due to no authorization or authentication in place yet.
* Improve deleting methods & introduce soft delete [using a key like "active" in the models and setting that to False on delete] as an intermediary/alternative to hard deleting [permanently removing the instance from the database].

