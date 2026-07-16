import streamlit as st
import os
from PIL import Image, ImageOps  # Added to handle phone image auto-rotation

# 1. Page Configuration for Mobile Devices
st.set_page_config(
    page_title="CDL Pre-Trip Trainer", 
    page_icon="🚌", 
    layout="centered"
)

# App Header
st.title("🚌 CDL Pre-Trip Inspection Helper")
st.write("Tap a section below, then select any part to view its location photo and exact CDL script.")
st.markdown("---")

# 2. Updated Helper Function to Fix Phone Image Rotation (EXIF Transpose)
def display_part_image(image_filename, fallback_text):
    """Displays the image, auto-correcting any smartphone rotation data!"""
    base_name = os.path.splitext(image_filename)[0]
    jpg_version = f"{base_name}.jpg"
    jpeg_version = f"{base_name}.jpeg"
    
    target_file = None
    if os.path.exists(jpg_version):
        target_file = jpg_version
    elif os.path.exists(jpeg_version):
        target_file = jpeg_version
        
    if target_file:
        try:
            # Open image and transpose it based on phone orientation data
            img = Image.open(target_file)
            fixed_img = ImageOps.exif_transpose(img)
            st.image(fixed_img, use_container_width=True, caption=f"Target Location: {fallback_text}")
        except Exception:
            # Fallback just in case something fails
            st.image(target_file, use_container_width=True, caption=f"Target Location: {fallback_text}")
    else:
        st.warning(f"📸 [Photo Placeholder for {fallback_text}] — Upload '{jpg_version}' or '{jpeg_version}' to your GitHub repository to see your bus photo here!")

# 3. Create Mobile-Friendly Tabs for the 4 Main Sections
tab1, tab2, tab3, tab4 = st.tabs([
    "🚌 Front of the Vehicle", 
    "🛞 Driver Side",
    "🔺 Rear of the Bus",
    "🚪 Passenger Side"
])

# ------------------------------------------------------------------
# SECTION 1: FRONT OF THE VEHICLE
# ------------------------------------------------------------------
with tab1:
    st.header("Front of the Vehicle")
    
    display_part_image("front_of_bus.jpg", "Front View of the Bus")
    st.write("Click a component to inspect:")
    
    # Top 3 Full-Width Buttons
    lights_clicked = st.button("💡 Lights & Lenses", use_container_width=True)
    mirrors_clicked = st.button("🪞 Mirrors / Brackets", use_container_width=True)
    leaks_clicked = st.button("💧 Leaks", use_container_width=True)
    
    st.markdown("---")
    
    # Two Columns: Passenger Side vs Driver Side Layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👉 Passenger Side")
        hoses_clicked = st.button("🪱 Hoses", use_container_width=True)
        steering_axle_clicked = st.button("🔩 Steering Axle (Springs/Mounts/U-Bolts)", use_container_width=True)
        shocks_clicked = st.button("🛢️ Shock Absorbers", use_container_width=True)
        brake_hoses_clicked = st.button("⛓️ Brake Hoses / Lines", use_container_width=True)
        drums_clicked = st.button("🥁 Brake Drums / Linings", use_container_width=True)
        tires_clicked = st.button("🛞 Tires", use_container_width=True)
        rims_clicked = st.button("⭕ Rims", use_container_width=True)
        
    with col2:
        st.subheader("👈 Driver Side")
        coolant_clicked = st.button("🧪 Coolant", use_container_width=True)
        oil_clicked = st.button("🛢️ Oil", use_container_width=True)
        ps_fluid_clicked = st.button("💧 Power Steering Fluid", use_container_width=True)
        ps_box_clicked = st.button("📦 Power Steering Box", use_container_width=True)
        drag_link_clicked = st.button("🔗 Drag Link", use_container_width=True)
        tie_rod_clicked = st.button("🥢 Tie Rod", use_container_width=True)
        joints_clicked = st.button("🔩 Joints / Cotter Key", use_container_width=True)

    st.markdown("---")

    # --- TOP BUTTONS LOGIC ---
    if lights_clicked:
        display_part_image("front_lights.jpg", "Lights and Lenses")
        st.info("""**💡 Lights & Lenses Script:**
Clearance lights (Amber), Student loading lights (Red and Amber), Turn signals / 4-way flashers or Hazards (Amber), Headlight low and High beam (Clear). - Working properly and clean, No missing parts, Not cracked or broken.""")
        
    elif mirrors_clicked:
        display_part_image("mirrors.jpg", "Mirrors and Brackets")
        st.info("""**🪞 Mirrors / Brackets Script:**
Mirrors are clean, not cracked or broken, and properly adjusted to me. Mirror brackets are securely mounted to the vehicle body, not bent or broken, with no missing hardware.""")
        
    elif leaks_clicked:
        display_part_image("front_leaks.jpg", "Ground & Engine Compartment Leaks")
        st.info("""**💧 Leaks Script:**
I am looking underneath the vehicle on the ground for any fresh puddles, drips, or spots of engine oil, coolant, power steering fluid, or fuel. I am also checking the engine compartment components for any active fluid leaks or the sound of escaping air.""")

    # --- PASSENGER SIDE BUTTONS LOGIC ---
    elif hoses_clicked:
        display_part_image("front_hoses.jpg", "Engine/Front Hoses")
        st.info("""**🪱 Hoses Script:**
Checking all visible passenger-side hoses. They are properly secured at both ends, not leaking, and have no abrasions, bumps, or cuts (ABC).""")
        
    elif steering_axle_clicked:
        display_part_image("suspension_springs.jpg", "Leaf Springs & U-Bolts")
        st.info("""**🔩 Steering Axle (Suspension) Script:**
Leaf springs are not cracked, broken, shifted, or missing. Spring mounts are securely bolted with no cracks. U-bolts are secure, not cracked or bent, with no rust trails or shiny metal indicating loose nuts.""")
        
    elif shocks_clicked:
        display_part_image("shocks.jpg", "Shock Absorbers")
        st.info("""**🛢️ Shock Absorbers Script:**
Shock absorbers are securely mounted at the top and bottom. They are straight, not bent or cracked, and there are no signs of active fluid leaking from the seals.""")
        
    elif brake_hoses_clicked:
        display_part_image("brake_hoses.jpg", "Brake Hoses / Lines")
        st.info("""**⛓️ Brake Hoses / Lines Script:**
Brake hoses and lines are properly secured, not cracked or leaking air or fluid. No abrasions, bumps, or cuts on the rubber lines.""")
        
    elif drums_clicked:
        display_part_image("brake_drums.jpg", "Brake Drums & Linings")
        st.info("""**🥁 Brake Drums / Linings Script:**
Brake drums are not cracked, thin, or broken, and free of oil, grease, or contaminants. Brake linings (shoes) are not worn dangerously thin (at least 1/4 inch thickness) and are free of cracks.""")
        
    elif tires_clicked:
        display_part_image("front_tires.jpg", "Steering Axle Tires")
        st.info("""**🛞 Tires Script (ICD Rule):**
* **Inflation:** Checked with an air gauge to manufacturer specs (100-110 psi).
* **Condition:** No sidewall cuts, bubbles, or dry rot.
* **Depth:** Must have at least 4/32 inch tread depth on front steering tires. Recaps or regrooved tires are strictly prohibited on the front axle.""")
        
    elif rims_clicked:
        display_part_image("rims.jpg", "Wheel Rims")
        st.info("""**⭕ Rims Script:**
The rim is properly mounted and secure. It is not cracked, bent, or distorted. There are no welding repairs, which are illegal on commercial wheels.""")

    # --- DRIVER SIDE BUTTONS LOGIC ---
    elif coolant_clicked:
        display_part_image("coolant_reservoir.jpg", "Coolant Reservoir")
        st.info("""**🧪 Coolant Reservoir Script:**
The coolant level is above the minimum marking line on the sight glass or reservoir tank. The container is secure, not cracked or leaking, and the cap is secure and tight.""")
        
    elif oil_clicked:
        display_part_image("oil_dipstick.jpg", "Engine Oil Dipstick")
        st.info("""**🛢️ Engine Oil Script:**
With the engine off, I would pull out the dipstick, wipe it clean, reinsert it, and pull it out again to verify the oil level is in the safe operating range, above the add mark.""")
        
    elif ps_fluid_clicked:
        display_part_image("ps_fluid_reservoir.jpg", "Power Steering Fluid Reservoir")
        st.info("""**💧 Power Steering Fluid Script:**
The power steering fluid reservoir is securely mounted, not cracked or leaking. The fluid level is within the safe zone on the dipstick or sight glass.""")
        
    elif ps_box_clicked:
        display_part_image("ps_box.jpg", "Power Steering Box")
        st.info("""**📦 Power Steering Box Script:**
The power steering box is securely mounted to the frame. Check that it is not cracked or leaking, and ensure no missing nuts, bolts, or mounting hardware.""")
        
    elif drag_link_clicked:
        display_part_image("drag_link.jpg", "Steering Drag Link")
        st.info("""**🔗 Drag Link Script:**
The drag link is a structural steering component. It is not bent, cracked, or broken, and it is securely connected to the steering arm with tight joints.""")
        
    elif tie_rod_clicked:
        display_part_image("tie_rod.jpg", "Tie Rod Assembly")
        st.info("""**🥢 Tie Rod Script:**
The tie rod connects the steering knuckles together. It is straight, not cracked or bent, and the joints are tight with no excessive play.""")
        
    elif joints_clicked:
        display_part_image("steering_joints.jpg", "Steering Joints & Cotter Keys")
        st.info("""**🔩 Steering Joints & Cotter Keys Script:**
All links, arms, and joints in the steering linkage are not worn or loose. All castle nuts are tight and secured with their required cotter keys.""")

# ------------------------------------------------------------------
# SECTION 2: DRIVER SIDE
# ------------------------------------------------------------------
with tab2:
    st.header("Driver Side")
    
    display_part_image("driver_side_bus.jpg", "Driver Side View of the Bus")
    st.write("Click a component to inspect:")
    
    col1, col2 = st.columns(2)
    with col1:
        side_lenses_clicked = st.button("🚨 Lenses & Reflectors", use_container_width=True)
        traffic_devices_clicked = st.button("🚘 Traffic Monitor Devices", use_container_width=True)
        electrical_box_clicked = st.button("⚡ Electrical Box", use_container_width=True)
    with col2:
        battery_clicked = st.button("🔋 Battery Compartment", use_container_width=True)
        stop_arm_clicked = st.button("🛑 Stop Arm", use_container_width=True)

    st.markdown("---")

    if side_lenses_clicked:
        display_part_image("side_lenses.jpg", "Side Lenses and Reflectors")
        st.info("""**🚨 Lenses & Reflectors Script:**
All side lenses, marker lights, and reflectors are clean, unbroken, properly mounted, and correct color—amber towards the front and center, red towards the rear. Reflective tape is securely affixed.""")
        
    elif traffic_devices_clicked:
        display_part_image("traffic_devices.jpg", "Traffic Monitor Devices (Crossover Mirrors)")
        st.info("""**🚘 Traffic Monitor Devices Script:**
Crossover mirrors and driver-side blind spot mirrors are securely mounted, brackets are not bent or broken, all hardware is tight, and glass is clean and uncracked.""")
        
    elif electrical_box_clicked:
        display_part_image("electrical_box.jpg", "Side Electrical Panel")
        st.info("""**⚡ Electrical Box Script:**
The electrical panel access door opens and closes properly, and the latch secures tightly. Wires inside are secure, insulation is intact with no bare copper, and there are no signs of corrosion or burning.""")
        
    elif battery_clicked:
        display_part_image("battery_compartment.jpg", "Battery Box")
        st.info("""**🔋 Battery Compartment Script:**
The battery tray slides in and out smoothly and locks securely. Connections are tight with no excessive corrosion. Cell caps are present if applicable. Wires are secure with no cracks or fraying. Box door latches closed.""")
        
    elif stop_arm_clicked:
        display_part_image("stop_arm.jpg", "School Bus Stop Arm")
        st.info("""**🛑 Stop Arm Script:**
The stop arm assembly is firmly mounted to the side framework with no loose or missing bolts. Hoses and electrical lines are secure. The rubber frame seals are clean and intact. Red lights are clean, uncracked, and functional.""")

# ------------------------------------------------------------------
# SECTION 3: REAR OF THE BUS
# ------------------------------------------------------------------
with tab3:
    st.header("Rear of the Bus")
    
    display_part_image("rear_of_bus.jpg", "Rear View of the Bus")
    st.write("Click a component to inspect:")
    
    rear_lights_clicked = st.button("🚨 Lights, Lenses and Reflectors", use_container_width=True)
    
    st.markdown("---")
    
    if rear_lights_clicked:
        display_part_image("rear_lights.jpg", "Rear Lights and Lenses")
        st.info("""**🚨 Lights, Lenses and Reflectors Script:**
All rear lenses, clearance lights, tail lights, school bus amber/red flashing lights, turn signals, hazards, and reflectors are clean, not cracked or broken, and the proper color (red on the rear). Reflective tape outlining emergency paths or exits is clean and secure.""")

# ------------------------------------------------------------------
# SECTION 4: PASSENGER SIDE
# ------------------------------------------------------------------
with tab4:
    st.header("Passenger Side")
    
    display_part_image("passenger_side_bus.jpg", "Passenger Side View of the Bus")
    st.write("Click a component to inspect:")
    
    col1, col2 = st.columns(2)
    with col1:
        ps_lenses_clicked = st.button("🚨 Lenses and Reflectors", key="ps_lens", use_container_width=True)
        ps_traffic_clicked = st.button("🚘 Traffic Monitor Devices", key="ps_traffic", use_container_width=True)
        def_tank_clicked = st.button("🧪 DEF Tank", use_container_width=True)
    with col2:
        fuel_tank_clicked = st.button("⛽ Fuel Tank", use_container_width=True)
        frame_clicked = st.button("🪵 Frame", use_container_width=True)

    st.markdown("---")

    if ps_lenses_clicked:
        display_part_image("passenger_lenses.jpg", "Passenger Side Lenses and Reflectors")
        st.info("""**🚨 Lenses & Reflectors Script:**
All passenger-side lenses, markers, and reflectors are clean, uncracked, and the correct color (amber at the front/middle, red at the rear). Dual-action indicator lights on the entrance door are fully functional.""")
        
    elif ps_traffic_clicked:
        display_part_image("passenger_mirrors.jpg", "Passenger Traffic Monitor Devices")
        st.info("""**🚘 Traffic Monitor Devices Script:**
Passenger-side blind spot mirrors, door glass, and crossover mirrors are secure, brackets are tight and unbroken, and the glass is completely clean, offering an unobstructed view.""")
        
    elif def_tank_clicked:
        display_part_image("def_tank.jpg", "DEF Tank")
        st.info("""**🧪 DEF Tank Script:**
The DEF tank is securely mounted with no loose straps or brackets. The tank cap is present and fits tightly. I am checking underneath for any white, powdery residue which would indicate a DEF leak.""")
        
    elif fuel_tank_clicked:
        display_part_image("fuel_tank.jpg", "Fuel Tank")
        st.info("""**⛽ Fuel Tank Script:**
The fuel tank is securely mounted to the frame with no loose or missing mounting straps. The fuel cap is tight and secure. There are no signs of active fuel leaks or wet spots underneath the tank or hoses.""")
        
    elif frame_clicked:
        display_part_image("frame.jpg", "Bus Frame")
        st.info("""**🪵 Frame Script:**
Inspecting the longitudinal frame members and cross members. There are no cracks, bends, welds, or illegal holes in the frame. The floor wood and metal supports show no signs of structural damage.""")