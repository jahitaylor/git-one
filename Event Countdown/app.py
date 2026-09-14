import streamlit as st
from datetime import datetime
import time

# Set up the page to stretch across a TV screen
st.set_page_config(page_title="TV Countdowns", layout="wide")

# Use HTML inside Markdown just to make the text massive for the TV
st.markdown("<h1 style='text-align: center; font-size: 4rem; color: #4dabf7;'>Resilient Lady Cruise</h1>", unsafe_allow_html=True)

# Create an empty placeholder block on the page that we will overwrite every second
clock_placeholder = st.empty()

# Set the target date
target_date = datetime(2026, 12, 13, 0, 0, 0)

# The ticking loop
while True:
    now = datetime.now()
    distance = target_date - now
    
    if distance.total_seconds() < 0:
        clock_placeholder.markdown("<h2 style='text-align: center; font-size: 6rem;'>ARRIVED!</h2>", unsafe_allow_html=True)
        break
        
    # Calculate days, hours, minutes, seconds
    days = distance.days
    hours, remainder = divmod(distance.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Format the string to always show two digits (e.g., 09s instead of 9s)
    time_string = f"{days}d : {hours:02d}h : {minutes:02d}m : {seconds:02d}s"
    
    # Push the updated time to the placeholder block
    clock_placeholder.markdown(f"<h2 style='text-align: center; font-size: 6rem;'>{time_string}</h2>", unsafe_allow_html=True)
    
    # Pause the script for 1 second, then loop again
    time.sleep(1)