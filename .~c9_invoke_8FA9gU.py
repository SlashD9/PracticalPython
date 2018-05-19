from sandbox import *

# Tests for get_question
# Testing questions are the same

qs1 = get_question(0)
qs2 = get_question(1)

# Question 1
if get_question(0) == qs1:
    print('Test Question 1: Passed')
else:
    print('Test Question 1: Failed')
    print(qs1 + " \"Does not match\" ")

# Question 2
if get_question(1) == qs2:
    print('Test Question 2: Passed')
else:
    print('Test Question 2: Failed')
    print(qs1 + " \"Does not match\" ")
    

# Testing question is NOT the same
# Question3
if get_question(0) != qs2:
    print('Test Question 3: Passed')
    
else:
    print('Test Question 3: Failed')
    print(qs1 + " \"Does not match\" ")
    
# Tests for get_answers
# Testing answers are the same

ans1 = get_answer(0)
ans2 = get_answer(1)

# Answer 1
if get_answer(0) == ans1:
    print('Test Answer 1: Passed')
else:
    print('Test Answer 1: Failed')
    print(ans1 + " \"Does not match\" ")

# Answer 2
if get_answer(1) == ans2:
    print('Test Answer 2: Passed')
else:
    print('Test Answer 2: Failed')
    print(ans2 + " \"Does not match\" ")
    
# Testing question is NOT the same
# Answer3
if get_answer(0) != ans2:
    print('Test Answer 3: Passed')
    
else:
    print('Test Answer 3: Failed')
    print(ans3 + " \"Does match\" ")

assert get_answer() == 'love' , "Does not match"