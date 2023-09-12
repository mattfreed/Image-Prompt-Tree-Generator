# Import required libraries and modules
import torch
from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

# Function to generate an image based on a given text prompt
def generate_image(prompt):
    # Initialize model ID and load pre-trained pipeline
    model_id = "stabilityai/stable-diffusion-2-1"

    # Initialize Euler scheduler for diffusion process
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    
    # Initialize the diffusion pipeline with the scheduler
    pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler)

    # Generate the image using the pipeline
    image = pipe(prompt, num_inference_steps=30, guidance_scale=7.5).images[0]
    
    return image

