# Employee Satisfaction Prediction Project

This project uses a Jupyter notebook to predict employee satisfaction levels based on various features using data analysis and machine learning techniques.

## Overview

- **Data Source**: [Employee Satisfaction Dataset](link_to_dataset)
- **Programming Language**: Python
- **Libraries Used**: pandas, numpy, scikit-learn, matplotlib, seaborn
- **Machine Learning Models**: Random Forest, Gradient Boosting

## Notebook

- **Notebook**: `Bi.ipynb`
    - **Description**: The main notebook for the project.


### Stages

1. **Data Exploration and Analysis:**
    - Conduct exploratory data analysis (EDA) to understand the dataset's structure and characteristics.
    - Visualize the distribution of key features using histograms, box plots, and correlation matrices.
    - Identify any outliers, patterns, or trends in the data that may impact the predictive modeling process.

2. **Feature Engineering Steps:**
    - Handle missing values by imputing or dropping them based on the context.
    - Encode categorical variables using techniques such as one-hot encoding or label encoding.
    - Transform numerical variables, for example, by scaling them to ensure features are on a similar scale.
    - Create new features if there are domain-specific insights that can enhance model performance.

3. **Model Training (Random Forest, Gradient Boosting):**
    - Split the dataset into training and testing sets to assess model generalization.
    - Utilize Random Forest and Gradient Boosting algorithms for model training.
    - Tune hyperparameters to optimize model performance.
    - Train the models on the training set and analyze their ability to capture patterns in the data.

4. **Model Evaluation:**
    - Evaluate model performance using metrics such as Mean Squared Error (MSE) and R-squared.
    - Compare the performance of Random Forest and Gradient Boosting models.
    - Visualize model predictions vs. actual values to understand where the models excel or struggle.
    - Interpret the evaluation results to select the most suitable model for the task.

5. **Ensemble Model Creation and Evaluation:**
    - Create an ensemble model by combining predictions from both Random Forest and Gradient Boosting models.
    - Analyze the ensemble model's performance and compare it to individual models.
    - Assess whether the ensemble approach improves predictive accuracy.
    - Visualize ensemble model predictions and understand how they complement each other.


## Deployment Steps

1. **Prepare Flask App:**
   - Ensure your Flask app serves the machine learning model on a specific port (e.g., `http://localhost:5002`).

2. **Install Ngrok:**
   - Sign up on [Ngrok](https://ngrok.com/) and install it on your machine.

3. **Update Flask App Script:**
   - Modify your Flask app script to integrate Ngrok for tunneling.

4. **Run Flask App:**
   - Start your Flask app using `python app.py`.

5. **Run Ngrok:**
   - Open a new terminal and run `ngrok http 5002` to generate a public URL.

6. **Test Deployed App:**
   - Access your app via the Ngrok URL (e.g., `https://your_ngrok_subdomain.ngrok.io`).

7. **Ngrok URL for Testing:**
   - Utilize the Ngrok-generated URL in your testing script to send requests to the deployed app.

## Model Deployment Using Ngrok

To make the trained employee satisfaction prediction model accessible for real-time predictions, the Flask API has been deployed using Ngrok for tunneling. The consolidated model can be accessed using the following URL: [https://e0e4-102-68-79-99.ngrok-free.app/predict](https://e0e4-102-68-79-99.ngrok-free.app/predict).

## Testing the Deployed Model

To test the deployed model, you can use the provided test.py script. Follow the steps below:

1. Ensure Python is installed on your machine.
2. Open a terminal and navigate to the project directory.
3. Run the test script:

   ```bash
   python test.py

