import itertools
import sys

def spilting(sentence):
    words = sentence.split()
    ns = range(1, len(words)) # n = 1..(n-1)
    for n in ns: # split into 2, 3, 4, ..., n parts.
        for idxs in itertools.combinations(ns, n):
            yield [' '.join(words[i:j]) for i, j in zip((0,) + idxs, idxs + (None,))]


def logic(size,array,k):
    maximum=0
    #if we can count all the words in the phrase, return the length of the phrase itself
    if(sum(array)<=k):
        return len(array)
    else:
        #Convert the number array into a string as we want all combinations of the phrase
        sentence=str(array[0])
        for i in range(1,size):
            sentence=sentence+" "+str(array[i])
        #Spliting function makes all combinations of phrases possible with an array
        for word in spilting(sentence):
            print("word",word)
            lists=[x for x in range(len(word))] #Contains the index range of the words (0...n)
            #Calculate the length of each subdivided word in the phrase
            for item in word:
                str1=item.split()
                int_str1=[int(i) for i in str1]
                if(len(int_str1)>maximum and sum(int_str1)<=k):#We need to find the maximum number of words in the entire phrase
                    maximum=len(int_str1)

        return maximum


def main():
    phrase=input("enter the phrase: ")
    wordCountList=[len(x) for x in phrase.split()]
    print("List of word length: ",wordCountList)
    k=int(input("Enter value of k: "))
    size=len(wordCountList)
    result=logic(size,wordCountList,k)
    print(result)

main()
