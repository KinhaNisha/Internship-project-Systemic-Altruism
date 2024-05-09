from flask import Flask, request, jsonify
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import MultiLabelBinarizer
import json

app = Flask(__name__)

# Load user data from the JSON file
def load_user_data():
    with open('users.json', 'r') as file:
        return json.load(file)     

@app.route('/')
def home():
    return "User Matching API is running!"

def find_best_match(input_user, all_users):
    best_score = 0
    best_match = None

    # Flatten the list of interests and preferences into sets
    input_interests = set()
    for interest_list in input_user['interests'].values():
        input_interests.update(interest_list)

    input_preferences = set()
    for pref_list in input_user['preferences'].values():
        input_preferences.update(pref_list)

    for user in all_users['users']:
        if user['id'] == input_user['id']:
            continue

        # Flatten the list of interests and preferences for comparison user
        user_interests = set()
        for interest_list in user['interests'].values():
            user_interests.update(interest_list)

        user_preferences = set()
        for pref_list in user['preferences'].values():
            user_preferences.update(pref_list)

        # Calculate match score based on shared interests and preferences
        # Simple scoring: count of shared items
        score = len(input_interests & user_interests) + len(input_preferences & user_preferences)

        if score > best_score:
            best_score = score
            best_match = user

    return best_match


@app.route('/match', methods=['POST'])
def match_user():
    data = request.get_json()
    all_users = load_user_data()
    best_match = find_best_match(data, all_users)
    return jsonify(best_match)




# second Method
def flatten_values(d):
    """Flatten values of a dictionary where values are lists, handle non-list items gracefully."""
    result = []
    for value in d.values():
        if isinstance(value, list):
            result.extend(value)
        else:
            result.append(value)
    return result


def load_user_data_and_features():
    with open('users.json', 'r') as file:
        users = json.load(file)['users']

    # Initialize binarizers
    mlb_interests = MultiLabelBinarizer()
    mlb_preferences = MultiLabelBinarizer()

     # Properly extract and flatten interests and preferences
    interests = [flatten_values(user['interests']) for user in users]
    preferences = [flatten_values(user['preferences']) for user in users]

    # Fit and transform data
    interests_encoded = mlb_interests.fit_transform(interests)
    preferences_encoded = mlb_preferences.fit_transform(preferences)

    # Concatenate both feature sets into one array per user
    features = np.hstack((interests_encoded, preferences_encoded))
    
    return users, features, mlb_interests, mlb_preferences


MAX_DISTANCE = 10

users, features, mlb_interests, mlb_preferences = load_user_data_and_features()
model = NearestNeighbors(n_neighbors=1, algorithm='ball_tree')
model.fit(features)
@app.route('/match/k-nearest', methods=['POST'])
def match_user_knn():
    input_data = request.get_json()
    
    # Extract the input user ID (ensure your input JSON contains 'id')
    input_user_id = input_data.get('id')
    
    # Flatten and prepare input data for interests and preferences
    interests = [item for sublist in input_data['interests'].values() for item in sublist]
    preferences = [item for sublist in input_data['preferences'].values() for item in sublist]

    # Generate feature vectors directly without additional nesting
    interests_vector = mlb_interests.transform([interests])
    preferences_vector = mlb_preferences.transform([preferences])

    # Combine into a single feature vector
    input_features = np.hstack((interests_vector, preferences_vector))

    # Perform nearest neighbor search excluding the input user
    # Exclude input user by masking other user features before search
    mask = [user['id'] != input_user_id for user in users]  # Create a mask to exclude input user
    filtered_features = features[mask]  # Apply mask to features array
    filtered_users = [users[i] for i, m in enumerate(mask) if m]  # Filter user data

    # Find the nearest neighbor in the filtered dataset
    if filtered_features.size > 0:
        distances, indices = model.kneighbors(input_features, n_neighbors=1, return_distance=True)
        best_match = filtered_users[indices[0][0]]
        distance = distances[0][0]

        # Calculate match percentage
        match_percentage = max(0, 100 * (1 - distance / MAX_DISTANCE))

        # Prepare response including the match percentage
        response = {
            "match_percentage": match_percentage,
            "match": best_match
        }
    else:
        response = {
            "error": "No other users to match against."
        }

    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
