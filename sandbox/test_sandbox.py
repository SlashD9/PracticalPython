from sandbox import *

# Tests for get_question
assert get_question(0) != None, 'First question should not be empty, chaeck question.txt file'
assert get_question(19) != None, 'Last question should not be empty, chaeck question.txt file'
assert get_question(20) == None, 'Question should not exist, check question.txt file'
assert get_question(0) == '1) The Rich Want It. The Poor Need It. The Wise Know It.', "This should return : {0}".format('The Rich Want It....')
assert get_question(1) != '1) The Rich Want It. The Poor Need It. The Wise Know It.', "This should not return : {0}".format('The Rich Want It....')
assert get_question(8) == '9) What do you call a robber with a list?', "This should return : {0}".format('What do you call a robber with a list?')

#Tests for get_answer
assert get_answer(0) != None, 'First question should not be empty, chaeck question.txt file'
assert get_answer(19) != None, 'Last question should not be empty, chaeck question.txt file'
assert get_answer(20) == None, 'Question should not exist, check question.txt file'
assert get_answer(0) == 'love' , "This should return : {0}".format('love')
assert get_answer(1) != 'love' , "Should not return : {0}".format('love')
assert get_answer(4) == 'breathe' , "This should return : {0}".format('breathe')

#Test for get scores
assert get_scores() != [], "Score's should not be empty, Check scores.txt file"
print ('All Assert tests have passed')
