

#main file





import os                    #to get the API key from the environment variable

                             #and also for changing the directory to the current dir,
                             #to create the logfile in the correct place,
                             #especially to avoid any kind of exception




import requests as req       #to handle the API call, aliased as req for wrting ease



import re                    #to sanatize user input for injection/attack prevention
                             #an important security layer 




import json                  #for handling the json data from the API response, 
                             #especially while converting it to python dict for our ease of 
                             #air quality calculation




import logging               #to keep real-time logs for the programs in a logfile,
                             #later stored in postgresql remote server




from typing import List      #used for type hinting   




#-----------------------











#changing the directory to the current directory 
#to avoid any kind of exceptions riased, while creating the logfile 
os.chdir(os.path.abspath(os.path.dirname(__file__)))





#creating the logfile for the program
logging.basicConfig(level=logging.DEBUG, filename='main_file_logfile.log',
                    filemode="a", format='%(levelname)s log at %(asctime)s | %(message)s',
                    datefmt='%I:%M:%S %p - %d/%m/%Y', encoding='utf-8')




#----------------------------











def check_air_quality(username: str, city: str) -> bool:
    #username is the name of the user, thus the one who's using the program

    """function to check the air quality"""






    #exception handling added to provide a better performance at production level
    try:

        #get the API key stored in the environment variable
        api_key=os.getenv("Air_Quality_API_Key")



        if not api_key:
            raise ValueError("Please set the API key in your environment variable to run the code.")






        #in case anyone tries to inject any malicious command
        if not re.match(r"^[a-zA-Z\s-]{2,50}$", city):
            print("Invalid city name.")
            

            #creating a log to keep a record of this situation in the logfile
            logging.error(f"API response failed; due to the user,   '{username}'   most probably tried to inject a malicious command,   '{city}'  , to break the program in any means.")


            #return a bool for the unit test
            return False
        






        else:
            #calling the api to fetch the weather data
            api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)



            #get the api key from the environment variable from your system and call the API
            #with a timeout of 10 second
            response = req.get(api_url, headers={'X-Api-Key': api_key}, timeout=10)
        




             #checking if the repsonse code is ok, otherwise the call may catch exception more easily
            if response.status_code == req.codes.ok:

                #when everthing is okay, thus the call is sucessfull,
            
            
                #converting that data (response.text) in a python dict
                #to make the logic rendering code more readable, in python
                python_data : dict = json.loads(response.text)







                #printing the values of the dict in a more human-readable way
                for key, value in python_data.items():


                    if isinstance(value, dict):
                    #If value is a dict, extract and print concentration and aqi

                        conc = value.get("concentration", "N/A")
                        aqi = value.get("aqi", "N/A")
                        print(f"Amount of {key} in air: concentration = {conc}, aqi = {aqi}")


                        



                    else:

                        # if the value is simple, ie overall aqi
                        print(f"Amount of {key} in air: {value}")
                       


                    



           

        








                #------------------

                """logic part for checking the weather condition based on scientific theories """




                #creating a list to compare the amount of pollutants
                aqi_list : List=[]
                # loop only for pollutants, skip the overall_aqi_response

                #based on the AQIs of all the pollutant, 
                #we're calculating the standard value
                for pollutant, aqi_info in python_data.items():
                    if isinstance(aqi_info, dict) and "aqi" in aqi_info:
                        aqi_list.append(aqi_info["aqi"])

               







                print("\n")  #print a blank line for code readability
                # or just use the overall_aqi directly
                standard_value : int = python_data.get("overall_aqi", max(aqi_list) if aqi_list else 0)

                print(f"Overall AQI for {city} is: {standard_value}")
                print("\n")   #print a blank line for code readability











                #main logic part for getting the weather condition based on the theory/formula    
                if 0 <= standard_value <= 50:
                    print(f"Today, the air quality in {city} is Good Enough! \n Have a nice day! Best wishes!")
                elif 51 <= standard_value <= 100:
                    print(f"Today, the air quality in {city} is Moderate. \n Don't worry, but always remember to Stay safe!")
                elif 101 <= standard_value <= 150:
                    print(f"Today, the air quality in {city} is only harmful for people with health-sensitivity, \n remember to stay safe if you have a sensitive health.")
                elif 151 <= standard_value <= 200:
                    print(f"Today, the air quality in {city} is Harmful for everybody. \n Beware of it")
                elif 201 <= standard_value <= 300:
                    print(f"Today, the air quality in {city} is Highly harmful for everybody")
                else:
                    print(f"Today, the air quality is in {city} Hazardous, \n High safety must be considered, especially in case you go outside.")






        
                #creating an info log when the API call response is successful
                logging.info(f"API response was successful; username: {username}     | user_input_city: {city}     | API call response data: {response.text} | Overall AQI: {standard_value} | Status Code: {response.status_code}")
            
                
                #return a bool for the unit test
                return True











            #in case the user provides an invalid city name as the input
            elif response.status_code==400:
                print("Please enter a valid city name to know its air quality/wheather conditon!")
            
                #creating a log to keep a record of this situation in the logfile
                logging.error(f"API response failed; due to the user,   '{username}'   provided an invalid city name   '{city}'  ,  Status Code: {response.status_code}.")


                #return a bool for the unit test
                return False






            #when there's something else wrong with the status code of the API call response
            else:
                print(f'Error:   \n Status Code: {response.status_code}, {response.text}')


                #creating a log to keep a record of this situation in the logfile
                logging.error(f'Error:   \n Status Code: {response.status_code}, {response.text}')



                #return a bool for the unit test
                return False

            





    #in case we get any exception, handle it gracefully
    except Exception as err:
        print(f"An error occured: {err}")

        
        #creating a log to keep a record of this situation in the logfile
        logging.error(f"API Call Failed; due to {err}")


        #return a bool for the unit test
        #new Flase ciloa ge
        return False




#-------------------------------










#running the main test to start program
if __name__=="__main__":

    
    print("\n")   #print a blank line for better strating, as well as code readability




    input_username : str = input("Enter your name: ").strip().capitalize()
    input_city : str = input("Enter a city name to check its Air Quality: ").strip().lower() 

    print("\n")   #print a blank line for code readability
    check_air_quality(input_username, input_city)





    print("\n")   #print a blank line for better ending, as well as code readability



