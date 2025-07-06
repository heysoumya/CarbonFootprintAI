import streamlit as st

st.title("🌍 Carbon Footprint Calculator")
car_miles = st.slider("🚗 Weekly car miles", 0, 100)
flights = st.number_input("✈️ Flights this year", 0)
bus_rides = st.number_input("Weekly bus/train rides", 0)
diet_type = st.selectbox("Diet", ["🍗 meat-heavy", "🍛 vegetarian", "🌱 vegan"])

if st.button("Calculate"):
    emissions -= bus_rides * 0.1  # Subtract emissions saved by public transport
    emissions = car_miles*0.4 + flights*90 + \
               (3.0 if diet_type=="meat-heavy" else 1.5)*365
    st.write(f"Annual CO2: {emissions:.1f} kg")
