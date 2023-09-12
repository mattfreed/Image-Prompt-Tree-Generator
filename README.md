# Image Prompt Tree Generator

<div align="center">
  <img src="/Diagrams/ezgif.com-gif-maker.gif" width="600"/>
</div>

This repository contains Python code to generate a tree of image prompts and the corresponding images. The program takes an initial prompt (or multiple prompts from a text file) and generates an image from each prompt. These images are then used to create new prompts, which are again used to generate new images, forming a tree structure.

<div align="center">
  <img src="/Diagrams/AIProcessVisual.jpg" width="600"/>
</div>

## Table of Contents

1. [Installation](#installation)
2. [How to Run](#how-to-run)
3. [File Descriptions](#file-descriptions)
4. [Contributing](#contributing)
5. [License](#license)

---

## Installation

To install the necessary packages, run the following command:

```bash
pip install -r requirements.txt
```

---

## How to Run

Run the `main.py` script to start the program.

```bash
python main.py [levels] [prompt_expansion] [input_file] [output_dir]
```

- `levels`: How many levels of hierarchical prompts to generate
- `prompt_expansion`: How many new prompts to be generated per node
- `input_file`: Path to the text file containing prompts, one per line
- `output_dir`: Path to the directory where the generated images will be saved

---

## File Descriptions

- `main.py`: The entry point of the application. Handles argument parsing and initiates the prompt tree generation.
- `src/`
  - `img2prompt.py`: Contains code for generating a textual prompt from an image using Salesforce's BLIP model.
  - `prompt2img.py`: Contains code to generate an image from a textual prompt.
  - `promptmixerOpenAI.py`: Utilizes OpenAI's GPT-3 model to generate new prompts based on existing ones.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License.

---
