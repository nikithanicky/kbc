from questions import QUESTIONS


def isAnswerCorrect(question, answer):
    
    '''     
    :param question: question (Type JSON)
    :param answer:   user's choice for the answer (Type INT)
    :return:
        True if the answer is correct
        False if the answer is incorrect
    '''

    return True if question['answer'] == answer else False    #remove this


def lifeLine(ques):
    if QUESTIONS[i]["answer"]==2:
        print("option2:" +QUESTIONS[i]["option2"])
        print("option4:" +QUESTIONS[i]["option4"])  
    elif QUESTIONS[i]["answer"]==1:
        print("option1:" +QUESTIONS[i]["option1"])
        print("option4:" +QUESTIONS[i]["option4"])
    elif QUESTIONS[i]["answer"]==3:
        print("option2:" +QUESTIONS[i]["option2"])
        print("option3:" +QUESTIONS[i]["option3"])
    elif QUESTIONS[i]["answer"]==4:
        print("option2:" +QUESTIONS[i]["option2"])
        print("option4:" +QUESTIONS[i]["option4"])
        
    #import random
    #if ques["answer"] == 1or2
    #option=["option1:"+ques["option1"], "option2:"+ques["option2"], "option3:"+ques["option3"], "option4:"+ques["option4"]]
    
   # result= random.choices(option, k=2)

    #print(result)     
    #print("ques["answer"]")


    '''
    :param ques: The question for which the lifeline is asked for. (Type JSON)
    :return: delete the key for two incorrect options and return the new ques value. (Type JSON)
    '''


def kbc():
    '''
        Rules to play KBC:
        * The user will have 15 rounds
        * In each round, user will get a question
        * For each question, there are 4 choices out of which ONLY one is correct.
        * Prompt the user for input of Correct Option number and give feedback about right or wrong.
        * Each correct answer get the user money corresponding to the question and displays the next question.
        * If the user is:
            1. below questions number 5, then the minimum amount rewarded is Rs. 0 (zero)
            2. As he correctly answers question number 5, the minimum reward becomes Rs. 10,000 (First level)
            3. As he correctly answers question number 11, the minimum reward becomes Rs. 3,20,000 (Second Level)
        * If the answer is wrong, then the user will return with the minimum reward.
        * If the user inputs "lifeline" (case insensitive) as input, then hide two incorrect options and
            prompt again for the input of answer.
        * NOTE:
            50-50 lifeline can be used ONLY ONCE.
            There is no option of lifeline for the last question( ques no. 15 ), even if the user has not used it before.
        * If the user inputs "quit" (case insensitive) as input, then user returns with the amount he has won until now,
            instead of the minimum amount.
    '''

    #  Display a welcome message only once to the user at the start of the game.
print("WELCOME TO THE KBC GAME")

    #  For each question, display the prize won until now and available life line.
    # For now, the below code works for only one question without LIFE-LINE and QUIT checks
flag=0    
for i in range(0, 15):
    print(f'\tQuestion %d: {QUESTIONS[i]["name"]}' %(i+1))
    print(f'\t\tOptions:')
    print(f'\t\t\tOption 1: {QUESTIONS[i]["option1"]}')
    print(f'\t\t\tOption 2: {QUESTIONS[i]["option2"]}')
    print(f'\t\t\tOption 3: {QUESTIONS[i]["option3"]}')
    print(f'\t\t\tOption 4: {QUESTIONS[i]["option4"]}')
    if flag==0 and i!=14:
        answ=input("Do you want to use Lifeline:")
        if answ=="yes":
            flag+=1
            lifeLine(QUESTIONS[i])
    if i>0:
        res=input("You want to Quit:") 
        if res=="quit":
            print(f'you rewarded {QUESTIONS[i-1]["money"]}')
            break      




    ans = input('Your choice ( 1-4 ) :')

    # check for the input validations

    if isAnswerCorrect(QUESTIONS[i], int(ans) ):

        # print the total money won.
        # See if the user has crossed a level, print that if yes
        print('\nCorrect !')
        
        
        if (i+1==5):
            print("you reward is 10,000, you crossed first level")
       # elif (i+1>5):
       #     print(f'you rewarded {QUESTIONS[i]["money"]}')    
        elif (i+1==10):
            print("you reward is 3,20,000, you crossed second level") 
        else :
            print(f'you rewarded {QUESTIONS[i]["money"]}')   
    else:
        # end the game now.
        # also print the correct answer
        print('\nIncorrect !')
        print(f'the correct answer is {QUESTIONS[i]["answer"]}')
        if(i<5):
            print("your reward is zero")
        elif(i<9):
            print("your reward is 10,000")
        else:   
            print("your reward is 3,20,000") 
        break
    # print the total money won in the end.


kbc()
