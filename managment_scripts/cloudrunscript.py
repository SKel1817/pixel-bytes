import functions_framework
from flask import jsonify, request
from datetime import datetime

# In-memory storage for pet's hunger data
pet_data = {
    'hunger_level': 100,
    'last_fed': datetime.now().date()
}

# Constants
HUNGER_DECREASE = 25
HUNGER_INCREASE = 25
MAX_HUNGER = 100
HUNGRY_THRESHOLD = 50

@functions_framework.http
def manage_hunger(request):
    """HTTP Cloud Function to manage pet's hunger level."""
    global pet_data

    # Handle CORS preflight request
    if request.method == 'OPTIONS':
        # Allows GET, POST, DELETE methods from any origin with the Content-Type header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }
        return ('', 204, headers)

    # Calculate days since last fed
    today = datetime.now().date()
    days_unfed = (today - pet_data['last_fed']).days

    # Decrease hunger level based on days unfed
    if days_unfed > 0:
        pet_data['hunger_level'] -= HUNGER_DECREASE * days_unfed
        pet_data['hunger_level'] = max(pet_data['hunger_level'], 0)
        pet_data['last_fed'] = today

    if request.method == 'GET':
        # Determine hunger status
        status = 'hungry' if pet_data['hunger_level'] < HUNGRY_THRESHOLD else 'not hungry'
        response = jsonify({
            'hunger_level': pet_data['hunger_level'],
            'status': status
        })
    elif request.method == 'POST':
        # Increase hunger level when fed
        pet_data['hunger_level'] += HUNGER_INCREASE
        pet_data['hunger_level'] = min(pet_data['hunger_level'], MAX_HUNGER)
        pet_data['last_fed'] = today
        response = jsonify({
            'message': 'Pet has been fed.',
            'hunger_level': pet_data['hunger_level']
        })
    elif request.method == 'DELETE':
        # Reset hunger level to zero for testing
        pet_data['hunger_level'] = 0
        response = jsonify({
            'message': 'Pet hunger level reset to zero for testing.',
            'hunger_level': pet_data['hunger_level']
        })
    else:
        response = jsonify({'error': 'Method not allowed.'}), 405

    # Add CORS headers to the response
    headers = {
        'Access-Control-Allow-Origin': '*'
    }
    return response, 200, headers
