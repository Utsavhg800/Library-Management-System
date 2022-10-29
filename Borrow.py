import DateTime as dt
import Library as lib


def borrow_book():
    """Handles operations for borrowing book"""
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    borrow_rec = f"text/Borrowed-{first_name}.txt"
    f = open(borrow_rec, "w+")
    f.write(f'''Library Management System: \n\n\n
    Borrowed by: {first_name} {last_name} 
    Date: {dt.getCurrentDate()}
    Time: {dt.getCurrentTime()}
    S.N.\tBook Name\t\t\t\t\t\tAuthor\t\t\t\tCost\n''')
    f.close()

    count = 1
    while True:  # until break
        print("Please select an option: ")
        [print(f"Enter {i} to borrow book {lib.bookInfoList['name'][i]}") for i in range(len(lib.bookInfoList['name']))]

        try:
            index = int(input("Please enter book number: "))
            try:  # can throw index out of bounds exception
                if lib.bookInfoList['quantity'][index] > 0:
                    print("Book is available")
                    f = open(borrow_rec, "a")  # in append mode
                    f.write(
                        f"\t{count} \t\t{lib.bookInfoList['name'][index]}\t\t\t\t{lib.bookInfoList['author'][index]}"
                        f"\t\t\t\t{lib.bookInfoList['price'][index]}\n")
                    f.close()

                    lib.bookInfoList['quantity'][index] -=  1
                    f = open("text/library.txt", "w+")
                    for i in range(3):
                        f.write(
                            f"{lib.bookInfoList['name'][i]},{lib.bookInfoList['author'][i]},"
                            f"{lib.bookInfoList['quantity'][i]},${lib.bookInfoList['price'][i]}\n")
                    f.close()
                    yn = input("Do you want to borrow more books?(y/n): ")
                    if yn.lower() != "y":
                        break  # end loop
                    count += 1
                else:
                    print("Book is not available in stock")
            except IndexError:
                print("\nPlease choose book as per their number.")
        except ValueError:
            print(f"\nPlease enter a valid number.")
