# Fine-tuning BERT for Identifying "The Simpsons" Characters

## Introduction

In this project, we aim to classify sentences based on whether they sound more like Homer or Bart from "The Simpsons". Our approach involves fine-tuning a pre-trained BERT model on a dataset manually curated composed of TheSimpsons dialogs collected online

BERT (Bidirectional Encoder Representations from Transformers) is a transformer-based architecture that's pre-trained on a vast amount of text. Fine-tuning it allows us to leverage the pre-trained weights and adapt them to our specific task, which, in this case, is classifying sentences based on their speaker.

<img src="img/bert_class.gif" width="700"/>

## Fine-tuning a BERT to classify
Fine-tuning a BERT model (or any pre-trained model) is essentially a process of adapting a model that was previously trained on a large dataset to a specific task or dataset that might be much smaller. Here's what happens when you fine-tune a model like BERT:
1. **Starting Point**: Instead of starting with random weights, when you fine-tune, you start with the pre-trained weights. These weights already contain a lot of information about the language due to being trained on a massive amount of text. 
2. **Adapting Layers**: All layers of BERT, from embeddings up to the high-level transformer blocks, are slightly adjusted during fine-tuning. The gradients are backpropagated through the entire model. 
3. **Task-Specific Head**: BERT is pre-trained using a masked language model objective, where it learns to predict missing words in a sentence. 
4. **Classification Fine-tuning**: A fully connected layer is added on top of the BERT output for the `[CLS]` token. This layer produces the final class scores. During fine-tuning, the weights of this new layer are learned from scratch, while the rest of the BERT weights are adjusted.
5. **Learning Rate**: Typically, a smaller learning rate is used for fine-tuning than for training from scratch. This ensures that the model doesn't deviate too drastically from the pre-trained weights. Sometimes, different learning rates are used for the pre-trained layers and the task-specific head.
6. **Regularization**: Because the datasets we fine-tune on are often much smaller than the datasets used for pre-training, there's a risk of overfitting. Techniques like dropout, weight decay, or even reducing the model size (e.g., using DistilBERT instead of BERT) can help.
7. **Shorter Training Time**: Since the model starts from a point where it already understands the language to a certain extent, it converges faster. Thus, fine-tuning often requires fewer epochs compared to training a model from scratch.

In essence, when fine-tuning BERT:

- You leverage the extensive knowledge BERT has gained during its pre-training phase.
- You make the model adapt to the specifics of your task and dataset, without forgetting its prior knowledge.
- You add and train task-specific layers to make predictions suitable for your needs.

Fine-tuning allows you to get state-of-the-art performance with much less data and training time than training a deep model from scratch, especially for tasks where large labeled datasets are not available.

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
