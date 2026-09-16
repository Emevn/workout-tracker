from datetime import date #importing the date module to get the current date

def show_menu(): # function to display main menu options
    print("\nWelcome to the Workout Tracker!")
    print("1. Log a new workout")
    print("2. View past workouts")
    print("3. Exit")

def get_number(prompt): # function to get a valid number input from the user
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number. Try again.")
            
            
def add_workout(): #function for inputs exercise, weight, sests, reps, and saves to workouts.txt
  
    print("--- New Workout ---")
    today = date.today() # gets the current date
    exercise = input("\nWhat exercise did you do? ")
    weight = get_number("How much weight did you use? ")
    sets = get_number("How many sets did you do? ")
    reps = get_number("How many reps did you do? ")
       
        
    print("\n--- Your Workout ---")
    today = date.today() # gets the current date 
    print(f"\nDate: {today}") # prints the current date in the format YYYY-MM-DD
    print(f"Exercise: {exercise}")
    print(f"Weight: {weight}")
    print(f"Sets: {sets}")
    print(f"Reps: {reps}")

    with open("workouts.txt", "a") as file: # saves the workout data to workouts.txt
        file.write(f"Date: {today} Exercise: {exercise}, Weight: {weight}, Sets: {sets}, Reps: {reps}\n")

def view_workouts(): # function to read and display past workouts from workouts.txt
    with open("workouts.txt", "r") as file:
        workouts = file.read()
        print("\n--- Past Workouts ---")
        print(workouts)
        
while True:        
    show_menu() # calls the show_menu function to display the main menu

    choice = input("Please select an option (1-3): ")  #gets user input for menu selection
    if choice == "1":
        add_workout()
    elif choice == "2":
        view_workouts()
    elif choice == "3":
        print("Thank you for using the Workout Tracker!")
        break
    else:
        print("Invalid option. Please try again.")
