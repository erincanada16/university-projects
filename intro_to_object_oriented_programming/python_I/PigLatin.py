#Defining the translation to pig latin
def pig_latin (word,cap = True):
    first_character = word [0]
    last_character = word [-1]
    way = "way"
    ay = "ay"
    vowel = ("a", "e","i", "u","A", "E", "I", "U")
    #Added punctuation for funzies :)
    punct = ("!", "," ,"." , "-", "?")
    for char in word:
        if char in punct:
            word = word [:-1]
            if first_character in vowel:
                return_value = word + way + last_character
                return return_value  
            else:
                return_value = word[1:] + first_character + ay + last_character
                if cap:  #Accounting for capitalizations
                    return_value = return_value[0].upper()+ return_value[1:].lower()
                return return_value
            
    if first_character in vowel:
        return_value = word + way 
        return return_value  
    else:
        return_value = word[1:] + first_character + ay
        if cap:    #Accounting for capitalizations
            return_value = return_value[0].upper()+ return_value[1:].lower()
        return return_value

    
#Defining count definition
def count (line_count, word_count):
    return ("A total of {} lines were translated successfully.\nA total of {} words were translated successfully").format (line_count, word_count) 
    
    

#Ask user for text file
file_path = raw_input("Please enter the text file name: ")

#Assign variable to open and read file_path and write to pig.output.txt
desired_file = open (file_path, "r")
out_file = open ("pig.output.txt", "w")

#Setting up line and word count
line_count = 0
word_count = 0

#Reading and writing to file ou
for line in desired_file:
    line_count += 1
    line.strip("\n")
    for word in line.split():
        if word[0].isupper():        
            word = pig_latin(word) +" "
            word_count += 1
            out_file.write (word)
        else:
            word = pig_latin(word,False) +" "
            word_count += 1
            out_file.write (word)
    out_file.write ("\n")
    
    

#Close file
desired_file.close()
out_file.close()

#Print confirmation message
print ("Translation finished and written to output.txt")   
print (count(line_count, word_count)) 





