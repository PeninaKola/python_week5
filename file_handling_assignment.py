# file_handling_assignment.py

def main():
    try:
        # File Creation
        with open('my_file.txt', 'w') as file:
            file.write("This is the first line of text.\n")
            file.write("The second line includes a number: 42\n")
            file.write("Here is the third line with some more text.\n")
        print("File 'my_file.txt' created and initial content written.")

        # File Reading and Display
        with open('my_file.txt', 'r') as file:
            content = file.read()
            print("\nContents of 'my_file.txt':")
            print(content)

        # File Appending
        with open('my_file.txt', 'a') as file:
            file.write("Appending a new line of text.\n")
            file.write("Adding another line with more information.\n")
            file.write("This is the final appended line.\n")
        print("\nAdditional lines appended to 'my_file.txt'.")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nFile operations completed.")

if __name__ == "__main__":
    main()