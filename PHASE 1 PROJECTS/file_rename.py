import os

def dir_path():
    while True:
            path = input(r"Folder / Directory address:  ").strip("")

            if os.path.exists(path):
                return path
            else:
                print("No such path exists.")

def show_dir_contents_rename_if_possible(path):
    contents = os.listdir(path)

    if not contents:
        print(f"No content in {path}")
        return False

    for idx, file in enumerate(contents, start=1):
         print(f"{idx}. '{file}'")

    while True:
         file = input(f"Enter the file name in {path} to rename or (0 to quit):  ")

         if file == "0":
              return False
         
         if file in contents:
              fullPath = os.path.join(path, file)

              if os.path.isfile(fullPath):
                print("File Found.")

                new_name = input("Enter a new name for your file: ")

                newFullPath = os.path.join(path, new_name)


                os.rename(fullPath, newFullPath)
                print(f"Old name {file} renamed to {new_name}")
              else:
                print("That's not a regular file (maybe a folder).")

         else:
            print("Check if you entered correctly or the file doesn’t exist.")
        
     
    

def main():
    path = dir_path()
    if not show_dir_contents_rename_if_possible(path):
        print("First add content to rename. Bye for now!")
        quit()



main()
