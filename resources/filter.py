import os

def remove_empty_lines_inplace(file_path):
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate(0)
        for line in lines:
            if line.strip():
                file.write(line)

def remove_duplicates_from_file(file_path):
    lines_seen = set()
    updated_lines = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            stripped_line = line.strip()
            if stripped_line not in lines_seen:
                lines_seen.add(stripped_line)
                updated_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)

def filter_files(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder_path, file_name)
            remove_duplicates_from_file(file_path)
            remove_empty_lines_inplace(file_path)
            print(f'{file_name} [+] Filtered')