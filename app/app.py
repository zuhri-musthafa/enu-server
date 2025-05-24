import os

from . import create_app
app = create_app(os.getenv("CONFIG MODE"))

if __name__ == '__main__':
    app.run()