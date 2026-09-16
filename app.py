print("Workout Tracker")
exercise = input("What exercise did you do? ")

while True:
    try:
        weight = int(input("How much weight did you use? "))
    except ValueError:
        print("Please enter a number. Try again.")
    else:break

while True:
    try:
        sets = int(input("How many sets did you do? "))
    except ValueError:
        print("Please enter a number. Try again.")
    else:
        break

while True:
    try:
        reps = int(input("How many reps did you do? "))
    except ValueError:
        print("Please enter a number. Try again.")
    else:
        break
    

print("\n--- Your Workout ---")
print(f"Exercise: {exercise}")
print(f"Weight: {weight}")
print(f"Sets: {sets}")
print(f"Reps: {reps}")

with open("workouts.txt", "a") as file:
    file.write(f"Exercise: {exercise}, Weight: {weight}, Sets: {sets}, Reps: {reps}\n")

