import datetime
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin
from peewee import *

# Singleton Meta Class
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Database Connection Class
class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.database = SqliteDatabase('social.db')

    def get_db(self):
        return self.database

# Global access point for the database
database = DatabaseConnection().get_db()

class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField(max_length=100)
    joined_at = DateTimeField(default=datetime.datetime.now)
    is_admin = BooleanField(default=False)

    class Meta:
        database = database
        order_by = ('-joined_at',)

    def get_posts(self):
        return Post.select().where(Post.user == self)

    def get_stream(self):
        return Post.select().where(
            (Post.user << self.following()),
            (Post.user == self)
        )

    def following(self):
        return (
            User.select().join(
                Relationship, on=Relationship.to_user
            ).where(
                Relationship.from_user == self
            )
        )

    def followers(self):
        return (
            User.select().join(
                Relationship, on=Relationship.from_user
            ).where(
                Relationship.to_user == self
            )
        )

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            with database.transaction():
                cls.create(
                    username=username,
                    email=email,
                    password=generate_password_hash(password),
                    is_admin=admin
                )
        except IntegrityError:
            raise ValueError("User already exists")

class Post(Model):
    timestamp = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, related_name='posts')
    content = TextField()

    class Meta:
        database = database
        order_by = ('-timestamp',)

class Relationship(Model):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')

    class Meta:
        database = database
        indexes = (
            (('from_user', 'to_user'), True),
        )

def initialize():
    db = database
    db.connect()
    db.create_tables([User, Post, Relationship], safe=True)
    db.close()
