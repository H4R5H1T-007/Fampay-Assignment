## Functionalities implemented :-
- Fetching data from Youtube API.
- Adding it to Database and recall api after every 600 seconds asynchronously.
- Created a Dashboard where you can see all of the videos in paginated form.
- Also added filter and sort-by option on right side of nav bar.

## Techstack used:-
- Django </br>
- Postgresql </br>
- Google client library

## Steps to run this project:-
- You make sure you have Postgresql installed and working properly.
- Clone this repo.
- Navigate to this repo folder in terminal

> Note :- You need to Add these to enviroment variables </br>
> 1. API_KEY generated from google cloud platform.</br>
>    (Don't generate Oauth2 id. Just generate the API Key for more info click [here.](https://developers.google.com/youtube/v3/getting-started))</br>
> 2. SECRET_KEY for Django settings.py.</br>
> 3. SQL_PASS Postgresql Password.</br> ie.</br>

> Note :- I have commented out some parts of `DATABASE` in settings.py for deployment purposes so to run it locally setup it accordingly

- Setup virtual enviroment
```
pip3 install virtualenv 
virtualenv venv
source venv/bin/activate
```
- Install dependencies
```
pip3 install -r requirements.txt
```

> Note :- You need to create a database in Postgresql before running the server.</br>
> Also you need to check the Database config in fampay/settings.py file to make sure database name and username matches correctly.

- Starting the server
    - When starting it for first time, run the following command.
```
python3 manage.py makemigrations main
python3 manage.py migrate main
```
- Now run
```
python3 manage.py runserver
```
- Copy and paste this address in your browser
```
http://127.0.0.1:8000/fetch-api-from-youtube/
``` 
This route `fetch-api-from-youtube` is to trigger async data fetch from youtube api in interval of 10 seconds.</br>
After Triggering, this route will redirect you to main home route where videos are listed in Paginated form along with a Sort-By Drop Down menu to specify Sort-By option and Filter-By search bar.</br>
Here I have choosen `query` as `football` and `max_results` as `40`.