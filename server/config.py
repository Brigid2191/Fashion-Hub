import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    UNSPLASH_ACCESS_KEY = os.getenv('unGYk1Aq4QPCkCTpNpz6uVkkazG1xKc3b_o4uUBPNKU')
    UNSPLASH_SECRET_KEY = os.getenv('Te3gqV5GWH8SY4yEfh5Rp3Se91-voXK1QDM-JcNgfYw')
