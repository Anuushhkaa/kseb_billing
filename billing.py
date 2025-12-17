print("------ KSEB ELECTRICITY BILL SYSTEM ------")

consumer_name = input("Enter consumer name: ")
phase = input("Enter phase (single/three/BPL): ").lower()
units = int(input("Enter units consumed: "))

energy_charge = 0
fixed_charge = 0
is_bpl_success = False

if phase == "bpl":
    watts = int(input("Enter watts: "))

    if watts <= 1000 and units <= 40:
        energy_charge = units * 1.50
        fixed_charge = 0
        duty = 0
        fuel_surcharge = 0
        meter_rent = 0
        total = energy_charge
        is_bpl_success = True  
        
        print("\n------ KSEB BILL (BPL SUBSIDY) ------")
        print("Consumer Name :", consumer_name)
        print("Units Consumed:", units)
        print("Energy Charge : ₹", energy_charge)
        print("Total Payable : ₹", total)
        print("-------------------------------------")
    else:
        print("\n Not eligible for BPL subsidy. Calculating as Single Phase...")
        phase = "single"  

if not is_bpl_success:
    
    if phase == "single":
        fixed_charge = 260
    elif phase == "three":
        fixed_charge = 520
    else:
        print("Invalid phase entered.")
        exit()

    if units <= 50:
        energy_charge = units * 3.15
    elif units <= 100:
        energy_charge = (50 * 3.15) + ((units - 50) * 3.70)
    elif units <= 150:
        energy_charge = (50 * 3.15) + (50 * 3.70) + ((units - 100) * 4.80)
    else:
        energy_charge = (50 * 3.15) + (50 * 3.70) + (50 * 4.80) + ((units - 150) * 6.40)

    
    duty = energy_charge * 0.10
    fuel_surcharge = units * 0.10
    meter_rent = 30

    
    total = energy_charge + fixed_charge + duty + fuel_surcharge + meter_rent
    payable = round(total)

    print("\n------ KSEB ELECTRICITY BILL ------")
    print("Consumer Name :", consumer_name)
    print("Phase         :", phase.upper())
    print("Units Consumed:", units)
    print("---------------------------------")
    print("Energy Charge : ₹", round(energy_charge, 2))
    print("Fixed Charge  : ₹", fixed_charge)
    print("Duty (10%)    : ₹", round(duty, 2))
    print("Fuel Surcharge: ₹", round(fuel_surcharge, 2))
    print("Meter Rent    : ₹", meter_rent)
    print("---------------------------------")
    print("TOTAL PAYABLE : ₹", payable)
    print("---------------------------------")
