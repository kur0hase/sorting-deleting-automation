from pathlib import Path
import os

directory = ''

# ------------------ Options Logic ---------------------

def setcwd(path):
    if path.exists() and not path.is_file():
        os.chdir(path)
        directory = path
        print(f'\nTarget directory changed to {directory}.')
    else:
        print('\nFailed to change directory: Directory not found.')

def see_cwd():
    cwd = os.getcwd()
    return f'\nCurrent working path: {cwd}'

def confirmation():
    this = input('\nConfirm your action [Y/n]: ')
    thislow = this.casefold()
    if thislow == 'y':
        return True
    elif thislow == 'n':
        return False

def available_suffix():
    types = set()
    for i in directory.iterdir():
        types.add(i.suffix)
    return types
        
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
print('\nWhat do you want to do?' \
'\nNote: Please check current working directory first before choosing modification options.' \
'\n1. See Current Working Directory    2. Change Working Directory    3. Auto Sort Files    4. Rename Files    5. Delete Files')

userinput = input('\nSelect option (number): ')

validoptions = ['1', '2', '3', '4']

# validating answer
if userinput in validoptions and len(userinput) == 1:
    if userinput == '1':
        print(see_cwd())
    elif userinput == '2':
        inputdir = input('\nEnter directory (e.g: ~/Documents/Files): ')
        setcwd(inputdir)
    elif userinput == '3':
        confirmation()
        if confirmation():
            sortfiles()
        else:
            print('\nProcess aborted.')
    elif userinput == '4':
        confirmation()
        if confirmation():
            print('\nAvailable file types in the directory:')
            print(available_suffix())
            extension = input('\nPick an extension of files to rename: ')
            name = input('\nInsert new name: ')
            renamefiles(extension, name)
        else:
            pass