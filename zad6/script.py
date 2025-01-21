import os

# Wyświetlenie aktualnego katalogu roboczego
print("Current working directory:", os.getcwd())
print("Contents of directory:", os.listdir("."))

# Wyświetlenie zawartości pliku dodanego przez ADD
with open("extracted_file.txt", "r", encoding="utf-16") as file:
    print("Contents of extracted_file.txt:", file.read())
