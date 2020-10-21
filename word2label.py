import jieba


class Novel():
    def __init__(self,book,dict,book_labeled):
        self.book = book
        self.dict = dict
        self.book_labeled = book_labeled

    def label(self):
        jieba.load_userdict(self.dict)
        path_read = self.book
        path_write = self.book_labeled
        with open(path_read, 'r') as file_raw:
            lines = file_raw.readlines()

        for line in lines:
            line = line.strip('\n')
            chars = jieba.cut(line)
            for char in chars:
                if len(char) == 1:
                    with open(path_write, 'a') as file_write:
                        file_write.write("{}\n".format(char+' S'))

                else:
                    temp = [' B']
                    for i in range(len(char) - 2):
                        temp.append(' M')
                    temp.append(' E')
                    with open(path_write, 'a') as file_write:
                        for i in range(len(char)):
                            file_write.write("{}\n".format(char[i]+temp[i]))


my_hot_landlord = Novel('my_hot_landlord.txt','dict_test.txt','res.txt')
my_hot_landlord.label()








