# Campus_Food
Campus_Food django backend for our cloud computing project


Environment:
> sudo apt install python-pip
> sudo -H pip install -U pipenv
> pipenv shell


To run local version:
> cd Campus_Food

# migrate the tables
> python manage.py makemigrations
> python manage.py migrate
> python manage.py migrate --run-syncdb

# start the server
> python manage.py runserver

Admin Pages:
Once the server is started the admin pages will be available at *http://127.0.0.1:8000/admin/*

Create a super user with
> python manage.py createsuperuser

Then login to see tables and data
