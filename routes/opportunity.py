from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Opportunity
from extensions import db

opp_bp = Blueprint("opportunity", __name__)

# CREATE
@opp_bp.route("/opportunities", methods=["POST"])
@jwt_required()
def create_opportunity():
    admin_id = get_jwt_identity()
    data = request.json

    opp = Opportunity(
        name=data.get("name") or data.get("opportunityName"),
        duration=data.get("duration"),
        start_date=data.get("start_date") or data.get("startDate"),
        description=data.get("description"),
        skills=data.get("skills"),
        category=data.get("category"),
        future_opportunities=data.get("future_opportunities") or data.get("futureOpportunities"),
        max_applicants=data.get("max_applicants"),
        admin_id=admin_id
    )

    db.session.add(opp)
    db.session.commit()

    return jsonify({"message": "Opportunity created"})


# GET ALL
@opp_bp.route("/opportunities", methods=["GET"])
@jwt_required()
def get_all():
    admin_id = get_jwt_identity()

    opps = Opportunity.query.filter_by(admin_id=admin_id).all()

    return jsonify({
        "opportunities": [
            {
                "id": o.id,
                "name": o.name,
                "category": o.category,
                "duration": o.duration,
                "startDate": o.start_date,
                "description": o.description
            }
            for o in opps
        ]
    })


# GET ONE
@opp_bp.route("/opportunities/<int:id>", methods=["GET"])
@jwt_required()
def get_one(id):
    admin_id = get_jwt_identity()

    opp = Opportunity.query.filter_by(id=id, admin_id=admin_id).first()

    if not opp:
        return jsonify({"message": "Not found"}), 404

    return jsonify({
        "id": opp.id,
        "name": opp.name,
        "duration": opp.duration,
        "startDate": opp.start_date,
        "description": opp.description,
        "skills": opp.skills,
        "category": opp.category,
        "futureOpportunities": opp.future_opportunities,
        "maxApplicants": opp.max_applicants
    })


# UPDATE
@opp_bp.route("/opportunities/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    admin_id = get_jwt_identity()

    opp = Opportunity.query.filter_by(id=id, admin_id=admin_id).first()

    if not opp:
        return jsonify({"message": "Not found"}), 404

    data = request.json

    for key, value in data.items():
        setattr(opp, key, value)

    db.session.commit()

    return jsonify({"message": "Updated"})


# DELETE
@opp_bp.route("/opportunities/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    admin_id = get_jwt_identity()

    opp = Opportunity.query.filter_by(id=id, admin_id=admin_id).first()

    if not opp:
        return jsonify({"message": "Not found"}), 404

    db.session.delete(opp)
    db.session.commit()

    return jsonify({"message": "Deleted"})
