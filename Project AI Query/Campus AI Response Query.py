import datetime

# Dictionary to store course offerings per campus
course_offerings = {
    "Campus1": ["Course1", "Course2", "Course3"],
    "Campus2": ["Course4", "Course5", "Course6"],
    "Campus3": ["Course7", "Course8", "Course9"],
}

# Dictionary to store class times per subject
class_times = {
    "Subject1": "10:00 - 12:00",
    "Subject2": "13:00 - 15:00",
    "Subject3": "16:00 - 18:00",
}

# Dictionary to store test dates per subject
test_dates_dict = {
    "Subject1": "2023-03-01",
    "Subject2": "2023-03-02",
    "Subject3": "2023-03-03",
}

# Dictionary to store finance department contact details per campus
finance_contacts = {
    "Campus1": "Finance1@NGI",
    "Campus2": "Finance2@NGI",
    "Campus3": "Finance3@NGI",
}

# Dictionary to store certificate issue dates per campus
certificate_dates = {
    "Campus1": "2023-06-30",
    "Campus2": "2023-07-01",
    "Campus3": "2023-07-02",
}

def greet():
    # """Print a greeting message"""
    print("Hello! I am Sandra, your AI assistant.")

def how_are_you():
    # """Print a response to 'how are you?'"""
    print("I am a chatbot and I do not have feelings, but I'm ready to assist you with whatever you need.")

def help():
    # """Print a response to help question"""
    print("Here is a helpfull list of all my commands\n--greet\n--how are you\n--courses offered\n--class time\n--test date\n--finance\n--cerificate issue date")


def courses_offered():
    # """Ask the user for a campus and print courses offered at that campus"""
    campus = input("Please enter the campus: ").capitalize()
    if campus in course_offerings:
        print(f"Courses offered at {campus}:")
        for course in course_offerings[campus]:
            print(course)
    else:
        print(f"No courses offered at {campus}.")

def class_time():
    # """Print class time for a specific subject"""
    subject = input("Please enter the subject: ").capitalize()
    if subject in class_times:
        print(f"Class time for {subject}: {class_times[subject]}")
    else:
        print(f"No class time found for {subject}.")

def test_dates():
    # """Print test dates for a specific subject"""
    subject = input("Please enter the subject: ").capitalize()
    if subject in test_dates_dict:
        print(f"Test dates for {subject}: {test_dates_dict[subject]}")
    else:
        print(f"No test dates found for {subject}.")

def finance_info():
    # """Ask the user for a campus and print finance department contact details for that campus"""
    campus = input("Please enter the campus: ").capitalize()
    if campus in finance_contacts:
        print(f"Finance department contact details for {campus}: {finance_contacts[campus]}")
    else:
        print(f"No finance department contact details found for {campus}.")

def certificate_issue_date():
    # """Ask the user for a subject and print the certificate issue date"""
    subject = input("Please enter the Campus: ").capitalize()
    if subject in certificate_dates:
        print(f"Certificate issue date for {subject}: {certificate_dates[subject]}")
    else:
        print(f"No certificate issue date found for {subject}.")
    

def main():
    # """Main function to handle user input"""
    greet()
    while True:
        user_input = input("\nWhat would you like to know?\n(Type 'help' for all Sandra's Commands)\n(Type 'quit' to exit) ").lower()
        if user_input == "quit" or user_input == "q": 
            break
        elif user_input == "help":
            help()
        elif user_input == "hello":
            greet()
        elif user_input == "how are you":
            how_are_you()
        elif "courses offered" in user_input:
            courses_offered()
        elif "certificate issue date" in user_input:
            certificate_issue_date()
        elif "class time" in user_input:
            class_time()
        elif "test date" in user_input:
            test_dates()
        elif "finance" in user_input:
            finance_info()
        else:
            print("I'm sorry, I didn't understand that. Please try again.")
if __name__ == "__main__":
    main()