# Function to generate a greeting message based on guest's details
def greet_guest(name, arrival_time, preference):
    # Determine the time of day
    if 0 < arrival_time <= 12:
        time_of_day = "morning"
    elif 13 <= arrival_time <= 18:
        time_of_day = "afternoon"
    elif 19 <= arrival_time <= 24:
        time_of_day = "evening"
    else:
        print(f"Invalid arrival time: {arrival_time} for {name}.")
        return

    # Customize greeting based on preference
    if preference == "formal":
        greeting = f"Good {time_of_day}, {name}. Welcome to the event!"
    else:
        greeting = f"Hey {name}, good {time_of_day}! Glad you could make it!"

    print(greeting)

# Function to greet all guests in a list
def greet_all_guests(guests):
    for guest in guests:
        name = guest['name']
        arrival_time = guest['arrival_time']
        preference = guest['preference']
        greet_guest(name, arrival_time, preference)

# Guest data
guests = [
    {"name": "James", "arrival_time": 11, "preference": "formal"},
    {"name": "Jacob", "arrival_time": 11, "preference": "formal"},
    {"name": "Benjamin", "arrival_time": 14, "preference": "informal"},
    {"name": "William", "arrival_time": 19, "preference": "formal"},
    {"name": "Alexander", "arrival_time": 20, "preference": "informal"},
]

# Greet all guests
greet_all_guests(guests)
