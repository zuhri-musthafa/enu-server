import os

from . import create_app
config_mode = os.getenv("CONFIG MODE", "development")
app = create_app(config_mode)

if __name__ == '__main__':
    app.run()