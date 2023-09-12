# Import necessary libraries and modules
import torch
import requests
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize BLIP Processor and Model for image captioning
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


# Function to get a prompt based on the given image
def get_prompt(img):
    # Convert image to model input format
    inputs = processor(img, return_tensors="pt")
    
    # Generate captions using the model
    out = model.generate(**inputs)
    
    # Decode the output tensor to get the prompt and return
    return processor.decode(out[0], skip_special_tokens=True)
