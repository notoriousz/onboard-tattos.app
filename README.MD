## Onboard Tattoo Artists

## What is it?

This is a backend application with PostgreSQL relational database. We insert tattoo artists and their respective portfolios. The data can be created, read, updated, and delete. I preferred to use the separate tables created with SQL, a public table for tattoo artists, and a public table for portfolios. The primary key in the first table connects both tables.


## Tables created with SQL

Sample to tattoo artist table

![Screenshot from 2021-10-26 22-59-58](https://user-images.githubusercontent.com/64628014/138987247-7bf8b139-569a-4807-9efa-75b34a6a0fe0.png)

Sample to portfolio table

![Screenshot from 2021-10-26 23-00-31](https://user-images.githubusercontent.com/64628014/138987291-f5cc0332-f7af-482f-be61-2bf38ad17b4e.png)


## How to run?

Clone this repository in a directory

~~~
git clone https://github.com/notoriousz/onboard-tattos-app.git
~~~

Install dependencies
~~~
pip install -r requirements.txt
~~~

Change the files database.ini to connect in postgresql
~~~
[postgresql]
host=localhost
database=databasename
user=myuser
password=mypasswod
~~~

Run Script to start
~~~
python manage.py
~~~
