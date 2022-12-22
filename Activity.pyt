# Initialize the password
password = "jonz"

# Ask the user to enter their password
user_password = input("Enter your password: ")

# Check if the password is correct
if user_password == password:
  # Initialize the questions and answers
  my_questions = ["What is the capital of France?", "What is the largest planet in the solar system?", "What is the chemical symbol for sodium?", "Who invented the telephone?", "What is the atomic number of carbon?"]
  my_answers = ["Paris", "Jupiter", "Na", "Alexander Graham Bell", "6"]

  # Initialize the number of correct answers
  correct_answers = 0

  # Ask the user to answer the questions
  for i in range(len(my_questions)):
    user_answer = input(my_questions[i] + " ")
    if user_answer == my_answers[i]:
      correct_answers += 1

  # Display the number of correct answers
  print("Number of correct answers:", correct_answers)
else:
  # Ask the user to enter the first number, interval, and last number
  first_number = int(input("Enter first number: "))
  interval = int(input("Enter interval: "))
  last_number = int(input("Enter last number: "))

  # Display the numbers in the given range with the given interval
  for i in range(first_number, last_number+1, interval):
    print(i)