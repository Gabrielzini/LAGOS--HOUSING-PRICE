import gradio as gr
import pandas as pd
import numpy as np
import json

# Load the model
import pickle
with open('huggingface_deployment/best_model.pkl', 'rb') as f:
    best_model = pickle.load(f)

#load the feature names
with open('huggingface_deployment/feature_names.json', 'r') as f:
    feature_names = json.load(f)

# Define the prediction function


def predict_price(input_data):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    
    # Make prediction
    prediction = best_model.predict(input_df)
    
    # Convert prediction to Nigerian Naira format
    prediction_naira = f"₦{prediction[0]:,.2f}"
    
    return prediction_naira
def main():
    interface = gr.Interface(
        fn=predict_price,
        inputs=[
            gr.inputs.Number(label="Input 1"),
            gr.inputs.Number(label="Input 2"),
            gr.inputs.Number(label="Input 3"),
        ],
        outputs="text"
    )
    interface.launch()
