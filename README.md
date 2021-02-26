# Overview

This web app allows users to enter the desserts they want to make including the name, description, and price. After the users submit the form, it will take them to the other page and display all the desserts in the database including those ones they just entered.

The purpose of writing this software is to help myself learn how Django framework works. I now understand how to make different pieces such as urls, views, models, and templates all work together. I also understand how to make my software connect with the SQLite database to read, add, and modify the data.

In order to get this web app up and running, you will need to install Django on your machine. I am currently running Django 3.1.5. After installing Django, make sure you are in the right directory that contains "manage.py" file, so you can run the commands you need. Next step is to type "python manage.py runserver" if you are using Windows. If it runs successfully, you should see the localhost: http://127.0.0.1:8000/, and you can click on it to see the dessert form.



[Software Demo Video](https://youtu.be/cleF4Nn5YTc)

# Web Pages

There are two pages (HTML templates) in this web app. The first one is the main page which contains the dessert form. After the users enter valid input and click submit, the web app will take them to the second page that contains all the desserts details in the database. How the two pages transit between each other is by setting up the urls, views, and form in the HTML templage correctly. All the users' input are connected with the database. The second page will display all the data in the database in a real-time. The web app will also take the users to different pages based on the urls they put in.

# Development Environment

* Django Framework
* Python
* HTML
* CSS
* SQLite Database
* Visual Studio Code
* GitHub

# Useful Websites

* [Django Documentation](https://docs.djangoproject.com/en/3.1/)
* [Django Book](https://djangobook.com/mdj2-models/)

# Future Work

* Allow the users to edit the information they just entered
* Create user authentication
* Make the web app look more professional