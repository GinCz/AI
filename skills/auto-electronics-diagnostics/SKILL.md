---
name: auto-electronics-diagnostics
description: >-
  Automotive electrical systems, ECU tuning, network diagnostics (CAN, LIN, FlexRay, DoIP, J1939), oscilloscope sensor analysis, parasitic drain testing, immobilizers, and EV/Hybrid high-voltage safety.
---
# Automotive Electronics, Network Diagnostics & EV/Hybrid Engineering

A master operational engineering manual for automotive electrical troubleshooting, in-vehicle communication bus analysis, ECU diagnostics, sensor oscilloscope signal tracing, and High-Voltage (EV/HEV) safety protocols.

---

## 1. In-Vehicle Communication Networks & Bus Diagnostics

Modern vehicles utilize layered serial networks to interconnect Electronic Control Units (ECUs):

### A. Controller Area Network (CAN Bus - ISO 11898):
- **Physical Layer**:
  - Twisted pair: `CAN-High` (CAN-H) and `CAN-Low` (CAN-L).
  - **Termination Resistors**: Two **120 $\Omega$** resistors placed at the extreme physical ends of the bus (typically inside the Engine ECU and Instrument Cluster/Gateway).
  - **Static Resistance Check** (Ignition OFF, battery disconnected, measure across OBD-II pins 6 & 14):
    $$R_{\text{total}} = \frac{120 \times 120}{120 + 120} = 60\ \Omega$$
    - If reading **$120\ \Omega$** -> One termination resistor or wiring branch is open-circuit.
    - If reading **$0\ \Omega$** -> Direct short circuit between CAN-H and CAN-L.
    - If reading **$> 120\ \Omega$** or open -> Complete bus disconnection.
- **Dynamic Voltage & Oscilloscope Waveforms** (High-Speed CAN 500 kbps):
  - **Recessive State (Logical 1)**: Both lines idle at approximately **2.5 V** (differential voltage $\approx 0\text{ V}$).
  - **Dominant State (Logical 0)**:
    - `CAN-H` rises to approximately **3.5 V** (+1.0 V swing).
    - `CAN-L` drops to approximately **1.5 V** (-1.0 V swing).
    - Differential voltage ($V_{\text{diff}} = V_{\text{CAN-H}} - V_{\text{CAN-L}}$) $\approx \mathbf{2.0\text{ V}}$.
  - Common Waveform Faults:
    - CAN-H or CAN-L shorted to Ground (0V flatline).
    - CAN-H shorted to Battery 12V (flatline at battery voltage, drives transceiver into thermal shutdown).
    - Distorted, rounded waveforms indicating missing termination, severe capacitive loading, or damaged wiring harness.

### B. LIN Bus (Local Interconnect Network - ISO 17987):
- Single-wire, 12V asynchronous protocol operating at low speed (max 20 kbps).
- Master-Slave architecture used for smart peripherals: Alternator voltage regulators (COM/BSS/LIN), wiper motors, window regulators, climate control flap actuators.
- Recessive level = Battery Voltage (~12.0–14.0 V); Dominant level = Ground (~0.0–1.0 V).

### C. FlexRay & MOST Bus:
- **FlexRay**: High-speed (10 Mbps), dual-channel deterministic bus used in advanced chassis control (active steering, dynamic suspension).
- **MOST (Media Oriented Systems Transport)**: Optical fiber ring network for infotainment. Diagnosed using optical loop bypass connectors (*optická propojka*) to isolate broken control units breaking the optical circuit.

### D. Commercial Truck Protocol (SAE J1939):
- Heavy truck network standard operating at 250 kbps or 500 kbps over CAN.
- Uses Diagnostic Link Connector (DLC) 9-pin Deutsch connector.
- Fault codes formatted as **SPN** (Suspect Parameter Number) and **FMI** (Failure Mode Identifier).

---

## 2. Advanced Diagnostic Protocols & Tooling

### A. OBD-II / EOBD Operational Modes:
- **Mode \$01**: Live sensor data stream (PIDs: RPM, vehicle speed, coolant temp, fuel trims).
- **Mode \$02**: Freeze frame data (snapshot of parameters at the exact moment a DTC was stored).
- **Mode \$03**: Confirmed Diagnostic Trouble Codes (DTC).
- **Mode \$06**: On-Board Monitoring Test Results for non-continuously monitored systems:
  - Essential for identifying misfiring cylinders prior to DTC triggering (TID/CID misfire counts).
  - Catalytic converter and oxygen sensor aging thresholds.

### B. Professional Tool Ecosystems:
- **VAG (Volkswagen, Audi, Škoda, Seat)**: VCDS (HEX-V2 / HEX-NET) for adaptations/coding; ODIS-S / ODIS-E for factory flashing and component protection (*ochrana dílů*).
- **BMW**: ISTA-D (Rheingold) for guided troubleshooting; ISTA-P / E-Sys for ECU coding and programming.
- **Mercedes-Benz**: Xentry Diagnosis / DAS, Vediamo, DTS Monaco.
- **Universal Multi-Brand**: Launch X431, Autel MaxiSys, Delphi DS150E, Bosch KTS.

---

## 3. Sensor & Actuator Oscilloscope Analysis

Multimeters measure root-mean-square (RMS) or average voltage; **only an oscilloscope** reveals transient dropouts, glitches, and phase misalignments.

### A. Crankshaft (CKP) & Camshaft (CMP) Phase Correlation:
- **Hall Effect Sensors**: Digital 0–5V or 0–12V square waves.
- **Inductive / Reluctor Sensors**: Analog AC sine wave where frequency and amplitude increase proportionally with engine speed. Missing tooth indicates TDC reference.
- **Timing Chain Stretch Diagnostics**:
  - Connect Channel A to CKP and Channel B to CMP.
  - Measure the precise number of crankshaft teeth or milliseconds between the missing tooth reference and camshaft sync edge. Compare against golden reference waveforms to identify timing chain stretch without engine disassembly.

### B. Fuel Trim & Lambda / Oxygen Sensor Diagnostics:
- **Short-Term Fuel Trim (STFT)** & **Long-Term Fuel Trim (LTFT)**:
  - Normal range: $-5\%$ to $+5\%$.
  - High Positive Fuel Trim ($> +15\%$ to $+25\%$): Lean condition (vacuum leak, unmetered air after MAF, low fuel pressure, clogged fuel injectors).
  - High Negative Fuel Trim ($< -15\%$ to $-25\%$): Rich condition (leaking injector, high fuel pressure, restricted air intake, stuck EVAP purge valve).
- **Broadband Lambda Sensor (Bosch LSU 4.9)**:
  - Operates via internal oxygen pump cell; current ($I_p$) in microamperes ($\mu\text{A}$) determines air-fuel equivalence ratio $\lambda$. Rapid response to throttle blips.

---

## 4. Vehicle Parasitic Drain & Electrical Distribution

### Parasitic Battery Drain Testing (*Měření klidového odběru*):
1. **Preparation**:
   - Close all door latches manually with a screwdriver while doors remain open to access fuse boxes.
   - Lock vehicle via key fob and wait **20 to 45 minutes** for all ECUs to enter deep sleep mode.
2. **Current Measurement**:
   - Normal quiescent sleep current: **$< 30\text{ mA} - 50\text{ mA}$** (0.03–0.05 A).
   - If drain $> 150\text{ mA} - 1.5\text{ A}$ -> Active parasitic draw discharging battery overnight.
3. **Non-Invasive Voltage Drop Technique**:
   - Measure DC millivolts ($mV$) directly across the test points on the back of each blade fuse without pulling the fuse (pulling fuses wakes sleeping modules).
   - Convert $mV$ drop to current using standard fuse chart (e.g. 1.0 mV across a standard 10A mini fuse indicates $\approx 135\text{ mA}$ flowing through that circuit).

---

## 5. ECU Engineering, Immobilizers & Key Programming

- **Microcontroller & EEPROM Work**:
  - Reading/Writing EEPROMs (e.g. 24Cxx, 93Cxx, 95xxx) and flash microcontrollers (Infineon TriCore TC17xx/TC2xx, Motorola/Freescale MPC5xx/MPC55xx).
  - Bench mode & Boot mode connections using pinout harnesses (eliminating need to desolder chips).
- **Immobilizer (Immo) Architectures**:
  - Transponder keys: Megamos Crypto 48, Hitag 2 (PCF7936), Texas Crypto (4D/4E/DST+).
  - Extracting PIN / Secret Key Code (SKC) from Instrument Cluster, BCM, or Engine ECU.
  - Component Protection (*Ochrana dílů*): Cryptographic pairing between donor modules and gateway/chassis VIN to prevent theft of parts.

---

## 6. High-Voltage (EV & Hybrid) Safety & Architecture

Working on electric (BEV) and hybrid (HEV/PHEV) vehicles requires certified High-Voltage qualifications and strict life-safety protocols:

### A. The 5 Safety Rules for High-Voltage Isolation:
1. **Disconnect Completely (*Odpojit*)**: Turn off ignition, remove key fob to safe distance (> 5m), disconnect 12V auxiliary battery negative terminal.
2. **Secure Against Reconnection (*Zabezpečit proti opětovnému zapnutí*)**: Pull the **Manual Service Disconnect (MSD / orange service plug)** and lock out / tag out (LOTO) with a safety padlock.
3. **Verify Absence of Voltage (*Ověřit beznapěťový stav*)**:
   - Use a calibrated, two-pole high-voltage detector rated for **CAT IV 1000V** (never use a standard multimeter).
   - Test tester on known live source -> Test vehicle HV terminals -> Retest tester on known source.
   - Verify that DC voltage between HV+ and HV-, HV+ and Chassis, and HV- and Chassis is **$< 60\text{ V DC}$** (safe threshold).
4. **Earth & Short-Circuit (where prescribed)**.
5. **Cover Adjacent Live Parts**.

### B. High-Voltage Components & Diagnostics:
- **HVIL (High Voltage Interlock Loop)**: Low-voltage series circuit looping through all HV connectors, lids, and service plugs. If any connector is opened, the BMS instantly drops the main contactors.
- **Battery Management System (BMS)**:
  - Monitoring individual cell voltages (millivolt variance between highest and lowest cell; delta $> 30-50\text{ mV}$ indicates degraded cell pack).
  - Isolation resistance monitoring ($R_{\text{iso}} > 500\ \Omega/\text{V}$ required).
- **Inverter & Power Electronics**:
  - Three-phase AC drive generation via IGBT or SiC MOSFET bridges.
  - Bidirectional DC-DC converter stepping 400V/800V pack voltage down to 12V/14V to charge auxiliary battery.
