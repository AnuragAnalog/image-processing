#!/usr/bin/python3

import numpy as np
import streamlit as st

from PIL import Image
from matplotlib import pyplot as plt

from skimage.color import rgb2gray, gray2rgb

st.set_option('deprecation.showfileUploaderEncoding', False)

st.title("Image Processing")
st.header("Upload an Image, which needs to be processed!")

uploaded_img = st.file_uploader("Choose a Jpeg", type=["jpeg", "jpg", "png"])

if uploaded_img is not None:
    img = Image.open(uploaded_img)
    img_arr = np.asarray(img)

show_raw_img = st.checkbox("Show Original Image")

if show_raw_img:
    plt.imshow(img_arr)
    st.pyplot()

rgb_or_gray = st.sidebar.selectbox("Deal with RGB or Grayscale Images?", ['RGB', 'GrayScale'])

if rgb_or_gray == 'RGB':
    st.subheader("Working on RGB Image")

    if len(img_arr.shape) == 2:
        img_arr = gray2rgb(img_arr)

    int_hist = st.checkbox("Intensity Histogram!")
    if int_hist:
        plt.hist(img_arr[:, :, 0].ravel(), bins=256, alpha=0.5, color='red', label='Red')
        plt.hist(img_arr[:, :, 1].ravel(), bins=256, alpha=0.5, color='green', label='Green')
        plt.hist(img_arr[:, :, 2].ravel(), bins=256, alpha=0.5, color='blue', label='Blue')
        plt.legend()
    # plt.imshow(img_arr)
    st.pyplot()
elif rgb_or_gray == "GrayScale":
    st.subheader("Working on GrayScale Image")

    if len(img_arr.shape) == 3:
        img_arr = rgb2gray(img_arr)
    plt.imshow(img_arr)
    st.pyplot()