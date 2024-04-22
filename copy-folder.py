import os
import shutil
import random
import string

def random_folder_name(length=12):
    # Generate a random string of uppercase letters and digits
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def create_folders_with_files(num_folders, source_folder, target_parent_folder):
    original_files = ['_index.md'] 

    for _ in range(num_folders):
        new_folder_name = random_folder_name()
        new_folder_path = os.path.join(target_parent_folder, new_folder_name)

        print(f"{new_folder_name}")

        # Create a new folder with the random name
        os.makedirs(new_folder_path, exist_ok=True)

        # Copy and modify files as necessary
        for file_name in original_files:
            source_file_path = os.path.join(source_folder, file_name)
            target_file_path = os.path.join(new_folder_path, file_name)

            if file_name == '_index.md':
                # Modify the index.mdx file
                with open(source_file_path, 'r') as file:
                    content = file.read()

                # Update the sidebar position and label
                modified_content = content.replace('title: policy', f'title: {new_folder_name}')

                # Write the modified content to the new file
                with open(target_file_path, 'w') as file:
                    file.write(modified_content)
            else:
                shutil.copy(source_file_path, target_file_path)

# Example usage


def main():
    source_folder = '/home/akshat/handbook-template/content/policy'  # Update this path
    target_parent_folder = '/home/akshat/handbook-template/content'  # Update this path
    create_folders_with_files(2, source_folder, target_parent_folder) 
    print("done")


if __name__ == "__main__":
    main()