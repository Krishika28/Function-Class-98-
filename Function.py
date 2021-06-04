def countWords ():
    fileName = input("Enter the file name:- ")
    noOfWords = 0
    file = open(fileName, 'r')
    for i in file :
        words = i.split()
        noOfWords = noOfWords+ len(words)   
    print("No. of words: ", noOfWords)

countWords()