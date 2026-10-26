---
name: auto-mechanics-powertrain
description: >-
  Automotive mechanical engineering and repair: ICE engines (petrol, diesel Common Rail, classic carbs), heavy commercial trucks (pneumatic brakes, SCR/AdBlue, Euro 3-6), transmissions (manual, automatic, DSG/DCT), chassis, steering, and suspension overhaul.
---
# Automotive Mechanics, Powertrain & Commercial Vehicle Overhaul

A master operational engineering manual for automotive mechanics, engine rebuilding, heavy-duty commercial truck systems, transmissions, and chassis overhaul across modern and classic vehicles.

---

## 1. Internal Combustion Engine (ICE) Mechanics & Rebuilding

### A. Petrol / Gasoline Engines (MPI, Direct Injection TSI/GDI):
- **Fuel Delivery Systems**:
  - Multi-Point Fuel Injection (MPI): Low pressure (3–4 bar), manifold injection.
  - Direct Injection (GDI, TSI/TFSI): High-pressure mechanical fuel pump driven by camshaft lobe (150–350 bar), carbon build-up on intake valves (cleaning via walnut blasting / chemical soaking), piezo vs solenoid high-pressure injectors.
- **Variable Valve Timing (VVT / VANOS / VTEC)**:
  - Oil control valves (solenoids), camshaft phasers. Diagnosis of timing rattle on cold start (worn camshaft sprockets or check valve failure).

### B. Diesel Engines (Common Rail & Pumpe-Düse):
- **Common Rail (CR) Architecture**:
  - High-pressure pump (Bosch CP1/CP3/CP4, Delphi, Denso) reaching 1,600 to 2,500 bar.
  - Fuel return flow test (*přepadová zkouška vstřikovačů*): Measuring return line volume across all cylinders via graduated vials to detect leaking injector valves causing hard hot start or rail pressure drop (DTC P0087).
  - High-pressure pump CP4 failure warning: Swarf/metal particles in fuel filter housing requiring complete fuel system replacement (tank, lines, rails, injectors).
- **Pumpe-Düse (PD / Unit Injector)**:
  - Camshaft-driven individual unit injectors; adjusting pre-load rocker lash (turn bottom out, back off 180°–225°).
  - Worn injector seats in aluminum cylinder head causing fuel mixing into engine oil or hard starting.

### C. Classic Engines & Carburetion:
- **Carburetor Tuning & Overhaul (Weber, Solex, Pierburg, Zenith)**:
  - Float height measurement and needle valve sealing.
  - Idle mixture (*bohatost směsi*) adjustment via idle screw and CO meter; secondary throttle progression; accelerator pump diaphragm check.
  - Multi-carburetor vacuum synchronization using flow meters / manometer sync gauges.
- **Mechanical Ignition Distributors**:
  - Breaker points gap and dwell angle (*úhel sepnutí kontaktů* - typically 50°–54° on 4-cylinder engines).
  - Stroboscopic timing light dynamic setting: Initial base timing with vacuum advance hose disconnected and plugged; verifying centrifugal advance curve across RPM range.

### D. Engine Overhaul Tolerances & Diagnostics:
- **Compression & Cylinder Leak-Down Testing (*Měření komprese a tlakové ztráty válců*)**:
  - Dry vs. wet compression test: If adding 10ml of engine oil into spark/glow plug hole restores low compression -> worn piston rings/cylinder bore; if unchanged -> leaking intake/exhaust valves or blown head gasket.
  - Leak-down test: Supplying regulated compressed air (e.g. 6 bar) at TDC compression:
    - Air hissing from intake manifold -> leaking intake valve.
    - Air hissing from exhaust pipe -> leaking exhaust valve.
    - Air bubbles in expansion tank -> cracked cylinder head or blown head gasket.
    - Air whistling from oil filler cap / dipstick -> worn piston rings or cylinder wall scoring.
- **Precision Metrology**:
  - Cylinder bore ovality and taper (*ovalita a kuželovitost válce*) measured via internal bore gauge (*dutinoměr*).
  - Crankshaft journal clearance verified using **Plastigauge** (typical clearance 0.025 mm – 0.050 mm).
  - Cylinder head surface planarity checked with precision straightedge and feeler gauge (max deflection < 0.05 mm across head length).

---

## 2. Heavy Commercial Vehicles & Trucks (Scania, Volvo, MAN, DAF, Actros)

### A. Pneumatic Air Brake Systems:
- **Air Generation & Preparation**: Compressor, integrated air dryer with desiccant cartridge (*vysoušeč vzduchu*), four-circuit protection valve (*čtyřokruhový jisticí ventil*) isolating independent circuits (front axle, rear axle, trailer, auxiliary).
- **Actuation & Parking**:
  - Foot brake valve (*pedálový brzdový ventil*), relay valves, ABS/EBS modulators.
  - Spring brake actuators (*pružinové brzdové válce - Tristop*): Spring-applied parking brake; mechanical wind-off procedure for emergency towing.
  - Brake disc and drum overhaul: Minimum thickness, heat cracks, pneumatic slack adjusters (*automatické stavěče vůle brzd*).

### B. Heavy Diesel Emissions & Aftertreatment:
- **SCR (Selective Catalytic Reduction) & AdBlue (DEF)**:
  - Urea injection pump, dosing unit, NOx sensors (pre-cat and post-cat).
  - Crystallization clearing in dosing injector; diagnosing SCR efficiency DTCs.
- **DPF & EGR in Commercial Fleets**:
  - Differential pressure sensor diagnostics; thermal management for active regeneration; EGR cooler failure (exhaust gas leaking into coolant or coolant ingestion into intake).
- **Auxiliary Retarders (Hydraulic Retarder & Engine Compression Brake / Jake Brake)**:
  - Fluid heat exchanger, proportional valve actuation, exhaust throttle flap.

---

## 3. Transmissions, Clutches & Drivetrain

### A. Manual Transmissions & Clutches:
- **Dual-Mass Flywheel (*Dvouhmotový setrvačník*) Inspection**:
  - Measuring rotational free play (*vůle pootočení*) in teeth/degrees and tilt rock play (*vůle vyklopení*). Metallic clatter on shutdown indicates worn internal damping springs.
- **Clutch Replacement**:
  - Self-Adjusting Clutch (SAC) installation requiring specialized pre-tensioning tool to avoid premature adjuster ratcheting.
  - Release bearing (*vypínací ložisko* / concentric slave cylinder - CSC) hydraulic bleeding.

### B. Dual-Clutch Transmissions (DSG / DCT / S-Tronic):
- **Dry Clutch (e.g. VAG DQ200 - 7-speed)**:
  - Exact clutch pack shimming with depth gauge; mechatronic hydraulic accumulator pressure checks (accumulator blow-out causing P17BF).
- **Wet Clutch (e.g. VAG DQ250, DQ381, DQ500 / BMW DKG)**:
  - Regular 60,000 km fluid and filter change; mechatronic solenoid cleaning; basic settings calibration via diagnostic tool (adaptation of clutch kiss points and gear selector synchronizers).

### C. Torque-Converter Automatic Transmissions:
- Planetary gear sets, torque converter lock-up clutch (*lock-up spojka*).
- Complete fluid exchange using automated ATF flushing machines (dynamic exchange under running engine) vs. static drain/fill; monitoring transmission oil temperature during level check.

### D. Differentials & Drivetrain Components:
- Setting ring and pinion gear backlash (*zubová vůle*) and tooth contact pattern using marking compound (*inženýrská modř*).
- CV joint (*homokinetický kloub*) boot replacement and grease repacking; propshaft center support bearing alignment.

---

## 4. Chassis, Suspension, Steering & Hydraulics

### A. Suspension Systems:
- **MacPherson & Multi-Link**: Bushing press-in/press-out techniques, ball joint taper extraction, coil spring compressor safety.
- **Air Suspension (*Pneumatické odpružení*)**:
  - Diagnosing leaking air bellows (*vzduchové měchy*) with soapy water / leak spray.
  - Air suspension compressor testing (max pressure output > 14–16 bar); valve block solenoid integrity; ride height sensor calibration via diagnostic software.

### B. Steering & Geometry:
- **Steering Racks**: Hydraulic rack seal rebuilding, electro-hydraulic pumps (EHPS), electric power steering (EPS) torque sensor zero-point calibration.
- **4-Wheel Alignment (*Geometrie kol*)**:
  - Toe-in / Toe-out (*sbíhavost*), Camber (*odklon*), Caster (*záklon rejdového čepu*), Kingpin inclination (*příklon*), Thrust angle (*jízdní osa*).
  - Calibrating Steering Angle Sensor (SAS / G85) after every wheel alignment.

### C. Hydraulic Brake Systems:
- Brake caliper slide pin cleaning and high-temp silicone lubrication (never use copper grease on rubber boots).
- Hydraulic pressure bleeding with automated brake bleeder (1.5–2.0 bar); ABS pump cycling procedure to evacuate air trapped in internal accumulator valves.
- Electronic Parking Brake (EPB): Driving caliper pistons into service mode via diagnostics prior to rear pad replacement; zero-point thickness calibration upon completion.
