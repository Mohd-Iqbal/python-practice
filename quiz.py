import random

while True:
    data = {"What is the capital of France?":[
    "London",
    "Paris",
    "Rome",
    "Berlin"],
    "Who wrote the play 'Romeo and Juliet'?":[
    "William Shakespeare",
    "Jane Austen",
    "Charles Dickens",
    "Mark Twain"],
    "Which planet is known as the 'Red Planet'?":[
    "Jupiter",
    "Mars",
    "Venus",
    "Saturn"],
    "What is the chemical symbol for gold?":[
    "Au",
    "Ag",
    "Fe",
    "Cu"]}
    

# this list_data creates list of data variable dictionary keys and then shuffles those keys  
    list_data = list(data)
    random.shuffle(list_data)

    options = ["a","b","c","d"]
    correct_answers = ["Paris","William Shakespeare","Mars","Au"] 

# this will hold the questions after adding questions number and options alphabetically sorted
    questions = {}

    correct_options = []
    choose_options = []

    q_number = 1
    for i in list_data:
        # this will hold options of each questions and then shuffles it 
        list_options = data[i]
        random.shuffle(list_options)

        print(str(q_number)+". "+i)

        # this new_list will hold options for each questions after options are alphabetically sorted
        new_list = []

        o_number = 0
        for j in list_options:
            option = options[min(o_number,len(data) - 1)]+". "+j
            new_list.append(option)
            print(option)
            o_number += 1 
        questions.update({str(q_number)+". "+i:new_list}) 

        # this while takes input ans from user and then checks if user input ans matches any values of options list, if not then it keeps looping until the user input ans mathces any options list values 
        ans = None
        while ans not in options:
            ans = input("Choose correct option. ").lower()
            # this if statement checks if ans matches any options list values, if true then append ans to choose_options list
            if ans in options:
                choose_options.append(ans) 

        q_number += 1
    
    # this set holds those valuse that matches any correct_answers list values, so that the loop doesn't include these values for checking agianst correct_answers after it matches once
    matched_strings = set()
    
    # this for loop is used to find the correct option for each question after options are alphabetically sorted and adds it's alphabet to correct_options list 
    for i in questions.values():
        for j in range(4):
            string1 = i[j][2:].strip()
            for k in range(4):
                string2 = correct_answers[k].strip()
                if string1 == string2 and string1 not in matched_strings:
                    correct_options.append(i[j][0])
                    break
    
    list_to_string1 = "".join(correct_options).replace("'", "").replace(",", "")
    list_to_string2 = "".join(choose_options).replace("'", "").replace(",", "")
    print("Correct options "+list_to_string1)
    print("Your answers "+list_to_string2)

    # this matches user choosen options with correct_options list values and if matches then adds 1 to number_correct_answers variable     
    number_correct_answers = 0
    for i in range(4):
        if correct_options[i] == choose_options[i]:
            number_correct_answers += 1
    
    efficiency = number_correct_answers / len(data) * 100
    
    print("You have answered "+str(number_correct_answers)+" questions correctly")
    print("Your efficiency is "+str(efficiency)+"%")

    # this asks user for playing the quiz again, if yes loops starts again else terminates the loop    
    play_again = input("Want to start again Yes/No ").lower().strip()
    if play_again == "no":
        break

# Note: we are striping whitespaces from user input so that during equating it doesn't make the condition statement false