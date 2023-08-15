
rm -rf migrations/
mysql -u root -p -e "DROP DATABASE sampleshop;"
mysql -u root -p -e "CREATE DATABASE sampleshop;"
flask db init
flask db migrate -m 'init'
flask db upgrade
