import string
import numpy as np
import os
import os.path as op
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import time
import matplotlib.ticker as ticker

thispath = op.abspath(op.dirname(__file__))
os.chdir(thispath)

mpl.rcParams["grid.alpha"] = 0.5
mpl.rcParams["axes.grid"] = True
mpl.rcParams['xtick.direction'] = 'out'
mpl.rcParams['ytick.direction'] = 'out'


def remove_other(bk):
    rt = []
    d = string.digits
    for b in bk:
        if not any(bb in d for bb in b):
            rt.append(b)       
        
    return rt


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
    
    stor = remove_other(story)
    
    return stor

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


def common_words(ubook_dict, nm):
    rt = []
    for k, v in ubook_dict.items():
        rt.append((v,k))

    rt.sort(reverse=True)
    return rt[:nm]


class Bookstats(object):
    def __init__(self, bk, nm):
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
        self.most_commonword  = common_words(self.book_counts, nm)
        
    def histo_word(self, axi):
        
        axi.bar(xrange(1,len(self.size_counts)+1), [float(h)/float(self.full_count)*100.0 for h in self.size_counts.values()])
        axi.xaxis.set_ticks(range(1, len(self.size_counts)+1))
        
        axi.set_xlabel('Length of Words')
        axi.set_ylabel('Percent of total words')
    

if __name__ == "__main__":
    
    booksuffix = ".txt"
    pltsuffix = ".pdf" 
    bookone = "FallenMagus_2"
    bkFile = bookone + booksuffix
    nwords = 100
    t = time.time()
    f = open(bkFile, "r")
    m = f.read()
    tBook = Bookstats(m, nwords)

    attr = [a for a in dir(tBook) if not a.startswith('__') and not callable(getattr(tBook,a))]
    for att in attr:
        ats = getattr(tBook, att)
        if sys.getsizeof(ats)>100:
            continue
        else:
            print "-----------" + att + "-----------"
            print ats

    print "----------- Most Common Words ----------"    
    print "Rank --- Number of uses --- Word"
    for i, m2 in enumerate(tBook.most_commonword):
        print i+1, ": ", m2
    
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    tBook.histo_word(ax)
    pltname = "_wordHistogram"
    fig.suptitle(bookone + pltname, fontsize="large", fontweight='bold')
    plt.savefig(op.join(thispath, bookone+pltname+pltsuffix), bbox_inches='tight')
    plt.show()
    
    print "\nThat took {:.2f} s.".format(time.time()-t)

