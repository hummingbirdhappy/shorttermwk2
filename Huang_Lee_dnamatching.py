string1 = raw_input("Please enter a string using the letters A, T, C, and G: ")
#for l in string1:
    #if l not in "ATCG":
        #string1 = raw_input("Please enter a string using only the letters A, T, C, and G: ")
    #else:
        #pass
string2 = raw_input("Please enter another string using the letters A, T, C, and G: ")

#prompt for one of four commandss:
indel_change = raw_input("What do you want to do: \n a (add indel) \n d (delete indel) \n s(score) \n q (quit): ")
# need to print list of possible commands together and specify raw_input as the response to this printed statement
if indel_change == "a":
    change_a = raw_input("Which string do you want to change?")
    index_a = raw_input("Before which index do you wish to place the indel?")
    if index_a.isdigit():
        index_a = int(index_a)
    else:
        index_a = raw_input("Please enter an integer for the index: ")

    if index_a > ((len(change_a))-1):
        print "This index is out of range."
    else:
        print change_a[0,((index_a)-1)]+'-'+change_a[index_a,len(change_a)]
        
elif indel_change == "d":
    change_d = raw_input("Which string do you want to change?")
    index_d = raw_input("At which index do you want to delete the indel?")
    if index_d.isdigit():
        index_d = int(index_d)
    else:
        index_d = raw_input("Please enter an integer for your index.")

    


