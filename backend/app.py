from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS
from config import Config
from extensions import db


from routes.endpoint_routes import endpoint_bp

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)
    db.init_app(app)

    app.register_blueprint(endpoint_bp, url_prefix="/api")

    # Home route
    @app.route("/")
    def home():
        return {"message": "AI API Monitor running"}

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)