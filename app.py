from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load user data from JSON file
users = []

try:
    with open('data.json', 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    print("Error: JSON file not found.")
    
# print(users)
# Input validation function
def validate_input(data):
    if not isinstance(data, dict):
        return False
    if 'id' not in data or 'interests' not in data or 'smartness' not in data:
        return False
    if not isinstance(data['id'], int) or not isinstance(data['interests'], list) or not isinstance(data['smartness'], dict):
        return False
    return True

@app.route('/match', methods=['POST'])
def match_users():
    # Validate input JSON
    user_data = request.json
    if not validate_input(user_data):
        return jsonify({"error": "Invalid input format"}), 400
    
    user_interests = user_data.get('interests', [])
    user_smartness = user_data.get('smartness', {})

    matched_users = []
    for user in users:
        if user['id'] != user_data['id']:  # Exclude current user
            common_interests = set(user_interests) & set(user['interests'])
            if common_interests:
                match_score = sum(user_smartness.get(interest, 0) for interest in common_interests)
                matched_users.append({"id": user['id'], "name": user['name'], "match_score": match_score})

    matched_users.sort(key=lambda x: x['match_score'], reverse=True)
    return jsonify(matched_users[:5])  # Return top 5 matched users

if __name__ == '__main__':
    app.run(debug=True)
