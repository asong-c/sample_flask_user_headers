# Basic flask application to print all headers in logs and return Remote-User in application output
!pip install flask

import flask
import pprint
import os
flask_app = flask.Flask(__name__)

  
@flask_app.route("/")
def index():
    headers = dict(flask.request.headers)
    if ("Remote-User" in headers.keys()):
      pprint.pprint(headers, indent=4)
      return "Remote-User : " + headers["Remote-User"]
    else:
      # Dont print or return remote-user here
      # Liveness checks from internal services have empty headers
      return "alive"

flask_app.run(host="127.0.0.1", port=int(os.environ["CDSW_APP_PORT"]))