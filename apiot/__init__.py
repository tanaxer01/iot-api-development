from flask import Flask
import apiot.routes
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'data.sqlite'),
        SECRET_KEY = "dis_is _secret"
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/")
    def pong():
        return "{ 'status': 'up' }"

    app.register_blueprint(routes.admin)
    app.register_blueprint(routes.sensor)
    app.register_blueprint(routes.location)

    from . import db
    from . import utils
    utils.init_app(app)


    return app

