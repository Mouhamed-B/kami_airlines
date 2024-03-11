# Kami Airlines
A Rest API for Aircraft company management

## Use and run
  Install dependencies:
  `pip install -r requirements.txt`
  
  Apply migrations:
  `python3 manage.py migrate`

  Then create a superuser with your email and a password:
  `python3 manage.py createsuperuser`

  Run test cases:
  `python3 manage.py test`

  Run code coverage checks:
  `coverage run --source='.' manage.py test`

  Report code coverage
  `coverage report`

  Run the app:
  `python3 manage.py runserver`
