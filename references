# Telemetry Parameter & Physics References
This document outlines the international engineering standards and physics principles used to establish the dataset boundaries for this EV Traction Motor thermal simulation.

---

### 1. Stator Winding Current Limits (50.0A - 450.0A)
The simulated current bounds map directly to international testing protocols for mid-to-high performance global passenger EV traction systems.

* **Nominal Cruise (50A - 150A):** Represents standard steady-state highway and urban cruising speeds.
* **Transient Peak Acceleration (350A - 450A):** Represents maximum transient torque demands under wide-open throttle conditions.
* **Global Benchmark:** Performance metrics comply with **ISO 21782**, the global standard for testing electric propulsion components in road vehicles. High-voltage powertrain architectures typically encounter maximum thermal evaluation limits within this 450A phase current envelope.
* **Reference Link:** [ISO 21782-1:2019 Test Specifications](https://www.iso.org/standard/69592.html)

---

### 2. Cooling Jacket Fluid Flow Rate (2.0 - 15.0 L/min)
The cooling system simulates a standard liquid water-glycol auxiliary loop commonly utilized by vehicle manufacturers globally.

* **Restricted Flow (2.0 - 5.0 L/min):** Models low-demand economy modes or system restrictions (e.g., fluid aeration or pump bottlenecks).
* **Maximum Heat Rejection (10.0 - 15.0 L/min):** Models full auxiliary electric pump activation during severe thermal stress.
* **Global Benchmark:** Empirical evaluations of liquid housing jackets for automotive passenger EV drivetrains confirm standard volumetric flow rates scale from a minimum operating threshold of 2.0 L/min to a peak heat rejection ceiling of 15.0 L/min.
* **Reference Link:** [ResearchGate: Survey of Drivetrain Cooling Methods](https://www.researchgate.net/publication/336414718_A_Survey_of_Different_Cooling_Methods_for_Traction_Motor_Application)

---

### 3. Thermal Dynamics Physics Rule ($I^2R$ Losses)
The safety override rule programmed into the dataset generator utilizes foundational electrical engineering equations rather than manufacturer-specific parameters.

$$\text{Joule Heating Losses } (P) = I^2 \cdot R$$

* **The Logic:** Because current ($I$) has a squared relationship with thermal power generation, ramping from nominal cruise to peak current generates roughly **9 times** more thermal energy within the copper slot windings. 
* **The Override:** If motor current crosses $>350\text{A}$ while cooling fluid flow is choked below $5.0\text{ L/min}$, conductive thermal dissipation drops below safe operating tolerances. This threatens stator insulation, requiring the VCU to trigger immediate current-clamping ("Turtle Mode").
* **Reference Link:** [HyperPhysics: Joule Heating & Resistive Power Losses](http://hyperphysics.phy-astr.gsu.edu/hbase/electric/joule.html)
