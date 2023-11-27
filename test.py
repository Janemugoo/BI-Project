import requests
import json

# Define the URL of the Flask application
url = 'https://e0e4-102-68-79-99.ngrok-free.app/predict'

# Define the test data
test_data = {
    'number_project': [5, 3, 7], # number of projects they have worked on
    'average_montly_hours': [200, 150, 250], # average monthly hours worked
    'performance_evaluation': [0.8, 0.6, 0.9],# performance_evaluation means the last evaluation for an employee last project its between 0.0 and 1.0
    'dept': [2, 1, 3],# department they work for sales, technical, support, IT, product_mng, marketing, RandD, accounting, HR, management
    'time_spend_company': [4, 2, 6],# number of years they have worked for the company
    'salary': [2, 1, 3] # salary level: 1 is low, 2 is medium, 3 is high
}



# Convert the test data into JSON format
data = json.dumps(test_data)

# Send a POST request to the Flask application
response = requests.post(url, data)

# Get the prediction from the response
prediction = response.json()['prediction']

# Convert the prediction to a percentage and format it with two decimal places
formatted_prediction = [f"{pred * 100:.2f}%" for pred in prediction]

# Print the formatted prediction
print(formatted_prediction)