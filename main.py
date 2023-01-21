score = 0
#Welcome Message
print("Welcome To Mini Quiz v1!")

playing = input("Would You Like To Play? ")

#isPlaying Input Variable
if playing == "Yes":
  print("Ok, Let's Get Started.")
else:
  if playing == "yes":
    print("Ok, Let's Get Started.")

#isNotPlaying Input Variable
if playing == "No":
  print("Ok, Come Back When You're Ready.")
  quit()
else:
  if playing == "no":
    print("Ok, Come Back When You're Ready.")
    quit()

#Question 1
answer = input("What Is 10 X 10? ")
if answer == "100":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 2
answer = input("What's the name of the river that runs through Egypt? ")
if answer == "The Nile River":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")

#Question 3
answer = input("How Many Days Are In A Week? ")
if answer == "7":
  print('Correct!')
  score = score + 1
  
else:
  print("Incorrect!")
#debug
#Question 4
answer = input("What Is The Fastest Land Animal? ")
if answer == " A Cheetah":
  print('Correct!')
  score = score + 1
else:
  if answer == "a cheetah":
    print("Correct!")
    score = score +1
  else:
    print("Incorrect!")

#Question 5
answer = input("What Does PC Stand For(Computer Wise)? ")
if answer == "Personal Computer":
  print('Correct!')
  score = score + 1
else:
  if answer == "personal Computer":
    print("Correct!")
    score = score +1
  else:
    print("Incorrect!")

#Question 6
answer = input("What Is A Normal #2 Pencil Made Of? ")
if answer == "Wood":
  print('Correct!')
  score = score + 1
else:
  if answer == "wood":
    print("Correct!")
    score = score +1
  else:
    print("Incorrect!")

#Question 7
answer = input("Is Normal Poop Brown? ")
if answer == "Yes":
  print('Correct!')
  score = score + 1
else:
  if answer == "yes":
    print("Correct!")
    score = score +1
  else:
    print("Incorrect!")

#Question 8
answer = input("Does Pineapple Belong On Pizza? ")
if answer == "No":
  print('Correct!')
  score = score + 1
else:
  if answer == "no":
    print("Correct!")
    score = score +1
  else:
    print("Incorrect!")

#Question 9
answer = input("What is the name of the Earth's largest ocean? ")
if answer == "The Pacific Ocean":
  print("Correct!")
  score = score +1
else:
  print("Incorrect!")

#Question 10
answer = input("Are avacados a fruit or a vegetable? ")
if answer == "a fruit":
  print("Correct!")
  score = score +1
else:
  if answer == "A Fruit":
    print("Correct!")
    score = score +1
  else:
    print("Incorrect!")

if score > 5:
    print("Congratulations! You Passed This Quiz With A Score Of: ", print(score, "/10"))

if score < 5:
  print("I'm Sorry, You Failed This Quiz With A Score Of: ", print(score))
