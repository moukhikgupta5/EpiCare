# EpiCare

A django based User Portal to manage patient's past history of seizures and update user settings like token to send notification.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

```bash
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
The application will be started and it will start running on port - [3254](http://127.0.0.1:3254/)