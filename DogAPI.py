import requests
import json

class DogAPI:
  def __init__(self):
    self.api_url = "https://dog.ceo/dog-api/documentation/random"
   # breeds = input ('random dog generator')
   # self.url = 
  def get(self):
    response = requests.get(self.api_url)
    #calls the url defined
    #self.images = repsonse.json()
  
  def __str__(self):
    return self.image ['results']
    #uses url
    print('Your dog breed is [breeds]')
  
    ##request.get(f'https://http.dog/[code].jpg')
    