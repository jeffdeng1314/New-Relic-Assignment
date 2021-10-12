# New-Relic-Assignment

## Goal

Create a program executable from the command line that when given text(s) will return a list of the 100 most common three word sequences.

## Running Application

This application is written in Python3, so make sure you have Python3 installed in your environment.
You can check by running `python --version`

Once you have Python3 installed, you can follow the steps below to run the application:

1. git clone https://github.com/jeffdeng1314/New-Relic-Assignment.git
2. cd New-Relic-Assignment
3. python solution.py text\ files/triangle_text.txt
   or
4. cat text\ files/triangle_text.txt | python solution.py

## Running Tests

There are some unit tests in the [test.py]. They primarily cover file inputs, arguments, and regex tests.

You can run the [test.py] by `python test.py` or `python test.py -v` to see all the test methods in verbose mode.

## Running Docker

Making you have docker installed in your environment and you follow the steps to run the dockerfile _however, there's a known bug that it is unable to parse the file path input_

1. docker build -t new_relic_assignment .
2. docker run new_relic_assignment

## What would you do next, given more time (if anything)

- Continue my research and work on the extra credit, because I think it's a great opportunity to learn about containerization and scalability and how these can be used at a production and infrastructure level.

- The files are currently being processed one at a time. I think the program's performance would increase considerably if I have each file running on its own thread. I have used this approach in the past with REST API calls and the result was great.

- Write more and better unit tests to possible test all aspects of the application; I have a bit of hard time to test functions with no return values and to simulate stdin.

- To effectively handles unicode characters because currently, the application doesn't handle those nor unicode characters like different types of apostrophes or hyphens.

## Are there any bugs that I am aware of?

- Lack of unicode support

- Possibly running the docker file. I was some having docker daemon connection issues when testing the docker file and building an image. After resolving the connection issue, there seems to be a bug with the file path in the CMD from the docker file.
