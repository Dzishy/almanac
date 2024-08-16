
# file name
fileName = "almanac/course-40-challenging-Pyton-programs/9-Work-with-files/messages.txt"
 
# writing string into a file
def write():
    message = input("\nType something you want to be written to a file: ")
    with open(fileName, "a") as file:
        file.write(f'{message}\n')
 
# reading of the file
def read():
    with open(fileName, "r") as file:
        print()
        for message in file:
            print(message, end='')


def main():             
    while(True):
        selection = input("\n1.Write into the file\t\t2.Read the file\t\t3.Exit\nYour choice: ").strip()
        match selection:
            case '1': write()
            case '2': read()
            case '3': break
            case _: print("Incorrect input")

    print("\nProgram finished.")
main()