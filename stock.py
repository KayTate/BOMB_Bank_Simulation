import json, requests, csv, helpers

#Returns most recent entry for the equity designated
def quote(symbol):
    #Gets the information from the API
    endpoint = 'function=GLOBAL_QUOTE&symbol=' + symbol +'&apikey=QFK2H96NRYJTAHC7'
    r = requests.get('https://www.alphavantage.co/query?' + endpoint)
    result = r.json()

    #Formats the information in a better dictionary
    formatted = {}
    formatted['Open Price Today'] = '$' + result['Global Quote']['02. open'][:-2] 
    formatted['High Price Today'] = '$' + result['Global Quote']['03. high'][:-2]
    formatted['Low Price Today'] = '$' + result['Global Quote']['04. low'][:-2]
    formatted['Current Price'] = '$' + result['Global Quote']['05. price'][:-2]
    formatted['Volume'] = result['Global Quote']['06. volume'] + ' shares traded'
    formatted['Previous Close'] = '$' + result['Global Quote']['08. previous close'][:-2]
    formatted['Net Change'] = result['Global Quote']['09. change']
    formatted['Change Percent'] = result['Global Quote']['10. change percent']

    return json.dumps(formatted, indent=1)


#Generates the dictionary of currency codes and currency names from the .csv files
def currency_dict():
    currency = {}

    with open('p_currency.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            currency[row['currency name']] = row['currency code']

    with open('d_currency.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            currency[row['currency name']] = row['currency code']

    return currency


#Gives the current exchange information from one currency to another
def exchange(origin, destin):
    #Gets the information from the API
    endpoint = 'function=CURRENCY_EXCHANGE_RATE&from_currency=' + origin + '&to_currency=' + destin + '&apikey=QFK2H96NRYJTAHC7'
    r = requests.get('https://www.alphavantage.co/query?' + endpoint)
    result = r.json()

    #Gets relevant information
    o_name = result['Realtime Currency Exchange Rate']['2. From_Currency Name']
    d_name = result['Realtime Currency Exchange Rate']['4. To_Currency Name']
    rate = result['Realtime Currency Exchange Rate']['5. Exchange Rate']

    formatted = {}
    formatted['Origin'] = o_name
    formatted['Destination'] = d_name
    formatted['Rate'] = rate + ' ' + d_name

    return json.dumps(formatted, indent=1)


#Returns sector performances
#Gets information for sector
def sector_s(sector):
    #Gets the information from the API
    r = requests.get('https://www.alphavantage.co/query?function=SECTOR&apikey=QFK2H96NRYJTAHC7')
    result = r.json()
    result.pop('Meta Data')

    #Selects sector
    if sector == 'All':
        return result
    else:
        results = {}
        for period in result:
            if sector in result[period]:
                results[period[8:]] = result[period][sector]
        return results

#Gets information for sector and period
def sector(sector, period):
    s_info = sector_s(sector)
    
    if period == 'All Periods':
        return json.dumps(s_info, indent=1)
    elif period == 'Current':
        if sector == 'All':
            return json.dumps(s_info['Rank A: Real-Time Performance'], indent=1)
        return s_info['Real-Time Performance']
    else:
        for p in s_info:
            if period in p:
                if sector == 'All':
                    return json.dumps(s_info[p], indent=1)
                return s_info[p]


#Searches for an equity code given a keyword
def search_eq(keyword):
    keyword = helpers.underscore(keyword)
    url = 'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=' + keyword + '&apikey=QFK2H96NRYJTAHC7'
    r = requests.get(url)
    result = r.json()

    results = {}
    for dictionary in result['bestMatches']:
        results[dictionary['2. name']] = dictionary['1. symbol']

    return json.dumps(results, indent=1)


#Compiles stock functions
def trader():
    invest = True
    
    while invest:
        option = input('''
        Hello, my name is Cassandra Zini, and I am the trade specialist for the BOMB.
        Would you like to view some stock information? (Y/N)
        ''')

        if option in 'Yy':
            function = input('''
            Great! I'm very excited to help you today.
            Would you like to:
            1) View the current stock quote for a company?
            2) View the current exchange rates between two currencies?
            3) Look at sector performancies for a selected period?
            ''')

            if function == '1':
                search = input('''
                Do you need to search for an equity code?
                (Y/N)
                ''')
                while search not in 'YyNn':
                    search = input('''
                    Please give me a valid answer.
                    (Y/N)
                    ''')
                while search in 'yY':
                    keyword = input('''
                    What keyword or phrase would you like to search for?
                    Please, no special characters.
                    ''')
                    results = search_eq(keyword)
                    print('Here are your results:')
                    print(results)
                    search = input('''
                    Do you need another search?
                    (y/n)
                    ''')

                    while search not in 'YyNn':
                        search = input('''
                        Please give me a valid answer.
                        (Y/N)
                        ''')


                equity = input('''
                Please enter the equity code you would like to request information about.
                ''')
                info = quote(equity)
                print('Here is the infomation you have requested about the entity related to the ' + equity + ' equity code.')
                print(info)

            elif function == '2':
                search = input('''
                Do you need to search for the currency code?
                (Y/N)
                ''')
                while search not in 'YyNn':
                    search = input('''
                    Please give me a valid answer.
                    (Y/N)
                    ''')
                while search in 'yY':
                    currencies = currency_dict()
                    name = input('''
                    What currency would you like to search for? 
                    Please give me the name with proper capitalization.
                    ''')
                    print('The code you are looking for is', currencies[name], '.')
                    search = input('''
                    Do you need another code?
                    (Y/N)
                    ''')
                    while search not in 'YyNn':
                        search = input('''
                        Please give me a valid answer.
                        (Y/N)
                        ''')
                origin = input('''
                What currency would you like to start with?
                Please give me the currency code.
                ''')
                destination = input('''
                What currency would you like to convert to?
                Please give me the currency code.
                ''')
                info = exchange(origin, destination)
                print('Here is the information you have requested:')
                print(info)

            elif function == '3':
                s = input('''
                What sector would you like to get information about?
                Here are your options:
                All
                Communication Services
                Real Estate (note: no data available for 3 year, 5 year, or 10 year)
                Consumer Discretionary
                Information Technology
                Consumer Staples
                Utilities
                Health Care
                Industrials
                Materials
                Energy
                Financials
                ''')
                while s not in ['All', 'Communication Services', 'Real Estate', 'Consumer Discretionary', 'Information Technology', 'Consumer Staples', 'Utilities', 'Health Care', 'Industrials', 'Materials', 'Energy', 'Financials']:
                    s = input('''
                    That was not a valid sector. Your options are:
                    All
                    Communication Services
                    Real Estate (note: no data available for 3 year, 5 year, or 10 year)
                    Consumer Discretionary
                    Information Technology
                    Consumer Staples
                    Utilities
                    Health Care
                    Industrials
                    Materials
                    Energy
                    Financials
                    ''')

                period = input('''
                What period would you like to get information about?
                Here are your options:
                All Periods
                Current
                1 Day
                5 Day
                1 Month
                3 Month
                Year-to-Date
                1 Year
                3 Year
                5 Year
                10 Year
                ''')
                while period not in ['All Periods', 'Current', '1 Day', '5 Day', '1 Month', '3 Month', 'Year-to-Date', '1 Year', '3 Year', '5 Year', '10 Year']:
                    period = input('''
                    That was not a valid period. Here are your options:
                    All Periods
                    Current
                    1 Day
                    5 Day
                    1 Month
                    3 Month
                    Year-to-Date
                    1 Year
                    3 Year
                    5 Year
                    10 Year
                    ''')
                print('Here is the information you have requested:')
                print(sector(s, period))
            
            else:
                print('I\'m sorry, but I cannot complete that search at this time.')

            fin = input('''
            Do you have all of the information you need?
            Y/N
            ''')
            while fin not in 'yYnN':
                fin = input('''
                Not to be pushy, but I need an answer.
                Yes or no? (Y/N)
                ''')
            if fin in 'Yy':
                print('''
                Thank you for speaking with me today!
                Come back later to see if we have started our trade broker program.
                ''')
                invest = False

        elif option in 'nN':
            print('''
            I'm sorry that I couldn't help you today.
            If you change your mind after you leave, please call the front desk and ask for Cassandra!
            ''')
            invest = False

        else:
            fin = input('''
            I'm sorry; I couldn't hear you.
            Can you repeat yourself? (Y/N)
            ''')
            while fin not in 'nNyY':
                fin = input('''
                I'm sorry; I couldn't hear you.
                Can you repeat yourself? (Y/N)
                ''')
            if fin in 'Nn':
                print('''
                I'm sorry for the miscommunication.
                If you change your mind about speaking to me, please call and ask for Cassandra.
                ''')
                invest = False