# PROGRAMMING PROJECT #
# Mathematics revision quiz #
import random
from guizero import App, TextBox, PushButton, Text, Window, ButtonGroup
import os

def SetLoginOrCreate():
   CheckLoginOrCreate.value = LoginOrCreate.value
   # obtains submitted value
   answer=str(CheckLoginOrCreate.value)
   # casts to string
   if "L" in answer:
      LoginGUI()
      # calls required subroutine depending on answer
   if "CA" in answer:
      CreateAccountGUI()


MathsQuiz=App(title="MathsQuiz", width=600, height=600)

StartPage = Window(MathsQuiz, width = 600, height = 600, layout = "grid" ) # creats apge
welcome =Text(StartPage,text="Welcome to the maths reivison quiz", grid=[0,0], align="top") # welcome message
choice = Text(StartPage,text= "Login or create account?",grid=[0,1], align = "top") # user prompt
LoginOrCreate = ButtonGroup(StartPage, options=[["Login","L"],["Create account","CA"]],grid=[0,2], horizontal= True, align = "left")
# displays user options ^
SubmitButton1 = PushButton(StartPage, text = "Submit",grid=[1,2], command = SetLoginOrCreate)
# submit button ^
CheckLoginOrCreate = Text(StartPage, grid =[0,4], align = "left")



def login():
      global inputUsername
      inputUsername = str(UsernameInput.value)
      inputPassword = str(PasswordInput.value)
      #obtains the inputted values from the user
      with open("UserData.txt", "r") as file:
          accountslist = [line.strip().split(",") for line in file]
          #gets all values from userdata file
      user_exists = any(user[0] == inputUsername for user in accountslist)
      #searches for username in the array
      if user_exists == True: 
          user_index = next(index for index, user in enumerate(accountslist) if user[0] == inputUsername)
          #finds the index of where the username is
          if inputPassword == accountslist[user_index][1]:
            # checks to see if the passwords match
            if accountslist[user_index][2] == "T":
                teacherspage()
                # opens teacher page if user is teacher
            else:
                studentpage()
                # otherwise opens studnet page
          else:
            wrongPasswordText = Text(LoginPage, text="Wrong password, retry", align="left", grid=[0, 5])
            # if password is wrong, it alerts the user
      else:
         CreateAccountGUI()
         NotFoundText = Text(LoginPage, text = "Username not found, please create account", align = "left", grid = [0,100])
         # if username isnt found, a message is displayed and create account subroutine is called

def CreateAccount():
      create_Username = str(UsernameInput.value)
      inputPassword = str(PasswordInput.value)
      teacher_or_student = StudentOrTeacher.value
      # if the user hasnt inputted anything, error is displayed
      if create_Username == "":
         emptyUserText = Text(CreateAccountPage, text = "Please enter a username",align="left",grid = [0,100])
         # if the user hasnt inputted anything, error is displayed
      elif inputPassword == "":
         emptyUserText = Text(CreateAccountPage, text = "Please enter a password",align="left",grid = [0,101])
         # if the user hasnt inputted anything, error is displayed
      else:
         with open("UserData.txt", "r") as file:
          existing_usernames = [line.strip().split(",")[0] for line in file]
          #gets existing usernames
          if create_Username in existing_usernames:
             takenwindow = Window(MathsQuiz, title="Username Taken")
             takentext = Text(takenwindow,text="Username already taken, try another")
             retryButton = PushButton(takenwindow, text="Retry", command=CreateAccountGUI)
             takenwindow.show()
          # if username taken, error message is shown
          else:
            with open("UserData.txt", "a") as file:
               file.write("\n"+ create_Username + "," + inputPassword + "," + teacher_or_student +"\n")
               #writes inputted values to a text file
               LoginGUI() # calls login GUI page
      

def StudentSearch():
   global SubmitTopic
   global SelectTopic
   SearchPage = Window(MathsQuiz, title = "Search", width=600, height=600, layout = "grid")
   # creates window
   SearchPage.show()
   SelectTopic = ButtonGroup(SearchPage, options=[["Binomial expansion","B"],["Differentiation","D"],["Polynomial divison","P"]],grid=[0,2], horizontal= True, align = "left")
   # Displays options
   SubmitTopic = PushButton(SearchPage, text = "Submit",grid=[1,2], command =SelectTopic2, align = "left")
   #submit selected option button
   HomeButton = PushButton(SearchPage, text = "Home",grid = [2,2], align = "left", command = studentpage)
   # return home button


def TeacherSearch():
   global SubmitTopic
   global SelectTopic
   SearchPage = Window(MathsQuiz, title = "Search", width=600, height=600, layout = "grid")
   # creates window
   SearchPage.show()
   SelectTopic = ButtonGroup(SearchPage, options=[["Binomial expansion","B"],["Differentiation","D"],["Polynomial divison","P"]],grid=[0,2], horizontal= True, align = "left")
   # Displays options
   SubmitTopic = PushButton(SearchPage, text = "Submit",grid=[1,2], command =AddAsignments, align = "left")
   #submit selected option button
   HomeButton = PushButton(SearchPage, text = "Home",grid = [2,2], align = "left", command = teacherspage)
   # return home button


def SelectTopic2():
   SelectedTopic = str(SelectTopic.value)
   # ^ obatins value from selected topic
   if SelectedTopic == "B":
      biniomialexpansionquiz()
      # calls required subrotine depending on answer
   elif SelectedTopic == "D":
      differentiationquiz()
   else:
      polynomialdivisionquiz()



def SubmitAnswer():
   global score
   answer = str(SelectAnswers.value)  # Gets the answer submitted by user
   if answer == correctanswer:
        CorrectText = Text(quizpage, text="Correct!", grid=[20, 0], align="left")
        #displays correct text to the user ^
        score = score + 1
        # incraments user score by 1
        newstats = ','.join([inputUsername, "1", "1", currentquiz]) + "\n"
   # writes the username, correct score, total answered and the quiz name, to a variable^
        with open("Userstats.txt", "a") as file:
            #opens file
            file.write(newstats)
   # writes the username, correct score, total answered and the quiz name, to the file^
   else:
        WrongText = Text(quizpage, text="Incorrect!", grid=[20, 0], align="left")
        #displays incorrect text to the user
        score = score - 1
        # lowers user score by 1
        newstats = ','.join([inputUsername, "0", "1", currentquiz]) + "\n"
        # writes the username, correct score, total answered and the quiz name, to a variable^
        with open("Userstats.txt", "a") as file:
            #opens file
            file.write(newstats)
      # writes the username, correct score, total answered and the quiz name, to the file^


def updatequestiondifferentiation():
   global differentiationquestions
   global correctanswer
   global easy_question_info
    
   easy_questions = [q for q in differentiationquestions if q[6] == "easy"]
   medium_questions = [q for q in differentiationquestions if q[6] == "medium"]
   hard_questions = [q for q in differentiationquestions if q[6] == "hard"]
    # obtains all questions for each difficulty level^
    
   easy_question = random.choice(easy_questions)
   medium_question = random.choice(medium_questions)
   hard_question = random.choice(hard_questions)
    # Select one question randomly from each difficulty level ^
    
   title, question, answerA, answerB, answerC, correctanswer, _ = easy_question
   easy_question_info = (question, answerA, answerB, answerC, correctanswer)
   title, question, answerA, answerB, answerC, correctanswer, _ = medium_question
   medium_question_info = (question, answerA, answerB, answerC, correctanswer)
   title, question, answerA, answerB, answerC, correctanswer, _ = hard_question
   hard_question_info = (question, answerA, answerB, answerC, correctanswer)
    # gets all the info for each level of difficulty question
    
   return easy_question_info, medium_question_info, hard_question_info
    # returns each question ^


def updatequestionpolynomial():
   global polynomialquestions
   global correctanswer
   global easy_question_info
    
   easy_questions = [q for q in polynomialquestions if q[6] == "easy"]
   medium_questions = [q for q in polynomialquestions if q[6] == "medium"]
   hard_questions = [q for q in polynomialquestions if q[6] == "hard"]
    # obtains all questions for each difficulty level^
    
   easy_question = random.choice(easy_questions)
   medium_question = random.choice(medium_questions)
   hard_question = random.choice(hard_questions)
    # Select one question randomly from each difficulty level ^
    
   title, question, answerA, answerB, answerC, correctanswer, _ = easy_question
   easy_question_info = (question, answerA, answerB, answerC, correctanswer)
   title, question, answerA, answerB, answerC, correctanswer, _ = medium_question
   medium_question_info = (question, answerA, answerB, answerC, correctanswer)
   title, question, answerA, answerB, answerC, correctanswer, _ = hard_question
   hard_question_info = (question, answerA, answerB, answerC, correctanswer)
    # gets all the info for each level of difficulty question
    
   return easy_question_info, medium_question_info, hard_question_info
    # returns each question ^




def updatequestionbinomial():
   global binomialquestions
   global correctanswer
   global easy_question_info
    
   easy_questions = [q for q in binomialquestions if q[6] == "easy"]
   medium_questions = [q for q in binomialquestions if q[6] == "medium"]
   hard_questions = [q for q in binomialquestions if q[6] == "hard"]
    # obtains all questions for each difficulty level^
    
   easy_question = random.choice(easy_questions)
   medium_question = random.choice(medium_questions)
   hard_question = random.choice(hard_questions)
    # Select one question randomly from each difficulty level ^
    
   title, question, answerA, answerB, answerC, correctanswer, _ = easy_question
   easy_question_info = (question, answerA, answerB, answerC, correctanswer)
   title, question, answerA, answerB, answerC, correctanswer, _ = medium_question
   medium_question_info = (question, answerA, answerB, answerC, correctanswer)
   title, question, answerA, answerB, answerC, correctanswer, _ = hard_question
   hard_question_info = (question, answerA, answerB, answerC, correctanswer)
    # gets all the info for each level of difficulty question
    
   return easy_question_info, medium_question_info, hard_question_info
    # returns each question ^


def polynomialdivisionquiz():
   global quizpage
   global polynomialquestions
   global SelectAnswers
   global currentquiz
   global score

   score = 0
   # intially sets user score to 0
    
   file = open("Questions.txt", "r")  # opens questions file
   questions = []
   for line in file:
      line = line.strip()
      line = line.split(",")
      questions.append(line)  # adds all items to an array
   file.close()

   polynomialquestions = [array for array in questions if array[0].startswith("PolynomialDivision")]
   currentquiz = "PolynomialDivision"  # creates a variable to state the current quiz
    
   quizpage = Window(MathsQuiz, width=600, height=600, layout="grid")  # creates window
   quizpage.show()
   easy_question_info, medium_question_info, hard_question_info = updatequestionpolynomial()
    # gets initial question ^
    
   question,answerA,answerB,answerC,correctanswer = easy_question_info
   # gets info for intial question

   currentquestion = Text(quizpage, text=question, grid=[1, 0], align="left")
   SelectAnswers = ButtonGroup(quizpage, options=[["", "A"], ["", "B"], ["", "C"]], grid=[0, 3], horizontal=True, align="left")
   # displays initial question
    
   def update_question_text():  # update question subroutine
      global SelectAnswers
      global correctanswer
      easy_question_info, medium_question_info, hard_question_info = updatequestionpolynomial()
      if score < 3:
          # selects easy question if score less than 3
          question,answerA,answerB,answerC,correctanswer = easy_question_info
          currentquestion.value = easy_question_info  # sets "question" to current question 
      elif 3<= score < 7:
          # selects medium question if score between 3 and 6
          question,answerA,answerB,answerC,correctanswer = medium_question_info
      else:
          # selects hard question if score over 7
          question,answerA,answerB,answerC,correctanswer = hard_question_info
      currentquestion.value = question
      SelectAnswers = ButtonGroup(quizpage, options=[[answerA, "A"], [answerB, "B"], [answerC, "C"]], grid=[0, 3], horizontal=True, align="left")
      # shows possible answers

   update_question_text()
   submitbutton = PushButton(quizpage, text="New question", command=update_question_text, align="left", grid=[1, 100])
   # button to update question ^
   submitanswer = PushButton(quizpage, text="Submit answer", command=SubmitAnswer, align="left", grid=[1, 1])
    # button to submit answer ^
   HomeButton = PushButton(quizpage,text="Home", align = "left", grid =[2,1], command = studentpage)
   # ^button to go home



def differentiationquiz():
   global quizpage
   global differentiationquestions
   global SelectAnswers
   global currentquiz
   global score

   score = 0
   # intially sets user score to 0
    
   file = open("Questions.txt", "r")  # opens questions file
   questions = []
   for line in file:
      line = line.strip()
      line = line.split(",")
      questions.append(line)  # adds all items to an array
   file.close()

   differentiationquestions = [array for array in questions if array[0].startswith("Differentiation")]
   currentquiz = "Differentiation"  # creates a variable to state the current quiz
    
   quizpage = Window(MathsQuiz, width=600, height=600, layout="grid")  # creates window
   quizpage.show()
   easy_question_info, medium_question_info, hard_question_info = updatequestiondifferentiation()
    # gets initial question ^
    
   question,answerA,answerB,answerC,correctanswer = easy_question_info
   # gets info for intial question

   currentquestion = Text(quizpage, text=question, grid=[1, 0], align="left")
   SelectAnswers = ButtonGroup(quizpage, options=[["", "A"], ["", "B"], ["", "C"]], grid=[0, 3], horizontal=True, align="left")
   # displays initial question
    
   def update_question_text():  # update question subroutine
      global SelectAnswers
      global correctanswer
      easy_question_info, medium_question_info, hard_question_info = updatequestiondifferentiation()
      if score < 3:
          # selects easy question if score less than 3
          question,answerA,answerB,answerC,correctanswer = easy_question_info
          currentquestion.value = easy_question_info  # sets "question" to current question 
      elif 3<= score < 7:
          # selects medium question if score between 3 and 7
          question,answerA,answerB,answerC,correctanswer = medium_question_info
      else:
          # selects hard question if score over 7
          question,answerA,answerB,answerC,correctanswer = hard_question_info
      currentquestion.value = question
      SelectAnswers = ButtonGroup(quizpage, options=[[answerA, "A"], [answerB, "B"], [answerC, "C"]], grid=[0, 3], horizontal=True, align="left")
      # shows possible answers

   update_question_text()
   submitbutton = PushButton(quizpage, text="New question", command=update_question_text, align="left", grid=[1, 100])
   # button to update question ^
   submitanswer = PushButton(quizpage, text="Submit answer", command=SubmitAnswer, align="left", grid=[1, 1])
    # button to submit answer ^
   HomeButton = PushButton(quizpage,text="Home", align = "left", grid =[2,1], command = studentpage)
   # ^button to go home




def biniomialexpansionquiz():
   global quizpage
   global binomialquestions
   global SelectAnswers
   global currentquiz
   global score

   score = 0
   # intially sets user score to 0
    
   file = open("Questions.txt", "r")  # opens questions file
   questions = []
   for line in file:
      line = line.strip()
      line = line.split(",")
      questions.append(line)  # adds all items to an array
   file.close()

   binomialquestions = [array for array in questions if array[0].startswith("BinomialExpansion")]
   currentquiz = "BinomialExpansion"  # creates a variable to state the current quiz
    
   quizpage = Window(MathsQuiz, width=600, height=600, layout="grid")  # creates window
   quizpage.show()
   easy_question_info, medium_question_info, hard_question_info = updatequestionbinomial()
    # gets initial question ^
    
   question,answerA,answerB,answerC,correctanswer = easy_question_info
   # gets info for intial question

   currentquestion = Text(quizpage, text=question, grid=[1, 0], align="left")
   SelectAnswers = ButtonGroup(quizpage, options=[["", "A"], ["", "B"], ["", "C"]], grid=[0, 3], horizontal=True, align="left")
   # displays initial question
    
   def update_question_text():  # update question subroutine
      global SelectAnswers
      global correctanswer
      easy_question_info, medium_question_info, hard_question_info = updatequestionbinomial()
      if score < 3:
          # selects easy question if score less than 3
          question,answerA,answerB,answerC,correctanswer = easy_question_info
          currentquestion.value = easy_question_info  # sets "question" to current question 
      elif 3<= score < 7:
          # selects medium question if score between 3 and 7
          question,answerA,answerB,answerC,correctanswer = medium_question_info
      else:
          # selects hard question if score over 7
          question,answerA,answerB,answerC,correctanswer = hard_question_info
      currentquestion.value = question
      SelectAnswers = ButtonGroup(quizpage, options=[[answerA, "A"], [answerB, "B"], [answerC, "C"]], grid=[0, 3], horizontal=True, align="left")
      # shows possible answers

   update_question_text()
   submitbutton = PushButton(quizpage, text="New question", command=update_question_text, align="left", grid=[1, 100])
   # button to update question ^
   submitanswer = PushButton(quizpage, text="Submit answer", command=SubmitAnswer, align="left", grid=[1, 1])
    # button to submit answer ^
   HomeButton = PushButton(quizpage,text="Home", align = "left", grid =[2,1], command = studentpage)
   # ^button to go home


def CallStats():
   StudentStatsPolynomialDivision()
   StudentStatsBinomialExpansion()
   StudentStatsDifferentiation()
   #calls all 3 subroutines

def StudentStatsPolynomialDivision():
   with open("UserStats.txt","r") as file:
      allStats = [line.strip().split(",") for line in file]
      # obtains all items from stats file
   userStats = [stat for stat in allStats if stat[0] == inputUsername and stat[3] == "PolynomialDivision"]
   # gets all instances for the logged in users recorded stats
   userCorrectScore = 0 # creates correct score variable
   userTotalAnswered = 0 # cretes total answered variable
   for stat in userStats:
      userCorrectScore = userCorrectScore + int(stat[1])
      # updates correct score 
      userTotalAnswered = userTotalAnswered + int(stat[2])
      # updates total answered
   with open(f"{inputUsername}_stats_PolynomialDivision.txt", "w") as file:
      file.write(f"{userCorrectScore},{userTotalAnswered},PolynomialDivision,{inputUsername}")
      # writes the 2 scores and the username to a new / existing text file
   file.close()

def StudentStatsBinomialExpansion():
   with open("UserStats.txt","r") as file:
      allStats = [line.strip().split(",") for line in file]
      # obtains all items from stats file
   userStats = [stat for stat in allStats if stat[0] == inputUsername and stat[3] == "BinomialExpansion"]
   # gets all instances for the logged in users recorded stats
   userCorrectScore = 0 # creates correct score variable
   userTotalAnswered = 0 # cretes total answered variable
   for stat in userStats:
      userCorrectScore = userCorrectScore + int(stat[1])
      # updates correct score 
      userTotalAnswered = userTotalAnswered + int(stat[2])
      # updates total answered
   with open(f"{inputUsername}_stats_BinomialExpansion.txt", "w") as file:
      file.write(f"{userCorrectScore},{userTotalAnswered},BinomialExpansion,{inputUsername}")
      # writes the 2 scores and the username to a new / existing text file
   file.close()

def StudentStatsDifferentiation():
   with open("UserStats.txt","r") as file:
      allStats = [line.strip().split(",") for line in file]
      # obtains all items from stats file
   userStats = [stat for stat in allStats if stat[0] == inputUsername and stat[3] == "Differentiation"]
   # gets all instances for the logged in users recorded stats
   userCorrectScore = 0 # creates correct score variable
   userTotalAnswered = 0 # cretes total answered variable
   for stat in userStats:
      userCorrectScore = userCorrectScore + int(stat[1])
      # updates correct score 
      userTotalAnswered = userTotalAnswered + int(stat[2])
      # updates total answered
   with open(f"{inputUsername}_stats_Differentiation.txt", "w") as file:
      file.write(f"{userCorrectScore},{userTotalAnswered},Differentiation,{inputUsername}")
   file.close()
      # writes the 2 scores and the username to a new / existing text file
   viewstats()
   # calls the page to show their stats within a GUI


def viewstats():
   ViewStatsWindow = Window(MathsQuiz, height=600, width=600, layout="grid")
   # creates window
   ViewStatsWindow.show()
   DifferentiationText = Text(ViewStatsWindow, text = "Differentiation stats:",grid=[0,1])
   BinomialText = Text(ViewStatsWindow, text = "Binomial stats:",grid=[0,3])
   PolynomialText = Text(ViewStatsWindow, text = "Polynomial stats:",grid=[0,5])
   # Displays texts for user to know what stats are which
   with open(f"{inputUsername}_stats_Differentiation.txt", "r") as file:
      DifferentiationStats = [line.strip().split(",") for line in file]
      # gets all user differentiation stats
      DifferentiationCorrectAnswers = int(DifferentiationStats[0][0])
      # gets the correct answer score
      DifferentiationTotalAnswered = int(DifferentiationStats[0][1])
      #gets total answered score
      if  DifferentiationTotalAnswered == 0:
         AverageScoreDiff = 0
         # avoids division by 0
      else:
         AverageScoreDiff = (DifferentiationCorrectAnswers / DifferentiationTotalAnswered) * 100
         # calculates average score
   file.close()
   with open(f"{inputUsername}_stats_BinomialExpansion.txt", "r") as file:
      BinomialExpansionStats = [line.strip().split(",") for line in file]
      # gets all user binomial expansion stats
      BinomialExpansionCorrectAnswers = int(BinomialExpansionStats[0][0])
      # gets the correct answer score
      BinomialExpansionTotalAnswered = int(BinomialExpansionStats[0][1])
      #gets total answered score
      if  BinomialExpansionTotalAnswered == 0:
         AverageScoreBio = 0
         # avoids division by 0
      else:
         AverageScoreBio = (BinomialExpansionCorrectAnswers / BinomialExpansionTotalAnswered) * 100
         # calculates average score
   file.close()
   with open(f"{inputUsername}_stats_PolynomialDivision.txt", "r") as file:
      PolynomialDivisionStats = [line.strip().split(",") for line in file]
      # gets all user polynomial division stats
      PolynomialDivisionCorrectAnswers = int(PolynomialDivisionStats[0][0])
      # gets the correct answer score
      PolynomialDivisionTotalAnswered = int(PolynomialDivisionStats[0][1])
      #gets total answered score
      if  PolynomialDivisionTotalAnswered == 0:
         AverageScorePoly = 0
         # avoids division by 0
      else:
         AverageScorePoly = (PolynomialDivisionCorrectAnswers / PolynomialDivisionTotalAnswered) * 100
          # calculates average score
   file.close()
   DifferentiationScoresText = Text(ViewStatsWindow, text = str(DifferentiationCorrectAnswers) + "/" + str(DifferentiationTotalAnswered) + " " + str(AverageScoreDiff) + "%", align = "left", grid = [0,2])
   # displays differentiation scores
   BinomialScoresText = Text(ViewStatsWindow, text = str(BinomialExpansionCorrectAnswers) + "/" + str(BinomialExpansionTotalAnswered) + " " + str(AverageScoreBio) + "%", align = "left", grid = [0,4])
   # displays binomial expansion scores
   PolynomialScoresText = Text(ViewStatsWindow, text = str(PolynomialDivisionCorrectAnswers) + "/" + str(PolynomialDivisionTotalAnswered) + " " + str(AverageScorePoly) + "%", align = "left", grid = [0,6])
   # displays polynomial divsion scores
   homeButton = PushButton(ViewStatsWindow, text = "home", align = "left", command = studentpage, grid = [0,7])
   # home button for user to return home


def updateB():
   userUpdate = str(SelectB.value) #gets the value from the button group
   with open("Assignments.txt","r") as file: # opens file
     CurrentAssignments = [line.strip().split(",") for line in file] # makes the elements of the file into 2D array
   CurrentAssignments[0] = userUpdate
   with open("Assignments.txt","w") as file:
      for assignment in CurrentAssignments:
            file.write(",".join(assignment) + "\n")

def updateD():
   userUpdate = str(SelectD.value) #gets the value from the button group
   with open("Assignments.txt","r") as file: # opens file
     CurrentAssignments = [line.strip().split(",") for line in file] # makes the elements of the file into 2D array
   CurrentAssignments[1] = userUpdate # selects needed value and updates it
   with open("Assignments.txt","w") as file:
      for assignment in CurrentAssignments:
            file.write(",".join(assignment) + "\n") # rewrites the text file
 

def updatePD():
   userUpdate = str(SelectPD.value) #gets the value from the button group
   with open("Assignments.txt","r") as file: # opens file
     CurrentAssignments = [line.strip().split(",") for line in file] # makes the elements of the file into 2D array
   CurrentAssignments[2] = userUpdate # selects needed value and updates it
   with open("Assignments.txt","w") as file:
      for assignment in CurrentAssignments:
            file.write(",".join(assignment) + "\n") # rewrites the text file


def AddAsignments():
   global SelectB
   global SelectD
   global SelectPD
   AddAsignmentsWindow = Window(MathsQuiz, width = 600, height= 600, layout= "grid") # creates window
   AddAsignmentsWindow.show()
   TextB = Text(AddAsignmentsWindow, text = "Binomial expansion", grid=[1,0], align = "left") # text indicating what topic will update
   SelectB = ButtonGroup(AddAsignmentsWindow, options=[["Add","A"],["Remove","R"]], grid =[1,1], align="left", horizontal= True) # buttons for either add / remove
   SubmitB = PushButton(AddAsignmentsWindow, text="Submit", command = updateB, align = "left", grid = [1,3]) # button to update the text file / add or remove assignment
   TextD = Text(AddAsignmentsWindow, text = "Differentiation", grid=[2,0], align = "left")
   SelectD = ButtonGroup(AddAsignmentsWindow, options=[["Add","A"],["Remove","R"]], grid =[2,1], align="left", horizontal= True)
   SubmitD = PushButton(AddAsignmentsWindow, text="Submit", command = updateD, align = "left", grid = [2,3])
   TextPD = Text(AddAsignmentsWindow, text = "Polynomial division", grid=[3,0], align = "left")
   SelectPD = ButtonGroup(AddAsignmentsWindow, options=[["Add","A"],["Remove","R"]], grid =[3,1], align="left", horizontal= True)
   SubmitPD = PushButton(AddAsignmentsWindow, text="Submit", command = updatePD, align = "left", grid = [3,3])
   homebutton = PushButton(AddAsignmentsWindow, text = "HOME", command = teacherspage, align= "left", grid = [7,7]) # button to return the user home




def ViewAssignments3():
   ViewAssignmentsWindow = Window(MathsQuiz, width = 600, height = 600, layout = "grid")#creates window
   ViewAssignmentsWindow.show()
   CurrentAssignmentsText = Text(ViewAssignmentsWindow, text = "Current assignments:", grid=[1,0], align = "left")
   # text indicating current assignemtns will be shown ^
   with open("Assignments.txt", "r") as file: # opens file
      CurrentAssignments = [line.strip().split(",") for line in file] # makes the elements of the file into 2D array
   if CurrentAssignments[0][0] == "A":
      BinomialText = Text(ViewAssignmentsWindow, text = "Binomial expansion exam questions", align = "left", grid = [0,1])
      #displays that they need to do certain questions if true
   if CurrentAssignments[1][0] == "A":
      DifferentiationText = Text(ViewAssignmentsWindow, text = "Differentiation exam questions", align = "left", grid = [0,2])
   if CurrentAssignments[2][0]== "A":
      PolynomialText = Text(ViewAssignmentsWindow, text = "Polynomial divsion exam questions", align = "left", grid = [0,3])
   if CurrentAssignments[0][0] == "R" and CurrentAssignments[1][0] == "R" and CurrentAssignments[2][0] == "R":
      # if all are set to remove, then display "nothing set" text
      nothingSetText = Text(ViewAssignmentsWindow, text = "Nothing set by teachers!", align = "left", grid = [0,1])
   homeButton = PushButton(ViewAssignmentsWindow, text = "home", command = studentpage, align="left", grid = [0,500])
   # home button to return user home^



def getquestions(inputUsername):
  questionSelect=input("Select a topic: Polynomial divison (1), Binomial expansion (2), Differentiation (3), mix (4): ")
  if questionSelect == "1":
    file=open("Questions.txt","r")
    questionlist = [line.strip().split(",") for line in file]
    questions = [q for q in questionlist if q[0] == "PolynomialDivision"]
    quiz(questions, questionSelect,inputUsername)
    return questions



  elif questionSelect == "2":
    file=open("Questions.txt","r")
    questionlist = [line.strip().split(",") for line in file]
    questions = [q for q in questionlist if q[0] == "BinomialExpansion"]
    quiz(questions, questionSelect,inputUsername)
    return questions




  elif questionSelect == "3":
    file=open("Questions.txt","r")
    questionlist = [line.strip().split(",") for line in file]
    questions = [q for q in questionlist if q[0] == "Differentiation"]
    quiz(questions, questionSelect,inputUsername)
    return questions


  elif questionSelect == "4":
    file=open("Questions.txt","r")
    questionlist = [line.strip().split(",") for line in file]
    polynomial_division_questions = [q for q in questionlist if q[0] == "PolynomialDivision"]
    binomial_expansion_questions = [q for q in questionlist if q[0] == "BinomialExpansion"]
    differentiation_questions = [q for q in questionlist if q[0] == "Differentiation"]
    for i in range(0,2):
      questions=random.choice(polynomial_division_questions)
      questions=questions+random.choice(binomial_expansion_questions)
      questions=questions+random.choice(differentiation_questions)
      quiz(questions, questionSelect,inputUsername)
      return questions



  else:
    print("Invalid input, please select a topic")



def loginhide():
   LoginPage.hide()


def quiz(questions, questionselect,inputUsername):
  if questionselect == "1":
    questionselect="Polynomial division"
  elif questionselect == "2":
    questionselect="Binoimal expansion"
  elif questionselect == "3":
    questionselect="Differentiation"
  else:
    questionselect= "A mixture of all questions!"
    print()
  print("Welcome!")
  print("You will be quizzed on",questionselect)
  print("You will be given a score the end of the quiz")
  counter = 0
  score = 0
  for i in range (0,5):
    question=questions[counter]
    print("Question",counter+1)
    print(question[1])
    print("A:",questions[counter][2])
    print("B:",questions[counter][3])
    print("C:",questions[counter][4])
    answer=input("Please enter your answer, A, B, or C: ").upper()
    if answer == question[5]:
      score = score + 1
      counter=counter+1
      print("Correct!")
      print()
    else:
      print("Incorrect, correct answer is", question[5])
      print(question[5])
      print()
      counter=counter+1

  print("You scored",score,"out of 6")
  file=open("UserStats.txt","a")
  file.write(inputUsername+","+str(score)+","+questionselect+"\n")
  file.close()
  CalculateStats(inputUsername)


def CalculateStats(inputUsername):
  TotalScore = 0  
  PolynomialScore = 0 
  BinomialScore = 0
  DifferentiationScore = 0
  count = 0 
  with open("UserStats.txt", "r") as file:
      statslist = [line.strip().split(",") for line in file]

  for stats in statslist:
      if stats[0] == inputUsername:
        count = count + 1 
        TotalScore = TotalScore + int(stats[1]) 
  averagescore = TotalScore/count if count != 0 else 0
  averagescore = str(averagescore)

  count = 0
  for stats in statslist:
    if stats[2] == "PolynomialDivision":
      count = count + 1
      PolynomialScore = PolynomialScore + int(stats[1])
  averagePolynomialScore = PolynomialScore/count if count != 0 else 0
  averagePolynomialScore = str(averagePolynomialScore)

  count = 0
  for stats in statslist:
    if stats[2] == "BinomialExpansion":
      count = count + 1
      BinomialScore = BinomialScore + int(stats[1])
  averageBinomialScore = BinomialScore/count if count != 0 else 0
  averageBinomialScore = str(averageBinomialScore)

  count = 0
  for stats in statslist:
    if stats[2] == "Differentiation":
      count = count + 1
      DifferentiationScore = DifferentiationScore + int(stats[1])
  averageDifferentiationScore = DifferentiationScore/count if count != 0 else 0
  averageDifferentiationScore =str(averageDifferentiationScore)

  with open("AverageScores.txt", "r") as file:
      averageslist = [line.strip().split(",") for line in file]

  target_word=inputUsername

  for i, stat in enumerate(averageslist):
    if target_word in averageslist[0]:
      print(averageslist.index(target_word))
    else:
      print("NOT FOUND")



def CheckNewPassword():
   inputedUsername = str(UsernameInput2.value)
   inputedPassword = str(PasswordInput2.value)
   inputedNewPassword = str(NewPasswordInput2.value)
   # obtains inputted values^
   found = False
   with open("UserData.txt", "r") as file:
        lines = file.readlines()
        # obtains data from file and adds it to a list
   with open("UserData.txt", "w") as file:
        # opens file to overwrite the existing data
        for line in lines:
            # iterates through the data
            username, password,teacherOrStudent = line.strip().split(",")
            # gets username, password, and role of the user from the file
            if username == inputedUsername and password == inputedPassword and inputedNewPassword != "":
               # check if the username and password matches, and if new pass isnt null
               file.write(f"{username},{inputedNewPassword},{teacherOrStudent}\n")
               # writes new value to the file
               found = True
            else:
               file.write(line)
               # if not found, doesnt update anything
   if found == True:
        FoundText = Text(ResetPasswordWindow,text = "Password updated successfully!", align="left", grid=[20,50])
        # alerts the user that it is updated
   elif inputedNewPassword == "":
      Text(ResetPasswordWindow, text = "Please enter a valid new password!", align = "left", grid =[20,51] )
      # if new password is null, error is displayed
   else:
        NotFoundText = Text(ResetPasswordWindow,text = "Username not found, or incorrect password!", align="left", grid=[20,50])
        # error message for the user

   

def ResetPassword():
   global UsernameInput2
   global PasswordInput2
   global NewPasswordInput2
   global ResetPasswordWindow
   ResetPasswordWindow = Window(MathsQuiz, width = 600, height= 600, layout= "grid")
   ResetPasswordWindow.show()
   username = Text(ResetPasswordWindow, text="Enter username", grid=[0,1]) # User prompt
   UsernameInput2 = TextBox(ResetPasswordWindow, grid=[1,1], align = "left") # box to enter name
   password = Text(ResetPasswordWindow, text="Enter current password", grid=[0,2]) # password prompt
   PasswordInput2 = TextBox(ResetPasswordWindow, grid=[1,2], align = "left", hide_text = True)
   #box to enter current password^
   newPassword = Text(ResetPasswordWindow, text="Enter new password", grid=[0,3]) # password prompt
   NewPasswordInput2 = TextBox(ResetPasswordWindow, grid=[1,3], align = "left", hide_text = True)
   # box to enter new password^
   SubmitNewPassword = PushButton(ResetPasswordWindow, align="left",grid=[0,50], command = CheckNewPassword, text = "Submit")
   # submit button ^
   homeButton = PushButton(ResetPasswordWindow, align = "left", grid = [0,500], command = LoginGUI, text = "Back")

def LoginGUI():
   global UsernameInput
   global PasswordInput
   global LoginPage
   StartPage.hide() # hides start page
   LoginPage = Window(MathsQuiz, width = 600, height= 600, layout= "grid")
   # ^creates page
   LoginPage.show()
   welcome = Text(LoginPage, text="Login page", grid=[0,0]) # title
   username = Text(LoginPage, text="Enter username", grid=[0,1]) # User prompt
   UsernameInput = TextBox(LoginPage, grid=[1,1], align = "left") # box to enter name
   password = Text(LoginPage, text="Enter password", grid=[0,2]) # password prompt
   PasswordInput = TextBox(LoginPage, grid=[1,2], align = "left", hide_text = True)
   # ^ box to input password
   LoginButton = PushButton(LoginPage, text="Login", grid=[1,3], command=login) # button to submit / login
   ResetPasswordButton = PushButton(LoginPage,text = "Reset Password", grid = [1,4], command=ResetPassword)
   # button to bring the user to the login page
   backButton = PushButton(LoginPage, grid = [0,50], align = "left", command = CreateAccountGUI, text = "Create account")
   # button to let the user go to the create account page


def WriteNewClass():
   NewClassName = str(NewClassInput.value) # obtains value from text box
   with open("Classes.txt", "r") as file:
        classes = file.readlines()
        # obtains data from test file
   if NewClassName in classes:
            Text(CreateClass3, text="Class already exists, try another", align="left", grid=[0, 50])
            # if input already exists in file, return an error
   elif NewClassName =="":
      Text(CreateClass3,text="Please enter a class", align= "left", grid = [0,51])
      # if input is empty return an error
   else:
      file = open("Classes.txt","a") # opens file
      file.write("\n"+NewClassName) # adds new class to file
      SuccessWindow = Window(MathsQuiz, width=600,height=600,layout="grid") # creates window
      text=Text(SuccessWindow,text="Class created successfully!",grid=[0,0],align = "left") # supplies sucess message
      HomeButton = PushButton(SuccessWindow, text = "home", command = teacherspage, grid = [1,4], align = "left") # home button

def CreateClass2():
   global NewClassInput
   global CreateClass3
   CreateClass3 = Window(MathsQuiz, width=600,height=600, layout="grid") # creats window
   CreateClass3.show() 
   text1 = Text(CreateClass3, text = "Enter new class name: ", grid=[0,0], align = "left") # prompt to enter class name
   NewClassInput = TextBox(CreateClass3, grid = [1,2], align = "left") # input box
   NewClassSubmit = PushButton(CreateClass3, text = "Submit", grid = [1,3], align = "left", command = WriteNewClass) # submit button
   HomeButton = PushButton(CreateClass3, text = "home", command = teacherspage, grid = [1,4], align = "left") # return home button
   return NewClassInput

def writeClassMembers():
    with open("Classes.txt", "r") as file: # opens file
        classes = [line.strip() for line in file] # gets contents to 2D array
    userClass = str(inputClass.value.strip()) # strips it of white space, casts it to string
    class_found = False
    for class_name in classes: # iterates through array
        if userClass == class_name:
            class_found = True # if it is found, return true
            break
    if class_found == True:
        successText = Text(JoinClassWindow, grid=[4, 4], text="Success! You have been added to the class!", align="left")
        with open(f"{userClass}.txt", "a") as file:
            file.write("\n" + inputUsername) # writes name to file
    else:
        failureText = Text(JoinClassWindow, grid=[4, 4], text="That class doesnt exist, please try another", align="left")
        ##^error message if not found



def JoinClass2():
   global inputClass
   global JoinClassWindow
   JoinClassWindow = Window(MathsQuiz, width=600, height = 600, layout="grid") # creates wubdiw
   JoinClassWindow.show()
   inputText = Text(JoinClassWindow, grid = [0,0], align = "left", text = "Enter the class name you wish to join: ") # prompt for user to enter class name
   inputClass = TextBox(JoinClassWindow, grid=[0,1], align="left") # input box
   submitClass = PushButton(JoinClassWindow, grid = [0,2], align = "left",  command = writeClassMembers, text = "Submit") # buttom to submit
   homeButton = PushButton(JoinClassWindow, grid = [0,3], align = "left", command = studentpage, text = "HOME") # button to go home



def CreateAccountGUI():
   global PasswordInput
   global UsernameInput
   global StudentOrTeacher
   global CreateAccountPage
   StartPage.hide() # hides start page
   CreateAccountPage = Window(MathsQuiz, width = 600, height= 600, layout= "grid") # creates window
   CreateAccountPage.show()
   welcome = Text(CreateAccountPage, text="Create account page", grid=[0,0]) # title
   username = Text(CreateAccountPage, text="Enter username", grid=[0,1]) # user prompt
   UsernameInput = TextBox(CreateAccountPage, grid=[1,1], align = "left") # text box to input username
   password = Text(CreateAccountPage, text="Enter password", grid=[0,2]) # user primpt
   PasswordInput = TextBox(CreateAccountPage, grid=[1,2], align = "left", hide_text = True)
   # text box to input password^
   StudentOrTeacher = ButtonGroup(CreateAccountPage, options=[["Student","S"],["Teacher","T"]], grid = [0,3], horizontal = True, align = "left")
   # displays 2 possible answers for user to chose
   LoginButton = PushButton(CreateAccountPage, text="Submit", grid=[1,3], command=CreateAccount)
   # submit all inputs
   backButton = PushButton(CreateAccountPage, grid = [0,50], align = "left", command = LoginGUI, text = "Login")
   # button to let the user go to the login page


def studentpage():
  loginhide() # hides login page
  global page
  StudentPage = Window (MathsQuiz, title="Student page", width=600, height=600, layout = "grid")
  # creates window ^
  StudentPage.show()
  page = StudentPage # updates current page
  welcome = Text(StudentPage, text="Welcome to the student page", grid=[0,0])
  # welcome text ^
  LogoutButton = PushButton(StudentPage, text="Logout", grid=[0,1], command=LogOut, align = "left")
  # logout button ^
  StatsButton = PushButton(StudentPage, text="Stats", grid=[1,1], command=CallStats, align = "left")
  # view stats button ^
  ViewAssignments = PushButton(StudentPage, text = "View Assignments", grid=[0,2], command=ViewAssignments3, align = "left")
  # view assignments button ^
  SearchAssignments = PushButton(StudentPage, text = "Search", grid=[1,2], command = StudentSearch, align = "left")
  # search assignments button ^
  JoinClass = PushButton(StudentPage, text = "Join class", grid = [2,2], command = JoinClass2, align = "left")
  # join class button ^
  

def LogOut():
   page.hide()
   StartPage.show()


def ViewStudentStatsDifferentiation():
    all_dataDiff = []
    # list to store all differentiation data^
    for data in os.scandir():
        # looks at all files in the directory they are stored in
        if data.is_file() and data.name.endswith("Differentiation.txt"):
            # Open the file and read its contents
            with open(data.path, "r") as file:
                # opens file^
                for line in file:
                    correct_number, answered_number, topic, username = line.strip().split(",")
                    all_dataDiff.append((correct_number, answered_number, topic, username))
                    # iterates through file and selects all data and writes it to list
    return all_dataDiff # returns the data

def ViewStudentStatsBinomial():
    all_dataBio = []
    # list to store all differentiation data^
    for data in os.scandir():
        # looks at all files in the directory they are stored in
        if data.is_file() and data.name.endswith("BinomialExpansion.txt"):
            # Open the file and read its contents
            with open(data.path, "r") as file:
                # opens file^
                for line in file:
                    correct_number, answered_number, topic, username = line.strip().split(",")
                    all_dataBio.append((correct_number, answered_number, topic, username))
                    # iterates through file and selects all data and writes it to list
    return all_dataBio # returns the data

def ViewStudentStatsPolynomial():
    all_dataPoly = []
    # array to store all differentiation data^
    for data in os.scandir():
        # looks at all files in the directory they are stored in
        if data.is_file() and data.name.endswith("PolynomialDivision.txt"):
            # Open the file and read its contents
            with open(data.path, "r") as file:
                # opens file^
                for line in file:
                    correct_number, answered_number, topic, username = line.strip().split(",")
                    all_dataPoly.append((correct_number, answered_number, topic, username))
                # iterates through file and selects all data and writes it to list
    return all_dataPoly # returns the data

def gatherAllStats():
    gatherAllStatsWindow = Window(MathsQuiz, width=600, height=600, layout="grid")
    gatherAllStatsWindow.show()
    # creates and shows window ^
    all_dataDiff = ViewStudentStatsDifferentiation()
    all_dataBio = ViewStudentStatsBinomial()
    all_dataPoly = ViewStudentStatsPolynomial()
    # gets all data from subroutines^
    all_data = all_dataDiff + all_dataBio + all_dataPoly
    i = 1
    # variable to update text position
    for data in all_data:
        correct_number, answered_number, topic, username = data
        Text(gatherAllStatsWindow, align="left", grid=[0, i], text=correct_number)
        Text(gatherAllStatsWindow, align="left", grid=[1, i], text="/")
        Text(gatherAllStatsWindow, align="left", grid=[2, i], text=answered_number)
        Text(gatherAllStatsWindow, align="left", grid=[3, i], text="username:")
        Text(gatherAllStatsWindow, align="left", grid=[4, i], text=username)
        Text(gatherAllStatsWindow, align="left", grid=[5, i], text=topic)
        # displays all data for the teacher to see ^
        i = i + 1 # incraments position counter by 1 w/ each iteration


 

def teacherspage():
  loginhide() # hides login screen
  global page
  TeachersPage = Window (MathsQuiz, title="Teachers page", width=600, height=600, layout = "grid") # creates page
  TeachersPage.show()
  page = TeachersPage # updates current page
  welcome = Text(TeachersPage, text="Welcome to the teachers page", grid=[0,0])
  LogoutButton = PushButton(TeachersPage, text="Logout", grid=[0,1], command=LogOut, align = "left") # button to logout
  StudentStatsButton = PushButton(TeachersPage, text="View student stats", grid=[1,1], command=gatherAllStats, align = "left") # button for student stats
  AddAssignments = PushButton(TeachersPage, text = "Add Assignments", grid=[0,2], command=AddAsignments, align = "left")
  SearchAssignments = PushButton(TeachersPage, text = "Search", grid=[1,2], command = TeacherSearch, align = "left") # add assigments button
  CreateClass = PushButton(TeachersPage, text = "Create class", grid = [2,2], command = CreateClass2, align = "left"  ) # create a new class button






def begin():
   MathsQuiz.display()
   StartPage.show()

begin()

#polynomialdivisionquiz()
#MathsQuiz.display()
