# Write the code to replace all the Python word fron the data in practice file with Java
def check_n_replace():
    with open("Practice.txt", "r") as file1:
        data = file1.read()

    new_data = data.replace("python", "Java")
    print(new_data)

    with open("Practice.txt", "w") as file2:
        file2.write(new_data)

check_n_replace()

#check for offering word inthe practice txt file
def check_for_word():
    word = "offering"
    with open("Practice.txt", "r") as file3:
        data1 = file3.read()
        if(data1.find(word)) != -1:
            # if(word in data) another way of writing above line
            print("Found")
        else:
            print("Not Found")

check_for_word()
    

