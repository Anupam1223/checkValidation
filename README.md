## Project userCRUD
### Developed by: @anupam
### Framework: django

UserCRUD is a simple admin panel where a user can login, if the user is admin then they can add, update, delete user product and category,
simple user can view the dashboard and can update and delete product and category. Default database(sqllite) is used for the development.

Virtual environment setup is done with poetry, all the required dependencies(help or plugins needed to develop this project) are already
present in pyproject.toml file, you dont have to worry about all the dependencies, but if you are new to django then you must install some 
of the plugins
```
pip install pillow
pip install django-utils-six
django-crispy-forms
```

automatically, project will setup in your device, incase if you dont have poetry in your device use `pip install poetry` to add poetry 
steps to run the code after cloning the project:
```
cd path/to/this/cloned/folder
POETRY INSTALL
POETRY RUN PYTHON MANAGE.PY RUNSERVER
```
for more information visit:
- [Poetry Docs] (https://python-poetry.org/docs/)
- [django documenation] (https://docs.djangoproject.com/)

hit `127.0.0.1/user` for accessing the website.

If you have any query regarding this project you can contact me @ mail anupam.siwakoti@gmail.com
