import os
import argparse

def read_files_recursively(folder_path):
    file_contents = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                relative_path = os.path.relpath(file_path, folder_path)
                file_contents.append((relative_path, content))
    return file_contents

def generate_divider(title):
    block_line = '█' * 80
    double_line = '═' * 80
    single_line = '─' * 80
    star_line = '★' * 80
    arrow_line = '➤' * 80
    title_line = f'█ {title} ' + '█' * (78 - len(title))
    return f"\n\n{block_line}\n{title_line}\n{block_line}\n{double_line}\n{single_line}\n{star_line}\n{arrow_line}\n"

def concatenate_contents(file_contents):
    concatenated_text = ""
    for file_path, content in file_contents:
        divider = generate_divider(file_path)
        concatenated_text += f"{divider}\n\n\n"
    return concatenated_text

def write_output_file(output_path, concatenated_text):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(concatenated_text)

def main():
    parser = argparse.ArgumentParser(description="Concatenate text files from a folder into a single markdown file with stylish dividers.")
    parser.add_argument("input_folder", help="The folder containing the files to be read.")
    parser.add_argument("output_file", help="The output file where the concatenated content will be written.")
    
    args = parser.parse_args()
    
    file_contents = read_files_recursively(args.input_folder)
    concatenated_text = concatenate_contents(file_contents)
    write_output_file(args.output_file, concatenated_text)
    print(f"Concatenated file created at {args.output_file}")

if __name__ == "__main__":
    main()
