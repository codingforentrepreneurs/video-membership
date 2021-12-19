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


## Bootstrap 101


Common Classes
- Layout
    - `container-fluid` or `container`
        - `row`
            - `col` (100% width)
        - `row`
            - `col-6` (50%)
            - `col-3` (25%)
            - `col-3` (25%)
        - `row`
            - `col-9` (75%)
            - `col-3` (25%)
        - `row`
            - `col-md-9 col-12` (75% at medium size screen, 100% below that)
            - `col-md-3 col-12` (25% at medium size screen, 100% below that)
- Buttons
    - `btn btn-primary` or `btn btn-secondary` this is a primary or secondary color (basically blue or gray)
    - `btn btn-outline-primary` this is a clear button with a blue outline
    - `btn btn-sm btn-success` this is a small button with green

- Forms
    - `form-control` on an `<input>` element makes the form input a bootstrap class

- Spacing
    - `my-5`, `my-4`, ..., `my-1` gives a relative margin on top and bottom
    - `py-5`, `py-4`, ..., `py-1` gives a relative padding on top and bottom
    - `mx-5` or `px-5`  changes the direction of the margin/padding to left and right (due the `x`) instead of top/bottom (which was due to the `y`)
    - `me-3` or `pe-3` changes the direction of the margin/padding to *only* the end (aka after & due to the `e`).
    - `ms-2` or `ps-2` changes the direction of the margin/padding to *only* the start (aka start due to the `s`).

- Video
    - `ratio ratio-16x9` or `ratio ratio-1x1` in a `div` above an `iframe` will resize the video to fit that ratio.

