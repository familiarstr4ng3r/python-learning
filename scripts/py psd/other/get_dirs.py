import os

folder_path = r'C:\Users\User\Desktop\spaceman'

subfolders = [f.path for f in os.scandir(folder_path) if f.is_dir()]
subfolders = [folder for folder in subfolders if not '#' in folder]

#print(subfolders)
#print(len(subfolders))

#folder = subfolders[0]
#print(folder)

target_image = 'jet_pack'

'''
image = 'belt_08.png'

if target_image in image:
    print('g')
else:
    print('b')
'''
#quit()

for folder in subfolders:
    #print(folder)
    folder_name = folder.split('\\')[-1]
    #print(folder_name)

    for _, _, file_names in os.walk(folder):
        #print(file_names)
        #print('#')

        '''
        for file_name in file_names:
            #print(file_name)
            #image_name = file_name.split('_')[0]
            #print(image_name)
            if not target_image in file_name:
                print(f'{folder} does not contains {target_image}')
                pass
        '''
        images = [img for img in file_names if target_image in img]
        if len(images) == 0:
            print(f'{folder} does not contains "{target_image}"')











