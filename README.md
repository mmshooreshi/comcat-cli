# Concatenate Files CLI

A CLI tool to concatenate text files from a folder into a single markdown file with stylish dividers.

## Installation

```sh
pip install git+https://github.com/mmshooreshi/comcat-cli.git
```

## Usage

### Concatenate Files

```sh
comcat path/to/input_folder path/to/output_file.md path/to/structure_file.md
```

### Send Text to GPT-4

```sh
cat *.txt | 2gpt --api_base "https://api.openai.com/v1" --api_key "your_api_key"
```

Replace `"your_api_key"` with your actual API key for the GPT-4 API.
```

### Directory Structure

Ensure your project directory looks like this:

```plaintext
comcat-cli/
├── comcat/
│   ├── __init__.py
│   ├── cli.py
│   └── gpt_request.py
├── setup.py
├── README.md
└── LICENSE
```
