print("hello how are you?")
print("In main file")
# get user input and write to file
data = input("Enter some data: ")
with open("user_data.txt", "w") as f:
    f.write(data)
# read file    
with open("file1.txt", "r") as f:
    data = f.read()
data_capitalized = data.upper()
print(data_capitalized)

print("End of main file")
print("Bye! See you later!")