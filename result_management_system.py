import json

print("")
print("This is a result calculator".center(40, "-"))


# Function to calculate result of a student based on user input and store it in the 'students' dictionary
def result_calculation():
    # Basic input from user
    name = input("\nEnter your name: ").strip().title()  # Converts the input name to title case (first letter of each word capitalized) for consistent formatting when storing and retrieving results.

    while name == "":
        print("\nName cannot be empty. Please enter a valid name.")
        name = input("Enter your name: ").strip().title()

    try:
        physics = int(input("Enter marks for Physics: "))
        while physics < 0 or physics > 100:
            print("\nInvalid input for Physics marks. Please enter a value between 0 and 100.")
            physics = int(input("Enter marks for Physics: "))

        chemistry = int(input("Enter marks for Chemistry: "))
        while chemistry < 0 or chemistry > 100:
            print("\nInvalid input for Chemistry marks. Please enter a value between 0 and 100.")
            chemistry = int(input("Enter marks for Chemistry: "))

        maths = int(input("Enter marks for Mathematics: "))
        while maths < 0 or maths > 100:
            print("\nInvalid input for Mathematics marks. Please enter a value between 0 and 100.")
            maths = int(input("Enter marks for Mathematics: "))
    except ValueError:
        print("\nInvalid input. Please enter numeric values for marks.")
        return result_calculation()  # Recursively call the function to prompt the user again for valid input if a non-numeric value is entered.

    total_marks = physics + chemistry + maths
    total_percentage = (physics + chemistry + maths)*100/300

    # Grade calculation based on total percentage
    if total_percentage>=90 and total_percentage<=100:
        grade = "A+"
    elif total_percentage>=80 and total_percentage<90:
        grade = "A"
    elif total_percentage>=70 and total_percentage<80:
        grade = "B"
    elif total_percentage>=60 and total_percentage<70:
        grade = "C"
    elif total_percentage<60 and total_percentage>=40:
        grade = "D"
    else:
        grade = "N/A"

    # Status calculation
    if (physics<33) or (chemistry<33) or (maths<33):
        status = "Fail"
    else:
        status = "Pass"

    result = {
        "Name": name,
        "Physics": physics,
        "Chemistry": chemistry,
        "Mathematics": maths,
        "Total Marks": total_marks,
        "Total Percentage": f"{total_percentage:.2f}",
        "Grade": grade,
        "Status": status
        }

    
    # Store the result in a JSON file
    def save_to_json():
        try:
            with open("results.json", "r") as file:
                data = json.load(file)

            found = False
            for student in data:
                if student["Name"] == name:
                    student["Physics"] = physics
                    student["Chemistry"] = chemistry
                    student["Mathematics"] = maths
                    student["Total Marks"] = total_marks
                    student["Total Percentage"] = f"{total_percentage:.2f}"
                    student["Grade"] = grade
                    student["Status"] = status
                    found = True
                    break

            if not found:
                data.append(result)

            with open("results.json", "w") as file:
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            data = []
            data.append(result)
            
            with open("results.json", "w") as file:
                json.dump(data, file, indent=4)

        print(f"\nResult for {name} has been saved successfully.")

    save_to_json()


# Function to display result of a specific student based on user input
def student_result():
    try:
        view_name = input("\nEnter the name of the student you want to view result for: ").strip().title()  # Converts the input name to title case for consistent formatting when retrieving results from the 'students' dictionary.
        
        with open("results.json", "r") as file:
            data = json.load(file)

            for student in data:
                if student["Name"] == view_name:
                    print("\n", f"Result of {view_name}".center(20, "-"), "\n")
                    for key, value in student.items():
                        print(f"{key}: {value}")
                        
                    return main_menu2()
                    
            else:
                print(f"\nNo result found for {view_name}")
                input_option = input("\nTry again? (y/n): ")
                if input_option == "y":
                    return student_result()
                else:
                    return main_menu2()

            

    except FileNotFoundError:
        print("\nNo results found. Please enter student results first.")
        main_menu2()
        
# Function to display results of all students in the class
def class_result():
    try:
        with open("results.json", "r") as file:
            data = json.load(file)

        print("\n", "Class results".center(40, "-"))
        for student in data:
            print("\n", f"Result of {student['Name']}".center(20, "-"), "\n")
            for key, value in student.items():
                print(f"{key}: {value}")

    except FileNotFoundError:
        print("\nNo results found. Please enter student results first.")
        main_menu2()
            
def main_menu3():
    input_option = input("\n1. Try again\n2. Go back to main menu\n\nPlease select an option (1 or 2): ")
    if input_option == "1":
        student_result()  # Recursively call the student_result function to prompt the user again for a valid student name if the entered name is not found in the 'students' dictionary.
    elif input_option == "2":
        main_menu()  # Call the main_menu function to return to the main menu if the user chooses to go back instead of trying again.
    else:
        print("Invalid option selected.")
        return main_menu3()  # Recursively call

    main_menu3()  # Call main_menu3 to handle the user's choice after an invalid student name is entered.

    
# internal function to handle user choice after entering student result or viewing specific student result, allowing them to either go back to the main menu or exit the program.
def main_menu2():
    menu_input = input("\n1. Go back to main menu\n2. Exit\n\nPlease select an option (1 or 2): ")
    if menu_input == "1":
        main_menu()
    elif menu_input == "2":
        print("\nThank you for using the result calculator. Goodbye!\n")
    else:
        print("\nInvalid option selected.")
        return main_menu2()

# Logic for user interaction and menu options
def main_menu():
    print("\n", "Main Menu".center(40, "-"))
    input_option = input("\n1. Enter student result\n2. View  specific student result\n3. View class results\n4. Exit\n\nPlease select an option (1, 2, 3 or 4): ")

    if input_option == "1":
        option = "y"
        while option == "y":
            result_calculation()
            option = input("\nDo you want to enter details for another student? (y/n): ")
        else:
            main_menu2()

    elif input_option == "2":
        student_result()

    elif input_option == "3":
        class_result()
        main_menu2()

    elif input_option == "4":
        print("\nThank you for using the result calculator. Goodbye!\n")

    else:
        print("\nInvalid option selected. Please select 1, 2, 3 or 4.")
        return main_menu()  # Recursively call the main function to prompt the user again for a valid option.

if __name__ == "__main__":
    main_menu()