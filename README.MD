## Objective:
The objective of this project is to perform String Calculation using TTD implementation. 
## Problem Statements:
1. Create a simple String calculator with a method signature like this:

>> def add(random_string)

Input: a string of comma-separated numbers

Output: an integer, sum of the numbers
> Input: “”, Output: 0
> Input: “1”, Output: 1

## Project Architecture:
This project has two python modules to modularized the entire solution.
* calculate.py --> It's holding "addition" method which is calculating the actual output.
* testcases.py --> It's containing a class "TestCalculatorNumbers" which is inheriting "unittest.TestCase".
* requirements.txt --> As of now, none of the external package is installed.If needed we can add all required packages in this file for easy installation with the below command. 
  >>"pip install -r requirements.txt"
* README.MD --> This file has all required information to handle this project like project guide book.

>Additional Info:
* Python Version: 3.11.9
## Test Cases & Results:
1. input("") output(0)
2. input("abcd") output(0)
3. input("*jauyw#$") output(0)
4. input("1") output(1)
5. input("1,2") output(3)


## Execution Steps:
Create a local project with "ProjectAssessment" and clone or download this project from the below url.
>> https://github.com/sumantas98/MiniProjectFASTAPI.git
> 
Now,create a virtual environment by running the following command in your terminal or command prompt:
>> pip install virtualenv
> 
>> python -m venv env
> 
Navigate the below location and run activate.bat file.
myenv\Scripts\activate

Navigate to project directory and run the below command to execute the testcases.
>> python testcases.py

## Commit Information:
https://github.com/sumantas98/IncubyteProjectAssessment/commits?author=sumantas98&since=2024-08-31&until=