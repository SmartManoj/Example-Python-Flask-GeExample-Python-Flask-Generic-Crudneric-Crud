import os

class Config(object):
    SECRET_KEY = 'do-or-do-not-there-is-no-try'
    SQLALCHEMY_DATABASE_URI = 'postgres://lwzskuzxhgobuz:d48d87d55a52497e9f59e6849e1d2feec6a08e0ab3951dbacc52c4f207e57206@ec2-52-200-134-180.compute-1.amazonaws.com:5432/d6si3a20mhi3ng'
    SQLALCHEMY_TRACK_MODIFICATIONS = False