print("In main file")
with open("file1.txt", "r") as f:
    data = f.read()
data_capitalized = data.upper()
print(data_capitalized)
print("End of main file")
print("Bye! See you later!")