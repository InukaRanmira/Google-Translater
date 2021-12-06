import os
from config import DB_URI, TOKEN
from helpers.database import Database

db = Database(DB_URI, TOKEN)
