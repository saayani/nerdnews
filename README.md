NerdNews
--------

A HackerNews replica built on top of Django. The project is in it initial
stage.

Features
--------
- Auto populate title from link
- Trendy UI experience

To be implemented
-----------------
- Comments
- Better Rating
- Karma
- Update ordering on upvote

Setup
-----

```
python3 -m venv nerdnewsvenv
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
python manage.py runserver
```

Go ahead and hit http://localhost:8000/ on your browser
