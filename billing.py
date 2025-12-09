phase=input("enter the phase:single/three/BPL").lower()

if phase=="bpl":
    
    watts=int(input("enter the watts"))
    units=int(input("enter the units:"))
    if watts<=1000 and units<=40:
        fixed_charge=0
        total_charge=units*1.50
        total=fixed_charge+total_charge
        print("BPL Bill")
        print("fixed_charge:",fixed_charge)
        print("current_charge:",total_charge)
        print("total:",total)
    else:
        print("not BPL, billing as single")
        phase="single"
        
units=int(input("enter the units:"))

if phase=="single":
    if units <= 50:
        fixed_charge = 40
    elif units <= 100:
        fixed_charge = 65
    elif units <= 150:
        fixed_charge = 85
    elif units <= 200:
        fixed_charge = 120
    elif units <= 250:
        fixed_charge = 130
    elif units <= 300:
        fixed_charge = 150
    elif units <= 350:
        fixed_charge = 175
    elif units <= 400:
        fixed_charge = 200
    elif units <= 500:
        fixed_charge = 230
    else:
        fixed_charge = 260
else:
    if units <= 50:
        fixed_charge = 100
    elif units <= 100:
        fixed_charge = 140
    elif units <= 150:
        fixed_charge = 170
    elif units <= 200:
        fixed_charge = 180
    elif units <= 250:
        fixed_charge = 200
    elif units <= 300:
        fixed_charge = 205
    elif units <= 350:
        fixed_charge = 210
    elif units <= 400:
        fixed_charge = 210
    elif units <= 500:
        fixed_charge = 235
    else:
        fixed_charge = 260
    
if units<=250:
    type="telescopic"
else:
    type="non-telescopic"
    
charge=0
if type=="telescopic":
    bal=units
    slab=min(bal,50)
    charge+=slab*3.15
    bal-=slab
    if bal>0:
        slab=min(bal,50)
        charge+=slab*3.70
        bal-=slab
    if bal>0:
        slab=min(bal,50)
        charge+=slab*4.80
        bal-=slab
    if bal>0:
        slab=min(bal,50)
        charge+=slab*6.40
        bal-=slab
    if bal>0:
        slab=min(bal,50)
        charge+=slab*7.60
        bal-=slab
else:
    if units <= 50:
        rate = 3.50
    elif units <= 100:
        rate = 4.50
    elif units <= 150:
        rate = 5.50
    elif units <= 200:
        rate = 6.50
    elif units <= 300:
        rate = 7.50
    else:
        rate = 8.00
    charge=units*rate
tot=fixed_charge+charge

print("KSEB")
print("phase:",phase)
print("units",units)
print("type",type)
print("fixed_charge",fixed_charge)
print("energy charge:",charge)
print("total=",tot)
    
    
    
