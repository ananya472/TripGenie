import streamlit as st
import ollama

# Function to generate itinerary using Ollama
def generate_itinerary(destination, days, budget, preferences, dietary, mobility, accommodation):
    prompt = f"""
    You are an AI travel planner. Plan a {days}-day trip to {destination} with a budget of {budget} USD.  

**User Preferences:**  
- **Interests:** {preferences}  
- **Dietary Preferences:** {dietary}  
- **Mobility Considerations:** {mobility}  
- **Preferred Accommodation Type:** {accommodation}  

### **Trip Itinerary Requirements:**  
Provide a **detailed and well-structured itinerary**, including:  
✅ **Daily Schedule** with morning, afternoon, and evening activities  
✅ **Top Attractions & Activities** aligned with user interests  
✅ **Accommodation Recommendations** within the budget  
✅ **Local Food Spots** that fit dietary preferences  
✅ **Transportation Tips** for navigating the destination  
✅ **Hidden Gems & Cultural Experiences** for an authentic experience  

Ensure the itinerary stays within budget while maximizing the experience!  

    """

    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# Streamlit UI
st.title("🌍 AI-Powered Travel Planner")

# User Inputs
destination = st.text_input("Enter your destination", "Paris")
days = st.slider("Number of days", 1, 10, 3)
budget = st.number_input("Budget (in USD)", min_value=100, value=1000, step=100)
preferences = st.text_area("Your Interests (e.g., adventure, history, food)")

# Additional Refinements
dietary = st.text_input("Dietary Preferences (e.g., vegan, halal, no restrictions)", "No restrictions")
mobility = st.text_input("Mobility Concerns (e.g., wheelchair accessible, long walks okay)", "No concerns")
accommodation = st.selectbox("Preferred Accommodation", ["Luxury", "Budget", "Central Location", "No preference"])

# Generate Final Itinerary
if st.button("Generate Itinerary"):
    with st.spinner("Planning your trip..."):
        itinerary = generate_itinerary(destination, days, budget, preferences, dietary, mobility, accommodation)
        st.subheader("📅 Your Personalized Itinerary")
        st.write(itinerary)
