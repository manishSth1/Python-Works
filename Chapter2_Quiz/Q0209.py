is_cloudy_today = input("Is it cloudy today, Y/N: ")       # ASKS FOR INPUT IF WEATHER IS CLOUDY FOR TODAY
it_rained_yesterday = input("Did it rainn yesterday, Y/N: ")  # ASKS FOR INPUT IF IT RAINED YESTERDAY

if ((is_cloudy_today == 'Y' or is_cloudy_today =='y')):
    if(it_rained_yesterday == 'Y' or it_rained_yesterday =='y'): 
        print("It will rain today")                         # IF USER INPUTS yes TO BOTH QUESTIONS
    else:
        print("The weather forecast for today is unclear")    # IF USER INPUTS yes TO FIRST QUESTION AND no TO SECOND
else:
    print("The weather forecast for today is unclear")  
 
