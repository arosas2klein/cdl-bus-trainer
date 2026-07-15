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
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🚌 Front of the Vehicle", 
    "🛞 Driver Side",
    "🛑 Air Brakes", 
    "👤 In-Cab & Safety", 
    "📐 External Walkaround"
])

# ------------------------------------------------------------------
# SECTION 1: FRONT OF THE VEHICLE
# ------------------------------------------------------------------
with tab1:
    st.header("Front of the Vehicle")
    
    # Main overview photo of the front of your bus
    display_part_image("front_of_bus.jpg", "Front View of the Bus")
    
    st.write("Click a component to inspect:")
    
    # 5 rows of 2 buttons for a clean mobile grid layout
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

    # Dynamic Display based on selection
    if lights_clicked:
        display_part_image("front_lights.jpg", "Lights and Lenses")
        st.info("**💡 Lights & Lenses Script:**\n\n'All lights and lenses are clean, not cracked or broken, and the proper color. Amber on the front/sides. I am checking clearance lights, identification lights, turn signals, and hazards.'")
        
    elif mirrors_clicked:
        display_part_image("mirrors.jpg", "Mirrors and Brackets")
        st.info("**🪞 Mirrors / Brackets Script:**\n\n'Mirrors are clean, not cracked or broken, and properly adjusted to me. Mirror brackets are securely mounted to the vehicle body, not bent or broken, with no missing hardware.'")
        
    elif hoses_clicked:
        display_part_image("front_hoses.jpg", "Engine/Front Hoses")
        st.info("**🪱 Hoses Script:**\n\n'Checking all visible power steering, coolant, and engine hoses. They are properly secured at both ends, not leaking, and have no abrasions, bumps, or cuts (ABC).'")
        
    elif steering_axle_clicked:
        display_part_image("suspension_springs.jpg", "Leaf Springs & U-Bolts")
        st.info("**🔩 Steering Axle (Suspension) Script:**\n\n'Leaf springs are not cracked, broken, shifted, or missing. Spring mounts are securely bolted with no cracks. U-bolts are secure, not cracked or bent, with no rust trails or shiny metal indicating loose nuts.'")
        
    elif shocks_clicked:
        display_part_image("shocks.jpg", "Shock Absorbers")
        st.info("**🛢️ Shock Absorbers Script:**\n\n'Shock absorbers are securely mounted at the top and bottom. They are straight, not bent or cracked, and there are no signs of active fluid leaking from the seals.'")
        
    elif brake_hoses_clicked:
        display_part_image("brake_hoses.jpg", "Brake Hoses / Lines")
        st.info("**⛓️ Brake Hoses / Lines Script:**\n\n'Brake hoses and lines are properly secured, not cracked or leaking air or fluid. No abrasions, bumps, or cuts on the rubber lines.'")
        
    elif drums_clicked:
        display_part_image("brake_drums.jpg", "Brake Drums & Linings")
        st.info("**🥁 Brake Drums / Linings Script:**\n\n'Brake drums are not cracked, thin, or broken, and free of oil, grease, or contaminants. Brake linings (shoes) are not worn dangerously thin (at least 1/4 inch thickness) and are free of cracks.'")
        
    elif tires_clicked:
        display_part_image("front_tires.jpg", "Steering Axle Tires")
        st.info("**🛞 Tires Script (ICD Rule):**\n\n* **Inflation:** Checked with a gauge to 100-110 psi.\n* **Condition:** No sidewall cuts, bubbles, or dry rot.\n* **Depth:** Must have at least 4/32 inch tread depth on front steering tires. Recaps/regrooved tires are strictly prohibited on the front axle.'")
        
    elif rims_clicked:
        display_part_image("rims.jpg", "Wheel Rims")
        st.info("**⭕ Rims Script:**\n\n'The rim is properly mounted and secure. It is not cracked, bent, or distorted. There are no welding repairs, which are illegal on commercial wheels.'")
        
    elif lug_nuts_clicked:
        display_part_image("lug_nuts.jpg", "Lug Nuts")
        st.info("**🔩 Lug Nuts Script:**\n\n'All lug nuts are present, tight, and secure. Look closely for rust streaks (on steel wheels) or white powder trails (on aluminum wheels), which indicate a loose nut. No cracked bolt holes.'")

# ------------------------------------------------------------------
# SECTION 2: DRIVER SIDE
# ------------------------------------------------------------------
with tab2:
    st.header("Driver Side")
    
    # Main overview photo of the driver side of your bus
    display_part_image("driver_side_bus.jpg", "Driver Side View of the Bus")
    
    st.write("Click a component to inspect:")
    
    # 5 buttons arranged neatly for a mobile layout
    col1, col2 = st.columns(2)
    with col1:
        side_lenses_clicked = st.button("🚨 Lenses & Reflectors", use_container_width=True)
        traffic_devices_clicked = st.button("🚘 Traffic Monitor Devices", use_container_width=True)
        electrical_box_clicked = st.button("⚡ Electrical Box", use_container_width=True)
    with col2:
        battery_clicked = st.button("🔋 Battery Compartment", use_container_width=True)
        stop_arm_clicked = st.button("🛑 Stop Arm", use_container_width=True)

    st.markdown("---")

    # Dynamic Display based on selection
    if side_lenses_clicked:
        display_part_image("side_lenses.jpg", "Side Lenses and Reflectors")
        st.info("**🚨 Lenses & Reflectors Script:**\n\n'All side lenses, marker lights, and reflectors are clean, unbroken, properly mounted, and correct color—amber towards the front and center, red towards the rear. Reflective tape is securely affixed.'")
        
    elif traffic_devices_clicked:
        display_part_image("traffic_devices.jpg", "Traffic Monitor Devices (Crossover Mirrors)")
        st.info("**🚘 Traffic Monitor Devices Script:**\n\n'Crossover mirrors and driver-side blind spot mirrors are securely mounted, brackets are not bent or broken, all hardware is tight, and glass is clean and uncracked.'")
        
    elif electrical_box_clicked:
        display_part_image("electrical_box.jpg", "Side Electrical Panel")
        st.info("**⚡ Electrical Box Script:**\n\n'The electrical panel access door opens and closes properly, and the latch secures tightly. Wires inside are secure, insulation is intact with no bare copper, and there are no signs of corrosion or burning.'")
        
    elif battery_clicked:
        display_part_image("battery_compartment.jpg", "Battery Box")
        st.info("**🔋 Battery Compartment Script:**\n\n'The battery tray slides in and out smoothly and locks securely. Connections are tight with no excessive corrosion. Cell caps are present if applicable. Wires are secure with no cracks or fraying. Box door latches closed.'")
        
    elif stop_arm_clicked:
        display_part_image("stop_arm.jpg", "School Bus Stop Arm")
        st.info("**🛑 Stop Arm Script:**\n\n'The stop arm assembly is firmly mounted to the side framework with no loose or missing bolts. Hoses and electrical lines are secure. The rubber frame seals are clean and intact. Red lights are clean, uncracked, and functional.'")

# ------------------------------------------------------------------
# SECTION 3: AIR BRAKE TEST (CRITICAL SEQUENCE)
# ------------------------------------------------------------------
with tab3:
    st.header("Air Brake Test")
    st.error("⚠️ WARNING: Missing or messing up any step in this sequence results in an AUTOMATIC FAILURE on the real CDL exam.")
    
    step = st.radio(
        "Select Brake Test Step to Study:", 
        ["Step 1: Applied Pressure Leak Test", "Step 2: Low Air Warning Signal", "Step 3: Parking Brake Valve Pop-Out"]
    )
    
    st.markdown("---")
    
    if step == "Step 1: Applied Pressure Leak Test":
        display_part_image("gauges_leak.jpg", "Air Pressure Gauges")
        st.warning("**🛑 Step 1 Script & Actions:**\n\n'With a fully charged system (120-140 psi), I will turn the engine off, turn the key back to the ON position, fully release both parking brakes, and hold down the service brake pedal firmly for one minute. I will monitor my gauges; I should not lose more than 3 psi in one minute.'\n\n*💡 Tip: Make sure the trainee times a full 60 seconds on a watch.*")
    
    elif step == "Step 2: Low Air Warning Signal":
        display_part_image("low_air_light.jpg", "Low Air Light/Buzzer")
        st.warning("**🛑 Step 2 Script & Actions:**\n\n'I will pump the brake pedal repeatedly to bleed off pressure. The low air warning light and dashboard buzzer must activate at or before the air pressure drops to 55 psi.'")
    
    elif step == "Step 3: Parking Brake Valve Pop-Out":
        display_part_image("brake_valves.jpg", "Yellow / Red Valve Knobs")
        st.warning("**🛑 Step 3 Script & Actions:**\n\n'I will continue to pump the brake pedal to deplete air pressure further. The parking brake valve knob should automatically pop out between 20 and 45 psi.'\n\n*💡 Tip: Do not pull the valve out by hand; let the system do it.*")

# ------------------------------------------------------------------
# SECTION 4: IN-CAB & SAFETY
# ------------------------------------------------------------------
with tab4:
    st.header("In-Cab & Passenger Area")
    
    in_cab_part = st.selectbox(
        "Choose a part to review:", 
        ["Safe Start Sequence", "Windshield & Wipers", "Emergency Equipment", "Passenger Seats & Exits"]
    )
    
    st.markdown("---")
    
    if in_cab_part == "Safe Start Sequence":
        display_part_image("dash_panel.jpg", "Gear Selector / Ignition")
        st.success("**✅ Safe Start Script:**\n\n'With the parking brake firmly set, I will verify the transmission is in Neutral. I turn the key to the ON position to let the dashboard ABS light cycle on and off, then I safely start the engine.'")
    
    elif in_cab_part == "Windshield & Wipers":
        display_part_image("windshield.jpg", "Windshield & Wipers")
        st.success("**✅ Windshield & Wipers Script:**\n\n'The windshield is clean, free of cracks, obstruction, or illegal stickers. The wiper arms and blades are properly mounted, the rubber is not torn, and the washer fluid operates smoothly.'")
    
    elif in_cab_part == "Emergency Equipment":
        display_part_image("safety_kit.jpg", "Fire Extinguisher & Triangles")
        st.success("**✅ Emergency Equipment Script:**\n\n'I have three red reflective triangles, spare fuses matching the vehicle requirements, and a fully charged fire extinguisher rated 10-BC with its safety pin securely in place.'")
    
    elif in_cab_part == "Passenger Seats & Exits":
        display_part_image("passenger_aisle.jpg", "Passenger Area")
        st.success("**✅ Passenger Area Script:**\n\n'All passenger seats are securely bolted to the floor framework with no broken frames or exposed spring metal. All emergency exit handles operate smoothly, doors seal correctly, and the warning alarms buzz when opened.'")

# ------------------------------------------------------------------
# SECTION 5: EXTERNAL WALKAROUND
# ------------------------------------------------------------------
with tab5:
    st.header("External Walkaround (Side & Rear)")
    
    walk_part = st.selectbox(
        "Choose external component:",
        ["Side / Rear Brakes (Chambers & Adjusters)", "Lights & Reflectors (Side/Rear)"]
    )
    
    st.markdown("---")
    
    if walk_part == "Side / Rear Brakes (Chambers & Adjusters)":
        display_part_image("brake_chamber.jpg", "Brake Chamber & Slack Adjuster")
        st.help("**📐 Brake Assembly Script:**\n\n'Brake chambers are securely mounted, not dented, cracked, or leaking air. Slack adjusters and pushpins have no loose or missing parts; when pulled by hand with the brakes released, the push rod should move no more than 1 inch.'")
    
    elif walk_part == "Lights & Reflectors (Side/Rear)":
        display_part_image("bus_lights.jpg", "External Lights")
        st.help("**📐 Lights & Reflectors Script:**\n\n'All external light lenses and reflectors are clean, unbroken, and the proper legal color (amber on the sides, red on the rear). I will check turn signals, emergency flashers, clearance indicators, and brake lights.'")