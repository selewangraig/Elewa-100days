#writing to file
var_name = open("statements.txt", "w")
var_name.write("The Tr wants us to do this on our own\n")
var_name.write("I am a student\n")
var_name.write("I check my emails daily\n")

var_name.close()

#appending file
var_name = open("statements.txt", "a")
var_name.write("I am so sleepy\n")
var_name.write("I think Nicole is a work of art.")

var_name.close()

#reading file
var_name = open("statements.txt", "r")
print(var_name.read())