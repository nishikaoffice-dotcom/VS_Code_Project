#Program to read number from the input file and write it into output file 
#Read the numbers from the file
with open("Input.txt", "r") as infile:
#"r" means Opens the file in read mode.
#"w" means opens the file in write mode
    content = infile.readlines()
#    print(content)


#open output file
with open("output.txt", "w") as outfile1:
    for num in content:
        num = num.strip()
        if num.isdigit():
            n = int(num)
            if n % 2 == 0:
                outfile1.write(f"{n} is Even\n")
            else:
                outfile1.write(f"{n} is Odd\n")
        else:
            print(f"Input number {n} is not a valid number\n")




        
          
