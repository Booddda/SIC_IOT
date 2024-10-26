import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime
import psutil

log_file_path = '2023-09-08-pub.log' 
colnames = ['Time', 'CPU Usage', 'Number logical CPUs', 'Used Memory', 'Used Disk Space', 'Host IP']
log_data = pd.read_csv(log_file_path, sep =",", header=None, names=colnames)

X = log_data[['Used Memory']]
Y = log_data['CPU Usage']

#create linear regression model
model = LinearRegression().fit(X, Y)

used_memory_perdict_value = int(input("Enter the used memory value u want to predict: "))

X_pred = [[used_memory_perdict_value]]

#predict the output
predicted_cpu_usage = model.predict(X_pred)

print(f"Predicted CPU usage: {predicted_cpu_usage}")