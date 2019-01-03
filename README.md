# RBS

Simple room bokking system (rbs) with Dajngo

Demo http://rbs.marcincdev.pl

## Getting started

RBS works with Python 3. Instalation instruction:

Create postgres database
```
psql -U 'username'
create databese rbs_db;
```
Create directory and clone repository
```
mkdir rbs
cd rbs
git clone https://github.com/marcincdev/RBS.git .
```
Create venv and install packages 
```
virtualenv -p pytho3 venv
source venv/bin/activate
pip install -r requirements.txt
```
Run RBS django applications
```
python manage.py makemigraion
python manage.py migrate
python manage.py runserver
```

