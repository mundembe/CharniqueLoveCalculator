import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

#----------------------Variables---------------
his = ["masimba", "my simba", "simba", "mysimba"]
his_passed = False
her = ["charnique", "cnique", "chernique"]
her_passed = False
text = "Give yor lover a chance\nYour life will change at a glance\nMy heart was placed inside a trance\nAs I fell in love from just one dance"
poem = "There once was a man named Masimba\nAnd he wanted a girl who\'s unique\nThere was only one girl for Masimba\nAnd the girl name was Charnique"

st.set_page_config(page_title="Love Calculator", page_icon=":heart:", layout="wide")

def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

#-----------Load Assets-----------
lottie_animation = load_lottie_url("https://assets8.lottiefiles.com/packages/lf20_we4yddwi.json")

# ----------Header Section------------

with st.container():
    st.header("HI")
    st.subheader("Welcome to the most truthfull Love Calculator")
    st.title("We will calculate if you are compatable with someone")
    st.write("Just type in the first names of the two would-be lovers down below, and leave the rest to us")
    st.write("This is the most accurate Love Calculator out there")
    st.write("---")

with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.header("LOVE CALCULATOR")
        st.write("##")
        name_1 = st.text_input("Her Name", placeholder="Enter Her Name Here")
        name_1 = name_1.lower()
        name_2 = st.text_input("His Name", placeholder="Enter His Name Here")
        name_2 = name_2.lower()


        if st.button("Calculate"):
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.001)
                progress_bar.progress(percent_complete + 1)

            if name_1 in her:
                her_passed = True
            if name_2 in his:
                his_passed = True
            if her_passed and his_passed:
                st.success("100% match:heart:This is truly a match made in Heaven")
                st.balloons()
                text = poem
            elif her_passed and not (his_passed):
                st.info("No Charnique, Masimba is the only one for you:laughing:")
            else:
                st.info('50% rate of success:broken_heart:')

        st.text_area("", text)

    with right_column:
        st_lottie(lottie_animation, height=300, key="coding")
    
#-----------Contact me-----------
with st.container():
    st.write("---")
    st.header("Get in touch with me")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/1488e08f91862990255ded1dd0e415e8" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
    