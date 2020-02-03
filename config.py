import os
#Settingan asli dari flask
CURRENT_PATH = os.path.abspath(".")
UPLOAD_FOLDER = os.path.join(CURRENT_PATH,"uploads")
MAX_CONTENT_LENGTH = 2 * 1024 * 1024
DEBUG = False
SECRET_KEY = "very_secret"