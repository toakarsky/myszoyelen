import os

from myelen import app


if __name__ == "__main__":
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))