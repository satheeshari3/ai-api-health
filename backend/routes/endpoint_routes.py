from flask import Blueprint, request, jsonify

from services.endpoint_service import create_endpoint, get_all_endpoints
from services.health_service import check_api_health
from services.ai_service import explain_error
from utils.validator import is_valid_url

endpoint_bp = Blueprint("endpoint", __name__)


@endpoint_bp.route("/endpoints", methods=["POST"])
def add_endpoint():

    data = request.json
    url = data.get("url")
    name = data.get("name")

    if not is_valid_url(url):
        return jsonify({"error": "Invalid URL"}), 400

    endpoint = create_endpoint(name, url)

    return jsonify({"id": endpoint.id})


@endpoint_bp.route("/endpoints", methods=["GET"])
def list_endpoints():

    endpoints = get_all_endpoints()

    return jsonify([
        {"id": e.id, "name": e.name, "url": e.url}
        for e in endpoints
    ])


@endpoint_bp.route("/check/<int:id>")
def check_endpoint(id):

    endpoints = get_all_endpoints()
    endpoint = next((e for e in endpoints if e.id == id), None)

    if not endpoint:
        return {"error": "not found"}, 404

    log = check_api_health(endpoint)

    explanation = explain_error(log.status)

    return {
        "status": log.status,
        "response_time": log.response_time,
        "ai_explanation": explanation
    }