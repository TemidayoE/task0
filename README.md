# HNG TASK0 API

This is a simple Django RESTAPi that provides:
* Registered Email Address
* Current datetime in ISO8601 format
* the Github URL of the project's codebase
_____________________________________________________
## SetUp Instructions
1. Clone the repo
```
git clone
https://github.com/TemidayoE/task0.git
cd basic_api

2. Create a venv & Install dependencies
```
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

3. Run Database migrations
```
python manage.py migrate

4. Start the development server
```
python manage.py runserver
_____________________________________________________