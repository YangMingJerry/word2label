

import word2label

def load_book_name(path):
    with open(path) as novel_tags:
        books = novel_tags.readlines()
        return books

def load_dict(path,book):
    pass

if __name__=='__main__':
    path_raw = '/data/corpus/ner_exp/cloudSourcing/raw'
    path_ner = '/data/corpus/ner_exp/cloudSourcing/ner'
    books = load_book_name(path_raw + '/novel_tag.txt')
    for book_name in books:
        book_labeled = 'BEMS_'+book_name
        book_dct = load_dict(path_ner,book_name)
        novel = word2label.Novel(book_name,book_dct,book_labeled)
        novel.label()

