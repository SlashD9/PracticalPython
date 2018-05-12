# IRiddle app
[logo]: https://github.com/SlashD9/PracticalPython/blob/master/Wireframe-XD/Home.jpg?raw=true "IRiddle"
This is the IRiddle app.

The Idea of the IRiddle game is to display riddles and ask the user to enter their guess as to the answer of the riddle.
The user will receive points for every question answered and the high scorers will be displayed on the scores page.

## Wireframing
This was created using the Adobe XD Program.
Here I was able to lay out the app in its exact proportions and
test the flow both on my MAC and on My IPhone.
This will allow me to translate the exact mockup into HTML and CSS later in the build.

## Makeup
The App consist of 4 major pages: 

* Home page (index.html)
* About page (about.html)
* Game page (game.html)
* Score page (scores.html)

## Questions and Answers
Most of the riddles I have used in this app are from riddlers.org

## Testing

For creating functions I have decided to create a Sandbox.py file. This allows 
me to test the functions outside the main run.py file.
By seperating them I can confirm that on their own they are working before adding 
them to the main run.py.

### Python

All Testing has been carried out in the same sequence:
1. Add tests
2. Run tests (They fail, no function)
3. Create the function to enable tests to pass
4. Run tests (They passed)
5. Change the parameters of the tests to make them fail
6. Run tests (They fail)
7. Change the parameters to original
8. Run tests (They passed)

#### Sandbox
1. Function 1: get_question()
    * This function returns a line (question) based on the number given as an argument to the function.

2. Function 2: get_answer()
    * This function returns a line (answer) based on the number given as an argument to the function.


### Run.py
* I have copied functions from sandbox.py and tested in the run.py file
* I have made adjustments to the get_answer and get_question functions and then placed them back into the sandbox.py for testing
* To allow the progression of the questions and the adding of the points I have added more arguments to the question route
* This has been tested and all values increase as they should