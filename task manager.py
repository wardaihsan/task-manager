subjects = {}

def Add_subjects():
    subject = input("Enter the subject you want to add: ")
    topics = {}
    subjects[subject] = topics
    print(f"You just added the subject {subject}")


def Add_topic():
    subject = input("Enter the subject for the topic: ")
    topic = input("Enter the topic: ")

    if subject in subjects:
        subjects[subject][topic] = False
        print(f"You added a new topic {topic} in {subject} now")
    else:
        print("This subject doesn't exist")


def show_subjects():
    print("-" * 50)
    print(" " * 15, subjects, " " * 15)
    print("-" * 50)


def mark_complete():
    subject = input("Enter the subject: ")
    topic = input("Enter the topic: ")

    if subject in subjects:
        if topic in subjects[subject]:
            subjects[subject][topic] = True
            print(f"{topic} has been marked as complete!")
        else:
            print("This topic is not in the tracker.")
    else:
        print("This subject doesn't exist.")


def show_progress():
    for subject, topics in subjects.items():
        total = 0
        completed = 0

        for topic, status in topics.items():
            total += 1

            if status == True:
                completed += 1

        if total > 0:
            percentage = (completed / total) * 100

            filled = round(percentage / 10)
            empty = 10 - filled

            bar = "█" * filled + "░" * empty

            print(f"{subject}: {bar} {percentage:.2f}%")

        else:
            print("You don't have any topics entered yet")


while True:
    print("-" * 50)
    print(" " * 15, "My Study Tracker", " " * 15)
    print("-" * 50)

    print("1.Add subject")
    print("2.show subject")
    print("3.Add topic")
    print("4.Mark a topic as complete")
    print("5.Show progress")
    print("6.Exit")

    choice = int(input("Enter your choice : "))

    if choice == 1:
        Add_subjects()
        show_subjects()

    elif choice == 2:
        print("you can now check the subjects")
        show_subjects()

    elif choice == 3:
        Add_topic()
        show_subjects()

    elif choice == 4:
        mark_complete()

    elif choice == 5:
        print("you can now see Your progress")
        show_progress()

    elif choice == 6:
        print("Goodbye")
        break

    else:
        print("Invalid input")