import streamlit as st
import random
from PIL import Image

def classify_image(image) -> bool:
    """Classify if an image has palm trees or not

    Params:
    -image (bytes)
    Returns:
    -bool: True for palm tree, False otherwise
    """
    return random.choice([True, False])

def analyze_image(image):
    """Analyze parts of image that most contributed to classification

    Params:
    -image(bytes): image to analyze

    Returns:
    -bytes: image showing most contributive part of the image
    """

    return Image.open(image).convert("L")  # convert image to grayscale


st.write("# Palm Tree Detector")

with st.sidebar:
    image_file = st.file_uploader("Choose an image", 
                                type=["jpg", "png"],
                                help="Select image to be classified",
                                )

if image_file is not None:
    bytes_image = image_file.getvalue()
    st.image(bytes_image, width = 256)

if st.button("Detect palm trees", disabled=(image_file is None)):
    result=classify_image(bytes_image)
    if result:
        st.write("Palm Trees detected")
    else:
        st.write("No palm Trees detected")

    with  st.expander("Sensibility Analysis", expanded=False):
        analysis_image = analyze_image(image_file)
        st.image(analysis_image)

