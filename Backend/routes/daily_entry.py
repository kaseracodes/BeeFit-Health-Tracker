from flask import Blueprint, request, jsonify
from controllers import daily_entry as controller
from schemas.daily_entry import DailyEntrySchema

daily_entry_bp = Blueprint('daily_entry_bp', __name__)
entry_schema = DailyEntrySchema()
entries_schema = DailyEntrySchema(many=True)

@daily_entry_bp.route('/', methods=['POST'])
def create():
    data = request.get_json()
    entry = controller.create_entry(data)
    return entry_schema.jsonify(entry), 201

@daily_entry_bp.route('/', methods=['GET'])
def get_all():
    entries = controller.get_all_entries()
    return entries_schema.jsonify(entries), 200

@daily_entry_bp.route('/<int:id>', methods=['GET'])
def get_one(id):
    entry = controller.get_entry_by_id(id)
    return entry_schema.jsonify(entry), 200

@daily_entry_bp.route('/<int:id>', methods=['PUT'])
def update(id):
    data = request.get_json()
    entry = controller.update_entry(id, data)
    return entry_schema.jsonify(entry), 200

@daily_entry_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    controller.delete_entry(id)
    return jsonify({'message': 'Entry deleted'}), 204
