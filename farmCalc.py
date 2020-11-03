#select animals
#print out per day nutrition (ingredients)
#kible calculator will output meat/eggs and veggies needed
#print plots of land required for daily (optional for x ammount of days) given perfect conditions
#take into account ground fertility
#mix and match ground fertilty(exact number of plots respectiveky)
#for sun lamp, give out expected harvest given perfect conditions
#make local version
#host website
import json


with open("C:\\Users\\fucku\\Documents\\Animals.json", "r") as f:
	animalData = json.load(f)
with open("C:\\Users\\fucku\\Documents\\output.json", "r") as g:
	FarmingData = json.load(g)


class Animal:
  def __init__(self, name, nutrition, quantity,raw):
    self._name = name
    self._nutrition = nutrition
    self._quantity = quantity
    self._raw = raw#Hay/Kibble/Day
  @property
  def nutrition(self):
  	return self._nutrition
  @property
  def name(self):
  	return self._name
  @property
  def quantity(self):
  	return self._quantity
  @property
  def raw(self):
  	return self._raw
  
  def nutritionNeeded(self):
  	return nutrition * quantity


def getAnimal(name,quantity):
	for i in  animalData:
		if i["Animal Name"] == name:
			return Animal(i["Animal Name"], float(i["Nutrition Needed/Day"]),quantity, float(i["Hay/Kibble/Day"]) )

def herdNutritionPerDay(herd):
	total = 0
	for i in herd:
		total += (i.nutrition * i.quantity)
	return total
def herdNutritionPerXDays(herd, x):
	return HerdNutritionPerDay(herd) * x
def rawPerDay(herd):  #Kibble and raw have same nutrition value
	total = 0
	for i in herd:
		total += (i.raw * i.quantity)
	return total
def rawPerXDays(herd, x):
	return HerdNutritionPerDay(herd) * x

myHerd = []
command = ""
animalInput = False
command=input("What is your command:")
while command != "q":
	if command == 1:
		animalInput = True
		while animalInput: 
			tmpAnimal = raw_input("Please enter the animal name: ").strip()
			tmpQuantity = input("Please enter the number of animals on this group: ")
			myHerd.append(getAnimal(tmpAnimal,tmpQuantity))
			addAnother = input("Add Another one? (1)yes (2)no: ")
			if addAnother == 2:
				animalInput = False
		print(herdNutritionPerDay(myHerd),rawPerDay(myHerd))
		command=input("What is your command:")
		





