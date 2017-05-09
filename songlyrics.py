#!/usr/bin/env python3
# (c) 2017 Kenneth An

hey_jude = "Hey, Jude, don't make it bad Take a sad song and make it better Remember to let her into your heart Then you can start to make it better Hey, Jude, don't be afraid You were made to go out and get her The minute you let her under your skin Then you begin to make it better And anytime you feel the pain, Hey, Jude, refrain Don't carry the world upon your shoulders For well you know that it's a fool Who plays it cool By making his world a little colder Nah, nah nah, nah nah, nah nah, nah nah Hey, Jude, don't let me down You have found her, now go and get her Remember to let her into your heart Then you can start to make it better So let it out and let it in, Hey Jude, begin You're waiting for someone to perform with And don't you know that it's just you, Hey Jude, you'll do The movement you need is on your shoulder Nah, nah nah, nah nah, nah nah, nah nah yeah Hey, Jude don't make it bad Take a sad song and make it better Remember to let her under your skin Then you'll begin to make it better, better, better, better, better... oh! Nah, nah nah, nah nah, nah, nah, nah nah, Hey Jude"

let_it_be = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom Let it be And in my hour of darkness She is standing right in front of me Speaking words of wisdom Let it be Let it be Let it be Let it be Let it be Whisper words of wisdom Let it be And when the broken-hearted people Living in the world agree There will be an answer Let it be For though they may be parted there is Still a chance that they will see There will be an answer Let it be Let it be, let it be, let it be, let it be Yeah, there will be an answer Let it be Let it be, let it be, let it be, let it be Whisper words of wisdom Let it be Let it be, let it be, let it be, let it be Whisper words of wisdom Let it be And when the night is cloudy There is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom Let it be Let it be, let it be, let it be, yeah, let it be There will be an answer Let it be Let it be, let it be, let it be, yeah, let it be There will be an answer let it be Let it be, let it be, let it be, yeah, let it be Whisper words of wisdom Let it be"

strawberry_fields_forever = "Let me take you down, 'cause I'm going to Strawberry Fields Nothing is real and nothing to get hung about Strawberry Fields forever Living is easy with eyes closed Misunderstanding all you see It's getting hard to be someone but it all works out It doesn't matter much to me Let me take you down, cause I'm going to Strawberry Fields Nothing is real and nothing to get hung about Strawberry Fields forever No one I think is in my tree I mean it must be high or low That is you can't you know tune in but it's all right That is I think it's not too bad Let me take you down, cause I'm going to Strawberry Fields Nothing is real and nothing to get hung about Strawberry Fields forever Always, no sometimes, think it's me But you know I know when it's a dream I think I know I mean a 'yes' but it's all wrong That is I think I disagree Let me take you down, cause I'm going to Strawberry Fields Nothing is real and nothing to get hung about Strawberry Fields forever Strawberry Fields forever Strawberry Fields forever Cranberry sauce"

beatles = [['Hey Jude', "Hey, Jude, don't make it bad Take a sad song and make it better Remember to let her into your heart Then you can start to make it better Hey, Jude, don't be afraid You were made to go out and get her The minute you let her under your skin Then you begin to make it better And anytime you feel the pain, Hey, Jude, refrain Don't carry the world upon your shoulders For well you know that it's a fool Who plays it cool By making his world a little colder Nah, nah nah, nah nah, nah nah, nah nah Hey, Jude, don't let me down You have found her, now go and get her Remember to let her into your heart Then you can start to make it better So let it out and let it in, Hey Jude, begin You're waiting for someone to perform with And don't you know that it's just you, Hey Jude, you'll do The movement you need is on your shoulder Nah, nah nah, nah nah, nah nah, nah nah yeah Hey, Jude don't make it bad Take a sad song and make it better Remember to let her under your skin Then you'll begin to make it better, better, better, better, better... oh! Nah, nah nah, nah nah, nah, nah, nah nah, Hey Jude"],["Let It Be","When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom Let it be And in my hour of darkness She is standing right in front of me Speaking words of wisdom Let it be Let it be Let it be Let it be Let it be Whisper words of wisdom Let it be And when the broken-hearted people Living in the world agree There will be an answer Let it be For though they may be parted there is Still a chance that they will see There will be an answer Let it be Let it be, let it be, let it be, let it be Yeah, there will be an answer Let it be Let it be, let it be, let it be, let it be Whisper words of wisdom Let it be Let it be, let it be, let it be, let it be Whisper words of wisdom Let it be And when the night is cloudy There is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom Let it be Let it be, let it be, let it be, yeah, let it be There will be an answer Let it be Let it be, let it be, let it be, yeah, let it be there will be an answer let it be Let it be, let it be, let it be, yeah, let it be Whisper words of wisdom Let it be"],["Strawberry Fields Forever","Let me take you down, 'cause I'm going to Strawberry Fields Nothing is real and nothing to get hung about Strawberry Fields forever Living is easy with eyes closed Misunderstanding all you see It's getting hard to be someone but it all works out It doesn't matter much to me Let me take you down, cause I'm going to Strawberry Fields Nothing is real and nothing to get hung about Strawberry Fields forever No one I think is in my tree I mean it must be high or low That is you can't you know tune in but it's all right That is I think it's not too bad Let me take you down, cause I'm going to Strawberry Fields Nothing is real and nothing to get hung about Strawberry Fields forever Always, no sometimes, think it's me But you know I know when it's a dream I think I know I mean a 'yes' but it's all wrong That is I think I disagree Let me take you down, cause I'm going to Strawberry Fields Nothing is real and nothing to get hung about Strawberry Fields forever Strawberry Fields forever Strawberry Fields forever Cranberry sauce"],["Yesterday","Yesterday, all my troubles seemed so far away Now it looks as though they're here to stay Oh, I believe in yesterday, Suddenly, I'm not half the man I used to be, There's a shadow hanging over me. Oh, yesterday came suddenly. Why she had to go I don't know she wouldn't say. I said something wrong, now I long for yesterday. Yesterday, love was such an easy game to play. Now I need a place to hide away. Oh, I believe in yesterday. Why she had to go I don't know she wouldn't say. I said something wrong, now I long for yesterday. Yesterday, love was such an easy game to play. Now I need a place to hide away. Oh, I believe in yesterday. Mm mm mm mm mm mm mm."]]


punctuation = [".",",","!","?",":",";",'"',"'","(",")"]
stopwords = ["and","but","in","it","its","that","to","is","are","on","a","the"]


from random import randint
from collections import Counter


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
    """Identifies an inputted number of w keywords of a in frequency list of b."""
    result = []
    for word in a:
        for term in b:
            if term[0] == word:
                result.append(term)
    return result

def identify(l):
    plug = input("Beatles Song Name? ")
    title = str(plug)
    compareList = []
    matchList = []
    matched = []
    
    for song in l:
        if song[0] == title:
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
    
    #if len(matched) == 1:
    
    print("Your generated song is: {}.".format(matched[0][-1]))
    print("The keywords identified are: {}".format(', '.join(keywords)))
    
    #elif len(matched) > 1:
    #    c = 0
    #    maxes = []
    #    for i in range(0,len(matched)):
    #        for j in range(0,len(matched[i])):
    #            if matched[i][j] == matched[i][-1]:
    #                c += matched[i][j][1]
    #                print(c)



if __name__ == "__main__":
    #title = str(input("Song Name? "))
    #title = title.lower()
    #title = title.replace(' ','_')
    #for song in beatles:
    #    if song[0] == title:
    #        lyrics1 = song[1]
    #lyrics2 = strawberry_fields_forever
    #canon1 = canon(lyrics1)
    #one = one(canon1)
    #key = input("How many keywords? (The more the merrier!): ")
    #window = window(one,int(key))
    #canon2 = canon(lyrics2)
    #freq = frequency(canon2)
    #print(match(one,freq))
    #file = ' '.join([line.strip() for line in open('thebeatles.txt')])
    
    #lyrics1 = strawberry_fields_forever
    #lyrics2 = hey_jude
    #canon1 = canon(lyrics1)
    #one = one(canon1)
    #canon2 = canon(lyrics2)
    #freq = frequency(canon2)
    #print(freq)
    
    identify(beatles)
    
