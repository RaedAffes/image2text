import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing 
  
#title
st.title("Easy OCR(Optical Character Recognition.) - Extract Text from Images")
 
#subtitle
st.markdown("## Optical Character Recognition - Using `easyocr`, `streamlit` -  hosted on 🤗 Spaces by Raed Affes")

st.markdown("Link to the app - [image2text on 🤗 Spaces](https://huggingface.co/spaces/RaedAffes/image2textapp)")
st.markdown("link to the github repository : https://github.com/RaedAffes/image2text ")

#image uploader
image = st.file_uploader(label = "Upload your image here",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    #st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")

st.caption("Made with ❤️ by @Raed. Credits to 🤗 Spaces for Hosting this ")
