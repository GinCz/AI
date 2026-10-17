# Engine Diagnostic Decision Trees (Diesel & Petrol)

Step-by-step diagnostic algorithms for troubleshooting engine start failures, power loss, and abnormal exhaust smoke.

---

## 1. Engine Cranks but Fails to Start (Diesel Common Rail)

```
                       [Engine Cranks - No Start]
                                   |
                +------------------+------------------+
                |                                     |
      [Scan Diagnostic Codes (DTC)]        [Live Data Inspection during Crank]
                |                                     |
   P0335/P0340? | P0087 (Low Rail Pressure)?          +--> Engine RPM signal visible? (> 200 RPM)
       +--------+--------+                                 |-- NO  -> Crankshaft position sensor (CKP) failure
       |                 |                                 \-- YES -> CKP is operational
[Replace Sensor]  [Rail Pressure Check]
                         |
           Target Rail Pressure >= 250-300 bar?
                         |
               +---------+---------+
               |                   |
             [YES]                [NO]
               |                   |
    [Check Injector Pulse]   [Perform Injector Leak-off Test]
               |                   |
      ECU authorizing?       Any cylinder filling vial rapidly?
        (Immobilizer?)             |
                             +-----+-----+
                             |           |
                           [YES]        [NO]
                             |           |
                      [Faulty Injector] [Check LP Fuel Delivery: Tank pump,
                                         Fuel filter clogging, CP4 HP pump]
```

---

## 2. Exhaust Smoke Color Diagnostic Guide

| Smoke Color | Root Cause | Primary Inspection Points |
| :--- | :--- | :--- |
| **Black Smoke** (Diesel) | Over-fueling or lack of combustion air (rich mixture). | - Boost leak in intercooler piping / split turbo hose.<br>- Clogged engine air filter.<br>- Sticking EGR valve (open during load).<br>- Dripping / leaking fuel injector nozzle.<br>- Worn MAF sensor measuring false high air flow. |
| **Blue Smoke** (Petrol & Diesel) | Engine oil burning in combustion chamber. | - Worn turbocharger shaft seals (oil in intercooler).<br>- Hardened/cracked valve stem seals (*gufera ventilů*).<br>- Stuck or worn piston oil control rings.<br>- Clogged PCV valve / crankcase breather (*odvětrání klikové skříně*). |
| **White Smoke** (Sweet Smell) | Coolant leaking into combustion chamber. | - Blown cylinder head gasket (*těsnění pod hlavou*).<br>- Cracked cylinder head or cylinder block liner.<br>- Leaking EGR cooler heat exchanger. |
| **White / Gray Smoke** (Pungent Acrid Diesel Smell) | Unburned raw diesel atomized in cold cylinders. | - Failed glow plug controller or glow plugs.<br>- Low compression across cylinders.<br>- Severely delayed injection timing (retarded timing).<br>- Low rail pressure causing poor droplet atomization. |
