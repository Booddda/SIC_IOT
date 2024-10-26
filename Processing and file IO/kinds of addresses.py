import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import psutil

log_file_path = '2023-09-08-pub.log'  # Replace with the actual log file path

# Read the log file into a pandas DataFrame
log_data = pd.read_csv(log_file_path, parse_dates=[0], header=None, names=['Timestamp', 'CPU Usage', 'Num Logical CPUs', 'Used Memory', 'Used Disk Space', 'Host IP'])

# Extract the relevant columns for regression
X = log_data[['Num Logical CPUs', 'Used Memory', 'Used Disk Space']]
y = log_data['CPU Usage']

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X, y)

# Generate the date for which you want to predict CPU usage
prediction_date = datetime.strptime('2023-09-09', '%Y-%m-%d')

# Predict CPU usage for the specified date
prediction_X = [[psutil.cpu_count(logical=True), psutil.virtual_memory().used, psutil.disk_usage('/').used]]
predicted_cpu_usage = model.predict(prediction_X)

# Print the predicted CPU usage
print(f"Predicted CPU usage for {prediction_date.date()}: {predicted_cpu_usage[0]}")