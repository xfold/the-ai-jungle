import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# Load the trained model (assuming it's saved as 'mario_luigi_toad_model.h5')
model = tf.keras.models.load_model('model/mario_luigi_toad_model.h5')

st.title("Mario, Luigi, or Toad Classifier")
st.write("Upload an image and the classifier will predict whether it's Mario, Luigi, or Toad.")

# Upload image via streamlit
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])
class_colors = ['red', 'green', 'orange']

if uploaded_file is not None:
    # Open and display the uploaded image (smaller width)
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width='auto', width=200)
    
    # Preprocess and predict with a spinner
    with st.spinner('Model is thinking...'):
        img_array = np.array(image.resize((128, 128))) / 255.0  # same preprocessing as before
        img_array = img_array[np.newaxis, ...]  # Add batch dimension
        prediction = model.predict(img_array)

    # Display the probabilities with fancy colors
    st.markdown(f"<h3 style='color: red;'>Mario: {100 * prediction[0][0]:.2f}%</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: green;'>Luigi: {100 * prediction[0][1]:.2f}%</h3>", unsafe_allow_html=True)
    st.markdown(f"<h3 style='color: orange;'>Toad: {100 * prediction[0][2]:.2f}%</h3>", unsafe_allow_html=True)

    # Find the class with the highest probability
    class_names = ['Mario', 'Luigi', 'Toad']
    predicted_class = class_names[np.argmax(prediction)]

    # Display the result in bigger letters
    st.markdown(f"<h1 style='text-align: center;'>It's <span style='color: {class_colors[np.argmax(prediction)]};'>{predicted_class}</span>!</h1>", unsafe_allow_html=True)