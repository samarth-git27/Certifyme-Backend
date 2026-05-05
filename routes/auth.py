from flask import Blueprint, request, jsonify
from models import Admin
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta

from utils.helpers import generate_reset_token, validate_reset_token

auth_bp = Blueprint("auth", __name__)

# SIGNUP
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    full_name = data.get("full_name") or data.get("fullName")
    email = data.get("email")
    password = data.get("password")
    confirm_password = data.get("confirm_password") or data.get("confirmPassword")

    if not all([full_name, email, password, confirm_password]):
        return jsonify({"message": "All fields required"}), 400

    if password != confirm_password:
        return jsonify({"message": "Passwords do not match"}), 400

    if len(password) < 8:
        return jsonify({"message": "Password must be at least 8 characters"}), 400

    if Admin.query.filter_by(email=email).first():
        return jsonify({"message": "Account already exists"}), 400

    admin = Admin(
        full_name=full_name,
        email=email,
        password=generate_password_hash(password)
    )

    db.session.add(admin)
    db.session.commit()

    return jsonify({"message": "Signup successful"})


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    email = data.get("email")
    password = data.get("password")

    admin = Admin.query.filter_by(email=email).first()

    if not admin or not check_password_hash(admin.password, password):
        return jsonify({"message": "Invalid email or password"}), 401

    token = create_access_token(identity=admin.id)

    return jsonify({
        "token": token,
        "user": {
            "id": admin.id,
            "email": admin.email,
            "fullName": admin.full_name
        }
    })


# FORGOT PASSWORD
@auth_bp.route("/forgot-password", methods=["POST"])
def forgot_password():
    email = request.json.get("email")

    admin = Admin.query.filter_by(email=email).first()

    if admin:
        token = generate_reset_token(admin.id)
        print(f"RESET LINK: http://localhost:5000/reset-password/{token}")

    return jsonify({"message": "If account exists, reset link sent"})


# RESET PASSWORD
@auth_bp.route("/reset-password/<token>", methods=["POST"])
def reset_password(token):
    admin_id = validate_reset_token(token)

    if not admin_id:
        return jsonify({"message": "Invalid or expired token"}), 400

    data = request.json

    password = data.get("password")
    confirm_password = data.get("confirm_password") or data.get("confirmPassword")

    if password != confirm_password:
        return jsonify({"message": "Passwords do not match"}), 400

    admin = Admin.query.get(admin_id)
    admin.password = generate_password_hash(password)

    db.session.commit()

    return jsonify({"message": "Password reset successful"})
