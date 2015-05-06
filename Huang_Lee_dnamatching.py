string1 = raw_input("Please enter a string using the letters A, T, C, and G: ")
string2 = raw_input("Please enter another string using the letters A, T, C, and G: ")

#prompt for one of four commandss:
print "What do you want to do: "
print "a (add indel)"
print "d (delete indel)"
print "s (score)"
print "q (quit):"
# need to print list of possible commands together and specify raw_input as the response to this printed statement
if raw_input == "a":
    change_a = raw_input("Which string do you want to change?")
    index_a = raw_input("Before which index do you wish to place the indel?")
    if index_a.isdigit():
        index_a = int(index_a)
    else:
        print ("Please enter an integer for your index.")
    for i in range(len(change_a)):
        if index_a > i:
            print "This index is out of range."
        else:
            print change_a[0,i-1]+'-'+change_a[i,len(change_a)]
        
elif raw_input == "d":
    string_change_d = raw_input("Which string do you want to change?")
    index_d = raw_input("At which index do you want to delete the indel?")
    if index_d.isdigit():
        index_d = int(index_d)
    else:
        print ("Please enter an integer for your index.")

    


