# TSETMC
This tool allows you to collect data from http://tsetmc.ir and create a list of all the names.


# RUN
~~~~~~~~~~~~~~~~

1. clone the repo
2. cd tsetmc/
3. python3 -m virtualenv venv
4. source venv/bin/activate
5. pip install -r requirements.txt
6. ./manage.py migrate  
7. ./manage.py collect_data
8. ./mange.py runserver

~~~~~~~~~~~~~~~~

**Note**: each time wanna collect new data from tsetmc run `./manage.py collect_data` it will delete all the objects of the database and collect new data.
