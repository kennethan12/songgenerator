#!/usr/bin/env python3
# (c) 2017 Kenneth An

hey_jude = "Hey, Jude, don't make it bad Take a sad song and make it better Remember to let her into your heart Then you can start to make it better Hey, Jude, don't be afraid You were made to go out and get her The minute you let her under your skin Then you begin to make it better And anytime you feel the pain, Hey, Jude, refrain Don't carry the world upon your shoulders For well you know that it's a fool Who plays it cool By making his world a little colder Nah, nah nah, nah nah, nah nah, nah nah Hey, Jude, don't let me down You have found her, now go and get her Remember to let her into your heart Then you can start to make it better So let it out and let it in, Hey Jude, begin You're waiting for someone to perform with And don't you know that it's just you, Hey Jude, you'll do The movement you need is on your shoulder Nah, nah nah, nah nah, nah nah, nah nah yeah Hey, Jude don't make it bad Take a sad song and make it better Remember to let her under your skin Then you'll begin to make it better, better, better, better, better... oh! Nah, nah nah, nah nah, nah, nah, nah nah, Hey Jude"

let_it_be = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom Let it be And in my hour of darkness She is standing right in front of me Speaking words of wisdom Let it be Let it be Let it be Let it be Let it be Whisper words of wisdom Let it be And when the broken-hearted people Living in the world agree There will be an answer Let it be For though they may be parted there is Still a chance that they will see There will be an answer Let it be Let it be, let it be, let it be, let it be Yeah, there will be an answer Let it be Let it be, let it be, let it be, let it be Whisper words of wisdom Let it be Let it be, let it be, let it be, let it be Whisper words of wisdom Let it be And when the night is cloudy There is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom Let it be Let it be, let it be, let it be, yeah, let it be There will be an answer Let it be Let it be, let it be, let it be, yeah, let it be There will be an answer let it be Let it be, let it be, let it be, yeah, let it be Whisper words of wisdom Let it be"

punctuation = [".",",","!","?",":",";",'"',"'","(",")"]
stopwords = ["and","but","in","it","its","that","to","is","are","on","a","the"]

from random import randint

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
    if w > len(s):
        print("Too many keywords! Try a smaller number.")
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

if __name__ == "__main__":
    lyrics = hey_jude
    canon = canon(lyrics)
    one = one(canon)
    key = input("How many keywords? (The more the merrier!): ")
    window = window(one,int(key))
    print(window)


__all__ = ['Keywords']

class Keywords(object):
    """A class which picks out certain keywords from the lyrics of an inputted song."""

    __slots__ = [ "_window"]

    def __init__(self, window = 5):
        self._window = window

    def canon(self, s):
        """Canonizes each word in the lyrics and adds them in an alphabetical list"""
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


    
