# Assignment4

In this assignment, the goal is to construct an all-encompassing picture retrieval system specifically connected to fashion. Starting with a selected dataset derived from a collection of defined sources, the method entails computing embeddings for photos and storing them using PINECONE, in addition to saving images in Amazon S3. To establish a connection between picture IDs and text tags and embeddings, a database is developed. The fundamental functionality is encased in a FAST application programming interface (API), which provides two primary functions:
 - getting the picture that is nearest to us based on text descriptions, and,
 - locating images that are similar to the one that is input.

An intuitive interface is provided for users to input text descriptions or upload images, and the entire system is encapsulated within a user-friendly Streamlit app. This allows users to interact seamlessly with the underlying functionalities of the FAST API, which allows for efficient image retrieval and similarity searches in the fashion domain.

## Usage/Steps:
- Open the terminal and clone this repo or use GitHub Desktop, Upload these notebooks on google colab or you can run locally as well.
- set up the Amazon AWS account to generate S3 keys and tokens. Also set up your FASTAPI token key (in this assignment we have used ngrok: https://dashboard.ngrok.com )
- Install all the requirements and run the streamlit application.

codelab documentation: https://codelabs-preview.appspot.com/?file_id=1bQzol0834n3zH-JHBs8_u7no6_6PIOLoG-YiIG_--sg#0

Streamlit Deployed Application: https://assignment4-wrcqmwtt3mobxgbn7ken23.streamlit.app/
