# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions, parameters, and classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   KMcGuire, 8/19/25, Added classes and parameters
# ------------------------------------------------------------------------------------------ #
import json


# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
# FILE_NAME: str = "Enrollments.csv"
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

# This section holds the classes that are used to process and present data

# Processing ---------------------------------------------------------------- #
class FileProcessor:
    """
    A collection of processing Layer functions that work with JSON files

    ChangeLog: (Who, When, What)
    KMcGuire,8/19/25,Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads the data from the file
        ChangeLog: (Who, When, What)
        KMcGuire,8/19/25,Created Class
        """

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Text file must exist before running the script!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function writes the data to the file

        ChangeLog: (Who, When, What)
        KMcGuire,8/19/25,Created Class
        """
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
        except TypeError as e:
            IO.output_error_messages("Please check that the data is in a valid format", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if file.closed == False:
                file.close()

# Presentation -------------------------------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input/output

    ChangeLog: (Who, When, What)
    KMcGuire,8/19/25,Created Class
    """
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """This function displays a custom error message to the user

        ChangeLog: (Who, When, What)
        KMcGuire,8/19/25,Created function

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function outputs a menu for the user
        ChangeLog: (Who, When, What)
        KMcGuire,8/19/25,Created function
        :return: None
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        KMcGuire,8/19/25,Created Class

        : return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your choice: ")
            if choice not in ("1", "2", "3", "4",):
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())
        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets a student data from the user

        ChangeLog: (Who, When, What)
        KMcGuire,8/19/25,Created function

        :return: str
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student = {"FirstName": student_first_name,
                       "LastName": student_last_name,
                       "CourseName": course_name}
            student_data.append(student)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages("That was not the correct data", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function outputs a student data from the user
        ChangeLog: (Who, When, What)
        KMcGuire,8/19/25,Created function
        """
        print("-" * 50)
        for row in student_data:
            print(f'{row["FirstName"]},{row["LastName"]},{row["CourseName"]}')
        print("-" * 50)

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file

# Function definitions

# End of function definitions

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        # Process the data to create and display a custom message
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        IO.output_student_courses(student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
