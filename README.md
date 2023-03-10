# Clone and requirements
After cloning repository (https://github.com/Hortmagen21/MySocialApp.git)

Make sure you are in the project folder and run 
```shell
pip install -r requirements.txt
```

To start a server run this command
```shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

# API
If you use tools like Postman make sure you added header Authorization and gave it value:

Bearer <jwt_token>

> http://127.0.0.1:8000/login/

Method: **Post**;

JWT: **not required**

Params: **username:str**, **password:str**

Response: **refresh**, **access** 

Example:

```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3NzA3NTQ2NiwiaWF0IjoxNjc2OTg5MDY2LCJqdGkiOiJhNmIxMDRjMjkzNDM0OTY4YTZkMDUxYTFjNDAzOGI0ZCIsInVzZXJfaWQiOjUsInVzZXJuYW1lIjoibWF4NCJ9.SgXAQ4NcV1Xh_NcqlBj5tFS9EkHG8sK0EExXe98NJ2g",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc2OTkwODY2LCJpYXQiOjE2NzY5ODkwNjYsImp0aSI6IjEzZjBhZjE4ZTlmOTQ1YTk5NjI3NDBjMzdlMjIwYTM3IiwidXNlcl9pZCI6NSwidXNlcm5hbWUiOiJtYXg0In0.n9X7wdWnoGJ-BGlmaWzeiebZ0LlAWf7MNrfW6fMa0DY"
}
```


> http://127.0.0.1:8000/register/

Method: **POST**;

JWT: **not required**

Params: **username:str**, **password:str**, **password2:str**, **email:email**, **first_name:str**, **last_name:str**

Response: **username**, **email**, **first_name**, **last_name**

Example:
```json
{
    "username": "max4",
    "email": "max4@gmail.com",
    "first_name": "rex",
    "last_name": "wex"
}
```

> http://127.0.0.1:8000/likes/

Method: **GET**;

JWT: **required**

Params: **date_from:date**, **date_to:date** 

Response: **date**, **likes**

Example:
```json
[
    {
        "date": "2023-02-20",
        "likes": 1
    },
    {
        "date": "2023-02-21",
        "likes": 5
    }
]
```

> http://127.0.0.1:8000/like_post/

Method: **POST**;

JWT: **required**

Params: **post:pk**

Response: **author**, **post**

Example:
```json
{"author":"max4","post":2}
```

> http://127.0.0.1:8000/info/

Method: **GET**;

JWT: **required**

Params: **None**

Response: **last_activity**, **user_last_login**, **user**

Example:
```json
[
    {
        "last_activity": "2023-02-21T13:53:37.429893Z",
        "user_last_login": "2023-02-21T13:53:51.734937Z",
        "user": "max4"
    }
]
```

> http://127.0.0.1:8000/post_create/

Method: **POST**;

JWT: **required**

Params: **content:str**

Response: **id**, **content**, **author**

Example:
```json
{
    "id": 8,
    "content": "Skipped content of prev post...",
    "author": "max"
}
```

> http://127.0.0.1:8000/dislike_post/<post_id:pk>

Method: **DELETE**;

JWT: **required**

Params: **None**

Response: **None**


# Bot activation

After you started a server you could use bot
to check API endpoints and create a lot of data.

### Bot default config start

```shell
python data_bot.py
```

### Additional Configuration
Configuration file is specified inside .env file
By default, bot works with local host: http://127.0.0.1:8000

A name of host param is **HOST_NAME** and you are free to change it for your needs

Also, you could specify such params as:

**NUMBER_OF_USERS** - how many users bot would create.

Default: 1;

**MAX_POSTS_PER_USERS** - the limit for amount of posts that user could create.

Default: 2;

**MAX_LIKES_PER_USER** - the limit for amount of likes that user could create.

Default: 4;

**PASSWORD_LEN** - the length of password for users register.

Default: 10;


**EMAIL_LENGTH** - the length of email core for users register.

Default: 8;

**FIRST_NAME_LENGTH** - the length of first_name for users register.

Default: 6;

**LAST_NAME_LENGTH** - the length of last_name for users register.

Default: 6;

**CONTENT_LENGTH** - the length of content for posts creation .

Default: 10;
