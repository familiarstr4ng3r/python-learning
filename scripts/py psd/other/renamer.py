import os

folder_path = r'C:\Users\User\Desktop\spaceman'

subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
subfolders = [folder for folder in subfolders if not '#' in folder]

#print(subfolders)
#print(len(subfolders))

#folder = subfolders[0]
#print(folder)

def get_files():

    for folder in subfolders:
        #print(folder)
        #folder_name = folder.split('\\')[-1]
        #print(folder_name)

        for _, _, file_names in os.walk(folder):
            #print(file_names)

            for file in file_names:
                if 'glove' in file:
                    continue

                rename_file(folder, file)

            print('#')


def rename_test():
    demo_file = r'C:\Users\User\Desktop\py psd\demo.txt'
    new_name = r'C:\Users\User\Desktop\py psd\demo.log'
    os.rename(demo_file, new_name)

#C:\Users\User\Desktop\spaceman\dark_blue\belt_08.png
def rename_file(folder, file):

    file_path = os.path.join(folder, file)
    #print(file_path)

    original_name = file.split('.')[0]
    extension = file.split('.')[-1]

    new_name = original_name.split('_')
    new_name = new_name[:-1]
    separator = '_'
    #new_name = '_'.join(str(i) for i in new_name)
    new_name = separator.join(new_name)
    new_name = f'{new_name}.{extension}'
    #print(new_name)

    new_path = os.path.join(folder, new_name)
    #print(new_path)
    os.rename(file_path, new_path)


#get_files()
#rename_test()










