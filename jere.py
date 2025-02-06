import os
import csv
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_process_kaggle_dataset(dataset_name, output_file, rows_limit=200):
    """
    Downloads a dataset from Kaggle, reads up to `rows_limit` rows, and writes to a new file.
    Handles exceptions during the process.
    """
    try:
        # Initialize Kaggle API
        api = KaggleApi()
        api.authenticate()

        # Download dataset
        print("Downloading dataset...")
        api.dataset_download_files(dataset_name, path="datasets", unzip=True)
        print("Download completed!")

        # Locate the CSV file
        dataset_path = "datasets"
        files = os.listdir(dataset_path)
        csv_file = next((file for file in files if file.endswith(".csv")), None)

        if not csv_file:
            raise FileNotFoundError("CSV file not found in the downloaded dataset.")

        input_file = os.path.join(dataset_path, csv_file)

        # Read and write up to `rows_limit` rows
        with open(input_file, 'r') as infile:
            reader = csv.reader(infile)
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                for i, row in enumerate(reader):
                    if i >= rows_limit:
                        break
                    writer.writerow(row)

        print(f"Dataset processed and saved as {output_file}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Specify the dataset and output file
kaggle_dataset = "abdoda1/classification-for-sandstone-and-shale"
output_file_name = "For_Prediction.csv"

# Call the function
download_and_process_kaggle_dataset(kaggle_dataset, output_file_name)

# File to analyze
output_file = 'For_Prediction.txt'

# Initialize variables to count rows, columns, and unique classes
row_count = 0
column_count = 0
classes = set()

# Analyze the output file
with open(output_file, 'r') as file:
    reader = csv.reader(file, delimiter=',')
    for i, row in enumerate(reader):
        if i == 0:
            column_count = len(row)  # Count columns from the header
        else:
            row_count += 1
            classes.add(row[-1].strip())  # Add the last column value to the set

print(f"Number of rows: {row_count}")
print(f"Number of columns: {column_count}")
print(f"Number of unique classes: {len(classes)}")
print(f"Classes: {classes}")

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('Data1.txt', delimiter=',', header=0)
data.columns = ['effporosity', 'Vshale', 'Class']  # Rename columns

# Features and target
X = data[['effporosity', 'Vshale']]
y = data['Class']

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict continuous values
y_pred_continuous = model.predict(X_test)

# Apply threshold (0.5) to classify
threshold = 0.5
y_pred = np.where(y_pred_continuous >= threshold, 1, 0)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred))
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Visualization of predictions
sns.scatterplot(x=y_test, y=y_pred_continuous)
plt.axhline(y=threshold, color='red', linestyle='--', label='Threshold = 0.5')
plt.xlabel('True Values')
plt.ylabel('Predicted Values')
plt.title('Linear Regression Predictions')
plt.legend()
plt.show()

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def run_linear_regression():
    # Load the dataset
    data = pd.read_csv('Data1.txt', delimiter=',', header=0)
    data.columns = ['effporosity', 'Vshale', 'Class']  # Rename columns

    # Features and target
    X = data[['effporosity', 'Vshale']]
    y = data['Class']

    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict continuous values
    y_pred_continuous = model.predict(X_test)

    # Apply threshold (0.5) to classify
    threshold = 0.5
    y_pred = np.where(y_pred_continuous >= threshold, 1, 0)

    # Evaluate the model
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

    # Visualization of predictions
    sns.scatterplot(x=y_test, y=y_pred_continuous)
    plt.axhline(y=threshold, color='red', linestyle='--', label='Threshold = 0.5')
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title('Linear Regression Predictions')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    run_linear_regression()