from PIL import Image
import requests
import streamlit as st
from  streamlit_lottie import st_lottie

st.set_page_config(page_title="My webpage",page_icon=":tada:",layout="wide")


def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
    
local_css("C:/Users/madhan/python_streamlit/style.css")

#-----load assets------
lottie_coding=load_lottieurl("https://lottie.host/2f1da471-5c85-4ffb-ba05-ea4397fe2ba1/oZrQjWNE31.json")
img_contact_form=Image.open("C:/Users/madhan/python_streamlit/images/Screenshot 2023-08-06 175657.png")

#-----header section------
st.subheader("Hi, I am Madhankumar :wave: :revolving_hearts:")
st.title("A Data engineer from India")
st.write("I am passionate about Data extracting from different resources and analyzing ")
st.write("[Learn more>](https://www.youtube.com/watch?v=rYE3VEiZ1Xk)")


#---------what i do-------
with st.container():
    st.write("----")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("what I do")
        st.write("##")
        st.write(
            """
            on my youtube channel i am creating tutorials for peoples who:
            - are looking for a way to leaverage the power of dataengineer in their day-to-day work.
            - are struggling to build pipeline task in informatica,snowflake and aws glue looking for way to use dataengineer.
            """
            )
        st.write("[youtube channel>](https://www.youtube.com/@samhudaya7549)")
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")

#----My project-------
with st.container():
    st.write("-----")
    st.header("My Project")
    st.write("##")
    image_column,text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader(" Data Engineer project with help of Python and PowerBi")
        st.write(
            """
            learn how to use PowerBi dashboard!
            dashboard make our Analysis more engaging and fun, and python  is the easiest way to do
            """
        )
        st.markdown("[watch video....](https://www.youtube.com/watch?v=VqgUkExPvLY&t=189s)")
with st.container():
    st.write("---")
    st.header("Get In Touch with Me!")
    st.write("##")

    #Documentation:https://formsubmit.co/ !!! change email address!!!
    contact_form="""
    <form action="https://formsubmit.co/mpmadhankumar5@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea type ="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """
    left_column,right_column=st.columns(2)
    with left_column:
        st.markdown(contact_form,unsafe_allow_html=True)
    with right_column:
        st.empty()

