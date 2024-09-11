## Objective:
The objective of this project is to perform String Calculation using TTD implementation. 
## Problem Statements:
1. Create a simple String calculator with a method signature like this:
>> def add(random_string)

Input: a string of comma-separated numbers

Output: an integer, sum of the numbers , 

Please refer the below two examples, for more cases kindly review "Test Cases & Results" section below.
> Input: “”, Output: 0
> 
> Input: “1”, Output: 1
2. Allow the add method to handle any amount of numbers.
3. Allow the add method to handle new lines between numbers (instead of commas). ("1\n2,3" should return 6).
4. Support different delimiters:

To change the delimiter, the beginning of the string will contain a separate line that looks like this: "//[delimiter]\n[numbers…]". For example, "//;\n1;2" where the delimiter is ";" should return 3.



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
6. input("2,2,0") output(4)
7. input("2,2,3") output(7)
8. input("2,1,5,7") output(15)
9. input("8,2,1") output(11)
10. input("1\n2,3") output(6)
11. input("8\n2,1") output(11)
12. input("8,2\n2") output(12)
13. input("//;\n1;2") output(3)
14. input("//@\n\t11#@11@1") output(23)


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