import jieba
import jieba.posseg as pseg
import jieba.analyse

jieba.set_dictionary('./extra_dict/dic.txt.px.txt')
jieba.load_userdict("./extra_dict/dic.txt.px.txt")
#jieba.set_dictionary('d:/Users/jacob_chuang/jiebaQA/env01/extra_dict/dic.txt.px.txt')
#jieba.load_userdict("d:/Users/jacob_chuang/jiebaQA/env01/extra_dict/dic.txt.px.txt")


def HMM(input):
    words = jieba.cut(input, HMM=True) #HMM 設為 True
    words_list = []
    for word in words:
        words_list.append(word)
    return words_list

def posseg(input):
    words = jieba.posseg.cut(input)
    print(words)
    words_list = []
    words_FREQ_list = []
    for word, flag in words:
        if flag == 'px' :
            words_list.append(word)
            words_FREQ_list.append(jieba.get_FREQ(word))
    print (words_list)  
    print (words_FREQ_list)        
    return words_list,words_FREQ_list
