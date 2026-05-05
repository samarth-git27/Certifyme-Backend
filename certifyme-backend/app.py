from flask import Flask
from config import Config
from extensions import db, jwt

from routes.auth import auth_bp
from routes.opportunity import opp_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt.init_app(app)

# ❗ NO /api prefix (important)
app.register_blueprint(auth_bp)
app.register_blueprint(opp_bp)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
