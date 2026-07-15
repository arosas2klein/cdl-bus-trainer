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
tab1, tab2, tab3, tab4 = st.tabs([
    "🔧 Engine Compartment", 
    "🛑 Air Brakes", 
    "👤 In-Cab & Safety", 
    "📐 External Walkaround"
])

# ------------------------------------------------------------------
# SECTION 1: ENGINE COMPARTMENT
# ------------------------------------------------------------------
with tab1:
    st.header("Engine Compartment")
    st.write("Click a component to inspect:")
    
    # Grid arrangement for thumb-tapping layout
    col1, col2 = st.columns(2)
    with col1:
        alt_clicked = st.button("⚡ Alternator", use_container_width=True)
        water_clicked = st.button("💧 Water Pump", use_container_width=True)
    with col2:
        steering_clicked = st.button("⚙️ Steering Box", use_container_width=True)
        fluid_clicked = st.button("🧪 Fluids (Oil/Coolant)", use_container_width=True)

    st.markdown("---")

    # Dynamic Display based on selection
    if alt_clicked:
        display_part_image("alternator.jpg", "Alternator")
        st.info("**⚡ Alternator Script:**\n\n'Properly mounted and secure. No loose or missing bolts. Wires are secure, not frayed, and connections are clean. Belt-driven with no more than 3/4 inch of play.'")
    
    elif water_clicked:
        display_part_image("water_pump.jpg", "Water Pump")
        st.info("**💧 Water Pump Script:**\n\n'Properly mounted and secure. Not cracked, bent, or broken. No loose or missing hardware. No signs of leaking. Belt-driven.'")
    
    elif steering_clicked:
        display_part_image("steering_box.jpg", "Steering Gear Box")
        st.info("**⚙️ Steering Gear Box Script:**\n\n'Properly mounted and secure. Not cracked, bent, or broken. No loose or missing bolts. No leaks from lines or the box itself.'")
        
    elif fluid_clicked:
        display_part_image("fluids.jpg", "Fluid Level Dipsticks")
        st.info("**🧪 Fluids Script:**\n\n'I will check the coolant sight glass or reservoir level, and pull the oil dipstick to ensure it is above the refill mark. I am checking all hoses and underneath the engine block for any active fluid leaks.'")

# ------------------------------------------------------------------
# SECTION 2: AIR BRAKE TEST (CRITICAL SECTION)
# ------------------------------------------------------------------
with tab2:
    st.header("Air Brake Test")
    st.error("⚠️ WARNING: Missing or messing up any step in this sequence results in an AUTOMATIC FAILURE on the real CDL exam.")
    
    # Radio buttons force step-by-step sequencing
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
# SECTION 3: IN-CAB & SAFETY
# ------------------------------------------------------------------
with tab3:
    st.header("In-Cab & Passenger Area")
    
    # Dropdown selector is great for large groups of items
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
# SECTION 4: EXTERNAL WALKAROUND
# ------------------------------------------------------------------
with tab4:
    st.header("External Walkaround")
    
    walk_part = st.selectbox(
        "Choose external component:",
        ["Tires (The ICD Rule)", "Suspension (Springs & U-Bolts)", "Brakes (Chambers & Adjusters)", "Lights & Reflectors"]
    )
    
    st.markdown("---")
    
    if walk_part == "Tires (The ICD Rule)":
        display_part_image("tires.jpg", "Tire Assembly")
        st.help("**📐 Tire Inspection Script (Remember ICD):**\n\n* **Inflation:** I will check inflation using an air pressure gauge to verify it is at manufacturer spec (around 100-110 psi).\n* **Condition:** No cuts, bubbles, dry rot, or separation on the tread or sidewalls.\n* **Depth:** Tread depth must be at least 4/32 inch on steering axle tires, and 2/32 inch on all other tires. Front steering tires cannot be recapped.")
    
    elif walk_part == "Suspension (Springs & U-Bolts)":
        display_part_image("suspension.jpg", "Leaf Springs Assembly")
        st.help("**📐 Suspension Script:**\n\n'Leaf springs are properly mounted, secure, and not cracked, broken, or shifted out of alignment. The U-bolts are secure with no cracked or missing hardware, and no shiny clean areas or rust trails indicating movement.'")
    
    elif walk_part == "Brakes (Chambers & Adjusters)":
        display_part_image("brake_chamber.jpg", "Brake Chamber & Slack Adjuster")
        st.help("**📐 Brake Assembly Script:**\n\n'Brake chambers are securely mounted, not dented, cracked, or leaking air. Slack adjusters and pushpins have no loose or missing parts; when pulled by hand with the brakes released, the push rod should move no more than 1 inch.'")
    
    elif walk_part == "Lights & Reflectors":
        display_part_image("bus_lights.jpg", "External Lights")
        st.help("**📐 Lights & Reflectors Script:**\n\n'All external light lenses and reflectors are clean, unbroken, and the proper legal color (amber on the front/sides, red on the rear). I will check high/low beam headlights, turn signals, emergency flashers, clearance indicators, and brake lights.'")