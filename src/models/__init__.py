from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user.user_model import User
