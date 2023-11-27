from flask import Flask, request, jsonify
import pandas as pd
import joblib

# Load the model
loaded_ensemble_model = joblib.load('C:/Users/User/Downloads/BI-Project/models/ensemble model.pkl')

# Create a new Flask web server
app = Flask(__name__)

# Define the route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the POST request
    data = request.get_json(force=True)

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(data)

    # Use the model to make a prediction
    y_pred_rf_new = loaded_ensemble_model['random_forest'].predict(df)
    y_pred_gb_new = loaded_ensemble_model['gradient_boosting'].predict(df)

    # Ensemble by averaging predictions
    y_pred_ensemble_new = (y_pred_rf_new + y_pred_gb_new) / 2

    # Create a JSON object with the predictions
    response = jsonify({'prediction': list(y_pred_ensemble_new)})

    # Return the JSON object
    return response

if __name__ == '__main__':
    app.run(port=5002, debug=True)
    
      #Open a ngrok tunnel to the flask app
    public_url = ngrok.connect(5002)
    print(f"Public URL: {public_url}")  