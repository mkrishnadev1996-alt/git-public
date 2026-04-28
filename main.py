print("hello how are you?")
print("In main file")
try:
    with open("file1.txt", "r") as f:
        data = f.read()
    data_capitalized = data.upper()
    print(data_capitalized)
except FileNotFoundError:
    print("file1.txt not found. Please make sure the file exists.")

print("End of main file")
print("Bye! See you later!")