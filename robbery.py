def robbery_story():
    q1 = input('''
    *Caution*
    This is a huge decision. Are you sure you would like to rob the Bank of Mashed Beats?
    1) Yes
    2) No
    ''')
    while q1 not in '12':
        q1 = input('''
        This is not a valid path for your adventure. Please try again:
        1) Yes
        2) No
        ''')

    if q1 == '1':
        q2 = input('''
        Armed or unarmed?
        1) Armed
        2) Unarmed
        ''')
        while q2 not in '12':
            q2 = input('''
            This is not a valid path for your adventure. Please try again:
            1) Armed
            2) Unarmed
            ''')
        if q2 == '1':
            q3 = input('''
            You lean in towards the teller threateningly and she looks faintly frightened. Holding your bag open on the counter and your jacket pulled back, you begin to speak.
            "This is a robbery. I don't want to hurt anyone, I just want the money."
            The teller looks around anxiously and her eyes land on the gun in your waist band.
            Will you
            1) Hold the teller at gunpoint until she gives you the money
            2) Threaten the teller verbally until she gives you the money
            ''')
            while q3 not in '12':
                q3 = input('''
                This is not a valid path for your adventure. Please try again:
                1) Hold the teller at gunpoint until she gives you the money
                2) Threaten the teller verbally until she gives you the money
                ''')
            if q3 == '1':
                q4 = input('''
                You slide over the counter and begin to hold the gun to her back. The other customers and tellers notice and begin to run out the door. She loads the money into your bag but as you are about to leave, you notice the police blockading the exits.
                Will you hold hostages?
                1) Yes
                2) No
                ''') 
                while q4 not in '12':
                    q4 = input('''
                    This is not a valid path for your adventure. Please try again:
                    1) Yes
                    2) No
                    ''')

                if q4 == '1':
                    q5 = input('''
                    As you expected, you recieve a phone call from a negotiator.
                    "Look, we want to get you out of here and we want those hostages safe. We are willing to negotiate with you.
                    Will you
                    1) Try to make requests for a safe get away
                    2) Try to negotiate for a plea deal
                    ''')
                    while q5 not in '12':
                        q5 = input('''
                        This is not a valid path for your adventure. Please try again:
                        1) Try to make requests for a safe get away
                        2) Try to negotiate for a plea deal
                        ''')
                    if q5 == '1':
                        print('''
                        You begin to make your requests.
                        "I want to get out of here alive and with the money, alright?" you ask. Your voice quivers but your resolve does not. "I need a car, cleared streets, or everyone in here dies."
                        Little did you know, they managed to get a sniper in place while you were thinking through your plan. Pow pow.
                        ''')

                    else:
                        print('''
                        "I messed up, man. I just want to see my family again," you cry, sweating.
                        "Drop the gun and the money. You'll be alright, buddy," the police officer says kindly. "You promise to walk out, no one harmed, and we'll take care of you in court, alright?"
                        You follow his orders and although you get charged for attempted armed robbery, they get you off with the minimum sentence.
                        ''')

                else:
                    print('''
                    Instead of holding hostages, you are able to find a secret exit and make it away with the money. Congradulations, you are $1,000,000,000 richer. Who knew the BOMB was so well off?
                    ''')

            else:
                q4 = input('''
                "Like I said, I don't want to hurt anyone but I will if I don't get my money. Don't make a scene," you whisper menacingly.
                She reaches behind the counter and begins to load piles of money into your bag. Unbeknownst to you, however, she also hit the panic button. You don't realize until you hear the police sirens. 
                Will you leave the money and run?
                1) Yes
                2) No
                ''')
                while q4 not in '12':
                    q4 = input('''
                    This is not a valid path for your adventure. Please try again:
                    1) Yes
                    2) No
                    ''')
                if q4 == '1':
                    print('''
                    You are able to run out before the police get there without the extra burden of your huge bag of money.
                    ''')

                else:
                    print('''
                    You aren't able to escape and are caught with the gun and the bag of money. You are charged with attempted armed robbery. Don't drop the soap.
                    ''')

        else:
            print('''
            You lean in towards the teller threateningly and she looks faintly frightened. Holding your bag open on the counter, you begin to speak.
            "This is a robbery. I don't want to hurt anyone, I just want the money."
            The teller looks around anxiously and you are sure that she will comply. Instead, however, she leaps across the counter screaming. "He's trying to rob the bank! Call 911!"
            Thanks to the help of the other tellers and the customers, you are detained until the police arrive. You go to jail for attempted robbery.
            ''')

    else:
        print('''
        You rethink your decision and decide not to rob the bank today. You left your ski mask at home anyway.
        ''')

    print('''
    ------FIN------
    ''')