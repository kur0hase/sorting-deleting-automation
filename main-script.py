from pathlib import Path
import shutil
import os

class main():
    def __init__(self):
        self.targetpath = ''
        self.useroption = ''
        self.foundextension = set()
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
        for s in self.targetpath.iterdir():
            self.foundextension.add(s.suffix)

    def sorting(self):
        if self.confirmation == True:
            for items in self.foundextension:
                os.mkdir(f'{items}')
            files_name = list(self.targetpath.iterdir())
            for items in files_name.suffix:
                if items.exists:
                    shutil.move(items, items)

    def deletion(self):
        pass