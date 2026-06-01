import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("Turtle Mode Predictive Engine ON\n")

# 1. Create Mock Sensor Driving Data (500 virtual trips)
np.random.seed(7)
n_drivers = 500

# Features: Throttle load and cooling pump status (scaled 1 to 10)
throttle_load = np.random.uniform(1.0, 10.0, n_drivers)
cooling_pump = np.random.uniform(1.0, 10.0, n_drivers)

# Target: Assign Turtle Mode (1) if throttle is pushed high while cooling is low
turtle_mode_triggered = []
for i in range(n_drivers):
    if throttle_load[i] > 7.5 and cooling_pump[i] < 3.5:
        turtle_mode_triggered.append(1) # 1 = Overheated! Turtle Mode Active
    else:
        turtle_mode_triggered.append(0) # 0 = Optimal Operation

# Convert arrays into a structured spreadsheet/dataframe
driving_data = pd.DataFrame({
    'Throttle_Load': throttle_load,
    'Cooling_Pump_Speed': cooling_pump,
    'Turtle_Trigger': turtle_mode_triggered
})

# 2. Split Data into Inputs (X) and Predictions (y)
X = driving_data[['Throttle_Load', 'Cooling_Pump_Speed']]
y = driving_data['Turtle_Trigger']

# Hold back 20% of the data to test the AI later
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# 3. Train the Binary Classifier
ai_brain = LogisticRegression()
ai_brain.fit(X_train, y_train)

# Calculate model performance accuracy
predictions = ai_brain.predict(X_test)
score = accuracy_score(y_test, predictions)

print(f"Training Complete! Prediction Accuracy: {score * 100:.1f}%\n")
print("-" * 60)
print("TEST THE DIGITAL TWIN COCKPIT LIVE:")
print("-" * 60)

# 4. Interactive Live Prediction Interface
try:
    user_throttle = float(input("Enter virtual Throttle Load (1 = Eco, 10 = Racing Track): "))
    user_cooling = float(input("Enter Cooling Pump Status (1 = Broken, 10 = Max Flow): "))
    
    # Bundle user entries into the exact matching schema format
    user_case = pd.DataFrame([[user_throttle, user_cooling]], columns=['Throttle_Load', 'Cooling_Pump_Speed'])
    
    # Run prediction calculation
    prediction = ai_brain.predict(user_case)[0]
    
    print("\n" + "="*45)
    print("EV SYSTEM STATUS REPORT:")
    print("="*45)
    if prediction == 1:
        print("WARNING: [TURTLE MODE ON]")
        print("Thermals critical. Core system power restricted to 20%.")
    else:
        print("STATUS: [SMOOTH CRUISE]")
        print("Thermal management optimal. Full power discharge permitted.")
    print("="*45)

except ValueError:
    print("Please enter numerical values only")
