#### Work with private APIs...

Protected routes for authorized users...access and permissions

APIs provide a means to access data in a reusable and standardized way.

Go through the entire CRUD - Create, Read, Update and Delete

Send and retrieve infor from a database

The endpoints would be 

- Sign up (Create an account)

- Sign in/log in

- Set up a recurring payment


http://127.0.0.1:8000/

##### Sign up

- POST request

- request body: username, email, password

http://127.0.0.1:8000/sign_up

##### Sign in

- If a GET:

http://127.0.0.1:8000/sign_in/user_id

http://127.0.0.1:8000/sign_in/user_name

If a POST:

http://127.0.0.1:8000/sign_in/user_id

http://127.0.0.1:8000/sign_in/user_name

message body

- request body: username, email, password


Sign up - send data to the database

Sign in - retrieve data from the database



#### Versioning

- How do we work with versioning in APIs?


#### Database Tables

- Users table?

