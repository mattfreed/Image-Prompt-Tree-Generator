# Import required modules
import argparse
import os
import csv
from tqdm import tqdm
from src import prompt2img, promptmixerOpenAI

# Append the array values to a CSV file located at file_path
def append_to_csv(file_path, array):
    # Concatenate file_path and "prompts.csv" to form the full path to the CSV file
    csv_file = file_path + "//prompts.csv"
    
    # If file doesn't exist, create it and write headers
    if not os.path.exists(csv_file):
        with open(csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            header = [f'Value_{i}' for i in range(1, len(array) + 1)]
            writer.writerow(header)

    # Append the array as a new row in the CSV
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(array)

# Generate the next level of image prompts based on the previous level
def generate_level(img_array, prompt_array, prompt_expansion, level, output_dir):
    new_prompt_array = []
    new_img_array = []
    
    # Loop through each prompt in prompt_array to generate image and new prompts
    for img_num, single_prompt_array in enumerate(prompt_array):
        for prompt_num, prompt in enumerate(single_prompt_array):
            img = prompt2img.generate_image(prompt)
            new_img_array.append(img)
            
            # Create file path for saving image
            output_path_img = str(output_dir)+"/images/"+str(level)+"_"+str(img_num)+"_"+str(prompt_num)+".jpg"
            img.save(output_path_img)
            
            # Append prompt to CSV
            prompt_id = str(level)+"_"+str(img_num)+"_"+str(prompt_num)
            append_to_csv(output_dir, [prompt_id, prompt])

            # Generate new prompts based on the generated image
            new_prompt_array.append(promptmixerOpenAI.get_prompts(img, prompt_expansion))
    return new_img_array, new_prompt_array

# Function to generate the hierarchy tree of images and prompts
def generate_tree(initial_prompt, levels, prompt_expansion, output_dir):
    prompt_array = initial_prompt
    img_array = []
    
    # Generate images and prompts for each level
    for level in range(levels):
        img_array, prompt_array = generate_level(img_array, prompt_array, prompt_expansion, level, output_dir)

# Main function
if __name__ == "__main__":
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Generate images based on an initial prompt")
    parser.add_argument("levels", help="How many levels of hierarical prompts to generate", type=int)
    parser.add_argument("prompt_expansion", help="How many new prompts to be generated per node", type=int)
    parser.add_argument("input_file", help="Path to the text file containing prompts, one per line.")
    parser.add_argument("output_dir", help="Path to the directory where the generated images will be saved.")
    args = parser.parse_args()

    # Read initial prompts from the input file
    with open(args.input_file, "r") as file:
        lines = file.readlines()
        
        # Loop through each initial prompt to generate the tree
        for initial_prompt in tqdm(lines, desc="Generating images"):
            initial_prompt_array = [[initial_prompt.strip()]]
            generate_tree(initial_prompt_array, args.levels, args.prompt_expansion, args.output_dir)
