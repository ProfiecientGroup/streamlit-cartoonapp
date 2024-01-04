import streamlit as st
import cv2
import numpy as np
from PIL import Image


def cartoonify(image):
    # Convert image to gray scale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    gray_blur = cv2.medianBlur(gray, 5)

    # Detect and enhance edges
    edges = cv2.adaptiveThreshold(gray_blur, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, 9, 9)

    # Apply bilateral filter to smoothen colors
    color = cv2.bilateralFilter(image, 9, 300, 300)

    # Combine edges with the color image
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cartoon

st.title("Image to Cartoon Converter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)

    cartoon = cartoonify(image)

    st.image(image, caption='Original Image', use_column_width=True)
    st.image(cartoon, caption='Cartoonified Image', use_column_width=True)
