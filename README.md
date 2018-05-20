# IRiddle app
![alt text](https://github.com/SlashD9/PracticalPython/blob/master/Wireframe-XD/Home.jpg?raw=true "IRiddle")

This is the IRiddle app.

App can be found at [iRiddle](http://iriddle.herokuapp.com/ "iRiddle")


The Idea of the IRiddle game is to display riddles and ask the user to enter their guess, as to the answer of the riddle.
The user will receive points for every question answered and the high scorers will be displayed on the scores page.
Any incorrect guess will be shown below the page in a list.

## Wireframing
This was created using the Adobe XD Program.
Here I was able to lay out the app in its exact proportions and
test the flow both on my MAC and on My IPhone.
This will allow me to translate the exact mockup into HTML and CSS later in the build.

## Makeup
The App consist of 5 major pages: 

* Home page (index.html)
* About page (about.html)
* Game page (game.html)
* Question page (question.html)
* Score page (scores.html)

## Questions and Answers
Most of the riddles I have used in this app are from riddlers.org, I have picked the top 20 riddles.

## Testing

For  the creation of functions I have decided to create a Sandbox.py file. This allows 
me to test the functions outside the main run.py file.
By seperating them I can confirm that on their own they are working before adding 
them to the main run.py, where I will use manual testing to confirm they continue to work.

test_sandbox.py file is where my tests are located here I have set up 6 assert 
tests for both get_answer() and get_question() functions.

Test Sequence is as follows:
* Check:
    1. First question/answer is in the file
    2. Last question/answer is in the file
    3. There are no other questions/answers in the file
    4. First question/answer matches
    5. Second question/answer does not matches
    6. Check a specific question/answer matches


test_sandbox.py tests for get_scores() function
This test checks to see if the file conatains any scores, file should always
be reset to have one score remain in file.


#### Sandbox
1. Function 1: get_question()
    * This function returns a line (question) based on the number given as an argument to the function.

2. Function 2: get_answer()
    * This function returns a line (answer) based on the number given as an argument to the function.

3. Function 3: get_scores()
    * This function reuturns a list of scores from the score.txt file.


### Run.py
* I have copied functions from sandbox.py and tested in the run.py file
* I have made adjustments to the get_answer and get_question functions and then placed them back into the sandbox.py for testing
* To allow the progression of the questions and the adding of the points I have added more arguments to the question route
* This has been tested and all values increase as they should


## Manual Tests
### Home Page
1. Check function of the menu buttons "HOME" & "ABOUT" - Working
2. Check function of the "PLAY" button - Working
3. Check function of the "LEARN MORE" button - Working


### About Page
1. Check function of the menu buttons "HOME" & "ABOUT" - Working


### Game Page
1. Check function of the menu buttons "HOME" & "ABOUT" - Working
2. Check function of Username entry - Working

### Question Page
1. Check function of the menu buttons "HOME" & "ABOUT" - Working
2. Check User: (Correct Name) - Working
3. Check Points: (Correct Points) - Working
4. Check correct Question - Working
5. Check Label (Before first guess = "Please enter your answer...") - Working
6. Check Input field - Working
7. Check Button - Working
8. Check incorrect answer Label (After first guess = "Please try again...") - Working
9. Check incorrect answer Button (After first guess = "Check Again" with red background) - Working
10. Check incorrect answer Text "Incorrect Guesses" shows after first guess - Working
11. Check incorrect answer(s) shows in <li> - Working
12. Check incorrect answer Points = -3 after first guess - Working
13. Check Progresses to nect question and resets all for incorrect guess - Working
14. Check Show Score page after all questions have been asked - Working