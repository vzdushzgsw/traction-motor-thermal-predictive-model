### Binary Classification for Powertrain Thermal Stator Preservation

This repository features a lightweight predictive machine learning model acting as an intelligent safety layer for an electric vehicle (EV) traction motor. By dynamically mapping the intersection between driver throttle loads (current density demand) and liquid cooling pump flow rates, this engine classifies operational health states and triggers a safety "Turtle Mode" constraint before critical stator core insulation degradation occurs.

---

### Repository Architecture

1. **[README.md](/README.md)**
   * Strategic overview, technical context, and quick-start roadmap.
2. **[scripts/motor_predictor.py](/scripts/motor_predictor.py)**
   * Self-contained operational script comprising data compilation, Logistic Regression model training, validation metrics, and an interactive command-line cockpit simulator.

---

### Domain Significance

In EV powertrain development, stomping on the accelerator pedal causes massive electrical current to surge through the stator windings, generating instantaneous copper losses (heating). If liquid cooling flow performance drops simultaneously, thermal localized hotspots occur. If left unchecked, this degrades copper line insulation ending in motor short-circuit.

Instead of waiting for slow physical temp sensors to register a delayed spike, this module applies a **Logistic Regression** classifier to construct a dynamic decision boundary. 
It flags thermal overload indicators and is ahead of hardware degradation thresholds.
