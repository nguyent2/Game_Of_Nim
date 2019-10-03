# A05: The Game of Nim

Name 1: Thy H. Nguyen

Name 2 (if needed):

Repository Link: https://github.com/2019-fall-csc-226/a05-nim-nguyent2-a05.git

Google Document Link: https://docs.google.com/document/d/1rqb0nXLGl4mU7Uyr-g9ncQtCFpHhvscLmO9TVIFR4Ws/edit?usp=sharing

This document is written in a language called Markdown, which is similar to HTML or other text-formatting languages. A helpful cheat sheet for Markdown is [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).

Note that the code for markdown and what appears in Github are not the same. I will be looking at what appears in Github, so you should definitely check Github before you consider your submission complete. 


## INITIAL DESIGN PLAN:

Design a plan which meets the computational requirements to solve the problem. Your plan does not need to be syntactically correct. It needs to capture the flow of logic in a human readable format.

#For example:

1. Capture user input about how many balls they want to put in the basket
2. Use a conditional to see if user's input is an integer (If user did not input an integer, REQUIRE user to re-enter the input)
3. Use a conditional to see if user's input is greater than 15 (If the input is not greater than 15, REQUIRE user to re-enter the input)
4. Ask the users how many balls they choose (between 1 to 4 balls) to remove from the pile.
5. Let the program choose randomly (between 1 to 4 balls) to remove from the pile.
6. Do the step 4 and 5 again and again until the number of balls left is less than or equal to 1.
7. Print out the result who is the winner.

#Replace this text and the text above with your design. Do this section before you begin coding.

## IMPLEMENTATIONS:

A list in bullet form of each function you created, and what is each function’s purpose.
* Function to check integer.
* Function to check integer greater than 15 (meaning if pass the first function, check if the number in the first function is greater than 15) </ul>
* Function to ask for the user's taking out balls.
* Function to randomly pick the balls from the program.
* Function to check to see who will get the last balls.
#Replace this text and the text above with your design. Do this section before you begin coding.

## TESTING:

An overview of what values you felt needed testing, and why.
1. I think that we need to test when the number of balls is around 4 or below.
* The reason is that this number will determine who will win the Game of Nim.
2. Test big number of balls (around 10 to the power of 10, Google pixel or more than that
* The reason is that as people find it hard to picture infinity (when the cardinality of a set of numbers is countably infinite or finite), there is a need to test those bigger numbers, as biggest as possible.
## ERRORS:

A list in bullet form of all known errors and deficiencies in your implementation.
* All inputs of user are treated as string, so it is neccessary to convert them into integers.
* The scope of the variables (Global vs. Local)
* Differentiate between the number of balls left after each turn (user vs. computer)
#Replace this text and the text above with your design. Do this section while you are coding and notice errors. Some you may even fix before your finished!

## SUMMARY:

A brief summary description of the design and implementation, including how much your initial design plan evolved, the final result you achieved, and the amount of time you spent as a programmer in accomplishing these results. This should be no more than two paragraphs. Consider this like a report of what you did.

This program is made for users interacting more with the computers. Through this assignment, this is some evidence that no matter how 
tricky the computer (or the program) can be, humans will always be the one who implement the program and tell the program do what they want to. 
The initial plan evolved smoothly as I chose to let computer choose the numbers randomly (in other words, I treat the computer as an object playing the game randomly with no strategy.) The final result I achieved was that I could make the computers become a player with no strategy. 
For better modification version of the code, I should treat the computer as an expert in playing this Game of Nim. With more clever thought and algorithm to the codes, my "computer player" would definitely be smarter and more clever.
I am satisfied with the time I spend coding this program, as I can think of different ways to solve a problem. Even though my algorithm to the problem is not as realistic and sufficient as the algorithm when the computer can become smarter and more strategic, I am still happy that
the Game of Nim is still complete. This program will be suitable for people who want to play the Game of Nim at the easiest level.

#Replace this text and the text above with your design. Do this section after you finish coding.

## COMMENTS:

A paragraph or so of your own comments on and reactions to this assignment. Consider this like a reflection.
I have learned a lot of coding, algorithm, and math through this assignment. I learn about implementing the scope of the program,
so I can get access to the variable in different functions. Through this problem, I can think of different ways to improve my strategy in playing the Game of Nim.
I am deeply in love with logic, proposition, math, and strategy. Therefore, the way of thinking how to make the computer become a more strategic player in the Game of Nim
interested me the most. However, I am still happy with the most basic and easiest level that my computer is playing with the user in the Game of Nim.
With little humor in writing this program (especially in the last sentence announcing who is the winner), I am satisfied with my time and effort for this program.

#Replace this text and the text above with your design. Do this section after you finish coding.
