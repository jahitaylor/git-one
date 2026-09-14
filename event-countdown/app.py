import streamlit as st
from datetime import datetime
import time

# Set up the page layout
st.set_page_config(page_title="TV Countdowns", layout="wide")

# The CSS to inject the background image
page_bg_img = """
<style>
/* Target the main app container */
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.imgur.com/ZSOkTQU.jpeg"); /* Replace with your URL */
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

/* Make the top header transparent so it doesn't block the image */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Add a darker, semi-transparent background to the clock cards so text stays readable */
.clock-card {
    background-color: rgba(30, 30, 30, 0.85) !important;
}
</style>
"""

# Push the CSS to the page
st.markdown(page_bg_img, unsafe_allow_html=True)
# Define your 4 events here
events = [
    {"name": "Test Flights CGH to UCH", "date": datetime(2026, 9, 24, 0, 0, 0)},
    {"name": "Hive Ribbon Cutting", "date": datetime(2026, 10, 6, 0, 0, 0)},
    {"name": "Part 135", "date": datetime(2027, 3, 1, 0, 0, 0)},
    {"name": "Path Lab Ops Ready", "date": datetime(2027, 4, 1, 0, 0, 0)}
]

st.markdown("<h1 style='text-align: center; margin-bottom: 40px;'>Upcoming Events</h1>", unsafe_allow_html=True)

# Create a 2x2 grid using Streamlit columns
row1_col1, row1_col2 = st.columns(2)
row2_col1, row2_col2 = st.columns(2)

# Create a placeholder block for each grid quadrant
placeholders = [
    row1_col1.empty(), 
    row1_col2.empty(), 
    row2_col1.empty(), 
    row2_col2.empty()
]

# The ticking loop
while True:
    now = datetime.now()
    
    for i, event in enumerate(events):
        distance = event["date"] - now
        
        # HTML/CSS to style each clock like a digital card
        card_style = """
            <div class='clock-card' style='padding: 30px; border-radius: 15px; 
                        text-align: center; margin-bottom: 20px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);'>
                <h3 style='color: #4dabf7; font-size: 2rem; margin-top: 0;'>{name}</h3>
                <h2 style='font-size: 3.5rem; margin-bottom: 0; font-family: monospace;'>{time}</h2>
            </div>
        """
        
        if distance.total_seconds() < 0:
            html = card_style.format(name=event['name'], time="ARRIVED!")
        else:
            days = distance.days
            hours, remainder = divmod(distance.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            time_string = f"{days}d : {hours:02d}h : {minutes:02d}m : {seconds:02d}s"
            html = card_style.format(name=event['name'], time=time_string)
            
        # Overwrite the placeholder with the new time
        placeholders[i].markdown(html, unsafe_allow_html=True)
        
    time.sleep(1)