import requests

def superMegaFunction(index, data):
    day = data.get('forecast').get('forecastday')[index].get('date')
    temp = data.get('forecast').get('forecastday')[index].get('day').get('avgtemp_c')
    description = data.get('forecast').get('forecastday')[index].get('day').get('condition').get('text')
    print (day,': ','Average temperature: ',temp,' Conditions: ',description)


def main():
    while True:
        userInput = input("Input the city you want to see the weather forecast for 3 days (or type stop)\n")
        if userInput == 'stop':
            break
        else:

            url = 'http://api.weatherapi.com/v1/forecast.json?key=6d4789b0a67a43fba74105123240407&q='+userInput+'&days=3&aqi=no&alerts=no'
            response = requests.get(url)
            data_json = response.json()

            print ("3 day weather forecast for ", userInput,":")        
            for i in range (3):
                superMegaFunction(i, data_json)
main()