from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user.user_model import User
from .planet.planet_model import Planet
from .people.people_model import People
from .favourite.favourite_model import Favorite