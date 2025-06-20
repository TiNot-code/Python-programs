#Pokedle game inspired by pokedle.net

import random
import requests
from prettytable import PrettyTable 

class cl:
    # colors
    ec  = '\033[0m'     #end of color
    red = '\033[91m'    #red
    gr  = '\033[92m'    #green
    ora = '\033[93m'    #orange


# define class pokemon
class pokemon:
    def __init__(self, response_json):
        self.name       = response_json['name']
        self.type1      = response_json['types'][0]['type']['name']
        self.height     = response_json['height']
        self.weight     = response_json['weight']
        try:
            self.type2  = response_json['types'][1]['type']['name']
        except: 
            self.type2  = 'None'   
        self.data       = [self.name, self.type1, self.type2, self.height, self.weight]
    def __str__(self):
         return f"Name  : {self.name}\nType 1: {self.type1}\nType 2: {self.type2}\nHeight: {self.height}\nWeight: {self.weight}"
    
    def color(self, compare_poke):      # funciton to compare the data and change the color 
        for idx in range(len(self.data)):   # get the index of self.data in loop
            if(type(self.data[idx]) == int):    # check for height and weight and add the arrow 
                if(self.data[idx] < compare_poke.data[idx]):    # check number is bigger
                    self.data[idx] = cl.red+str(self.data[idx])+cl.ec+' ↑'
                elif(self.data[idx] > compare_poke.data[idx]):  # if number is smaller 
                    self.data[idx] = cl.red+str(self.data[idx])+cl.ec+' ↓'
                else:   # paint green
                    self.data[idx] = cl.gr+str(self.data[idx])+cl.ec                
            elif(self.data[idx] == compare_poke.data[idx]): # if equal -> change color to green
                self.data[idx] = cl.gr+str(self.data[idx])+cl.ec                
            else: # color red 
                self.data[idx] = cl.red+str(self.data[idx])+cl.ec
    
def api_call(url: str) -> dict | None: # function for api calls
    base_url = 'https://pokeapi.co/api/v2/'
    try:    # try to fetch api
        apiresponse = requests.get(base_url+url)
        if apiresponse.status_code == 200:  
            return apiresponse.json()   # return response as json 
        elif apiresponse.status_code == 404:
            return None
        else:
            print(apiresponse.status_code)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def pokeapi_num() -> int:
    # this function generates an id for the Pokeapi || all available ids are: 1-1025 10001-10277
    ran_num = random.randint(1,1302)    # generate random number
    if(ran_num > 1025):     # increase the numbers above 1025 to >=10001
        ran_num =+ 8975
    return ran_num
        
def main():
    result_pokemon_details = api_call(f'/pokemon/{pokeapi_num()}')    # call api with the random number
    correct_poke = pokemon(result_pokemon_details)  # create class pokemon for the correct pokemon   
    # create Table for visual output
    table_header = ['Name','Type 1', 'Type 2', 'Height', 'Weight']  
    table = PrettyTable(table_header)
    
    user_guessed_correct = False    # declare win condition
    while user_guessed_correct == False: # user guesses the right Pokemon
        try:
            userinput = input('Type your guess: ')  # user guesses the pokemon
        except: # prevent ctrl+c error
            break
        
        guess_response = api_call(f'/pokemon/{userinput}')  # get api details for user input & store in class
        if(guess_response == None): # if userinput is invalid (404 response) -> retry
            print(f'{cl.ora}Your input is invalid, try again{cl.ec}')
            continue
        user_poke = pokemon(guess_response)
        if correct_poke.name == user_poke.name: # if the user guessed the right pokemon -> win 
            correct_poke.color(user_poke)   # color the data
            table.add_row(correct_poke.data)    # add and print table row with the right pokemon
            user_guessed_correct = True # change win condition
        else:
            user_poke.color(correct_poke)
            # add and print the user input pokemon
            table.add_row(user_poke.data)
            print(table)
    return print(f'{table}\nCongratulations you won')

# execute main function    
if __name__ == '__main__':
    main()
