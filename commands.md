# install virtual environment
pip install virtualenv

# create virtual environment
virtualenv name
python -m venv name

# activate virtual env
env\Scripts\activate
source env\Scripts\activate
source env/bin/activate


# Django:  Python based full stack framework(backend,),
# MVT Architecture
Model: data, database, table, fields, datatypes
View: logic: request-response, Model data httprequeset, template building 
Templates: Frontend(html, css)

- project: core configurations
# start project
django-admin startproject project_name .    (. is optional)


- app: function
python manage.py startapp app_name

# run server
python manage.py runserver

# migration file create
python manage.py makemigrations

python manage.py migrate

# create superuser
python manage.py createsuperuser

# shell
python manage.py shell

# CRUD : Create, Retrieve, Update, Delete
# get all data
model_name.objects.all()

# create data
model_name.objects.create(field1 = "...", field2 = "...", ....)

# Retrieve: single data 
a = model_name.objects.get(id = 1)
a.field1
a.field2

# Update
a.field1 = new_data
a.field2 = new data
a.field3 = new data
a.save()

# Delete:
- retrieve a data
- a.delete()

# Filter
model_name.objects.filter(field1= "...", field2 = "...", field3 = "...", ......)