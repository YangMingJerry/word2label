
#from loguru import logger
import word2label
import glob
def load_book_name(path):
    with open(path) as novel_tags:
        books = novel_tags.readlines()
        return books

def load_dict(path,book):
    dict_name = glob.glob(path+book+'*')[0]
    try:
        with open(dict_name) as dct:
            print(book+' NER dictionary found')
    except Exception as e:
        #logger.error(e)
        print('===WARNING:'+book+' NER dictionary found')


if __name__=='__main__':
    path_raw = '/data/corpus/ner_exp/cloudSourcing/raw/'
    path_ner = '/data/corpus/ner_exp/cloudSourcing/ner/'
    books = load_book_name(path_raw + '/novel_tag.txt')
    books = books[:5]
    for book_name in books:
        book_name.strip('\n')
        book_dct = load_dict(path_ner,book_name)
        book_name = book_name + '.txt'
        book_labeled = 'BEMS_'+book_name

        novel = word2label.Novel(book_name,book_dct,book_labeled)
        novel.label()

