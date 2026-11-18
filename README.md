 My Study Tracke

 What Is This Project About?

My Study Tracker is a simple, interactive command-line application built with Python. I created it to help students organize their coursework by breaking big subjects down into smaller, manageable study topics. Instead of guessing how much work is left, users can log their subjects, check off completed topics, and immediately see their study progress.
 How It Works

The program runs inside a continuous loop in the terminal and gives the user a numbered menu with six options:

1. **Add Subject:** Prompts the user for a subject name and creates a new entry for it.
2. **Show Subject:** Displays all current subjects and their nested topics in the terminal.
3. **Add Topic:** Lets the user assign a new study topic to an existing subject, automatically setting its completion status to `False`.
4. **Mark a Topic as Complete:** Checks if the subject and topic exist, then updates the topic's status to `True`.
5. **Show Progress:** Calculates the percentage of completed topics for each subject and draws a 10-block visual progress bar (`█` for completed, `░` for remaining).
6. **Exit:** Breaks the loop and closes the program cleanly.
## 💡 What I Learned

Building this project helped me strengthen several core Python concepts:

- **Nested Data Structures:** I learned how to store, access, and update dictionaries inside other dictionaries to represent subjects and their individual topics.
- **Functions & Modular Code:** Breaking the menu choices into separate functions (`Add_subjects()`, `Add_topic()`, `show_progress()`, etc.) made the program much cleaner and easier to debug.
- **Loops & Conditional Logic:** I practiced using `while True` loops for interactive menus, `for` loops to count completed tasks, and `if/else` statements to verify that a subject or topic exists before modifying it.
- **String Manipulation & Formatting:** Creating the visual progress bar (`"█" * filled + "░" * empty`) and formatting percentages taught me how to turn raw numbers into readable terminal output.
