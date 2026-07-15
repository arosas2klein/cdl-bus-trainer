import streamlit as st
import os

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

# 2. Define Helper Function to Safely Load Images
def display_part_image(image_filename, fallback_text):
    """Displays the image if it exists in the GitHub folder, otherwise shows a nice placeholder."""
    if os.path.exists(image_filename):
        st.image(image_filename, use_container_width=True, caption=f"Target Location: {fallback_text}")
    else:
        st.warning(f"📸 [Photo Placeholder for {fallback_text}] — Upload '{image_filename}' to your GitHub repository to see your bus photo here!")

# 3. Create Mobile-Friendly Tabs for Bus Sections
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🚌 Front of the Vehicle", 
    "🛞 Driver Side",
    "🔺 Rear of the Bus",
    "🛑 Air Brakes", 
    "👤 In-Cab & Safety", 
    "📐 External Walkaround"
])

# ------------------------------------------------------------------
# SECTION 1: FRONT OF THE VEHICLE
# ------------------------------------------------------------------
with tab1:
    st.header("Front of the Vehicle")
    
    display_part_image("front_of_bus.jpg", "Front View of the Bus")
    st.write("Click a component to inspect:")
    
    col1, col2 = st.columns(2)
    with col1:
        lights_clicked = st.button("💡 Lights & Lenses", use_container_width=True)
        hoses_clicked = st.button("🪱 Hoses", use_container_width=True)
        shocks_clicked = st.button("🛢️ Shock Absorbers", use_container_width=True)
        drums_clicked = st.button("🥁 Brake Drums / Linings", use_container_width=True)
        rims_clicked = st.button("⭕ Rims", use_container_width=True)
    with col2:
        mirrors_clicked = st.button("🪞 Mirrors / Brackets", use_container_width=True)
        steering_axle_clicked = st.button("🔩 Steering Axle (Springs/Mounts/U-Bolts)", use_container_width=True)
        brake_hoses_clicked = st.button("⛓️ Brake Hoses / Lines", use_container_width=True)
        tires_clicked = st.button("🛞 Tires", use_container_width=True)
        lug_nuts_clicked = st.button("🔩 Lug Nuts", use_container_width=True)

    st.markdown("---")

    if lights_clicked:
        display_part_image("front_lights.jpg", "Lights and Lenses")
        st.info("""**💡 Lights & Lenses Script:**

All lights and lenses are clean, not cracked or broken, and the proper color (amber on the front and sides). I am checking clearance lights, identification lights, turn signals, and hazards.""")
        
    elif mirrors_clicked:
        display_part_image("mirrors.jpg", "Mirrors and Brackets")
        st.info("""**🪞 Mirrors / Brackets Script:**

Mirrors are clean, not cracked or broken, and properly adjusted to me. Mirror brackets are securely mounted to the vehicle body, not bent or broken, with no missing hardware.""")
        
    elif hoses_clicked:
        display_part_image("front_hoses.jpg", "Engine/Front Hoses")
        st.info("""**🪱 Hoses Script:**

Checking all visible power steering, coolant, and engine hoses. They are properly secured at both ends, not leaking, and have no abrasions, bumps, or cuts (ABC).""")
        
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
        
    elif lug_nuts_clicked:
        display_part_image("lug_nuts.jpg", "Lug Nuts")
        st.info("""**🔩 Lug Nuts Script:**

All lug nuts are present, tight, and secure. Look closely for rust streaks (on steel wheels) or white powder trails (on aluminum wheels), which indicate a loose nut. No cracked bolt holes.""")

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
# SECTION 4: AIR BRAKE TEST (CRITICAL SEQUENCE)
# ------------------------------------------------------------------
with tab4:
    st.header("Air Brake Test")
    st.error("⚠️ WARNING: Missing or messing up any step in this sequence results in an AUTOMATIC FAILURE on the real CDL exam.")
    
    step = st.radio(
        "Select Brake Test Step to Study:", 
        ["Step 1: Applied Pressure Leak Test", "Step 2: Low Air Warning Signal", "Step 3: Parking Brake Valve Pop-Out"]
    )
    
    st.markdown("---")
    
    if step == "Step 1: Applied Pressure