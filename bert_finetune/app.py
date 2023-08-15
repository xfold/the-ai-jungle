import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load the model and tokenizer
MODEL_PATH = 'model/simpsons/'  # Adjust this to your model's path
tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

def predict_speaker(sentence):
    inputs = tokenizer(sentence, padding=True, truncation=True, return_tensors="pt", max_length=512)
    with torch.no_grad():
        outputs = model(inputs['input_ids'], attention_mask=inputs['attention_mask'])
    label = torch.argmax(outputs.logits).item()
    return 'Homer' if label == 0 else 'Bart'

st.title('Homer vs Bart Predictor')
st.write('This app predicts whether a given sentence sounds more like Homer or Bart from The Simpsons.')

# User input
user_input = st.text_input("Enter a sentence:")

if user_input:
    prediction = predict_speaker(user_input)
    
    # Display the prediction and corresponding image
    st.write(f'The sentence is likely said by: {prediction}')
    if prediction == 'Homer':
        st.image('img/homer.jpg', width=300)
    else:
        st.image('img/bart.jpg', width=300)

# Additional details or footer
st.write('---')
st.write('Created using fine-tuned BERT model.')


