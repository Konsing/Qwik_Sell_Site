import os
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()

def get_env_variable(name, required=True):
    value = os.getenv(name)
    if required and value is None:
        raise ValueError(f"Missing required environment variable: {name}")
    print(f"{name}:", value)
    return value


SQLALCHEMY_DATABASE_URL = get_env_variable("SQLALCHEMY_DATABASE_URL")
SECRET_KEY = get_env_variable("SECRET_KEY")
ALGORITHM = get_env_variable("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(get_env_variable("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(get_env_variable("REFRESH_TOKEN_EXPIRE_DAYS"))

# # AWS variables are not required in testing
# AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID", required=not TESTING)
# AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY", required=not TESTING)
# BUCKET_NAME = get_env_variable("BUCKET_NAME", required=not TESTING)

# # PREVIOUS ENV VARIABLES, NOT SURE IF STILL NEEDED
# ALLOWED_HOSTS = get_env_variable("ALLOWED_HOSTS").split(',')
# DATABASE_URL = get_env_variable("DATABASE_URL")
# CORS_ALLOWED_ORIGINS = get_env_variable("CORS_ALLOWED_ORIGINS")