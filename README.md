# fbhelpdesk

This is project for fb help desk

## Prerequisite

Social app library

pip3 install social-auth-app-django

SSL library

pip3 install django-sslserver


## Run server

python3 manage.py runsslserver


## Technology we used:

1. Graph api
2. Facebook app
3. Django
4. Javascript
5. Django library django-ssl
6. Django library social-auth-app-django

## Problem faced:

1. First time created facebook app to took time to implement login
2. Facebook auth was not working with http protocol it worked only in https
3. Faced issue designing HTML and css still not very good.
4. Facebook permission couldn't getting assigned to application.
5. Rate limiting while implementing the application, facebook was blocking me after some time.

## Implemented in solution:

1. Login via facebook
2. Getting posts of the facebook page.
3. Getting comments of the facebook page.
4. Commenting on the facebook posts.

## Not implemented in the solution:

1. User profile image dynamic for the posts.
2. Right side user profile section is not dynamic.
3. Getting conversations of the facebook page and reply.
4. Not hosted the application on Heroku.

Note: Couldn't implement full solution because of lack of time. This can be included in future scope.
