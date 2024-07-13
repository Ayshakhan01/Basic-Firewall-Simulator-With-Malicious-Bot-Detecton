import pandas as pd
from prophet import Prophet

# Load the historical data
data = pd.read_csv('network_data.csv')

# Aggregate the data by date
data['date'] = pd.to_datetime(data['date'])
aggregated_data = data.groupby('date')['f'].sum().reset_index()
aggregated_data.columns = ['ds', 'y']  # Rename columns to fit Prophet's requirements

# Initialize the model
model = Prophet()

# Fit the model
model.fit(aggregated_data)

# Create a DataFrame for future dates
future = model.make_future_dataframe(periods=30)  # Forecast for the next 30 days

# Generate the forecast
forecast = model.predict(future)

# Save the forecasted data
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv('forecasted_data.csv', index=False)
