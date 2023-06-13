from flask import Flask
import apiot.routes 
import os 

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DATABASE=os.path.join(app.instance_path, 'data.sqlite'),
        secret="iot-api-devel"
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/ping")
    def pong():
        return "pong"

    app.register_blueprint(routes.admin)
    app.register_blueprint(routes.location)

    from . import db
    db.init_app(app)

    return app


