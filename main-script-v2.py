from pathlib import Path
import shutil
import os

class main():
    def __init__(self):
        self.targetpath = ''
        self.useroption = ''
        self.foundextension = set()
        self.files = []
        self.confirmation = False

    def interface(self):
        while True:
            q1 = input("\nEnter directory path (e.g. ~/Documents/Folder/):\n")
            self.targetpath = Path(q1)
            if self.targetpath.exists():
                break
            else:
                print('\nDirectory not found!')

        while True:
            q2 = input("\nSelect an action:\na. Sorting        b. Deletion\n\nSelect: ")
            self.useroption = q2.lower()
            if self.useroption == 'a' or self.useroption == 'b':
                break
            else:
                print('\nPlease select an action')

        while True:
            q3 = input("\nConfirm action? [Y/n]: ")
            confirmation = q3.casefold()
            if confirmation == 'y':
                self.confirmation = True
                break
            elif confirmation == 'n':
                print('\nOperation cancelled')
                break
            else:
                print("\nPlease confirm the action")

    def change(self):
        os.chdir(self.targetpath)
        return f'\nMaking {self.targetpath} as target'

    def identify_extension(self):
        for items in self.targetpath.iterdir():
            self.foundextension.add(items.suffix)

    def sorting(self):
        for file_path in self.targetpath.iterdir():
            if file_path.is_file():
                folder_name = file_path.suffix.lstrip('.').lower() or "no_extension"
                new_folder = self.targetpath / folder_name
                new_folder.mkdir(parents=True, exist_ok=True)
                new_file_path = new_folder / file_path.name
                file_path.rename(new_file_path)
        

    def deletion(self):
        pass