# Fine-tuning BERT for Identifying "The Simpsons" Characters

## Introduction

In this project, we aim to classify sentences based on whether they sound more like Homer or Bart from "The Simpsons". Our approach involves fine-tuning a pre-trained BERT model on a dataset manually curated composed of TheSimpsons dialogs collected online

BERT (Bidirectional Encoder Representations from Transformers) is a transformer-based architecture that's pre-trained on a vast amount of text. Fine-tuning it allows us to leverage the pre-trained weights and adapt them to our specific task, which, in this case, is classifying sentences based on their speaker.

<img src="img/bert_class.gif" width="350"/>

## Methodology

### Data Preprocessing
The dataset was sourced from various TheSimpsons dialogs collected online. Only sentences from 'Homer', 'Homer Simpson', 'Homer Simpsons', 'Bart', or 'Bart Simpson' (in any combination of capital letters) were retained. The processed dataset contained the speaker's name, the sentence, and the episode from which the line originated.

### Model Training
We employed the BERT model, which is a transformer-based architecture known for its remarkable performance in various NLP tasks. The model was fine-tuned on our dataset for classification. 
Training was carried out only with a few epochs; increasing the number of epochs should improve the model.

### Model Evaluation
After training, the model was evaluated using a test set to determine its performance. We looked at metrics like loss and accuracy to gauge how well the model generalizes to unseen data.

## Improvements

1. **Data Augmentation**: Increase the dataset size using techniques like back translation or sentence paraphrasing.
2. **Hyperparameter Tuning**: Experiment with different learning rates, batch sizes, and model architectures.
3. **Training Duration**: Train the model for more epochs while monitoring for signs of overfitting.
4. **Model Ensembling**: Combine predictions from multiple models to improve accuracy.
5. **Use Advanced Models**: Explore newer models or variants of BERT like RoBERTa, DistilBERT, or ALBERT.

## Additional Notes

- **Early Stopping**: To prevent overfitting, consider implementing early stopping based on validation loss.
- **Regularization**: Techniques like dropout or weight decay can help in regularizing the model and preventing overfitting.
- **Deployment**: The model has been deployed using a Streamlit app, which offers a simple interface for users to input sentences and get predictions.

## Streamlit App Interface

To provide an interactive interface for users to test the fine-tuned BERT model, we've developed a web application using Streamlit. This application allows users to input sentences and view predictions on whether the sentence sounds more like Homer or Bart.

1. **User Input**: A text box for users to enter any sentence they wish to evaluate.
2. **Model Prediction**: Upon entering a sentence, the model evaluates the input and predicts the speaker. The result is then displayed to the user.
3. **Visual Feedback**: Based on the prediction, an image of either Homer or Bart is displayed, providing a visual cue in addition to the textual prediction.

To run the Streamlit app locally
```
streamlit run app.py
```