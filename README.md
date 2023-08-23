
### DEPENDENCIES

- Mysql server


## CONFIGURATION

sudo apt-get install python3-dev default-libmysqlclient-dev build-essential


python -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt

flask db init
flask db migrate -m "Initial migration"
flask db upgrade

## LAUNCH THE APP

flask run