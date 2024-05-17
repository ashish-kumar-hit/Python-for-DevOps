# List down all the files names in the given folder path
import os

def list_files(folder_path):
        try:
            files = os.listdir(folder_path)
            return files, None
        except FileNotFoundError:
            return None, "Folder Not Found"
        except PermissionError:
            return None, "Permission Denied"

def main():
     folder_paths = input("Please provide one by one folder path using spaces: ").split()
     for folder_path in folder_paths:
          files, error_message = list_files(folder_path)
          if files:
               print(f'Files in {folder_path}')
               for file in files:
                    print(file)
          else:
               print(f'Error in {folder_path}: {error_message}')

if __name__ == "__main__":
     main()

    