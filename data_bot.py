from random_username.generate import generate_username
import secrets
import string
import random
import requests
from decouple import config

NUMBER_OF_USERS = config('NUMBER_OF_USERS', default=1, cast=int)
MAX_POSTS_PER_USERS = config('MAX_POSTS_PER_USERS', default=2, cast=int)
MAX_LIKES_PER_USER = config('MAX_LIKES_PER_USER', default=4, cast=int)

# Additional params
PASSWORD_LEN = config('PASSWORD_LEN', default=10)
HOST_NAME = config('HOST_NAME', default="http://127.0.0.1:8000")
FIRST_NAME_LENGTH = config('FIRST_NAME_LENGTH', default=6, cast=int)
LAST_NAME_LENGTH = config('LAST_NAME_LENGTH', default=6, cast=int)
EMAIL_LENGTH = config('EMAIL_LENGTH', default=8, cast=int)
CONTENT_LENGTH = config('CONTENT_LENGTH', default=10, cast=int)


def string_generator(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def password_generator(length=None):
    pass_len = length if length else PASSWORD_LEN
    return secrets.token_urlsafe(pass_len)


def email_generator():
    return f"{secrets.token_hex(EMAIL_LENGTH)}@gmail.com"


class AutoUser:

    def __init__(self):
        self.username = generate_username(1)[0]
        self.password = password_generator()
        self.first_name = string_generator(length=FIRST_NAME_LENGTH)
        self.last_name = string_generator(length=LAST_NAME_LENGTH)
        self.email = email_generator()
        self.jwt_token = None

    def register(self):
        post_data = \
            {
                'username': self.username,
                'password': self.password,
                'password2': self.password,
                'email': self.email,
                'first_name': self.first_name,
                'last_name': self.last_name
            }
        response = requests.post(HOST_NAME + '/register/', data=post_data)
        return response.status_code

    def login(self):
        post_data = \
            {
                'username': self.username,
                'password': self.password,
            }
        response = requests.post(HOST_NAME + '/login/', data=post_data)
        response_data = response.json()
        self.jwt_token = response_data['access']

    def add_post(self, content):
        post_data = \
            {
                "content": content
            }
        headers = self.form_auth_headers()
        response = requests.post(HOST_NAME + '/post_create/', data=post_data, headers=headers)
        response_data = response.json()
        return response_data["id"]

    def like_post(self, post_pk):
        post_data = \
            {
                'post': post_pk
            }
        headers = self.form_auth_headers()
        response = requests.post(HOST_NAME + '/like_post/', data=post_data, headers=headers)
        return response.status_code

    def form_auth_headers(self):
        return {'Authorization': f'Bearer {self.jwt_token}'}

    def __str__(self):
        return f"User: {self.username}"


if __name__ == "__main__":

    print(f"Started creation of {NUMBER_OF_USERS} users, max posts per user is {MAX_POSTS_PER_USERS},"
          f" max likes per user is {MAX_LIKES_PER_USER}")
    users_created = []
    posts_created = []
    posts_count = 0
    # process of users and posts creation
    while len(users_created) < NUMBER_OF_USERS:
        new_user = AutoUser()
        register_status = new_user.register()
        # if user was generated with duplicates and couldn't create we just go on
        if register_status == 201:
            users_created.append(new_user)
            # process of user login to get JWT token
            new_user.login()
            # process of user create_random_posts
            posts_num = random.randint(0, MAX_POSTS_PER_USERS)
            posts_count += posts_num
            print(f"For {new_user} will be created {posts_num} posts")
            for _ in range(posts_num):
                post_id = int(new_user.add_post(content=string_generator(length=CONTENT_LENGTH)))
                posts_created.append(post_id)

    # if users can't make such amount of likes we force_decrease a number of MAX_LIKES
    if MAX_LIKES_PER_USER > posts_count:
        MAX_LIKES_PER_USER = posts_count
        print(f"Sorry but with such amount of users and posts I could make only {MAX_LIKES_PER_USER} likes,"
              f"so max likes was edited to this value")

    print('-' * 100)
    # process of liking posts
    for user in users_created:
        likes_created = 0
        likes_num = random.randint(0, MAX_LIKES_PER_USER)
        print(f"For {user} will be created {likes_num} likes")
        while likes_created < likes_num:
            random_post_id = random.choice(posts_created)
            status_code = user.like_post(random_post_id)
            # if user tried liked the same post we need skip this
            if status_code == 201:
                likes_created += 1
    print("Creation is completed!")














