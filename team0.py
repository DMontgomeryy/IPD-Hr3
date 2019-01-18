import random
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Danny Montgomery Team' # Only 10 chars displayed.
strategy_name = 'creating_maze_bianary'
strategy_description = '''I used subtraction operation it tracks if they program could colude then I betray after coludes stop to reduce bulk fails.It does it 100 times.
'''
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    Make my move.
    Returns 'c' or 'b'. 
    '''

    if [my_history] == []:
        return 'c'
    
    if len(my_history)<8:
        if int(their_score)< -1000:
            return 'c' # this prevents me from breaking my score on my first turns
        else:
            return 'b'    
        return 'c'
    if 7<len(my_history)<31:
        if their_history[-2] == 'b' or my_score < -1000:
            return 'b'
        else:
            return 'c'
    elif 101>len(my_history)>30:
            colludee=int(1)
            '''it is a random choice it runs seventy times for the IPD program
            '''
            if random.randint(0,1)  == colludee:
                return 'c' 
            else:
                return 'b'
    if len(my_history)>100:
        if random.random()<0.6: # 60% of the other rounds
            return 'b' 
        else:
            return 'c'
 
    
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # theze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.

   

   
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print ('Test passed')
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             