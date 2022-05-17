import requests
import json

class CatAPI:
  def __init__(self):
    self.api_url = "https://api.thecatapi.com/v1/images/search"
    
  def get(self):
    response = requests.get(self.api_url)
      #calls the url defined

    #self.images = repsonse.json()
  
  def __str__(self):
    return self.image ['results']
    #uses url
    print ('Your cat breed is [breed]')

    