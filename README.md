# Fullstack Technical Test

## About

This is a full-stack application that will extract data from a provided source, store that data into an SQL table, and display it on a frontend React application.

## Functionality

1. Will show a table of data from database(if already exists) into the webpage
2. If database has no data, will extract data from the provided source
3. Then store that data into database
4. Finally, will show the extracted table of data from database in the webpage

## Implemented using

1. ReactJS
2. Python Flask
3. MySQL
4. Selenium

## Project Setup

### Database and git setup:

Create a database

```
 host = 'localhost'
 username = 'root'
 password = 'root'
 database = 'seleniumdb'
```

Create a clone of the project

```sh
git clone https://github.com/joy2441139/Fullstack-Flask-React-Application-with-Selenium-MySQL.git
```

```sh
cd Fullstack-Flask-React-Application-with-Selenium-MySQL
```

### Install all dependencies for Windows (Backend):

Open a terminal for backend and run below commands

```sh
cd flask-server
```

Install selenium using pip command

```sh
pip install selenium
```

Install webdriver-manager using pip command

```sh
pip install webdriver-manager
```

Install mysql-connector using pip command

```sh
pip install mysql-connector
```

Install Flask using pip command

```sh
pip install Flask
```

### Install all dependencies for Windows (Frontend):

Open another terminal for frontend and run below commands

```sh
cd client
```

Install all npm packages

```sh
npm install
```

flask run

npm start
