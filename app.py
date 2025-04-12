from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model (ensure it's in the right path)
model = pickle.load(open('model/gwp.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/predict")
def predict_form():
    return render_template('predict.html')

@app.route("/submit", methods=['POST'])
@app.route("/submit", methods=['POST'])
def submit_page():
    # Retrieve the form data
    quarter = request.form['quarter']
    department = request.form['department']
    day = request.form['day']
    team = request.form['team']
    targeted_productivity = request.form['targeted_productivity']
    smv = request.form['smv']
    over_time = request.form['over_time']
    incentive = request.form['incentive']
    idle_time = request.form['idle_time']
    idle_men = request.form['idle_men']
    no_of_style_change = request.form['no_of_style_change']
    no_of_workers = request.form['no_of_workers']
    month = request.form['month']

    # Collect data into a list that the model can process
    total = [[int(quarter), int(department), int(day), int(team),
              float(targeted_productivity), float(smv), int(over_time), int(incentive),
              float(idle_time), int(idle_men), int(no_of_style_change), float(no_of_workers), int(month)]]
    
    # Use the model to predict
    prediction = model.predict(total)[0]

    # Determine the productivity level based on the prediction value
    if prediction <= 0.3:
        text = '" Averagely productive ".'
    elif prediction > 0.3 and prediction <= 0.8:
        text = '" Medium productive ".'
    else:
        text = '" Highly productive ".!'
        
    # Return the result to the user
    return render_template('submit.html', prediction_text=text)


if __name__ == "__main__":
    app.run(debug=True)


"""
Project: Employee Performance Prediction using ML
Developer: Vinay
Year: 2025
"""
