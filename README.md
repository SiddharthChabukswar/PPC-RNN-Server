# PPC-RNN-Server

## Django-restframework server for ppc grader.

### Follow the steps to setup the server locally

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
The server can be found on address : https://localhost:8000/

### Follow the steps to send request from client

Save the heroku Postman response to response.json file in TestJSON directory

run the remotepostcall.py file in TestJSON to send request to the server

The body of the request must contain(implicit):
```
{
"Type":"Type1",
"Data":[[1], [2] ...]
}
```