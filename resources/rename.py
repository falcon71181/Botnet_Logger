import os

def rename_folders(base_folder):
    folder_list = [name for name in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, name))]
    index = 1

    for folder_name in folder_list:
        old_folder = os.path.join(base_folder, folder_name)
        new_name = str(index)
        new_path = os.path.join(base_folder, new_name)

        try:
            os.rename(old_folder, new_path)
            print(f"[+] Renaming '{folder_name}' to '{new_name}'")
        except OSError as e:
            if e.errno == 39:  # Directory not empty
                index += 1
                continue
            else:
                print(f"Error renaming '{folder_name}': {str(e)}")
        
        index += 1
