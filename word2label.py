import jieba


path_read = 'my_hot_landlord.txt'
path_write = 'res.txt'
with open(path_read,'r') as file_raw:
    lines = file_raw.readlines()

for line in lines:
    line = line.strip('\n')
    chars = jieba.cut(line)
    for char in chars:
        if len(char) == 1:
            with open(path_write, 'a') as file_write:
                file_write.write("{}\n".format(char.join(' S')))

        else:
            temp = [' B']
            for i in range(len(char)-2):
                temp.append(' M')
            temp.append(' E')
            print(char)
            print(temp)
            with open(path_write,'a') as file_write:
                for i in range(len(char)):
                    file_write.write("{}\n".format(char[i].join(temp[i])))





