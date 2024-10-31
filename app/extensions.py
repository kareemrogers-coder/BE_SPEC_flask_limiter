from flask_marshmallow import Marshmallow
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

ma=Marshmallow()

limiter = Limiter ( 
    get_remote_address, 
    # app = app, 
    default_limits=["10 per day", "3 per hour"], ## please change to #200 per day and 50 per hour
)