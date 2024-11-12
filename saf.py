import os
from colorama import Fore, init

init(autoreset=True)

class scan_all_files:

    def __init__(self):
        self.root_directory = "C:\\"
        self.pc_name = "jthej"  # Change this to your PC name
        self.specific_directory = False  # Would you like to specify the directory to list?
        self.wanted_directory = f'C:\\Users\\{self.pc_name}\\Desktop\\test'  # If no specific directory, leave this blank
        self.save_output = False  # Would you like to save your output to files.txt?
        self.specifyfileExtension = False  # Would you like to specify file extension?
        self.FileExtension = '.txt'  # If specifyfileExtension is False, leave this blank

    def main_function(self):
        if self.save_output:
            of = open('files.txt', 'w')
        for root, dirs, files in os.walk(self.root_directory):
            for file in files:
                file_path = os.path.join(root, file)

                if self.specific_directory:
                    if file_path.startswith(self.wanted_directory):
                        if self.specifyfileExtension:
                            if file.endswith(self.FileExtension):
                                print(Fore.GREEN + f"[*]: {file_path}")
                                if self.save_output:
                                    of.write(f"{file_path}\n")
                        elif not self.specifyfileExtension:
                            print(Fore.GREEN + f"[*]: {file_path}")
                            if self.save_output:
                                of.write(f"{file_path}\n")
                
                elif not self.specific_directory:
                    if self.specifyfileExtension and file.endswith(self.FileExtension):
                        print(Fore.GREEN + f"[*]: {file_path}")
                        if self.save_output:
                            of.write(f"{file_path}\n")
                    elif not self.specifyfileExtension:
                        print(Fore.GREEN + f"[*]: {file_path}")
                        if self.save_output:
                            of.write(f"{file_path}\n")

        if self.save_output:
            of.close()


# if you want to use this module heres what you do 
# create a new file in the same directory named whatever with .py at the end
# put this code
# replace saf with the name of this file that your looking at right now (from filename import scan_all_files)
# from saf import scan_all_files

# saf = scan_all_files()
# saf.main_function()
