## Overview

This repo features an intelligent, data-driven safety layer designed for eV traction motor protection. By simulating real-world Controller Area Network (CAN) bus telemetry, this software utilizes a Logistic Regression model to evaluate the critical thermal boundary.

When the model predicts a high risk of overheating, it triggers a Vehicle Control Unit (VCU) override to engage an adaptive **"Turtle Mode"**. This safety feature instantly limits the inverter's power output, protecting the motor's internal wire insulation from thermal damage or short circuits.

### Core Telemetry Features
* **Motor Current (`Stator_Current_Amps`):** Simulates the real-time electrical current drawn by the motor, ranging from a light 50.0A cruise up to a heavy 450.0A acceleration.
* **Coolant Flow (`Coolant_Flow_Lmin`):** Simulates the liquid cooling system's fluid flow rate, ranging from a restricted 2.0 L/min up to a maximum pump capacity of 15.0 L/min.
* **Prediction Target (`Turtle_Trigger`):** The final AI output decision (`0` = Safe / Normal Operation, `1` = Overheating Risk / Activate Turtle Mode).

This project was developed and validated inside **Google Colab**. You can run the interactive live cockpit interface instantly without installing any local Python environment.
