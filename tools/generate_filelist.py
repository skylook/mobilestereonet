import os
PATH = '/home/skylook/Develop/Data/MonoRectified'
LEFT_PATH = f'{PATH}/Left'
left_files = [f'{LEFT_PATH}/{x}' for x in os.listdir(LEFT_PATH)]
# print(left_files)

dst_file_path = f'{PATH}/stereo_files.txt'

with open(dst_file_path, 'w') as the_file:

    list = []

    for left_path in left_files:
        # left_path = file_path
        right_path = left_path.replace('Left', 'Right')
        disp_path = left_path.replace('Left', 'Disp')

        # the_file.write(f'{left_path} {right_path} {disp_path}\n')
        list.append(f'{left_path} {right_path}\n')

    the_file.writelines(list)

print(dst_file_path)

