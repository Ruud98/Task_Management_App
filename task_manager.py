# Compulsory Task Part 1
from datetime import date
import datetime

# Code to check if there is info in the user text file
# If there is no information, then the sign up func will be executed
file = open('user.txt', 'r').readlines()
user_counter = [line for line in file]

# Function to allow admin to sign up only if its the first time the program is being run
def sign_up():
    # Printing the welcome message and giving instructions to the first user(admin)
    print("||===========================| Welcome to the TASK MANAGER |==========================||")
    print("\t\t>>>>>>PLEASE NOTE THAT THE FIRST USER MUST BE THE ADMIN<<<<<<")
    print("\n>>>Now, lets create an ADMIN user profile:")
    print("\n||==========| By default your Username is set to 'Admin' |==========||")

    admin_username = 'admin' # Setting up the admin default username
    admin_password = input('Please confirm your new password here: ') # Requesting the admin to enter their new password
    admin_password2 = input('Please retype your new password here: ')

    while admin_password != admin_password2:
        print("Password do not match, Please Retry!!")
        admin_password = input('Please confirm your new password here: ') # Requesting the admin to enter their new password
        admin_password2 = input('Please retype your new password here: ')

    # Writing the admin username and password to the user.txt file
    file = open('user.txt', 'w')
    file.write(f"{admin_username}, {admin_password}")
    file.close()
    print("\nAdmin profile Successfully created!")

# Executing the signup function if its the first time the program is being ran   
if len(user_counter) == 0:
    sign_up()

# Welcoming the user and asking them to give their username and password
print("||======================| TASK MANAGER |======================||")
print()
print("         ==================| LOGIN |===================")
print("\nPlease follow the prompts below and enter your login credentials.\n")

# Asking the user to enter username so they may log in
user_name = input("Enter username: ")
user_name = user_name + ',' # Adding a ',' charecter inorder to match username as it is saved in the user txt file
user_name = user_name.lower()

# Asking the user to enter the password so they may login
password = input("Enter password: ")
password = password.lower()

# Function for loging-in, function will check if user is registered to use task manager
def cred_check():
    """ Function to check login credentials """
    # Block below runs if the passowrd and username are diffent as required by the program
    user_info = open("user.txt", "r") # Extracting password and username from the user text file
    password_username = '' # Variable holds password and username
    
    for line in user_info:
        password_username += line
    user_info.close
    password_username = password_username.split() # Splitting the lines in the user text file so we may find password/username
        
    global user_name # Using 'Global' keyword in order to
                     # make use of the variables assigned out of the function
    global password

    # Ensuring that password and username are not similar
    while user_name == password + ',': # While loop will run until a password and username that are not similar are entered
        print("\nUsername and Password cannot be similar!!\nPlease try again.") # If passord and username are similar
        print()  # Blank space
        user_name = input("Enter username: ")
        password = input("Enter password: ")

    while user_name not in password_username or password not in password_username:
        print("\nInvalid Login Credentials!!\n\nPlease Try Again!!")
        user_name = input("Enter username: ")
        user_name = user_name + ',' # Adding a ',' charecter inorder to match username as it is saved in the user txt file
        user_name = user_name.lower()

        # Asking the user to enter the password so they may login
        password = input("Enter password: ")
        password = password.lower()

# Function to register a user
# Asking the user to enter a new username and password
# noinspection PyUnboundLocalVariable
def create_user():
    """  Function to register a user """
    # Ensuring that new username does not already exist
    print("NB: Please ensure that the username and password are different!") # Advising the user to enter password and username that are not similar
    name_exists = True
    while name_exists: # While will run until a new username is entered
        username = input("\nPlease enter the new username: ")
        username = username.lower()

        # Mini code block to extract username-password and store in a string
        file = open("user.txt", "r")
        password_username = ''
        for line in file:
            password_username += line
        file.close()
        password_username = password_username.split()# Seperating the passoword & usernames 

        # Validating username - checking new username does not already exist
        existing_username = 0  # to hold the existing name so we can use it later
        user_name_exist = False
        for name in password_username: # For loop searching for username 
            if name.lower() in username + ',':
                existing_username = name
                user_name_exist = True # If new username provided is found then user is asked to enter
                                       # a different one
        if user_name_exist: # Code will run if new username entered already exists
            print("Oops!!") 
            print(f"Username '{existing_username}' already exists!! Please enter a different one")
        else:
            break # Code will break and move to the next stage if the entered new username does not already exist

    # Asking the user for the new password, and adding new user credentials to the user.txt file
    password = input("Please enter the new password: ")
    password = password.lower()

    # Below mini code block appends the new user's password to the user txt file
    file = open("user.txt", 'a')
    # noinspection PyUnboundLocalVariable
    file.write('\n{0}, {1}'.format(username, password)) # Writing the username and password to the user txt file
    file.close()

    # Informing user that account creation was successful
    print("Account creation Successful!!")

# Function to add a task
def add_task():
    """Function to add a task"""
    username_of_task_owner = input("Please enter the username of user being assigned the task: ") # Username the task is assigned to
    username_of_task_owner = username_of_task_owner.lower()
    title_of_the_task = input("Please enter the title of the task: ")
    title_of_the_task = title_of_the_task.lower()
    task_description = input("Please enter the description of the task: ")
    task_description = task_description.lower()
    task_due_date = input("Please enter the due date of the task (yyyy-mm-dd): ")
    task_due_date = task_due_date.lower()
    date_task_given = datetime.date.today()
    date_task_given = str(date_task_given)
    date_task_given = date_task_given.lower()
    task_completed = 'No'

    # writing provided task information to the task.txt file
    file = open('tasks.txt', 'a')
    file.write(
        f"\n{username_of_task_owner},{title_of_the_task},{date_task_given},{task_due_date},"
        f"{task_completed},{task_description}")
    file.close()

    # Telling user that task information has been recorded
    print("\nTask information has been recorded successfully.\n")

# Function to to view all tasks
# noinspection PyUnusedLocal
def view_all_tasks():
    """Function to to view all tasks"""
    print("*********\tBelow are all the tasks********")

    # Calculating number of lines so that we may print the tasks accordingly
    line_counter = 0
    file = open('tasks.txt', 'r')
    for line in file:
        line_counter += 1
    file.close()

    # Printing out tasks in readable format
    file2 = open('tasks.txt', 'r')

    newest = []
    new = [line.split('\n') for line in file2] # Splitting the lines in task file so we may print specific info
    for i in new: # Splittin the lines further
        newest.append(str(i).split(','))
    file2.close()

    for i in range(line_counter): # Printing the tasks in reader friendly formart
        print(f"Task:\t\t\t{newest[i][1]}")
        print("Assigned to:\t\t{}".format(newest[i][0].replace("['", '')))
        print(f"Date Assigned:\t\t{newest[i][2]}")
        print(f"Due date:\t\t{newest[i][3]}")
        print(f"Task Completed?:\t{newest[i][4]}")
        task_description = newest[i][5].replace("]", '')
        task_description2 = newest[i][5].replace("'", '')
        task_description3 = task_description2.replace(task_description2[-1], '')
        print(f"Task Description:\t{task_description3}")
        print()

# Function to view tasks assigned to a user
# noinspection PyUnusedLocal
def view_my_task():
    """Function to view tasks assigned to current user"""
    global user_name # using the global keyword so func may use globally defined username variable
    new_name = user_name.replace(',','')
    username = new_name

    # Function to edit tasks, will be used later below
    def replace_line(file_name, line_num, text): 
        """Function to replace words in the text file"""
        lines = open(file_name, 'r').readlines() # Opening a file
        lines[line_num] = text # Using line number that will be provided when func is executed
        out = open(file_name, 'w')
        out.writelines(lines) # Writing the newly entered information to the file 
        out.close()

    # Calculating number of lines in the tasks.txt file
    line_counter = 0
    file = open('tasks.txt', 'r')
    for line in file:
        line_counter += 1
    file.close()

    # Printing out tasks in readable format
    file2 = open('tasks.txt', 'r')
    newest = []
    new = [line.split('\n') for line in file2] # Splitting the lines in txt file every where there is '\n'
    for i in new:
        newest.append(str(i).split(',')) # Splitting the lines further so we may extract exact info
    file2.close()

    # Searching for the username and printing out the tasks
    print("\nNB: IF NOTHING IS PRINTED BELOW, IT MEANS THAT YOU CURRENTLY DO NOT HAVE TASKS!.")
    print("\t*****Your Tasks:****\n")
    task_number = [] # keeping track of task count so we may allocate numbers to tasks
    for i, value in enumerate(newest):
        user_provided_username = str(newest[i][0]).replace(' ', '') # removing blank space
        user_provided_username = user_provided_username.replace("['", '') # removing ['
        user_provided_username = user_provided_username.replace(":", '') # removing :
        if user_provided_username == username: # Checking the current user so their tasks are printed
            task_number.append(i)
            print(f"Task number: {i}")
            print(f"Task:\t\t\t{newest[i][1]}")
            print("Assigned to:\t\t{}".format(newest[i][0].replace("['", ''))) # removing ['
            print(f"Date Assigned:\t\t{newest[i][2]}")
            print(f"Due date:\t\t{newest[i][3]}")
            print(f"Task Completed?:\t{newest[i][4]}")
            task_description = newest[i][5].replace("]", '') # removing ']
            task_description2 = newest[i][5].replace("'", '') # removing blank space
            task_description3 = task_description2.replace(task_description2[-1], '') # removing char ] at the end
            print(f"Task Description:\t{task_description3}")
            print()

    # Section to allow user to select and alter a Task
    print("If you would like to alter a task please enter the Task Number or -1 to go back to the Menu\n")

    # Below mini code block is for ensuring that user input is valid. 
    for i in range(5): # Giving the user only 5 tries before asking them to restart
        try:
            user_task_number = int(input("Enter the task number or -1: ")) # 
        except:
            print("Invalid input!!, Please Retry!!") # Line to catch error if user enters an invalid input eg a word
            continue
        
        if user_task_number == -1:
            break
        
        elif user_task_number not in task_number: # If user enters a number not aligned to any task
            print("Invalid task number!!, Please Retry!!")
        else:
            break

    run = True
    while run:
        if user_task_number != -1: # Code below will run if the user does not choose to go back/exit
            # if user has selected a task
            print(f"\nYou have selected to edit Task {user_task_number}")
            print("\nPlease select 1 of the options below.\n\n1 - Mark the task as complete.\n2 - Edit the task.")

            # Asking the user to select whether to mark or edit one of their task
            user_choice = int(input("\nEnter either 1 or 2.\nEnter your option here: "))

            # If the user has chosen to mark their task complete
            if user_choice == 1:
                file15 = open('tasks.txt','r').readlines()
                file16 = [line.split(',') for line in file15]
                
                if (file16[user_task_number][4]) == 'Yes':
                    print("Task is Already marked complete!!!\n")
                    break
                    
                task_status = input("\nIs the task complete? (y/n): ")
                
                # Updating the selected line in the file to mark the task complete
                if task_status.lower() == 'y':
                    task_lines = open('tasks.txt', 'r').readlines()
                    exact_task_number = user_task_number
                    split_line = task_lines[exact_task_number].split(',') # Splitting the line aligned to the selected task
                    split_line[4] = 'Yes'
                    
                    
                    # Lambda function to turn list into string so we can write to the file
                    list_to_string = lambda a, str1='' + ',': str1.join(a)
                    new_string = list_to_string(split_line)

                    # Writing the updated file line to our text file
                    replace_line('tasks.txt', exact_task_number, new_string)
                    print("\nTask has been marked complete!")
                    

            # Code block for changing the task due date and/or user task is assigned to
            elif user_choice == 2:
                # First checking if the selected is not yet marked complete
                task_lines = open('tasks.txt', 'r').readlines()
                split_line = task_lines[user_task_number].split(',')
                if 'yes' in split_line or 'Yes' in split_line: # Checking if task is not yet completed
                    print("\nALERT!!! Task is marked complete hence cannot be edited!")
                    break

                # If task is not marked complete then user can move forward to edit it
                elif 'yes' not in split_line or 'Yes' not in split_line:
                    print("\nWhat part of the task would you like to change?") # Asking the user to enter a part of the task they would like to alter
                    print("N - Username to whom task is assigned\nD - Due Date\nB - Both")
                    user_answer = input("\nEnter your answer here: ")

                    if user_answer.lower() == 'n':  # Code block for changing the username
                        new_task_username = input("Enter the new Username here: ")

                        # Updating the selected line in the file to change the username to which the task is assigned to
                        task_lines = open('tasks.txt', 'r').readlines()
                        exact_task_number = user_task_number
                        split_line = task_lines[exact_task_number].split(',')
                        split_line[0] = new_task_username

                        # Lambda function to turn list into string so we can write to the file
                        list_to_string = lambda a, str1='' + ',': str1.join(a)
                        new_string = list_to_string(split_line) # Convrting list into a string

                        # Writing the updated file line to our text file(replacing the old username with the new one)
                        replace_line('tasks.txt', exact_task_number, new_string)
                        print("\nThe username has been changed successfully")
                        break

                    elif user_answer.lower() == 'd':  # Code block for changing the Due date
                        new_due_date = input("\nEnter the new Due Date here(dd/mm/yyyy): ")

                        # Updating the selected line in the file to change the username to which the task is assigned to
                        task_lines = open('tasks.txt', 'r').readlines() # Opening the task.txt file
                        exact_task_number = user_task_number
                        split_line = task_lines[exact_task_number].split(',')
                        # noinspection PyUnboundLocalVariable
                        split_line[3] = new_due_date
                        
                        # Lambda function to turn list into string so we can write to the file
                        list_to_string = lambda a, str1='' + ',': str1.join(a)
                        new_string = list_to_string(split_line) # Convrting list into a string so we may write to the txt file

                        # Writing the updated file line to our text file( replacing the old username with the new one
                        replace_line('tasks.txt', exact_task_number, new_string)
                        print("\nThe Task due date has been changed successfully")
                        break

                    # If the user selects to change both due date and user task is assigned to
                    elif user_answer.lower() == 'b':

                        # Code below is for changing the username to whom a task is assigned to
                        new_task_username = input("Enter the new Username here: ")

                        # Updating the selected line in the file to change the username to which the task is assigned to
                        task_lines = open('tasks.txt', 'r').readlines()
                        exact_task_number = user_task_number
                        split_line = task_lines[exact_task_number].split(',')
                        split_line[0] = new_task_username

                        # Lambda function to turn list into string so we can write to the file
                        list_to_string = lambda a, str1='' + ',': str1.join(a)
                        new_string = list_to_string(split_line) # Convrting list into a string

                        # Writing the updated file line to our text file(replacing the old username with the new one)
                        replace_line('tasks.txt', exact_task_number, new_string)
                        print("\nThe username has been changed successfully")
                        
                        # Code below is for changing the due date of the selected task
                        new_due_date = input("\nEnter the new Due Date here(dd/mm/yyyy): ")
                        
                        # Updating the selected line in the file to change the username to which the task is assigned to
                        task_lines = open('tasks.txt', 'r').readlines() # Opening the task.txt file
                        exact_task_number = user_task_number
                        split_line = task_lines[exact_task_number].split(',')
                        # noinspection PyUnboundLocalVariable
                        split_line[3] = new_due_date
                        
                        # Lambda function to turn list into string so we can write to the file
                        list_to_string = lambda a, str1='' + ',': str1.join(a)
                        new_string = list_to_string(split_line) # Convrting list into a string so we may write to the txt file

                        # Writing the updated file line to our text file( replacing the old username with the new one
                        replace_line('tasks.txt', exact_task_number, new_string)
                        print("\nThe Task due date has been changed successfully")
                        print("\nThe Task due date has been changed successfully")
                        break
                        
                    else:
                        print("\nInvalid Input!!! Please read the programs prompts carefully!") # Error catch - If user enters invalid input
                else:
                    print("Invalid input!! Please enter a Valid number or option") # Error catch - If user enters invalid input
                    
            else:
                print("Invalid input!! Please enter a Valid number or option") # Error catch - If user enters invalid input
        

#############################################|| STATISTICS SECTION ||####################################
# noinspection PyUnusedLocal
def admin_stats(): # Function to calculate and display stats
    
    # Calculating the number of the tasks
    task_counter = 0
    file = open('tasks.txt', 'r')
    for line in file:
        task_counter += 1
    file.close()

    # Calculating the number of users
    user_counter = 0
    file = open('user.txt', 'r')
    for line in file:
        user_counter += 1
    file.close()

    # Printing out the statistics
    print("\nWelcome Admin! the statistics are as follows:\n")
    print(f"The total number of the registered users is: {user_counter}")
    print(f"The total number of the tasks is: {task_counter}")

# A Function that generates reports linked to tasks
# noinspection PyUnusedLocal
def generate_task_reports():
    # Counting the tasks
    task_lines = open('tasks.txt', 'r').readlines()
    tasks_counter = len([line for line in task_lines])
    
    # Writing the tasks total to the task_overview.txt file
    out = open('task_overview.txt', 'w')
    out.write(f"tasks, {str(tasks_counter)}")
    out.close()

    # Counting the completed tasks
    completed_task_counter = 0
    comp_task = open('tasks.txt', 'r').readlines()
    split_lines = [line.split(',') for line in comp_task if 'Yes' in line] # Collecting all completed tasks
    completed_task_counter = len([line for line in split_lines])

    # Writing the completed tasks total to the task_overview.txt file
    with open('task_overview.txt', 'a') as out_file:
        out_file.write(f"\ncompleted task, {str(completed_task_counter)}")
    
    # Counting the incomplete tasks
    comp_task2 = open('tasks.txt', 'r').readlines()
    split_lines = [line.split(',') for line in comp_task2 if 'No' in line] # Collecting all incomplete tasks
    incomplete_task_counter = len([line for line in split_lines])

    # Writing the incomplete tasks total to the task_overview.txt file
    with open('task_overview.txt', 'a') as out2:
        out2.write(f"\nincomplete task, {str(incomplete_task_counter)}")

    # Calculating the number of tasks that haven't been completed and are overdue
    today = str(date.today()) # Getting current date and turning it into a string

    # Collecting all incomplete tasks
    comp_task2 = open('tasks.txt', 'r').readlines()
    split_line2 = [line.split(',') for line in comp_task2 if 'No' in line] 

    # Counting the tasks that are due
    due_tasks_counter = len([task for task in split_line2 if task[3] < today])

    # Writing overdue tasks to the file task_overview
    with open('task_overview.txt', 'a') as out3:    
        out3.write(f"\ndue tasks, {str(due_tasks_counter)}")
    
    # Calculating the percentage of tasks that are incomplete
    task_perc = open('task_overview.txt', 'r').readlines() # Opening the tasks overview file
    split_line4 = [line.split(',') for line in task_perc] # Splitting the lines in tasks overview .txt
    all_tasks = [line[1] for line in split_line4 if line[0] == 'tasks'] # Splitting the lines in tasks overview further
    all_tasks = int(all_tasks[0]) # Collecting number of tasks
    incomplete_tasks = [line[1] for line in split_line4 if line[0] == 'incomplete task'] # Collecting incomplete tasks
    incomplete_tasks = int(incomplete_tasks[0]) # Collecting the actual number of incomplete tasks 
    incomplete_task_percentage = ((incomplete_tasks * all_tasks) / 100) # Calculating percentage of incomplete tasks
    incomplete_task_percentage = round(incomplete_task_percentage, 2) # Rounding off the total to 2 decimal places

    # Writing the percentage of the tasks that are incomplete to the task_overview.txt file
    with open('task_overview.txt', 'a') as out4:
        out4.write(f"\nincomplete task percentage, {str(incomplete_task_percentage)}")

    # Calculating the percentage of tasks that are due
    task_perc = open('task_overview.txt', 'r').readlines() # Opening the tasks overview file
    split_line5 = [line.split(',') for line in task_perc] # Splitting lines in tasks overview
    all_tasks = [line[1] for line in split_line5 if line[0] == 'tasks'] # Looking for a "tasks" heading so we can find number of tasks
    all_tasks = int(all_tasks[0]) # Assigning number of tasks to the variable all-tasks
    due_tasks = [line[1] for line in split_line5 if line[0] == 'due tasks'] # Looking for a "tasks" heading so we can find number of tasks
    due_tasks = int(due_tasks[0]) # Assigning number of due tasks to the variable due_tasks
    due_task_percentage = ((due_tasks * incomplete_tasks) / 100) # Now calculating percentage of due tasks
    due_task_percentage = round(due_task_percentage, 2) # Rounding off the total to 2 decimal places

    # Writing the percentage of the tasks that are incomplete to the task-overview.txr file
    with open('task_overview.txt', 'a') as out5:
        out5.write(f"\ndue task percentage, {str(due_task_percentage)}")

    # Printing out results from the tasks_overview file
    print(f"\nTotal tasks: {str(tasks_counter)}")
    print(f"\nTotal of completed tasks: {str(completed_task_counter)}")
    print(f"\nIncomplete Tasks: {str(incomplete_task_counter)}")
    print(f"\nTotal of Due Tasks: {str(due_tasks_counter)}")
    print(f"\nIncomplete Tasks Percentage: {str(incomplete_task_percentage)}%")
    print(f"\nDue Tasks Percentage: {str(due_task_percentage)}%")

# Function to generate reports linked to users
def generate_user_reports():
    with open('user_overview.txt', 'w+'): # Line to ensure file is overwriten everytime code is run
        
        #=====================================================================================
        # Counting the total of tasks
        with open('tasks.txt', 'r') as num_tasks:
            total_task = len([line for line in num_tasks]) 

        # Adding total users to the user_overview txt file
        with open('user_overview.txt', 'a') as file:
            file.write(f"Total Users,{total_task}")

        #=======================================================================================  
        def total_tasks_per_user(): # Function to calculate total tasks per user
            with open('tasks.txt', 'r') as file:
                name_holder = [line.split(',')[0] for line in file]

                num_tasks_per_user = []

                for i in range(len(name_holder)):
                    track = (f"\nTotal Tasks Assigned To,{name_holder[i]},{name_holder.count(name_holder[i])}")
                    if track not in num_tasks_per_user:
                        num_tasks_per_user.append(track)
            
        #-----------------------------------------------------------------------------------------
                        # Adding number of tasks assigned to user to the user_overview.txt
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)
        total_tasks_per_user()
                            
        #=========================================================================================
        def percentage_tasks_assigned_user(): # Function to calculate percentage of tasks assigned to each user
            # Retrieving all names so we can count their occurrence thus determining tasks assigned to each user
            with open('tasks.txt', 'r') as file:
                name_holder = [line.split(',')[0] for line in file] 

                num_tasks_per_user = [] # This variable is declared so that we don't print duplicate lines

                for num in range(len(name_holder)):
                    track = (f"\nTotal Percentage of Tasks Assigned To,{name_holder[num]},{int((name_holder.count(name_holder[num]) * 100) / total_task)}%")
                    if track not in num_tasks_per_user: # Ensuring we don't have duplicate lines
                        num_tasks_per_user.append(track)
                        
        #------------------------------------------------------------------------------------------
                        # Adding number of tasks assigned to user to the user_overview.txt
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)
        percentage_tasks_assigned_user()
        
        #===========================================================================================
        def percentage_comp_tasks_assigned_user(): # Function to calculate percentage of completed tasks
            # Retrieving all names so we can count their occurrence thus determining tasks assigned to each user
            with open('tasks.txt', 'r') as file:
                name_holder = [line.split(',')[0] for line in file]

                # Retrieving names linked to complete tasks so we can count their occurrence thus determining Percentage of Complete tasks assigned to user
                with open('tasks.txt', 'r') as file2:
                    user_complete_task = [line.split(',')[0] for line in file2 if line.split(',')[4] == 'Yes']

                num_tasks_per_user = [] # This variable is declared so that we don't print duplicate lines
                for num in range(len(user_complete_task)):
                    track = (f"\nTotal Percentage of Complete Tasks Assigned To,{user_complete_task[num]},{int((user_complete_task.count(user_complete_task[num]) * 100) / name_holder.count(user_complete_task[num]))}%")
                    
                    if track not in num_tasks_per_user: # Ensuring we don't have duplicate lines
                        num_tasks_per_user.append(track)
        #------------------------------------------------------------------------------------------
                        # Adding number of tasks assigned to user to the user_overview.txt
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)
        percentage_comp_tasks_assigned_user()                   
        #==========================================================================================
        def percentage_incomp_tasks_assigned_user(): # Function to calculate percentage of incomplete tasks assigned per user
            # Retrieving all names so we can count their occurrence thus determining tasks assigned to each user
            with open('tasks.txt', 'r') as file:
                name_holder = [line.split(',')[0] for line in file] # This line gives us number of tasks assigned to each user

                # Retrieving names linked to complete tasks so we can count their occurrence thus determining Percentage of inomplete tasks assigned to user
                with open('tasks.txt', 'r') as file2:
                    user_incomplete_task = [line.split(',')[0] for line in file2 if line.split(',')[4] == 'No']

                num_tasks_per_user = [] # This variable is declared so we eradicate duplicate lines
                for num in range(len(user_incomplete_task)):
                    track = (f"\nTotal Percentage of Incomplete Tasks Assigned To,{user_incomplete_task[num]},{int((user_incomplete_task.count(user_incomplete_task[num]) * 100) / name_holder.count(user_incomplete_task[num]))}%")
                    
                    if track not in num_tasks_per_user: # Ensuring we don't have duplicate lines
                        num_tasks_per_user.append(track)
        #------------------------------------------------------------------------------------------
                        # Adding number of tasks assigned to user to the user_overview.txt
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)
        percentage_incomp_tasks_assigned_user()
        
        #==========================================================================================
        def percentage_incomp_due_tasks_assigned_user(): # Function to calculate percentage of incomplete due tasks assigned per user
            # Retrieving all names so we can count their occurrence thus determining tasks assigned to each user
            with open('tasks.txt', 'r') as file:
                name_holder = [line.split(',')[0] for line in file] # This line gives us number of tasks assigned to each user

                # Retrieving names linked to incomplete due tasks so we can count their occurrence thus determining Percentage of inomplete tasks assigned to user
                with open('tasks.txt', 'r') as file2:
                    user_incomplete_task = [line.split(',')[0] for line in file2 if line.split(',')[4] == 'No' and line.split(',')[3] < str(date.today())]

                num_tasks_per_user = [] # This variable is declared so we eradicate duplicate lines
                for num in range(len(user_incomplete_task)):
                    track = (f"\nTotal Percentage of Incomplete Due Tasks Assigned To,{user_incomplete_task[num]},{int((user_incomplete_task.count(user_incomplete_task[num]) * 100) / name_holder.count(user_incomplete_task[num]))}%")
                    
                    if track not in num_tasks_per_user: # Ensuring we don't have duplicate lines
                        num_tasks_per_user.append(track)

        #------------------------------------------------------------------------------------------
                        # Adding number of tasks assigned to user to the user_overview.txt
                        with open('user_overview.txt', 'a') as file2:
                            file2.write(track)
    percentage_incomp_due_tasks_assigned_user()
generate_user_reports() # Executing the function for generating reports
#===================================================================================================

# Function to display reports in a user-friendly way
def display_reports():
    with open('user_overview.txt', 'r') as file:
        splitted_info = [line.split(',') for line in file] # Splitting data so we may be able to use specific parts

        print("=================================================================================================================")
        print("   DESCRIPTION                               ||        NAME                   ||            INFO                   ")
        print("============================================ ||===============================||=================================")
        for line in splitted_info:
            if line[0] == 'Total Users': # Printing out Total Users
                print(f"Total Users                                 ||             N\A                            {line[1]}")
                print("____________________________________________||________________________________||_______________________________")
                
            elif line[0] == 'Total Tasks Assigned To': # Printing out Total Tasks per user
                print(f"Total Number of Tasks Assigned To           ||            {line[1]}                            {line[2]}")
                print("____________________________________________||________________________________||_________________________________")
        print()
        print("==================================================================================================================")
        for line in splitted_info:
            if line[0] == 'Total Percentage of Tasks Assigned To': # Printing out Total Percentage of Tasks
                print(f"Percentage of Tasks Assigned To              ||             {line[1]}                            {line[2]}")
                print("_____________________________________________||_________________________________||_______________________________")
                
        print()
        print("=================================================================================================================")
        for line in splitted_info: # Printing out Total Percentage of Complete Tasks per user
            if line[0] == 'Total Percentage of Complete Tasks Assigned To':
                print(f"Percentage of Complete Tasks Assigned To      ||            {line[1]}                            {line[2]}")
                print("______________________________________________||________________________________||________________________________")

        print()
        print("==================================================================================================================")
        for line in splitted_info: # Printing out Total Percentage of Incomplete Tasks per user
            if line[0] == 'Total Percentage of Incomplete Tasks Assigned To':
                print(f"Percentage of Inomplete Tasks Assigned To      ||            {line[1]}                            {line[2]}")
                print("_______________________________________________||_______________________________||________________________________")

        print()
        print("==================================================================================================================")
        for line in splitted_info: # Printing out Total Percentage of Incomplete Due Tasks per user
            if line[0] == 'Total Percentage of Incomplete Due Tasks Assigned To':
                print(f"Percentage of Incomplete Due Tasks Assigned To ||            {line[1]}                            {line[2]}")
                print("_______________________________________________||_______________________________||________________________________||")
                

   # PROGRAM LOGIC SECTION

# Asking user to log in, program will only allow user to proceed only if the credentials are valid

cred_check()  # Calling the credential validity checker function inorder to ensure entered credentials are correct
print("\nLogin Successful!")
print(' ') # Blank space

go_on = True

while go_on:

    # Printing out the welcome message
    print("\n||======================| TASK MANAGER |======================||")

    # Printing out the Main Menu
    print("Please select one of the following options:\n")
    if user_name == 'admin,': # Ensuring that the priviledge to register user is given to the admin only
        print("r  - register user")
    print("a  - add task")
    print("va - view all tasks")
    print("vm - view my tasks")
    if user_name == 'admin,': # Ensuring that the priviledge to generate reports is given to the admin only
        print("gr - generate reports")
    if user_name == 'admin,': # Ensuring that the priviledge to view stats is given to the admin only
        print("vs - view statistics")
    print("e  - exit")

    # Asking the user to select an option
    print()
    user_option = input("\nEnter your option here: ")
    user_option = user_option.lower()

    # If user option is register user
    if user_option == 'r':
        if user_name == 'admin,':  # Ensuring that the priviledge to register users is given to the admin only
            create_user()

    # If user option is to add a task
    if user_option == 'a':
        add_task()

    # if user option is to view all task
    if user_option == 'va':
        view_all_tasks()

    # If user option is to view their task
    if user_option == 'vm':
        view_my_task()

    # If user option is to view statistics
    if user_option == 'vs':
        if user_name == 'admin,':
            admin_stats() # Ensuring that the priviledge to view stats is given to the admin only

    # If user option is to view statistics
    if user_option == 'gr':
        if user_name == 'admin,': # Ensuring that the priviledge to generate reports is given to the admin only
            display_reports()
            

    # If user option is to exit
    if user_option == 'e':
        go_on = False
print("\nThank you for using our program :)")
print("\nBye!")
