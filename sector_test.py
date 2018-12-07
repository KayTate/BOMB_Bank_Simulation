import requests, json

def sector_p(period):
    #Gets the information from the API
    r = requests.get('https://www.alphavantage.co/query?function=SECTOR&apikey=QFK2H96NRYJTAHC7')
    result = r.json()
    result.pop('Meta Data')

    #Selects period
    if period == 'All Periods':
        return json.dumps(result, indent=1)
    elif period == 'Current':
        return json.dumps(result['Rank A: Real-Time Performance'], indent=1)
    else:
        for p in result:
            if period in p:
                return json.dumps(result[p], indent=1)
    

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

print(sector('Real Estate', 'All Periods'))