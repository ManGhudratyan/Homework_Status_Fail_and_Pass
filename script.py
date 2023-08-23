import os

file_name = 'result.txt'
directory_path = '/home/mane/Desktop/Homework_Status_Fail_and_Pass/Test';

with open(file_name, 'w') as file:
    for i in os.listdir(directory_path):
        if i.endswith('.txt'):
            with open(os.path.join(directory_path, i), 'r') as txt_file:
                status = txt_file.read().strip();
                file.write(f"{i[:-4]} -> {status[8:]}\n")
print(f"File '{file_name}' created successfully")



