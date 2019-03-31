# fossee3

Project for IITB summer Internship Entrance<br>
Please see the demo video on maximum possible volume with Earphones.<br>

-About the application

It's an application where user is allowed to upload multiple files with ppt,pptx and pps extensions<br>
and refer as and when required.

<b> Setting up the project:</b>


- Clone the repo
``` 
git clone https://github.com/mananpoddar/fossee3
cd fossee3/mysite
```
- Create a virtualenv
```
virtualenv -p python3 venv
source venv/bin/activate
```

- Install the requirements
```
pip install -r requirements.txt
```
- Setup your mysql database and sync it with my project
```
go to fossee3/mysite/mysite/settings.py and in DATABASE array, change the password and 
username to yours.
do python manage.py makemigrations
then, python manage.py migrate
```
- close any libreoffice application running on your system for better experience

- Run the dev server
```
python manage.py runserver
```
- request localhost:8000/fossee3

<br><br>

<b>Important directories and files to make your look up to the code easier:</b>
```
core backend logic - > fossee3/mysite/fossee3/views.py
core frontend logic - > fossee3/mysite/fossee3/static/fossee3/ajax.js
templates(html files) - > fossee3/mysite/fossee3/templates/fossee3/
routing files - > fossee3/mysite/fossee3/urls.py

```
