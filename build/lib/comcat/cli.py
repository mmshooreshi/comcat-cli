import os
import re
import fnmatch
import argparse
from collections import defaultdict
from datetime import datetime

def load_catignore(ignore_file_path):
    ignore_patterns = []
    if os.path.exists(ignore_file_path):
        with open(ignore_file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    return ignore_patterns

def should_ignore(path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
        try:
            if re.search(pattern, path):
                return True
        except re.error:
            pass
    return False

def get_file_stats(file_path):
    stats = os.stat(file_path)
    latest_edited = stats.st_mtime
    # For demonstration purposes, the number of times edited and frequency of edits are set to dummy values.
    # In a real scenario, you would need a way to track these, possibly with a version control system.
    num_edits = 5  # Dummy value
    freq_edits = 2  # Dummy value
    return latest_edited, num_edits, freq_edits

def prioritize_files(files):
    prioritized_files = sorted(files, key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))
    return prioritized_files

def read_files_recursively(folder_path, ignore_patterns):
    file_contents = []
    for root, dirs, files in os.walk(folder_path):
        dirs[:] = [d for d in dirs if not should_ignore(os.path.relpath(os.path.join(root, d), folder_path), ignore_patterns)]
        for file in files:
            file_path = os.path.join(root, file)
            if should_ignore(os.path.relpath(file_path, folder_path), ignore_patterns):
                continue
            stats = get_file_stats(file_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='latin-1') as f:
                    content = f.read()
            relative_path = os.path.relpath(file_path, folder_path)
            file_contents.append((relative_path, stats, content))
    return file_contents

def generate_divider(title):
    block_line = '█' * 80
    double_line = '═' * 80
    single_line = '─' * 80
    star_line = '★' * 80
    arrow_line = '➤' * 80
    title_line = f'█ {title} ' + '█' * (77 - len(title))
    return f"\n\n{block_line}\n{title_line}\n{block_line}\n{double_line}\n{single_line}\n{star_line}\n{arrow_line}\n"

def protect_sensitive_data(content):
    content = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '*****@*****.com', content)
    content = re.sub(r'(?i)password\s*:\s*\S+', 'password: *****', content)
    content = re.sub(r'(?i)secret\s*:\s*\S+', 'secret: *****', content)
    content = re.sub(r'(?i)name\s*:\s*\S+', 'name: *****', content)
    return content

def concatenate_contents(file_contents):
    concatenated_text = ""
    structure_dict = {}
    
    for file_path, _, content in file_contents:
        divider = generate_divider(file_path)
        protected_content = protect_sensitive_data(content)
        concatenated_text += f"{divider}\n\n```\n{protected_content}\n```\n"
        add_to_structure(structure_dict, file_path.split(os.sep))
    
    structure_text = build_tree(structure_dict)
    return concatenated_text, structure_text

def add_to_structure(structure_dict, path_parts):
    if len(path_parts) == 0:
        return
    part = path_parts[0]
    if part not in structure_dict:
        structure_dict[part] = {}
    add_to_structure(structure_dict[part], path_parts[1:])

def build_tree(structure_dict, level=0):
    tree_text = ""
    for part, sub_parts in structure_dict.items():
        tree_text += "  " * level + f"- {part}\n"
        tree_text += build_tree(sub_parts, level + 1)
    return tree_text

def write_output_file(output_path, text):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    parser = argparse.ArgumentParser(description="Concatenate text files from a folder into a single markdown file with stylish dividers.")
    parser.add_argument("input_folder", help="The folder containing the files to be read.")
    parser.add_argument("output_file", help="The output file where the concatenated content will be written.")
    parser.add_argument("structure_file", help="The output file where the structure of the concatenated content will be written.")
    
    args = parser.parse_args()
    
    ignore_file_path = os.path.join(args.input_folder, '.catignore')
    ignore_patterns = load_catignore(ignore_file_path)
    
    file_contents = read_files_recursively(args.input_folder, ignore_patterns)
    prioritized_files = prioritize_files(file_contents)
    concatenated_text, structure_text = concatenate_contents(prioritized_files)
    write_output_file(args.output_file, concatenated_text)
    write_output_file(args.structure_file, structure_text)
    print(f"Concatenated file created at {args.output_file}")
    print(f"Structure file created at {args.structure_file}")

if __name__ == "__main__":
    main()
