print "Welcome to the super awesome word guessing game!"
secret_word = 'inspiration'
print "I am thinking of a word that is "+str(len(secret_word))+" letters long."


if t in range(len(secret_word)):
    i = secret_word[t]
    word_so_far = secret_word.replace(i,'-')
    print word_so_far
    

