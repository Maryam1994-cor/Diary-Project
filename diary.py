def add_entry():
    date = input("Enter the date: ")
    entry = input("Write your diary entry: ")

    file = open("diary.txt", "a")
    file.write(date + " - " + entry + "\n")
    file.close()

    print("Entry saved")


while True:
    print("\nDiary Menu")
    print("1. Add diary entry")
    print("2. View diary entries by date")
    print("3. Exit")

    choice = input("Choose 1, 2, or 3: ")

    if choice == "1":
        add_entry()
    elif choice == "3":
        print("Goodbye")
        break
