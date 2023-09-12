#chatGPT Alternative


import openai
import json
import csv
from .img2prompt import get_prompt

# Open and read the API key from the 'key.txt' file, then strip any newline characters
# Set the API key for OpenAI
openai.api_key = "" #set your api key here

def generate_prompts(prompt_estimate, prompt_expansion):
    # Assign the string containing the request for poem themes to the variable 'input_val'
    input_val = "generate " + str(prompt_expansion) + " prompts about " + prompt_estimate + "."
    # Initialize an empty string variable 'additional_info' to hold any additional information or context

    additional_info = "You are making unique prompts to generate an image from. The prompts contain captions, descriptions, and styles of the image to generate. Make each prompt unique and include an artistic style to stylize the generated image. You are provided with a general context of what the image should be and how many prompts to generate. Double check to make sure you provide the EXACT amount on prompts requested. Here is the request: "

    message = str(additional_info) + str(input_val)
    #chatGPT function call

    # Initialize 'list_theme' variable to store the category of the list (i.e., 'prompts')
    list_theme = "prompts"

    # Make a function call to the OpenAI API's ChatCompletion endpoint
    completion = openai.ChatCompletion.create(

    # Specify the model to use, in this case, "gpt-3.5-turbo-0613"
    model="gpt-3.5-turbo-0613",
        
    # Pass in the list of messages to simulate a conversation
    # 'input_val' is the user's question or command 
    messages=[{"role": "user", "content": message}],

    # Define the function that the OpenAI API will execute
    functions=[
        {
            # Name of the function, "get_list_of_poem_themes"
            "name": "list_of_prompts",
            # Description of what the function does
            "description": "a function that returns an array of multiple prompts themes",
            # Parameters that the function will use
            "parameters": {
                "type" : "object",
                "properties": {
                    # Define 'prompt_array' which will be an array of strings (prompts)
                    "prompt_array": {
                        "type" : "array",
                        "items": {
                            "type": "string",
                            "description": "A singular prompt"
                            },
                        "description": "a list of the requested prompts"
                        },
                    },
                },
                
            }
    ],
    # Call the function 'get_list_of_poem_themes' to execute
    function_call={"name": "list_of_prompts"},
    )

    # Access the ChatCompletion response from GPT
    # 'completion.choices[0].message' fetches the first (and usually only) generated message from GPT
    reply_content = completion.choices[0].message

    # Extract the 'function_call' arguments from the message
    # '.to_dict()' converts the object to a dictionary so that we can easily access its elements
    # We then access the 'arguments' key under the 'function_call' to get the arguments passed to the function
    response_options = reply_content.to_dict()['function_call']['arguments']


    # Convert the 'response_options' string to a JSON object using 'json.loads'
    # This assumes that 'response_options' is a JSON-formatted string
    options = json.loads(response_options)
    #print(options)
    return (options['prompt_array'])


def get_prompts(img, prompt_expansion):
        prompt_estimate = get_prompt(img)
        new_prompts = generate_prompts(prompt_estimate, prompt_expansion)
        
        #returns an array of new prompts prompts
        return generate_prompts(prompt_estimate, prompt_expansion)