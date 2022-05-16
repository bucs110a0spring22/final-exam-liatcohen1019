import requests 
import DogAPI
import CatAPI
#calls the classes 


def main():
  dapi = DogAPI.DogAPI()
  #calls the dog class
  breed = dapi.get() 
  #tells the program to use the dog class where breed is used
  data = dapi.__str__()
  capi = CatAPI.CatAPI()
  #calls the cat class
  breeds = capi.get()
   #tells the program to use the cat class where breeds is used
  image = capi.__str__()
  
  print('Your dog breed is [breeds]')
  print ('Your cat breed is [breed]')

  main()