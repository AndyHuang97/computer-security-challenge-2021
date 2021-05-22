import sys
from flask import Flask

app = Flask(__name__)

from views import *

app.config.from_object('config.ProductionConfig')

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == debug:
        app.config.from_object('config.DevConfig')
        app.run(debug=True)
    else:
        app.run(host="0.0.0.0")