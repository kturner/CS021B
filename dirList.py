#Author Kevin Turner CS21B
#Assignment 2, working directory list
import os

count = 1
cwd=os.getcwd()
fileList = os.listdir(cwd)
print('Files:')
for fileName in fileList:
    print('    <', fileName,' ',  count, '>')
    count += 1

"""
Files:
    < .DS_Store >
    < .idea >
    < __pycache__ >
    < abstract.py >
    < account.py >
    < assignment10 results.pdf >
    < assignment1docstrings.txt >
    < Assignment3Dictonaries-1.py >
    < Assignment3Dictonaries.py >
    < Assignment4SpellingNumbers.py >
    < Assignment5Cardobject.py >
    < card.py >
    < card2.py >
    < data.pkl >
    < data.txt >
    < dice.py >
    < dirList.py >
    < employee-old.py >
    < employee.py >
    < employeeTest-old.py >
    < employeeTest.py >
    < factorial.py >
    < fileCompare.py >
    < FinalQuestion.py >
    < first_file.txt >
    < greetingApp.py >
    < greetingAppKT.py >
    < greetingKT.py >
    < greetingKTerror.py >
    < hand.py >
    < hand2.py >
    < input_try_except.py >
    < main.py >
    < manager-old.py >
    < manager.py >
    < myFrame.py >
    < Rectangle.py >
    < save.p >
    < savingsAccount.py >
    < second_file.txt >
    < tempConverter.py >
    < Test.py >
    < test1B.py >
    < Testcs1.py >
    < TestHand.py >
    < TestHand1.py >
    < TestHand2.py >
    < testpy.py >
    < voting_letter.py >

Process finished with exit code 0

"""