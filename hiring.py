import json, random, validators

name = ''
number = ''
address = ''
age = ''
crime = ''
drug = ''

#Saves name, number, and address just in case the user gets hired but is "thrown away"
def application():
    global number, name, address, age, crime, drug

    name = input('Please enter your Name. ')
    number = input('Please enter a valid 10-digit Phone Number. ')
    address = input('Please enter a valid Address. ')
    age = input('Are you older than 18 years of age? (Y/N) ')
    input('Please enter the last four digits of your social security number? ')
     
    military = input('Have you served in the Military? (Y/N) ')
    if military == 'Y':
        input('Please enter the time you served.')

    crime = input('Have you been convicted of a crime? (Y/N) ')

    drug = input('Are you willing to comply with a mandatory drug screening? (Y/N) ')


#Adds new hire to text file; takes wage as paramater as the wage will be different based on the story path
def hire(wage):
    global name, number, address

    #Loads employee dictionary
    e = open('employees.txt', 'r')
    employees = json.loads(e.read())
    e.close()

    #Loads account dictionary
    a = open('accounts.txt', 'r')
    accounts = json.loads(a.read())
    a.close()

    #Creates dictionary entry for the newly hired employee
    employees[name] = {}
    employees[name]['Phone'] = number
    employees[name]['Address'] = address
    employees[name]['Wage'] = wage
    employees[name]['Hours'] = 0

    #Creates dictionary entry for the employee banking account
    acc_num = str(random.randint(1000000000,10000000000))
    while acc_num in accounts:
        acc_num = str(random.randint(1000000000,10000000000))
    accounts[acc_num] = {}
    accounts[acc_num]['Account'] = 'E'
    accounts[acc_num]['Holder'] = [name]
    accounts[acc_num]['Phone'] = number
    accounts[acc_num]['Address'] = address
    accounts[acc_num]['Account Alias'] = 'Employee Account' 
    pin = str(random.randint(1000,10000))
    accounts[acc_num]['PIN'] = pin
    accounts[acc_num]['Balance'] = 0

    #Saves this dictionary to the text file of employees
    e = open('employees.txt', 'w')
    e.write(json.dumps(employees))
    e.close()

    #Saves the account to the account dictionary
    a = open('accounts.txt','w')
    a.write(json.dumps(accounts))
    a.close()


#Story line function
def hiring_story():
    global age, crime, drug

    print( '''
    The teller hands you an application.
    "Welcome," she says. "Here is an application. Please fill it out correctly."
    You take the application to a chair in the corner and fill it out quickly.
    ''')

    application()

    if age == 'Yy' and crime == 'nN' and drug == 'Yy':
        print('''
        You walk over to the teller when you are done and hand her the application.
        Without so much as a glance down, she throws the stack of papers away.
        "So, now that that's out of the way, what's your name?"
        ''')

        q1 = input('''
        Feeling disrespected, you have four options.
        1) Walk away without letting her speak. After all, you need a job, but not badly enough to deal with that disrespect.
        2) Tell her that she should have looked at the application. Why should you have spent all that time without her using it?
        3) Tell her your name with attitude. You are pretty desperate for the job, but you have a hard time managing your anger.
        4) Politely tell her your name. Who are you kidding? You need this job pretty darn badly.
        ''')

        if q1 == '1':
            print('You angrily walk out of the bank. You even make sure the door slams shut for emphasis. It\'s time to look for a job elsewhere.')

        elif q1 == '2':
            print('''
            "Well maybe if you had looked at the application I spent 20 minuites filling out, you would know what my name was!" you say angrily. A couple of other customers and tellers look over but you don't really care.
            The teller raises an eyebrow. You're quite sure she's about to tell you a few things about yourself so you quickly start to prepare clapbacks.
            Instead of giving you the third degree, she says "I like your attitude. Go sit and wait for the hiring manager to come out.
            ''')

            q2 = input('''
            Slightly confused now, you have two options.
            1) Walk away. Do you really want to work with these crazy people? You're honestly surprised the bank even has members.
            2) Wait for the hiring manager. You kind of want to hear what they have to say and you also know this is an opportunity to tell them how crappy this teller is.
            ''')

            if q2 == '1':
                print('''
                You walk away a little more angry than you were five minutes ago. You're honestly contemplating closing your account there but decide it's not that deep. You will definetly be making a Facebook post later though. #CanISpeakToYourManager???
                ''')

            else:
                print('''
                The manager walks out of the back room looking...rough. You're thinking that you probably should have left while you had the chance. This bank's reputation is sinking lower by the minute.
                "Hey, we're extremely short handed here. We NEED new tellers. I understand that you are looking for a job?" the manager says.
                ''')

                q3 = input('''
                This situation is getting weirder by the second. You have three options.
                1) Play the "Can I speak to your manager card?" and complain about the teller's attitude.
                2) Play on the fact that they need you more than you need the job. They don't have to know how much you are struggling...you might even manage to negotiate higher wages.
                3) Lay all your chips on the table...notably the fact that you can't even afford a single chip to eat.
                ''')

                if q3 == '1':
                    print('''
                    "Well, of course you need new tellers! The ones you have now are absolute trash! I came here looking for a job and I will leave after by closing my account! So much attitude, so much disrespect! I hope this bank is closed by Christmas!" you scream, gathering your things and storming out of the door.
                    ''')
                
                elif q3 == '2':
                    print('''
                    You really need this job. Your rent is due. Your Netflix is off. You need food. Your Netflix is off. It's rough out here in these streets. BUT, and that's a big but, they don't have to know that.
                    You decide to use this to your advantage.
                    ''')

                    q4 = input('''
                    You have two options.
                    1) Lie about your qualification so that they want you even more.
                    2) Go directly into negotiating for a higher wage.
                    ''')

                    if q4 == '1':
                        print('''
                        Too bad they overheard you on the phone earlier telling your friend about your lack of experience. No one likes a lying skank...
                        ''')

                    else:
                        print('''
                        "I have a couple of different offers on the table...Are you willing to pay more than $12 an hour?" you say with confidence that you don't have. Minimium wage is $7.40 and $12 is asking a lot...
                        To your surprise, the manager nods, albiet reluctantly. He hands you an application (one much shorter than the first) for you to fill out.
                        ''')
                        hire(12.00)
                
                elif q3 == '3':
                    print('''
                    "I'm going to be honest," you start, "I'm extremely broke right now. This is my last option and I don't have a lot of experience."
                    With a glance at the over flowing trashcans and dirty windows, the manager nods. "I can offer you $10 an hour as a janitor or $8 an hour as a teller but with more hours."
                    ''')

                    q4 = input('''
                    You have two options.
                    1) Accept the job as a janitor
                    2) Accept the job as a teller
                    ''')

                    if q4 == '1':
                        print('''
                        You start your job the same day but soon find out that you will only be able to work 5 hours a week. You guess some money is better than no money, but you are still looking for another job.
                        ''')
                    else:
                        print('''
                        The manager hands you a short hire to fill out and sends you on your way. You will be able to work 30 hours a week which is a lot more than you would have as a janitor. Apparently times are very rough in the banking industry and they have been cutting corners where they can.
                        ''')
                        hire(8.00)

        elif q1 == '3':
            print('''
            With a roll of your eyes and a toss of your hair, you reluctantly tell her your name. She quirks her eyebrow and squints a little. That buttfish face.
            "I don't think you're cut out to be a teller with that attitude. You're going to have to work with a lot of angry people and if you can't handle recieving a little, you aren't going to make it long. Fortunately, we have positions open as a janitor.
            ''')

            q2 = input('''
            You're pretty offended, slightly confused. You have two options:
            1) You can leave angrily. You might not be qualified for a lot but you sure do know more than what's required for a janitor.
            2) You can accept the job as the janitor. It's not what you came here for but you need a job pretty badly.
            ''')

            if q2 == '1':
                print('''
                With one last dirty look, you leave the bank, slamming the door behind you.
                ''')
            
            else:
                print('''
                You have to fill out another hire, albiet one much shorter than the first one. You are making $10 an hour but can only work 5 hours a week. Some money is better than no money, but you're barely making enough gas money to make it to and from work. Maybe try with less attitude next time.
                ''')

        else:
            print('''
            You reply kindly and the teller looks at you curiously. With a much more polite tone, she begins to speak.
            "Are you always this polite?"
            ''')

            q2 = input('''
            You have two options to reply:
            1) Yes
            2) No
            ''')

            if q2 == '1':
                print('''
                Satisfied with your answer, the teller explains that your reaction to her rude action determines whether or not you are cut out for teller work. You passed, so you will be able to start at $8 an hour as a teller.
                ''')
                hire(8.00)

            else:
                print('''
                The teller is intrigued.
                "I can be mean if I need to be. Until that time comes, however, I try to treat everyone with kindness," you reply to her look of questioning.
                The manager comes out as you finish with a smile on her face. "Spoken like a true manager," she says. "We are in need of another branch manager. Would you like to come on board?"
                ''')

                q3 = input('''
                You have three options:
                1) Accept the job as the manager. You're not for sure that you will be able to perhire adequately but the pay will be bomb.
                2) You can push for the teller job. You know you'll be able to handle that one even if the pay isn't as great.
                3) You can simply decline the job offer. Do you really want to work with these weirdos?
                ''')

                if q3 == '1':
                    print('''
                    You accept the job as the manager and get paid a whopping $20 an hour. You work 35 hours a week and couldn't be happier.
                    ''')

                elif q3 == '2':
                    print('''
                    They relent and let you join the squad as a teller. You make a cool $10 an hour.
                    ''')
                    hire(10.00)

                else:
                    print('''
                    Deciding that the people at this bank are kind of weird, you decline politely and walk out. You plan on closing your account soon.
                    ''')
    
    else:
        print('''
        Based on your answers to the application, you are not qualified for a job.
        ''')
    
    print('''
    ------FIN------
    ''')