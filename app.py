import streamlit as st

# Set up the mobile-responsive page title
st.set_page_config(page_title="CDL Pre-Trip Trainer", page_icon="🚌", layout="centered")

st.title("🚌 CDL Pre-Trip Inspection Helper")
st.write("Tap a section, then select a part to see exactly what you need to say to the examiner.")

# Create main categories as mobile-friendly tabs
tab1, tab2, tab3 = st.tabs(["🔧 Engine Compartment", "🛑 Air Brakes", "👤 In-Cab & Passenger"])

# ----------------- SECTION 1: ENGINE COMPARTMENT -----------------
with tab1:
    st.header("Engine Compartment")
    # You can host your bus images anywhere online (like Imgur or GitHub itself)
    st.image("https://images.unsplash.com/photo-1557223562-6c77ef16210f?q=80&w=600", caption="Engine Side View")
    
    # Create rows of mobile-friendly click buttons
    col1, col2 = st.columns(2)
    with col1:
        alt_clicked = st.button("⚡ Alternator")
        water_clicked = st.button("💧 Water Pump")
    with col2:
        steering_clicked = st.button("⚙️ Steering Gear Box")
        belt_clicked = st.button("🎗️ Engine Belts")

    # Display the correct CDL verbiage based on what they tapped
    if alt_clicked:
        st.info("**Alternator Script:**\n\n'Properly mounted and secure. No loose or missing bolts. Wires are secure, not frayed, and connections are clean. Belt-driven with no more than 3/4 inch of play.'")
    elif water_clicked:
        st.info("**Water Pump Script:**\n\n'Properly mounted and secure. Not cracked, bent, or broken. No loose or missing hardware. No signs of leaking. Belt-driven.'")
    elif steering_clicked:
        st.info("**Steering Gear Box Script:**\n\n'Properly mounted and secure. Not cracked, bent, or broken. No loose or missing bolts. No leaks from lines or the box itself.'")
    elif belt_clicked:
        st.info("**Engine Belts Script:**\n\n'Check all belts for cracks, frays, or loose fibers. Belts should have no more than 3/4 inch of play when pushed.'")

# ----------------- SECTION 2: AIR BRAKE TEST -----------------
with tab2:
    st.header("Air Brake Test (Must be 100% Perfect)")
    
    step = st.radio("Select Brake Test Step:", ["Step 1: Applied Pressure Leak Test", "Step 2: Low Air Warning", "Step 3: Valve Pop-Out"])
    
    if step == "Step 1: Applied Pressure Leak Test":
        st.warning("**What to say & do:**\n\n'With a fully charged system, I will turn the engine off, turn the key back to the ON position, release both brakes, and hold down the service brake pedal for one minute. I should not lose more than 3 psi in one minute.'")
    elif step == "Step 2: Low Air Warning":
        st.warning("**What to say & do:**\n\n'I will pump the brake pedal repeatedly. The low air warning light and buzzer must activate at or before the air pressure drops to 55 psi.'")
    elif step == "Step 3: Valve Pop-Out":
        st.warning("**What to say & do:**\n\n'I will continue to pump the brake pedal. The parking brake valve knob should pop out between 20 and 45 psi.'")

# ----------------- SECTION 3: IN-CAB -----------------
with tab3:
    st.header("In-Cab & Passenger Area")
    
    part = st.selectbox("Choose a part to inspect:", ["Safe Start", "Windshield & Wipers", "Emergency Equipment", "Passenger Seats"])
    
    if part == "Safe Start":
        st.success("**Safe Start Script:**\n\n'With the parking brake set, I will place the transmission in Neutral, turn the key to ON to let the ABS dashboard light cycle, then start the engine safely.'")
    elif part == "Windshield & Wipers":
        st.success("**Windshield & Wipers Script:**\n\n'Windshield is clean, not cracked, with no illegal stickers. Wipers are properly mounted, rubber is not torn, and washer fluid sprays effectively.'")
    elif part == "Emergency Equipment":
        st.success("**Emergency Equipment Script:**\n\n'I have 3 red reflective triangles, a fully charged fire extinguisher rated 10-BC with its pin in place, and spare electrical fuses.'")
    elif part == "Passenger Seats":
        st.success("**Passenger Seats Script:**\n\n'All seats are securely mounted to the floor with no loose frames. Cushions are firmly attached with no exposed metal or sharp springs.'")