from pathlib import Path
import os

directory = ''

    # ------------------ Options Logic ---------------------

def setcwd(path):
    global directory
    directory = path
    userpath = Path(directory)
    if userpath.exists() and not userpath.is_file():
        os.chdir(path)
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
    userpath = Path(directory)
    types = set()
    for i in userpath.iterdir():
        types.add(i.suffix)
    return types
            
def sortfiles():
    userpath = Path(directory)
    for file_path in userpath.iterdir():
        if file_path.is_file():
            folder_name = file_path.suffix.lstrip('.').lower() or "no_extension"
            new_folder = userpath / folder_name
            new_folder.mkdir(parents=True, exist_ok=True)
            new_file_path = new_folder / file_path.name
            file_path.rename(new_file_path)
    print('\nFiles sorted successfully!')

def renamefiles(extension, name):
    userpath = Path(directory)
    for count, file in enumerate(userpath.iterdir()):
        if extension in file.suffix:
            src = f"{file}"
            dst = f"{name}{str(count)}{file.suffix}"
            os.rename(src, dst)
    print('\nFile(s) renamed successfully!')

def deletefiles(extension):
    userpath = Path(directory)
    filelist = userpath.iterdir()
    for file in filelist:
        if file.is_file() and extension in file.suffix:
            os.remove(file)
            print(f'Deleting: {file}')
    print('\nFiles deleted successfully!')

def aborting_process():
    print('\nProcess aborted.')


# -------------- Interface ----------------

print('---------------- File Type-based Auto Sort and Deletion Tool ----------------' \
'\nGitHub: kur0hase')
print('\nWhat do you want to do?' \
'\n\nNote: Please set current working directory first before choosing other modification options.' \
'\n\n1. See Current Working Directory    2. Set Current Working Directory    3. Auto Sort Files    4. Rename Files    5. Delete Files')

while True:
    userinput = input('\nSelect option (number): ')

    validoptions = ['1', '2', '3', '4', '5']

    # validating answer
    if userinput in validoptions and len(userinput) == 1:
        if userinput == '1':
            print(see_cwd())
        elif userinput == '2':
            inputdir = input('\nEnter directory (e.g: ~/Documents/Files): ')
            setcwd(inputdir)
        elif userinput == '3':
            if confirmation():
                sortfiles()
            else:
                aborting_process()
        elif userinput == '4':
            if confirmation():
                print('\nAvailable file types in the directory:')
                print(available_suffix())
                extension = input('\nPick an extension of files to rename (e.g: .jpg): ')
                name = input('\nInsert new name: ')
                if extension in available_suffix():
                    renamefiles(extension, name)
                    break
                else:
                    print('\nPlease input a valid extension suffix available.')
            else:
                aborting_process()
        elif userinput == '5':
            if confirmation():
                print('\nAvailable file types in the directory:')
                print(available_suffix())
                extension = input('\nPick an extension of files to delete: ')
                deletefiles(extension)
                break
            else:
                aborting_process()
    else:
        print('\nPlease input a valid option.')


# /home/0x96hase/Downloads/try1/docx
