import os

from muscle_metrics import app

"""
This script is used to run a web application defined in the
'muscle_metrics' module.

The script imports the 'os' module for environment variable access and
imports the 'app' object from the 'muscle_metrics' module, which
represents the web application.
"""


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=bool(os.environ.get("DEBUG")),
    )
