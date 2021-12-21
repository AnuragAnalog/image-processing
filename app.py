#!/usr/bin/python3

import numpy as np
import streamlit as st

from PIL import Image
from matplotlib import pyplot as plt

from skimage.color import rgb2gray, gray2rgb

# Required functions
def show_image(image, cmap='gray'):
    fig, ax = plt.subplots()

    if cmap == 'gray':
        ax.imshow(image, cmap=cmap)
    elif cmap == 'rgb':
        ax.imshow(image)
    ax.axis('off')
    st.pyplot(fig)

    return

# Setting page config's
st.set_page_config(page_title="Image Processing")

# Suppressing streamlit warnings
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Image Processing")
st.header("Upload an Image, which needs to be processed!")

uploaded_img = st.file_uploader("Choose a Jpeg", type=["jpeg", "jpg", "png"])

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    img_arr = np.asarray(img)

    show_raw_img = st.checkbox("Show Original Image")

    if show_raw_img:
        show_image(img_arr, cmap='rgb')

    rgb_or_gray = st.sidebar.selectbox("Deal with RGB or Grayscale Images?", ['RGB', 'GrayScale'])

    if rgb_or_gray == 'RGB':
        st.subheader("Working on RGB Image")

        if len(img_arr.shape) == 2:
            img_arr = gray2rgb(img_arr)

        int_hist = st.checkbox("Intensity Histogram!")
        if int_hist:
            fig, ax = plt.subplots()

            ax.hist(img_arr[:, :, 0].ravel(), bins=256, alpha=0.5, color='red', label='Red')
            ax.hist(img_arr[:, :, 1].ravel(), bins=256, alpha=0.5, color='green', label='Green')
            ax.hist(img_arr[:, :, 2].ravel(), bins=256, alpha=0.5, color='blue', label='Blue')
            ax.legend()
            st.pyplot(fig)

        rgb_channel = st.checkbox("Images in different channels")
        if rgb_channel:
            fig, ax = plt.subplots(nrows=1, ncols=3)

            ax[0].imshow(img_arr[:, :, 0])
            ax[1].imshow(img_arr[:, :, 1])
            ax[2].imshow(img_arr[:, :, 2])
            st.pyplot(fig)
    elif rgb_or_gray == "GrayScale":
        st.subheader("Working on GrayScale Image")

        if len(img_arr.shape) == 3:
            img_arr = rgb2gray(img_arr)
        show_image(img_arr)
