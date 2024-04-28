import turtle
import random
import time
from data import *

# Initialize the screen
screen = turtle.Screen()
screen.setup(width=1200, height=800)
screen.bgcolor("Black")

language_scores = {
    'Python': {'correct': 0, 'incorrect': 0},
    'C++': {'correct': 0, 'incorrect': 0},
    'Java': {'correct': 0, 'incorrect': 0}
}

current_correct = 0
current_incorrect = 0

score = 0

option_buttons = []  # This will hold tuples of (button_turtle, option_text_turtle)

def python_click(x, y):
    show_lesson('Python')

def cpp_click(x, y):
    show_lesson('C++')

def java_click(x, y):
    show_lesson('Java')

def back_click(x, y):
    show_home()

def create_button(label, x, y, button_function, color, text_color="misty rose", shape='square', size=(2, 8)):
    button_turtle = turtle.Turtle()
    button_turtle.hideturtle()
    button_turtle.speed('fast')
    button_turtle.penup()
    button_turtle.goto(x, y)
    button_turtle.shape(shape)
    button_turtle.color(color)
    button_turtle.shapesize(stretch_wid=size[0], stretch_len=size[1])
    button_turtle.onclick(button_function)
    button_turtle.showturtle()
    label_turtle = turtle.Turtle()
    label_turtle.hideturtle()
    label_turtle.speed('fast')
    label_turtle.penup()
    label_turtle.goto(x, y - 10)
    label_turtle.color(text_color)
    label_turtle.write(label, align='center', font=('Comic Sans MS', 11, 'bold'))

def clear_screen():
    for turtle_obj in screen.turtles():
        turtle_obj.hideturtle()
    screen.clear()
    screen.bgcolor("Black")  # Reset the background color after clearing

def draw_title(title):
    title_turtle = turtle.Turtle()
    title_turtle.hideturtle()
    title_turtle.penup()
    title_turtle.color("misty rose")
    title_turtle.goto(0, 350)
    title_turtle.write(title, align='center', font=('Comic Sans MS', 24, 'bold'))

def create_data_type_button(language, label, x, y, color):
    button_turtle = turtle.Turtle()
    button_turtle.hideturtle()
    button_turtle.speed('fast')
    button_turtle.penup()
    button_turtle.goto(x, y)
    button_turtle.shape('square')
    button_turtle.color(color)
    button_turtle.shapesize(stretch_wid=1, stretch_len=6)

    # Use the updated function to handle clicks, passing the current language and data type label
    button_turtle.onclick(get_data_type_handler(language, label))

    button_turtle.showturtle()

    label_turtle = turtle.Turtle()
    label_turtle.hideturtle()
    label_turtle.speed('fastest')
    label_turtle.penup()
    label_turtle.goto(x, y - 10)
    label_turtle.color("misty rose")
    label_turtle.write(label, align='center', font=('Comic Sans MS', 10, 'bold'))

    data_type_buttons.append(button_turtle)
    data_type_labels.append(label_turtle)
    return button_turtle

# Modify this function to pass language and data type
def get_data_type_handler(language, data_type):
    def handler(x, y):
        show_data_type_description(language, data_type)
    return handler

def show_data_type_description(language, data_type):
    clear_screen()
    draw_title(f'{language} - {data_type} Description')

    description = data_type_descriptions[language][data_type]
    description_turtle = turtle.Turtle()
    description_turtle.hideturtle()
    description_turtle.penup()
    description_turtle.color("misty rose")
    description_turtle.goto(0, 0)
    description_turtle.write(description, align="center", font=("Comic Sans MS", 15, "normal"))

    # Clear previous buttons
    clear_data_type_buttons()

    # Add a 'Start Quiz' button that will start the quiz for this data type
    create_button('Start Quiz', 0, -100, get_quiz_start_handler(language, data_type), "dodger blue")

    # Back button to return to the data type selection
    create_button('Back to Data Types', 0, -200, get_back_to_data_types_handler(language), "cadet blue")

def get_quiz_start_handler(language, data_type):
    def handler(x, y):
        start_quiz(language, data_type)
    return handler

def start_quiz(language, data_type):
    global current_correct, current_incorrect
    current_correct = 0
    current_incorrect = 0
    # Reset each question's answered state
    for question in quiz_questions[language][data_type]:
        question['answered'] = False
    show_quiz_question(language, data_type, 0)


def clear_data_type_buttons():
    global data_type_buttons, data_type_labels
    # Hide all data type buttons and labels
    for btn in data_type_buttons:
        btn.hideturtle()
    for lbl in data_type_labels:
        lbl.hideturtle()
    # Clear the lists
    data_type_buttons = []
    data_type_labels = []

def get_back_to_data_types_handler(language):
    # Returns a handler that calls show_lesson for the given language
    def handler(x, y):
        show_lesson(language)
    return handler

# Function to handle the click on a data type button
def on_data_type_click(data_type):
    print(f"You clicked on data type: {data_type}")

back_button_colors = {
    'Python': 'magenta',
    'C++': 'medium orchid',
    'Java': 'blue violet',
}
# Update the show_lesson function to use the new data type button creation
def show_lesson(language):
    clear_screen()
    draw_title(f'{language} - Data Types')
    # Display the cumulative score for the language
    score_display = f"Total Correct: {language_scores[language]['correct']}, Total Incorrect: {language_scores[language]['incorrect']}"
    score_turtle = turtle.Turtle()
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("medium slate blue")
    score_turtle.goto(-550, 300)  # Adjust position as needed
    score_turtle.write(score_display, align="left", font=("Comic Sans MS", 12, "normal"))
    # Proceed to create buttons for data types

    # Reset the lists for new buttons and labels
    global data_type_buttons, data_type_labels
    data_type_buttons.clear()
    data_type_labels.clear()

    data_type_colors = {
        'Python': 'magenta',
        'C++': 'medium orchid',
        'Java': 'blue violet',
    }

    y_position = 100
    for data_type in data_types[language]:
        color = data_type_colors.get(language, 'grey')
        create_data_type_button(language, data_type, 0, y_position, color)
        y_position -= 50  # Adjust the y_position for the next button

    # Back button to return to main menu
    back_button_color = back_button_colors.get(language, "gray")  # Default to gray if not found
    create_button('Back to Menu', 0, -300, get_back_click_handler(), back_button_color)

# Function to create a back button click handler
def get_back_click_handler():
    # """Return a handler function that, when called, returns the user to the home screen."""
    def handler(x, y):
        clear_screen()
        show_home()
    return handler

data_type_buttons = []  # List to keep track of data type button turtles
data_type_labels = []  # List to keep track of data type label turtles

def on_back_click(x, y):
    show_home()
    # Clear data type buttons and labels when going back
    for btn in data_type_buttons:
        btn.clear()
        btn.hideturtle()
    for lbl in data_type_labels:
        lbl.clear()
        lbl.hideturtle()
    data_type_buttons.clear()
    data_type_labels.clear()

def show_home():
    screen.clear()  # Clear any previous settings
    screen.bgcolor("Black")
    draw_title('Programming Crash Course')
    # Setup buttons
    create_button('Python', -200, 0, python_click, "magenta")
    create_button('C++', 0, 0, cpp_click, "medium orchid")
    create_button('Java', 200, 0, java_click, "blue violet")

def exit_program(x, y):
    turtle.bye()

def create_exit_button():
    exit_button = turtle.Turtle()
    exit_button.penup()
    exit_button.shape("circle")  # Makes the turtle shape a circle
    exit_button.shapesize(3, 3)  # Makes the turtle shape half the size
    exit_button.color("red")  # Red color to indicate it's a stop button
    exit_button.goto(550, -350)  # Position the button at the bottom right corner
    exit_button.onclick(exit_program)  # Bind the exit function to the button click
    exit_button.showturtle()

    exit_label = turtle.Turtle()
    exit_label.hideturtle()
    exit_label.penup()
    exit_label.goto(550, -360)  # Position the label below the button
    exit_label.write("End", align="center", font=("Arial", 12, "normal"))


# Inside the show_quiz_question function, reset this list
def show_quiz_question(language, data_type, question_index):
    global option_buttons
    option_buttons.clear()
    clear_screen()
    draw_title(f'{language} - {data_type} Quiz')
    question_info = quiz_questions[language][data_type][question_index]

    # Display the question
    question_turtle = turtle.Turtle()
    question_turtle.hideturtle()
    question_turtle.penup()
    question_turtle.color("misty rose")
    question_turtle.goto(0, 100)
    question_turtle.write(question_info["question"], align="center", font=("Comic Sans MS", 16, "normal"))
    question_turtle.goto(0, 50)  # Position the options below the question

    # Display the options as buttons
    y_position = 0
    for i, option in enumerate(question_info["options"]):
        y_position = -50 * (i + 1)
        create_option_button(option, -100, y_position, language, data_type, question_index, i)

def create_option_button(option, x, y, language, data_type, question_index, option_index):
    button_turtle = turtle.Turtle()
    button_turtle.penup()
    button_turtle.hideturtle()
    button_turtle.goto(x, y)
    button_turtle.shape('square')
    button_turtle.color('powder blue')
    button_turtle.shapesize(stretch_wid=2, stretch_len=8)
    button_turtle.showturtle()

    # This function handles button clicks, only allowing one click per question
    def button_click(x, y):
        # Access the quiz_questions directly
        if not quiz_questions[language][data_type][question_index].get('answered', False):
            option_click_handler(option, language, data_type, question_index, option_index)
            quiz_questions[language][data_type][question_index]['answered'] = True  # Mark as answered
            disable_option_buttons()

    button_turtle.onclick(button_click)

    option_text_turtle = turtle.Turtle()
    option_text_turtle.hideturtle()
    option_text_turtle.penup()
    option_text_turtle.goto(x, y - 10)
    option_text_turtle.color("dark blue")
    option_text_turtle.write(option, align="center", font=("Comic Sans MS", 10, "normal"))

    option_buttons.append((button_turtle, option_text_turtle))

    return button_turtle, option_text_turtle

def disable_option_buttons():
    """Disable all option buttons to prevent re-answering."""
    for button_turtle, _ in option_buttons:
        button_turtle.onclick(None)  # Remove the click event handler


def setup_timer_handler(correct, language, data_type, question_index):
    def timer_handler():
        clear_feedback_and_proceed(correct, language, data_type, question_index)
    return timer_handler

def clear_feedback_and_proceed(correct, language, data_type, question_index):
    """Clear feedback and decide the next step based on the correctness of the answer."""
    feedback_turtle.clear()  # Clear the feedback message only
    if correct:
        proceed_to_next_question(language, data_type, question_index)
    # Do not reload or clear the screen if the answer was incorrect, just wait for the next input

def get_next_question_handler(language, data_type, question_index):
    def handler(x, y):
        if question_index < len(quiz_questions[language][data_type]):
            show_quiz_question(language, data_type, question_index)
        else:
            show_final_score(language, data_type)
    return handler

def option_click_handler(selected_option, language, data_type, question_index, option_index):
    global current_correct, current_incorrect
    question_info = quiz_questions[language][data_type][question_index]
    correct = selected_option == question_info['answer']
    if correct:
        current_correct += 1
        language_scores[language]['correct'] += 1
        message = "Correct! Good job!"
    else:
        current_incorrect += 1
        language_scores[language]['incorrect'] += 1
        correct_answer = question_info['answer']
        message = f"Incorrect! The correct answer was '{correct_answer}'."
    show_feedback(message, correct, language, data_type, question_index)

# Initialize the feedback turtle
feedback_turtle = turtle.Turtle()
feedback_turtle.hideturtle()
feedback_turtle.penup()
feedback_turtle.color("red")
feedback_turtle.goto(200, -200)

def show_feedback(message, correct, language, data_type, question_index):
    # Hide all option buttons and clear the text
    for button, text in option_buttons:
        button.hideturtle()
        text.clear()  # This will clear the text of the option

    # Clear any existing feedback first
    feedback_turtle.clear()

    # Set the feedback color
    feedback_color = "cyan" if correct else "medium violet red"
    feedback_turtle.color(feedback_color)

    # Show the feedback message
    feedback_turtle.goto(0, -50)  # Adjust the position as needed
    feedback_turtle.write(message, align="center", font=("Comic Sans MS", 18, "bold"))

    # Setup the 'Next Question' button
    next_handler = get_next_question_handler(language, data_type, question_index + 1)
    create_button('Next Question', 0, -150, next_handler, "dodger blue", size=(1, 8))


def proceed_to_next_question(language, data_type, question_index):
    next_question_index = question_index
    if next_question_index < len(quiz_questions[language][data_type]):
        show_quiz_question(language, data_type, next_question_index)
    else:
        show_final_score(language, data_type)

def show_final_score(language, data_type):
    global current_correct, current_incorrect
    clear_screen()
    message = f"Quiz completed! Correct: {current_correct}, Incorrect: {current_incorrect}"
    feedback_turtle.goto(0, 0)
    feedback_turtle.color("medium slate blue")
    feedback_turtle.write(message, align="center", font=("Comic Sans MS", 24, "bold"))
    back_handler = get_back_to_data_types_handler(language)
    create_button('Back to Data Types', 0, -100, back_handler, "cadet blue")

# Ensure the program initializes correctly
show_home()
create_exit_button()
turtle.mainloop()