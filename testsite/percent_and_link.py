import os
files_new = []
cur_path = os.getcwd()
path = cur_path + '/src2'
print(path)
for i in os.listdir(path):
    if i.endswith('.txt'):
        file = open(path + '/' + i, 'r', encoding='utf-8')
        for line in file:
            lines_new = line.split()
            for line_new in lines_new:
                if line_new.startswith('%'):
                    print('filename: '+i + ' link: '+ line_new)

