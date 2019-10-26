# ironbronco

Description

Installation
After installing Python 3.8, open a terminal within the project directory and install the following to meet the Pipfile requirements:

Pip—
```csh
$ sudo easy_install pip
$ sudo pip install --upgrade pip
```

Venv and Flask
python3 -m venv venv
. venv/bin/activate
pip install flask

Gunicorn
pip install gunicorn

Requests
python3.8 -m pip install requests

Setup—
To run the application on Linux:
export FLASK_APP=flaskr
export FLASK_ENV=development

. venv/bin/activate
flask run —or— python -m flask run

Visit http://127.0.0.1:5000
