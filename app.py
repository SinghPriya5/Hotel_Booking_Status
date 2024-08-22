from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model_pipeline_final.joblib')

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    # Collect form data
    data = {
        'lead_time': float(request.form.get('lead_time')),
        'arrival_date_year': int(request.form.get('arrival_date_year')),
        'arrival_date_month': request.form.get('arrival_date_month'),
        'arrival_date_week_number': int(request.form.get('arrival_date_week_number')),
        'arrival_date_day_of_month': int(request.form.get('arrival_date_day_of_month')),
        'stays_in_weekend_nights': int(request.form.get('stays_in_weekend_nights')),
        'stays_in_week_nights': int(request.form.get('stays_in_week_nights')),
        'adults': int(request.form.get('adults')),
        'children': int(request.form.get('children')),
        'babies': int(request.form.get('babies')),
        'meal': request.form.get('meal'),
        'country': request.form.get('country'),
        'market_segment': request.form.get('market_segment'),
        'distribution_channel': request.form.get('distribution_channel'),
        'is_repeated_guest': int(request.form.get('is_repeated_guest')),
        'previous_cancellations': int(request.form.get('previous_cancellations')),
        'previous_bookings_not_canceled': int(request.form.get('previous_bookings_not_canceled')),
        'reserved_room_type': request.form.get('reserved_room_type'),
        'assigned_room_type': request.form.get('assigned_room_type'),
        'booking_changes': int(request.form.get('booking_changes')),
        'deposit_type': request.form.get('deposit_type'),
        'agent': request.form.get('agent'),
        'company': request.form.get('company'),
        'days_in_waiting_list': int(request.form.get('days_in_waiting_list')),
        'customer_type': request.form.get('customer_type'),
        'adr': float(request.form.get('adr')),
        'required_car_parking_spaces': int(request.form.get('required_car_parking_spaces')),
        'total_of_special_requests': int(request.form.get('total_of_special_requests')),
    }

    # Convert to DataFrame
    df = pd.DataFrame([data])

    # Predict using the model
    prediction = model.predict(df)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
