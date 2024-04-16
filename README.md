# Billing system
#### on-counter billing system for a small-scale shopping

## How to run?

### STEPS: 

Clone the repository 

```bash
git clone https://github.com/Pritamn11/counter-billing-system-using-Django-restframework.git
```

#### STEPS 01 - Create a virtual environment after opening the repository

```bash
python -m venv newenv
```

```bash
.\newenv\Scripts\activate
```

#### STEPS 02 - Install the requirements

```bash
pip install -r requirements.txt
```

#### STEPS 03 -Set Up PostgreSQL Database

##### Set Up PostgreSQL Database on Railway

Step 1: Create an account on [railway.app](https://railway.app/)

Step 2: In your dashboard (railway.app/dashboard) click "+ New Project" and select "Provision PostgresSQL". It should take a few seconds for your database to be ready.

Step 3: Once your database is ready, select the new database and go to the "Connect" tab. Here you will see your "Postgres Connection URL".

This connection URL may seem like a bunch of random character's so lets extract all the values from this url by selecting the "Variables" tab if you want a more user friendly version of this connection.

Go ahead and stick to the default values provided and update our connection in our django settings.py file.

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<PGDATABASE>',
        'USER': '<PGUSER>',
        'PASSWORD': '<PGPASSWORD>',
        'HOST': '<PGHOST>',
        'PORT': '<PGPORT>',
    }
}

```


#### STEPS 04 - Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### STEPS 05 - Start the Development Server

```bash
python manage.py runserver
```

# Django Restframework Billing system App Setup Guide for AWS EC2

## Update the System

```bash
sudo apt-get update
```

### To get this repository, run the following command inside your git enabled terminal

```bash
git clone https://github.com/Pritamn11/counter-billing-system-using-Django-restframework.git
```

### You will need Django installed on your EC2 instance to run this app. You can install Django using pip. Head over to [here](https://www.djangoproject.com/download/) for the download guide.

### Download Django using pip

```bash
sudo apt install python3-pip -y
```

```bash
pip install django
```

```bash
pip install djangorestframework
```

```bash
sudo apt install libpq-dev
```
```bash
pip install psycopg2
```

```bash
pip install drf-spectacular
```

```bash
pip install djangorestframework-simplejwt
```


### Once Django is installed, go to the cloned repo directory and run the following command to create all the migration files required to run this app.

```bash
python3 manage.py makemigrations
```

This will create all the migrations files (database migrations) required to run this App.

### Now, to apply these migrations, run the following command

```bash
python3 manage.py migrate
```

### One last step to access the admin interface, create a superuser by running the following command in the terminal. Provide a username, password, and email for the admin user

```bash
python3 manage.py createsuperuser
```

### Start the server by running the following command.

```bash
python3 manage.py runserver 0.0.0.0:8000
```


Once the server is hosted, navigate to your EC2 instance's public IP address followed by port 8000 (e.g., http://your_ec2_public_ip:8000/api/schema/swagger-ui) to access the Todo App.

Cheers and Happy Coding :)