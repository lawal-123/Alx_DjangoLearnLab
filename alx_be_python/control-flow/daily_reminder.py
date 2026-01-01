task = input("enter your task: ")
priority = input("priority(high, medium, low): ")
time_bound = input("is it time-bound?(yes/no): ")
match priority:
    case "high":
        print(f"reminder: {task} is a high priority task that requires immediate attention today")
    case "low":
        print(f"{task} is a low priority task . consider completing it done when u're done today") 
if time_bound == "yes":
     print(f"reminder:(reminder)that requires immediate attention today!")
if time_bound == "no":
     print(f"{task} is a low priority task . consider completing it done when u're done today") 
else: 
    print("Invalid input for time-bound. Please enter yes or no.")


