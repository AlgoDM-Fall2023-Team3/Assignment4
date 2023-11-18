import streamlit as st
import requests
import json
from PIL import Image
from io import BytesIO
import base64

st.title("Image Search by CLIP")

c1, c2 = st.tabs(["Text Search","Image Search"])


with c1:
    st.header("Image Search By Text")

    text_input = st.text_input("Enter Text Description")
    api_url = "https://fb89-35-196-84-171.ngrok-free.app/search_images_by_text"

    if st.button("Search by Text"):
        # Use the ngrok URL to make the API request


        # Make the API request to FastAPI
        params = {"search_query": text_input, "results_count": 1}
        response = requests.post(url=api_url, json=params)

        if response.status_code == 200:
          # Convert the binary image data to a PIL Image
            image = Image.open(BytesIO(response.content))
            st.image(image, caption='Processed Image', use_column_width=True)
        else:
        # If the request was not successful, print the status code
            st.error(f"Error: {response.status_code}")

with c2:
    st.header("Image Search By Image")

    uploaded_file = st.file_uploader("Upload an image")

    api_url = "https://fb89-35-196-84-171.ngrok-free.app/search_images_by_image"
    if st.button("Search by Image") and uploaded_file is not None:

        bytes_data = uploaded_file.getvalue()
        base64_image = base64.b64encode(bytes_data).decode('utf-8')

        # Prepare the payload as a JSON object
        payload = {
            "image_file": base64_image,
            "results_count": 3
        }

        response = requests.post(url=api_url, json=payload)

        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)

        if response.status_code == 200:
            # Assuming images are separated by [SEP]
            # st.write(response.content)
            image_data_list = response.content.split(b'YOUR_CUSTOM_SEPARATOR')
            # image_data_list = response.content.split(b'[SEP]')
            # st.write(image_data_list)
            # st.write(len(image_data_list))
            st.write(f"len(image_data_list) = {len(image_data_list)}")
            # st.write(print(type(image_data_list)))
            for i, image_data in enumerate(image_data_list[:3]):
                try:
                    # Create an Image object from the BytesIO data
                    image = Image.open(BytesIO(image_data))

                    # Display the processed image
                    st.image(image, caption=f'Processed Image {i + 1}', use_column_width=True)

                except Exception as e:
                    st.warning(f"Unable to process image {i + 1}: {str(e)}")
        else:
            st.error(f"Error: {response.status_code}")
