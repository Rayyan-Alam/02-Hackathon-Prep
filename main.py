import streamlit as st
import time

st.title("Hello, Whats Good! 👋")
st.markdown(
    """ 
    This is a playground for you to try Streamlit and have fun. 

    **There's :rainbow[so much] you can build!**
    
    We prepared a few examples for you to get started. Just 
    click on the buttons above and discover what you can do 
    with Streamlit. 
    """
)

for i in range(1, 4):
    st.markdown(i)
    time.sleep(1)

if st.button("Send balloons!"):
    st.balloons()
