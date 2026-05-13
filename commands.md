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