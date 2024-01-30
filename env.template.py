"""
This is a template file, rename this to env.py for your
environment to work properly
"""

import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
# Add secret key, a secure random string/passcode
os.environ.setdefault("SECRET_KEY", "")
os.environ.setdefault("DEBUG", "True")
# Update DB_URL with your local postgresql credentials.
# Ensure an empty database called muscle_metrics exists on the Postgres server.
os.environ.setdefault(
    "DB_URL",
    "postgresql://<username>:<password>@<hostname>:<port>/muscle_metrics"
)
