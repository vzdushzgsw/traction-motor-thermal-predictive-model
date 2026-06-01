import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

print("EV Traction Motor Thermal Predictive Engine Active\n")

# 1. Simulate Real Vehicle CAN Bus Telemetry (500 Historical Data Points)
np.random.seed(7)
n_records = 500

# Features: Stator Current (Amps) and Liquid Cooling Flow Rate (Liters/minute)
stator_current_amps = np.random.uniform(50.0, 450.0, n_records)
coolant_flow_lmin = np.random.uniform(2.0, 15.0, n_records)

# Target: Trigger Turtle Mode (1) if current spikes dangerously while cooling flow is low
turtle_mode_triggered = []
for i in range(n_records):
    # Physics rule: High current density causes rapid I²R copper losses
    if stator_current_amps[i] > 350.0 and coolant_flow_lmin[i] < 5.0:
        turtle_mode_triggered.append(1) # 1 = Thermal Boundary Violated! Active Power Clamp
    else:
        turtle_mode_triggered.append(0) # 0 = Thermal Equilibrium (Smooth Cruise)

# Structuring our real-world vehicle diagnostic dataframe
powertrain_telemetry = pd.DataFrame({
    'Stator_Current_Amps': stator_current_amps,
    'Coolant_Flow_Lmin': coolant_flow_lmin,
    'Turtle_Trigger': turtle_mode_triggered
})

# 2. Split Data Channels into Inputs (X) and Target (y)
X = powertrain_telemetry[['Stator_Current_Amps', 'Coolant_Flow_Lmin']]
y = powertrain_telemetry['Turtle_Trigger']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)

# 3. Train the Predictive VCU Brain
ai_brain = LogisticRegression()
ai_brain.fit(X_train, y_train)

# Validate performance
predictions = ai_brain.predict(X_test)
score = accuracy_score(y_test, predictions)

print(f"VCU Core Training complete. Algorithm Prediction Accuracy: {score * 100:.1f}%\n")
print("-" * 65)
print("LIVE COCKPIT DIAGNOSTIC INTERFACE (EMULATING VEHICLE CAN BUS):")
print("-" * 65)

# 4. Interactive Live Prediction Interface
try:
    user_amps = float(input("Enter Live Inverter Stator Current (Range: 50.0A to 450.0A): "))
    user_flow = float(input("Enter Live Cooling Jacket Flow Rate (Range: 2.0 to 15.0 L/min): "))
    
    # Format the real-time sensor packet
    sensor_packet = pd.DataFrame([[user_amps, user_flow]], columns=['Stator_Current_Amps', 'Coolant_Flow_Lmin'])
    
    # Calculate adaptive boundary prediction
    prediction = ai_brain.predict(sensor_packet)[0]
    
    print("\n" + "="*55)
    print("EV POWERTRAIN SYSTEM STATUS REPORT:")
    print("="*55)
    if prediction == 1:
        print("ALERT: CRITICAL STATOR THERMAL OVERLOAD DETECTED!")
        print("Action: Engaging [TURTLE MODE]")
        print("Inverter gate signals clamped to 20% max current capacity.")
    else:
        print("STATUS: [SMOOTH CRUISE]")
        print("Thermal management optimal. Continuous torque discharge permitted.")
    print("="*55)

except ValueError:
    print("Error: Input mismatch. Please enter numerical values only.")
