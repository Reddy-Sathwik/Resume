import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image
from streamlit_lottie import st_lottie
image = Image.open("RVUC.jpeg")
st.set_page_config(layout='centered', page_title="My Portfolio")
st.header("Hey Guys :wave:")
st.subheader("I am Kumbam Sathwik Reddy")
st.title("My portfolio Website")
st.write("Click below to know about myself")
def l(url):
    r = requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lc =l("https://lottie.host/ad96ff28-e06b-4e20-a81a-910e3f288b0a/k8sB6zbsWg.json")
with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact','Resume'],
        icons=['person', 'code-slash', 'chat-left-text-fill','file-earmark-text'],
        orientation="horizontal"
    )
if selected=='About':
    with st.container():
        c1,c2 = st.columns(2)
        with c1:
            st.subheader("I am Kumbam Sathwik Reddy")
            st.title("Undergrad at Chandigarh University")
        with c2:
            st.lottie(lc)
    st.write("______")
    with st.container():
        c3,c4 = st.columns(2)
        with c3:
            st.subheader("""
                         Education:
                             Chandigarh University:
                                -BE Computer Science
                                -Grade:7.7 cgpa
                             Narayana Educations Institutions
                                -MPC
                                -Grade: 96%
                             Spr School
                                -Xth
                                -Grade:9.2 cgpa
                         """)
        with c4:
            st.subheader("""
                         Experience:
                            Software Developer Intern @Techno India Pvt Ltd (November 2023 - Present)
                         """)
if selected=="Projects":
    with st.container():
        st.header("My Projects")
        st.write('##')
        c5,c6 = st.columns((1,2))
        with c5:
            st.image(image)
        with c6:
            st.subheader("""
                    Real Time Video Analysis using Mobile Cloud
                    Description: Real-time video analysis, also 
                    known as real-time video processing or 
                    real-time video analytics, is the process
                    of analyzing and extracting meaningful information 
                    from video data as it is being captured and streamed,
                    without significant delay.""")
            st.text("Tools Used: Python and AWS")
if selected=="Contact":
    st.subheader("Get in Touch")
    st.text("Click below")
    st.write("reddy.sathwikkumbam@gmail.com")

if selected=="Resume":
    #st.subheader("Resume")
    # Replace 'your_document.pdf' with the actual document file and provide the desired link text.
    st.markdown("[View Resume](https://drive.google.com/file/d/1pzer_j4XfarzHKrzlQnaBiHhR3CoVmRy/view?usp=drive_link)")
