#Open files in list and show the content
filenames = ['cats.txt', 'dogs.txt'] 
try:
    with open(filenames) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = "Sorry " + filename + " doesn't exist."
    print(msg)



