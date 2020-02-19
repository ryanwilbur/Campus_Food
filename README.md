# Campus_Food
Campus_Food django backend for our cloud computing project


# Setup the environment:
> sudo apt install python3-pip
>
> pip3 install pipenv
>
> cd Campus_Food
>
> pipenv install
>
> pipenv shell

# Migrate the tables
> python manage.py makemigrations
>
> python manage.py migrate
>
> python manage.py migrate --run-syncdb

# Start the server
> python manage.py runserver

# Admin Pages
Once the server is started the admin pages will be available at *http://127.0.0.1:8000/admin/*

# Create a super user with
> python manage.py createsuperuser

Then login to see tables and data
