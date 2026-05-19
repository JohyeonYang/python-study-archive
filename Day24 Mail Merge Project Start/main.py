#TODO: Create a letter using starting_letter.txt 

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

# for each name in invited_names.txt 
# r"Input/Names/invited_names.txt" 
with open(r"Input/Names/invited_names.txt") as name : 
    names = name.readlines() # readlines() reading every line from name(str), returning List with all elements 'name'

with open(r"Input/Letters/starting_letter.txt") as letter : 
    letter_content = letter.read() 
    
    for name in names :
        striped_name = name.strip() #strip() : cutting space, \t, \n from String
        new_letter = letter_content.replace(PLACEHOLDER, striped_name)
        with open(f"Output/To{striped_name}.txt", mode = "w") as completed_letter :
            completed_letter.write(new_letter)