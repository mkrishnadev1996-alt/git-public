print("hello how are you?")
print("In main file")
data = input("Enter some data: ")
with open("file1.txt", "r") as f:
    data = f.read()
data_capitalized = data.upper()
print(data_capitalized)
with open("user_data.txt", "w") as f:
    f.write(data)
print("End of main file")
print("Bye! See you later!")