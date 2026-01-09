
with open("lorem.txt", "r") as f:
    content = f.read()
    count = content.lower().count('e')
    print(f"The letter 'e' appears {count} times in the file lorem.txt.")
