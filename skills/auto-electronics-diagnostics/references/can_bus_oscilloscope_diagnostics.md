# CAN Bus Oscilloscope Waveform & Physical Layer Diagnostics

An operational electrical reference for diagnosing High-Speed CAN Bus (ISO 11898-2) networks using a digital storage oscilloscope (DSO).

---

## 1. Electrical Specification Table

| State | Line | Nominal Voltage | Acceptable Range | Differential ($V_{\text{CAN-H}} - V_{\text{CAN-L}}$) |
| :--- | :--- | :--- | :--- | :--- |
| **Recessive (Bit 1)** | CAN-High | 2.5 V | 2.0 V – 3.0 V | $\approx 0.0\text{ V}$ |
| **Recessive (Bit 1)** | CAN-Low | 2.5 V | 2.0 V – 3.0 V | $\approx 0.0\text{ V}$ |
| **Dominant (Bit 0)** | CAN-High | 3.5 V | 3.0 V – 4.25 V | $\mathbf{\approx 2.0\text{ V}}$ |
| **Dominant (Bit 0)** | CAN-Low | 1.5 V | 1.0 V – 2.0 V | $\mathbf{\approx 2.0\text{ V}}$ |

---

## 2. Common Physical Fault Signatures

```
1. Normal Balanced Waveform:
   CAN-H: 2.5V --------/\/\-------- 3.5V
   CAN-L: 2.5V --------\/\/-------- 1.5V
   [Mirror-image symmetry around 2.5V baseline]

2. CAN-H Shorted to Ground (0V):
   CAN-H: 0V ----------------------- (Flatline at 0V)
   CAN-L: 2.5V --------\/\/-------- 1.5V (Distorted, communication failure)

3. CAN-L Shorted to Battery (12V):
   CAN-H: Floating / distorted
   CAN-L: 12V ---------------------- (Flatline at 12V)
   [Triggers transceiver thermal shutdown]

4. Missing One 120-Ohm Termination Resistor:
   Measured resistance = 120 Ohms (instead of 60 Ohms).
   Waveform exhibits ringing, overshoot spikes on signal edges, and reflections.
```

---

## 3. Oscilloscope Setup & Troubleshooting Procedure

```bash
# DSO Setup:
- Channel A: Probe connected to CAN-High (OBD pin 6).
- Channel B: Probe connected to CAN-Low (OBD pin 14).
- Ground clips: Connected to verified chassis ground (OBD pin 4 or 5).
- Timebase: 2 us / div to 10 us / div (for 500 kbps bit analysis) or 1 ms / div (for packet burst analysis).
- Coupling: DC.
- Trigger: Channel A, Rising edge, Threshold ~3.0V.
- Math Channel: Set to [CH A - CH B] to display the pure differential signal.
```
