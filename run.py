import os
from muscle_metrics import app

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=bool(os.environ.get("DEBUG")),
    )
