import os

def renameFiles():
    os.chdir("C:\Users\Prateek\Desktop\PythonPrograms\Test")
    file_list = os.listdir("C:\Users\Prateek\Desktop\PythonPrograms\Test");
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"1234567890"))

renameFiles()
