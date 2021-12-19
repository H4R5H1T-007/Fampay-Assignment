## Steps to run this project:-
- You make sure you have Postgresql installed and working properly.
- Clone this repo.
- Navigate to Github-Extenship-Assignment-Fampay/

> Note :- You need to create a cred.json file which contains </br>
> 1. API_KEY generated from google cloud platform.</br>
>    (Don't generate Oauth2 id. Just generate the API Key)</br>
> 2. SECRET_KEY for Django settings.py</br>
> 3. Postgresql Password</br>
> You need to put this file along with manage.py file

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
  python3 manage.py migrate
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
After Triggering, this route will redirect you to main home route where videos are listed in Paginated form.</br>
Here I have choosen `query` as `football` and `max_results` as `40`.

## Techstack used:-
> Django </br>
> Postgresql </br>
> Google client library