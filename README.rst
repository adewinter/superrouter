DESC
====

This is the django code for the super router frontend.  


SETUP
=====
Super standard. Create a virtualenv (optional) then run::

 pip install -r pip-requires.txt   (assuming you're currently in the root folder of this repo)
 cd srweb
 cp localsettings.py.example localsettings.py
 nano localsettings.py

You should only really have to set the DB settings as you prefer.  Fastest way to get set up is to just configure it for sqlite3

then::
 
 cd ../
 python manage.py syncdb
 python manage.py runserver

Now you should be able to navigate to http://localhost:8000 with your browser and see... things.



