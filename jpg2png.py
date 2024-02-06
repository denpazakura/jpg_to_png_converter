import sys
import os
from PIL import Image

def main():
    check_args()
    
    source_folder_path = sys.argv[1]
    destination_folder_path = sys.argv[2]
    
    check_source_path(source_folder_path)
    check_directory(source_folder_path)
    create_destination_if_needed(destination_folder_path)
    process_files(source_folder_path, destination_folder_path)

def check_args():
    if len(sys.argv) < 3:
        print("usage: python script_name.py <source_folder_path> <destination_folder_path>")
        sys.exit(1)

def check_source_path(source_folder_path):
    if not os.path.exists(source_folder_path):
        print("source folder path does not exist.")
        sys.exit(1)

def check_directory(source_path):
    if not os.path.isdir(source_path):
        print("source path is not a directory.")
        sys.exit(1)    

def create_destination_if_needed(destination_path):
    if not os.path.exists(destination_path):
       os.makedirs(destination_path)

def process_files(source, destination):
    for filename in os.listdir(source):
        file_path = os.path.join(source, filename)
        if os.path.isfile(file_path):
            image_extensions = ['.jpg', '.jpeg']
            for ext in image_extensions:
                if filename.lower().endswith(ext):
                    img = Image.open(file_path) 
                    destination_file_name = f'{os.path.splitext(filename)[0]}.png'
                    destination_file_path = os.path.join(destination, destination_file_name)
                    img.save(destination_file_path, 'png')

if __name__ == "__main__":
    main()