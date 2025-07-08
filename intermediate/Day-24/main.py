# project: this is just a sample file irrespective of the input and the output files.this is just to refer to the format and syntax.
PLACEHOLDER="[name]"


with open("./input/names/invited_names.txt") as names_file:
    names = names_file.readlines()
    #readlines will give the output of names as a list
    print(names)
with open ("./input/letters/starting_letter.txt") as letter_file:
    letter=letter_file.read()
    for name in names:
        stripped_name=name.strip()
        new_letter=letter.replace(PLACEHOLDER,name) 
      # to print the output files in the same folder.
        with open(f"./output/readytosend/letter_for {stripped_name}.docx",'w') as complete_letter:
            complete_letter.write(new_letter)
        print(new_letter)

#for loop to read every name in the list
