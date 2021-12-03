1. Video
    - Host -> YouTube - Private Video -> Udacity
            -> Vimeo, Wistia
            -> Self Hosted - nginx
    - Analytics
        - Lot of data
        - 1 user watches for 10 seconds on 100 videos * 10_000
        - Lot of writes
        - Frame by Frame analysis -> 30 FPS -> 120 second -> 3600 

2. Members
    - Sign up
    - Login
    - Remember things
    - Email Validation / Confirmation
    - Payments



AstraDB - Managed NoSQL Cassandra

- Database name
    - Keyspace name
        - Tables
    - Keyspace name A
        - Table A
        - Table b
        - Table c



- Database for Testing
    - keyspace -> Project 1
        - tables (correspond to prod)


## Create a user via shell


```python
from app import db
from app.users.models import User

db.get_session()
User.objects.create(email='hello@teamcfe.com', password='abc123')
User.objects.create(email='hello@teamcfe.com', password='abc123d')
```

```python

q = User.objects.all()

for user in q:
    print(user.email, user.user_id, user.password)
```