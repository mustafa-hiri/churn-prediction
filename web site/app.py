from flask import Flask, render_template, request, jsonify
import requests
import json  # Import json to handle string to JSON conversion

app = Flask(__name__)

# Update with your actual API Gateway URL including the root path
API_GATEWAY_URL = 'https://n270eeux89.execute-api.us-east-2.amazonaws.com/model01/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form as a single comma-separated string
    input_data = request.form.get('inputData', '')  # Default to an empty string if not provided

    # Prepare the data as a JSON payload for the API Gateway
    payload = {'data': input_data}

    # Send a POST request to the API Gateway
    try:
        response = requests.post(API_GATEWAY_URL, json=payload)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
        
        # Check if the response content is JSON and parse the body as JSON
        if response.headers.get('Content-Type') == 'application/json':
            result = json.loads(response.json().get('body', '{}'))  # Convert the string inside 'body' to JSON
            predicted_value = result.get('predicted_value', 'N/A')
            predicted_label = result.get('predicted_label', 'N/A')
        else:
            # If the response is not JSON, log the raw response
            return render_template('index.html', input_data=input_data, predicted_value="Invalid response format", predicted_label="Invalid response format")
        
    except requests.exceptions.HTTPError as http_err:
        # Display HTTP errors
        return render_template('index.html', input_data=input_data, predicted_value=f"HTTP Error: {http_err}", predicted_label="N/A")
    except Exception as e:
        # Display other exceptions
        return render_template('index.html', input_data=input_data, predicted_value=f"Error: {str(e)}", predicted_label="N/A")

    return render_template('index.html', input_data=input_data, predicted_value=predicted_value, predicted_label=predicted_label)

if __name__ == '__main__':
    app.run(debug=True)
