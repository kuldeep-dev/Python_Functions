# 
# Python practice problem 3 solution

# Take the size of the list from the user
print("Enter the numbers of the list one by one\n")
size = int(input("Enter size of list\n"))

# Initialize a blank list
mylist = []

# Take the input from the user one by one
for i in range(size):
    mylist.append(int(input("Enter list element\n")))

# mylist = [7,3,2, 34, 1,0]
print(f"Your list is {mylist}\n")

reverse1 = mylist[:]
reverse1.reverse()

reverse2 = mylist[::-1]
print(f"My First reversed list of {mylist} is {reverse1}")
print(f"My Second reversed list of {mylist} is {reverse2}")

reverse3 = mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3) -i -1] = reverse3[len(reverse3) -i -1], reverse3[i] 
    # print(f"the reversed list at i={i} is {reverse3}")
    

print(f"My Third reversed list of {mylist} is {reverse3}")
if reverse1 == reverse2 and reverse2 == reverse3:
    print("All three methods give same result\n")
    


    # exeercise 

'''
Author: kuldeep
'''


def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]


if __name__ == "__main__":
    n = int(input("Enter the number of test cases\n"))
    numbers = []
    for i in range(n):
        number = int(input("Enter the number:\n"))
        numbers.append(number)

    for i in range(n):
        print(
            f"Next palindrome for {numbers[i]} is {next_palindrome(numbers[i])}")


 # exercise 

 def next_palindrome(n):
    n = n+1
    while not is_palindrome(n):
        n += 1
    return n


def is_palindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":
    size = int(input("Enter the size of your list\n"))
    num_list = []
    for i in range(size):
        num_list.append(int(input("Enter the number of the list\n")))
    print(f"You have entered {num_list}")

    print(f"Output List: {[num_list[i] if num_list[i] < 10 else next_palindrome(num_list[i] ) for i in range(size)]}")


    # new_list = []
    # for element in num_list:
    #     if element >10:
    #         n = next_palindrome(element)
    #         new_list.append(n)

    #     else:
    #         new_list.append(element)   
    # print(f"Output List: {new_list}")


    # exercise 

    # Guess the number

import random

def guessGame(a, b, actual):
    guess = int(input(f"Guess a number between {a} and {b}\n"))
    nguess = 1
    while guess != actual:
        if guess< actual:
            guess = int(input(f"Enter a bigger number\n"))
            nguess += 1
        else: 
            guess = int(input(f"Enter a smaller number\n"))   
            nguess += 1

    print(f"You guessed the number in {nguess} guesses\n")
    return nguess


if __name__ == "__main__":
    a = int(input("Enter the value of a\n"))    
    b = int(input("Enter the value of b\n"))
    actual1 = random.randint(a, b)  
    print("Player 1's turn\n")
    g1 = guessGame(a, b, actual1)
    print("Player 2's turn\n")
    actual2 = random.randint(a, b)  
    g2 = guessGame(a, b, actual2)

    if g1 < g2:
        print("Player 1 won the match!\n")

    elif g1 > g2:
        print("Player 2 won the match!\n")    
    
    else:
        print("Its a Tie!\n")
    
    print(f"The number for player 1 was {actual1} and for player 2 was {actual2}")
    


    # exercise 

    '''
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query. 
Sentences = [“This is good”, “python is good”, “python is not python snake”]

Input:
Please input your query string
“Python is”

Output:
3 results found:
1.	python is not python snake
2.	python is good
3.	This is good
'''


def mathingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score


if __name__ == "__main__":
    # mathingWords("This is good", "python is good")
    sentences = ["python is a good", "this is snake",
                 "harry is a good boy", "Subscribe to code with harry"]

    query = input("Please enter the query string\n")
    scores = [mathingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences), reverse=True) if sentScore[0] !=0 ]
    # print(sortedSentScore)

    print(f"{len(sortedSentScore)} results found!")
    for score, item in sortedSentScore:
        print(f" \"{item}\": with a score of {score}")



# exercise 

'''         
Python Practice problem 8 (Easy, 10 points)
Rohan Das Is A Fraud
Rohan das is a fraud by nature.
Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.
Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this! 
So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.
Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.
Note: Rohan’s function returns a list of numbers like this
Rohan Das’s Function Input:
rohanMultiplication(6)
Rohan’s function returns this output:
[6, 12, 18, 26, …., 60]
You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None.
'''
import random

def rohanMultiplication(number):
    wrong = random.randint(0, 9)
    table = [i * number for i in range(1, 11)]
    table[wrong] = table[wrong] + random.randint(0, 10)
    return table

def isCorrect(table, number):
    for i in range(1, 11):
        if table[i-1] != i*number:
            return i - 1 

    return None

if __name__ == "__main__":
    # print(rohanMultiplication(7))
    number = int(input("Enter a number: "))
    myTable = rohanMultiplication(number)
    print(myTable)
    wrongIndex = isCorrect(myTable, number)
    print(f"The table is wrong at index {wrongIndex}")
    

    

# exercise 



 

