import string
import numpy as np
import os
import os.path as op
import sys
import matplotlib.pyplot as plt
import collections
import time

#Put some deco on this biatch

def remove_pun(book):
    pn1=string.punctuation
    #You don't want to replace the hypens.
    pn1=string.replace(pn1,'-',"")
    pn1=string.replace(pn1,"'","")
    
    St="".join(book)
    for item in pn1:
        St=string.replace(St,item," ")

    St=string.replace(St,"--"," ")
    story=St.split()
    
    return story
    
def histo_dict(book, uniqueBook):
    mybk = dict()
    for ubk in uniqueBook:
        mybk[ubk] = book.count(ubk)
    return mybk
    
def word_length(wcnt, ubook_dict):
    gr = 0
    for ky in ubook_dict.keys():
        gr += (len(ky)*ubook_dict[ky])
    
    return float(gr)/float(wcnt)
    
def count_wordlength(ubook_dict):
    mx = max([len(k) for k in ubook_dict.keys()])
    wL = {x+1 : 0 for x in xrange(mx)}
    for ub in ubook_dict.keys():
        wL[len(ub)] += ubook_dict[ub]
        
    return wL

class Bookstats(object):
    def __init__(self, bk):
        #self.split_up = bk.split()
        self.unpunctuated_book = remove_pun(bk)
        self.full_count = len(self.unpunctuated_book)
        self.unique_book = list(set(self.unpunctuated_book))
        self.unique_count = len(self.unique_book)
        self.book_counts = histo_dict(self.unpunctuated_book, self.unique_book)
        self.sentences = bk.count(".")
        self.commas = bk.count(",")
        self.avg_wordlength = word_length(self.full_count, self.book_counts)
        self.commas_per_sentence = float(self.sentences)/float(self.commas)
        self.words_per_sentence = float(self.full_count)/float(self.sentences)
        self.size_counts = count_wordlength(self.book_counts)
        
    def histo_word(self):
        plt.figure()
        plt.bar([.5+x for x in xrange(len(self.size_counts))], [float(h)/float(self.full_count)*100.0 for h in self.size_counts.values()])
        plt.xticks(range(1, len(self.size_counts)+1), self.size_counts.keys())
        plt.xlabel('Length of Words')
        plt.ylabel('Percent of total words')
        plt.grid(True)
        plt.show()
    

if __name__ == "__main__":
    bookone = "FallenMagus_2.txt"
    
    t = time.time()
    f = open(bookone, "r")
    m = f.read()
    thisBook = Bookstats(m)
    attr = [a for a in dir(thisBook) if not a.startswith('__') and not callable(getattr(thisBook,a))]
    for att in attr:
        ats = getattr(thisBook, att)
        if sys.getsizeof(ats)>100:
            continue
        else:
            print att, ats
    
    thisBook.histo_word()
    
    print "\nThat took {:.2f} s.".format(time.time()-t)

