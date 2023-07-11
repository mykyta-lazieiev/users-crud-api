from flask import Flask
import traceback

app = Flask(__name__)


@app.route("/")
def index():
    return "Welcome to test Users API"


import routes


def set_global_exception_handler(app):
    @app.errorhandler(Exception)
    def unhandled_exception(e):
        response = dict()
        error_message = traceback.format_exc()
        app.logger.error("Caught Exception: {}".format(error_message))
        response["errorMessage"] = error_message
        return response, 500
