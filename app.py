import pywhatkit as pw 
import streamlit as st
st.title("Convert text to handwriting")
st.image("https://cdn.pixabay.com/photo/2019/03/26/04/30/influencer-4081842_960_720.jpg",width=1000)
st.subheader("Enter the text you want to convert: ")
x=st.text_input(label="Write here: ")

st.image("https://excelatfinance.com/xlf/media/xlf-colindx2ws.png",width=1000)
st.subheader("You take a look at the scale above please select the color in which you want the handwriting in(R-red,G-green,B-blue):")
a=st.slider("Enter The value of red scale you want: ",0,255)
b=st.slider("Please enter the green scale you want: ",0,255)
c=st.slider("Please enter the blue scale you want: ",0,255)
if st.button("Click me for action"):
    try:
        pw.text_to_handwriting(x,"Flower.png",[a,b,c])
        with open("Flower.png", "rb") as file:
            btn = st.download_button(label="Download image",data=file,file_name="flower.png",mime="image/png")
    except:
        st.text("Sorry the server seems busy")

