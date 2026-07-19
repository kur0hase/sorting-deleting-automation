from pathlib import Path
import os

directory = ''
confirmation = False

def setcwd(path):
    if path.exists() and not path.is_file():
        os.chdir(path)
        directory = path
        print(f'\nTarget directory changed to {directory}.')
    else:
        print('\nFailed to change directory: Directory not found.')

def see_cwd():
    cwd = os.getcwd()
    print(f'\nCurrent working path: {cwd}')

def available_suffix():
    types = set()
    for i in directory.iterdir():
        types.add(i.suffix)
    print(types)
        
def sortfiles():
    for file_path in directory.iterdir():
        if file_path.is_file():
            folder_name = file_path.suffix.lstrip('.').lower() or "no_extension"
            new_folder = directory / folder_name
            new_folder.mkdir(parents=True, exist_ok=True)
            new_file_path = new_folder / file_path.name
            file_path.rename(new_file_path)
    print('\nFiles sorted successfully!')

def renamefiles(extension, name):
    for count, file in enumerate(directory.iterdir()):
        if extension in file.suffix:
            src = f"{file}"
            dst = f"{name}{str(count)}.{file.suffix}"
            os.rename(src, dst)
    print('\nFile(s) renamed successfully!')

def deletefiles(extension):
    filelist = directory.iterdir()
    for file in filelist:
        if file.is_file():
            if extension in file:
                os.remove(file)
                print(f'Deleting: {file}')
    print('\nFIles deleted successfully!')


# -------------- Interface ----------------
print('---------------- File Type-based Auto Sort and Deletion Tool ----------------' \
'\nGitHub: kur0hase')
print('\nWhat do you want to do?\na. Change Working Directory    b. See Current Working Directory    c. Auto Sort Files    d. Rename Files    e. Delete Files')
userinput = input('\nSelect option: ')

useroption = userinput.lower()
validoptions = "a b c d e"

# validating answer
if useroption in validoptions:
    if useroption == 'a':
        pass