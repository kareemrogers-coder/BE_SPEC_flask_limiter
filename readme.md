## Rate Limiting 

Today in class we covered Rate Limiting, and discussed the importance of limiting access to resources to prevent malicious attacks. In class we covered how to apply specific limits to individual routes, but for your homework you are to dig into the Flask-Limiter Documentation to discover how you can apply a default rate limit to defend all of your routes

``` py
from app import create_app
from app.models import db
from flask import Flask
from flask_limiter.util import get_remote_address
from flask_limiter import Limiter

app = create_app('DevelopmentConfig')
limiter = Limiter ( 
    get_remote_address, 
    app = app, 
    ### for testing purposes.
    default_limits=["10 per day", "3 per hour"], 
    
    ## will  change to 200 per day and 50 per hour
)
   


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

