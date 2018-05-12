from sandbox import *

# Tests for get_question
# Testing questions are the same

qs1 = get_question(0)
qs2 = get_question(1)

# Question 1
if get_question(0) == qs1:
    print('Test Question 1: Passed')
    print(qs1 + " \"Is the same as\" \n" + qs1)
else:
    print('Test Question 1: Failed')

# Question 2
if get_question(1) == qs2:
    print('Test Question 2: Passed')
    print(qs2 + " \"Is the same as\" \n" + qs2)
else:
    print('Test Question 2: Failed')
    

# Testing question is NOT the same
# Question3
if get_question(0) != qs2:
    print('Test Question 3: Passed')
    print(qs2 + " \"Is not the same as\" \n" + qs1)
    
else:
    print('Test Question 3: Failed')
    
    
# Tests for get_answers
# Testing answers are the same

ans1 = get_answer(0)
ans2 = get_answer(1)

# Answer 1
if get_answer(0) == ans1:
    print('Test Answer 1: Passed')
    print(ans1 + " \"Is the same as\" \n" + ans1)
else:
    print('Test Answer 1: Failed')

# Answer 2
if get_answer(1) == ans2:
    print('Test Answer 2: Passed')
    print(ans2 + " \"Is the same as\" \n" + ans2)
else:
    print('Test Answer 2: Failed')
    
# Testing question is NOT the same
# Answer3
if get_answer(0) != ans2:
    print('Test Answer 3: Passed')
    print(ans2 + " \"Is not the same as\" \n" + ans1)
    
else:
    print('Test Answer 3: Failed')

