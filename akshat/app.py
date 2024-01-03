

'''import json
import time
from flask import Flask, request, jsonify,render_template

app = Flask(__name__)

def write_coordinates_to_json(coordinates):
    with open('coordinates.json', 'w') as json_file:
        json.dump(coordinates, json_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_coordinates', methods=['POST'])
def receive_coordinates():
    data = request.get_json()
    center_x = data['centerX']
    center_y = data['centerY']

    # Print received coordinates to the server console
    print(f"Received coordinates: X={center_x}, Y={center_y}")

    # Write coordinates to JSON file
    write_coordinates_to_json({'X': center_x, 'Y': center_y})

    return jsonify({'message': 'Coordinates received successfully'})

if __name__ == '__main__':
    while True:
        app.run(host='0.0.0.0', port=5000, debug=True)  # Prevent Flask from restarting in each loop
        #time.sleep(10)  # Sleep for 10 seconds before writing to JSON file again'''

'''import json
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

def write_coordinates_to_json(coordinates):
    with open('coordinates.json', 'w') as json_file:
        json.dump(coordinates, json_file)

@app.route('/')
def index():
    return render_template('index.html')




@app.route('/send_coordinates', methods=['POST'])
def receive_coordinates():
    data = request.json  # Assuming data is sent as JSON
    center_x = data['centerX']
    center_y = data['centerY']

    # Print received coordinates to the server console
    print(f"Received coordinates: X={center_x}, Y={center_y}")

    # Write coordinates to JSON file
    write_coordinates_to_json({'X': center_x, 'Y': center_y})

    return jsonify({'message': 'Coordinates received successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True,ssl_context=("cert.pem", "key.pem"))
    app.wait(10)'''
'''import json
from flask import Flask, render_template, session, request, jsonify
import uuid
import os

app = Flask(__name__)
app.secret_key = '1244555'  # Replace with your actual secret key
def write_coordinates_to_json(coordinates):
    with open('coordinates.json', 'w') as json_file:
        json.dump(coordinates, json_file)

def generate_unique_id():
    return str(uuid.uuid4())

@app.route('/')
def home():
    if 'user_id' not in session:
        session['user_id'] = generate_unique_id()
    return render_template('index.html', user_id=session['user_id'])

@app.route('/send_coordinates', methods=['POST'])
def send_coordinates():
    if request.method == 'POST':
        data = request.get_json()
        user_id = data.get('userID')
        coordinates = data.get('coordinates')
        # Process the received data as needed
        return jsonify({'status': 'success', 'user_id': user_id, 'coordinates': coordinates})

@app.route('/send_waves', methods=['POST'])
def send_waves():
    data = request.get_json()
    user_id = data.get('userID')
    wave_count = data.get('waveCount')

    # Specify the file path (you can change this to your preferred location)
    file_path = './received_data.json'

    # Write data to file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

    return jsonify({'status': 'success', 'user_id': user_id, 'wave_count': wave_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=("cert.pem", "key.pem"))'''


from flask import Flask, render_template, session, request, jsonify
import uuid
import json

app = Flask(__name__)
app.secret_key = '123414'  # Replace with your actual secret key

def generate_unique_id():
    return str(uuid.uuid4())

@app.route('/')
def home():
    if 'user_id' not in session:
        session['user_id'] = generate_unique_id()
    return render_template('index.html', user_id=session['user_id'])

@app.route('/send_waves', methods=['POST'])
def send_waves():
    data = request.get_json()
    user_id = data.get('userID')
    wave_count = data.get('waveCount')

    # Specify the file path for saving the data
    file_path = 'received_data.json'

    # Append data to the file
    with open(file_path, 'a') as file:
        json.dump({'user_id': user_id, 'wave_count': wave_count}, file)
        file.write('\n')  # Add a newline for readability

    return jsonify({'status': 'success', 'user_id': user_id, 'wave_count': wave_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=("cert.pem", "key.pem"))




