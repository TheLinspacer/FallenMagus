#!/usr/bin/env python

#Lab 7.  War and Peace bilingual and revisited.

import matplotlib.pyplot as plt
import string

def load_dictionary(filename):
    words = []
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines=line.strip().split()
            for x in xrange(len(lines)):
                words.append(lines[x])
    
    return words

def remove_pun(li):
    import string
    pn1=string.punctuation
    #You don't want to replace the hypens.
    pn1=string.replace(pn1,'-',"")
    pn1=string.replace(pn1,"'","")
    St="".join(li)
    for item in pn1:
        St=string.replace(St,item," ")

    St=string.replace(St,"--"," ")
    story=St.split()
    
    return story


#This is passed lists.  It implements all improvements and answers the extra credit questions.
def dict_compare(li_1,li_2):

    d=dict()
    #Ah you can't make War and peace a set because then it would need to be unique!
    s_dictionary=set(li_2)
    c=0
    unused=set()
    
    for item in li_1:
        if item.lower() not in d:
            d[item.lower()] = 1
        else:
            d[item.lower()] += 1

        if item.lower() not in s_dictionary:
            c += 1
            unused.add(item)

    return c, unused, d

def dict_each_letter(li):
    import string
    c=0
    WP="".join(li)
    for item in WP:
        c += 1
        if item == ".":
            l1 = remove_pun(li)
            WP="".join(l1)
            break
        if c>len(WP)/10000:
            break
        
    Alpha=set(string.ascii_letters.lower())
    d2=dict()
    WP=WP.lower()
    for item in (string.digits + string.punctuation):
        WP=string.replace(WP,item,"")
        
    for letter in Alpha:
        d2[letter] = 0

    for item in WP:
        if item in Alpha:
            d2[item] += 1

    return d2

def word_length(li):
    di2=dict()
    c=0
    WP="".join(li)
    for item in WP:
        c += 1
        if item == ".":
            book = remove_pun(li)
            break
        if c>len(WP)/10000:
            book = li[:]
            break

    for x in xrange(100):
        di2[x] = 0

    for item in book:
        di2[len(item)] += 1

    for x in xrange(100):
        if di2[x] == 0:
            di2.pop(x)
    
    return di2

def histo_word(dt):

    plt.figure()
    plt.bar(range(len(dt)),dt.values())
    plt.xticks(range(len(dt)),dt.keys())
    plt.xlabel('Length of Words')
    plt.ylabel('Frequency')
    plt.draw()


def histo_letter(dt):
    Alpha=string.ascii_letters.lower()
    Alpha=Alpha[:26]
    print Alpha
    val =[]
    for item in Alpha:
        val.append(dt[item])
    
    
    plt.figure()
    plt.bar(range(26),val)
    plt.xticks(range(26),Alpha[:26])
    plt.xlabel('Letters of the alphabet')
    plt.ylabel('Frequency')
    plt.draw()

def compare_dict(lst1,lst2):

    dct1=dict()
    dct2=dict()
    s1=set(lst1)
    s2=set(lst2)
    s3=s1 & s2
    print("There are {0} words in common between the French and English Version.".format(len(s3)))
    print s3
    for item in s1:
        dct1[item] = 0

    for word in lst1:
        dct1[word] +=1

    for item in s2:
        dct2[item] = 0

    for word in lst2:
        dct2[word] +=1

    return dct1, dct2
                


if __name__ == "__main__":
    
    WarAndPeace = load_dictionary('WarandPeace.txt')
    print('There are {0} words in War and Peace by Leo Tolstoy.'.format(len(WarAndPeace)))
    TheBrothersKaramazov = load_dictionary('TheBrothersKaramazov.txt')
    print('There are {0} words in The Brothers Karamazov by Fyodor Dostoyevsky.'.format(len(TheBrothersKaramazov)))
    Ulysses = load_dictionary('Ulysses.txt')
    print('There are {0} words in Ulysses by James Joyce.'.format(len(Ulysses)))
    WPFr=load_dictionary('WPFrench.txt')

    L_WPF = word_length(WPFr)
    L_WP = word_length(WarAndPeace)
    L_BK = word_length(TheBrothersKaramazov)
    L_US = word_length(Ulysses)

##    plt.ion()
##
##    histo_word(L_WP)
##    plt.title('War and Peace: English (' + str(len(WarAndPeace)) + ' Total words)')
##    histo_word(L_WPF)
##    plt.title('War and Peace: French (' + str(len(WPFr)) + ' Total words)')
####    histo_word(L_BK)
####    plt.title('The Brothers Karamazov (' + str(len(TheBrothersKaramazov)) + ' Total words)')
####    histo_word(L_US)
####    plt.title('Ulysses (' + str(len(Ulysses)) + ' Total words)')
##
##    
##    Al_WP = dict_each_letter(WarAndPeace)
##    AL_WPF = dict_each_letter(WPFr)
####    Al_BK = dict_each_letter(TheBrothersKaramazov)
####    Al_US = dict_each_letter(Ulysses)
##
##    g=raw_input('Press any key to continue.')
##
##    for x in xrange(3):
##        plt.close(x+1)
##
##    histo_letter(Al_WP)
##    plt.title('War and Peace: English (' + str(len(WarAndPeace)) + ' Total words)')
##    histo_word(AL_WPF)
##    plt.title('War and Peace: French (' + str(len(WPFr)) + ' Total words)')
####    histo_letter(Al_BK)
####    plt.title('The Brothers Karamazov (' + str(len(TheBrothersKaramazov)) + ' Total words)')
####    histo_letter(Al_US)
####    plt.title('Ulysses (' + str(len(Ulysses)) + ' Total words)')

    g=raw_input('Press any key to continue.')

    [WEn,WFr] = compare_dict(WarAndPeace,WPFr)

    Fval = sorted(WFr.values(),reverse=True)
    Enval = sorted(WEn.values(),reverse=True)

    


    print("Sorting the 30 most common words.")

    print("English      French")
    print("-------      -------")

    for x in xrange(30):
        for key in WEn:
            if WEn[key] == Enval[x]:
                m1=key
                break
        for key in WFr:
            if WFr[key] == Fval[x]:
                m2=key
                break
                
        print "{0}    {1}".format(m1,m2)
 
    
    

