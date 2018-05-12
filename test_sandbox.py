from sandbox import *



# Tests for get_question
# Testing questions are the same

qs1 = get_question(0)
qs2 = get_question(1)

# Question 1
if get_question(0) == qs1:
    print('Test 1: Passed')
    print(qs1 + " \"Is the same as\" \n" + qs1)
else:
    print('Test 1: Failed')

# Question 2
if get_question(1) == qs2:
    print('Test 2: Passed')
    print(qs2 + " \"Is the same as\" \n" + qs2)
else:
    print('Test 2: Failed')
    
# Question3
# Testing question is NOT the same
if get_question(0) != qs2:
    print('Test 3: Passed')
    print(qs2 + " \"Is not the same as\" \n" + qs1)
    
else:
    print('Test 3: Failed')
    
    
# Tests for get_answers
# Testing answers are the same

ans1 = get_answer(0)
ans2 = get_answer(1)

# Answer 1

