#!/usr/bin/env python3
# (c) 2017 Kenneth An

"""A song generator: The user can enter a Beatles song and the program
will return a song that has the most words matched with the inputted 
song. The user can also enter a keyword and the program will return 
the song that has the most frequency of these words."""


from random import randint
import csv
import codecs
import itertools

punctuation = [".",",","!","?",":",";",'"',"'","(",")","-","/","\\"]
stopwords = ["and","but","in","it","its","that","to","is","are","on","a","the","i","of","oh"]


def canon(s):
    """Canonizes each word in the lyrics and adds them in a list alphabetically. Punctuation is taken out."""
    s = s.lower()
    s = s.split()
    s = sorted(s)
    result = []
    
    for word in s:
        for i in punctuation:
            if i in word:
                word = word.replace(i, '')
        result.append(word)
    return result

def one(s):
    """When a word in a list has more than one frequency this limits the word into one frequnecy."""
    result = []
    for word in s:
        if word not in stopwords:
            if word not in result:
                if s.count(word) > 1:
                    result.append(word)
    return result

def window(s, w):
    """Creates a list of keywords in lyrics under a certain window of the number of words."""
    if w > len(s):
        print("Too many keywords! There are only {} keywords.".format(len(s)))
    else:
        result1 = []
        result2 = []
        while (len(result1) < w):
            n = randint(0,len(s)-1)
            if n not in result1:
                result1.append(n)
        
        for i in range(0,len(result1)):
            term = result1[i]
            result2.append(s[term])
        return(result2)

def frequency(l):
    """Find the frequency of words in a list."""
    result = []
    entry = [l[0]]
    for i in range(1,len(l)):
        if i != (len(l)-1):
            if l[i] == l[i-1]:
                entry.append(l[i])
            else:
                result.append([l[i-1],len(entry)])
                entry = [l[i]]
        else:
            if l[i] == l[i-1]:
                entry.append(l[i])
                result.append([l[i],len(entry)])
            else:
                result.append([l[i-1],len(entry)])
                result.append([l[i],1])
    return result

def match(a,b):
    """Identifies keywords of a in frequency list of b."""
    result = []
    for word in a:
        for term in b:
            if term[0] == word:
                result.append(term)
    return result

def readDB(database='thebeatles.csv'):
    """Reads the Beatles lyrics csv file."""
    results = []
    with codecs.open(database,'r', encoding='utf-8', errors='ignore') as f:
        csvf = csv.reader(f)
        for row in csvf:
            results.append(row)
    return results

def generate(l):
    """Finds the song that has the most words in the inputted song matched in its lyrics."""
    plug = input("The Beatles song name? ")
    title = str(plug)
    compareList = []
    matchList = []
    matched = []
    
    for song in l:
        if song[0].lower() == title.lower():
            inputtedSong = song
            lyrics1 = song[1]
        else:
            compareList.append(song)
    
    song1 = one(canon(lyrics1))
    
    for song in compareList:
        lyrics2 = song[1]
        song2 = frequency(canon(lyrics2))
        wordList = match(song1,song2)
        wordList.append(song[0])
        matchList.append(wordList)
    
    for i in range(0,len(matchList)):
        if len(matchList[i]) == len(max(matchList,key=len)):
            matched.append(matchList[i])
    
    keywords = []
    for i in range(0,len(matched)):
        for j in range(0,len(matched[i])):
            if matched[i][j] != matched[i][-1]:
                key = matched[i][j][0].title()
                keywords.append(key)
    
    print("Your generated song is: {}.".format(matched[0][-1]))
    print("The keywords identified are: {}".format(', '.join(keywords)))

def identify(s,l):
    """Finds the song with the most frequency of an inputted keyword."""
    find = []
    most = []
    titles = []
    s = str(s)
    s = s.lower()
    for i in range(0,len(l)):
        if s in l[i][1]:
            lyrics = frequency(canon(l[i][1]))
            for i in range(0,len(lyrics)):
                if s == lyrics[i][0]:
                    song = [l[i][0],int(lyrics[i][1])]
                    find.append(song)
                    most.append(int(lyrics[i][1]))
    for i in range(0,len(find)):    
        if max(most) == find[i][1]:
            titles.append(find[i][0])
    
    if titles != []:
        if len(titles) > 1:
            print("The songs that have the most of these keywords are: {}. The word '{}' comes up {} times.".format(', '.join(titles), s, max(most)))
    
        print("The song that has the most of this word is: {}. The word '{}' comes up {} times.".format(titles[0], s, max(most)))
    
    elif titles == []:
        print("No result, sorry! Come back with a new keyword.")

if __name__ == "__main__":
    print("""
""")
    print("""Welcome to The Beatles Song Generator!
This application shows you a Beatles song that either:

1) has the most words similar to a song you input, or
2) has the most frequency of a word you input.

The Beatles song lyric database is from George Wagner's Beatles Website.
""")

    for i in itertools.count():
        decision = input("""Would you like to enter a song or a keyword? 
(Please type 'song' or 'word') """)

        if decision == "song":
            generate(readDB())

        elif decision == "word":
            s = input("Keyword? ")
            identify(s, readDB())

        print("""
""")
        decision2 = input("Would you like to use this app again? (yes or no) ")

        print("""
""")

        if decision2 == 'no':
            print("Thank you for using The Beatles Song Generator!")
            print("""
""")
            break
