import json
import datetime

def load_inv(filepath):
	with open(filepath)as inv:
		data = json.load(inv)
		inv.close()
	return data

def save_inv(filepath, data):
	with open(filepath, 'w')as inv:
		json.dump(data, inv)
		inv.close()

def add(data, item):
	data.append(item)

def remove(data, item_index):
	data.pop(item_index)

def read_inv():
	print("Inventory read out")
	data = load_inv('inventory.json')
	i = 0
	while i<len(data):
		print('\n')
		print("Name:")
		print(data[i]["name"])
		print("\nLocation:")
		print(data[i]["location"])
		print("\nDate registered in inventory:")
		print(data[i]["date"])
		print("\nNotes")
		print(data[i]["note"])
		i = i+1
	print("End Of Inventory")

def add_item():
	name = input("Name : ")
	location = input("Location : ")
	date = str(datetime.date.today())
	note = input("Notes : ")
	data = load_inv("inventory.json")
	add(data, {"name": name, "location": location, "date": date, "note": note})
	save_inv("inventory.json", data)
	print("added new item!")

def remove_item():
	target = input("Please enter name of item to remove from inventory : ")
	data = load_inv("inventory.json")
	i = 0
	found = False
	while i<len(data) and not found:
		if target.upper() == data[i]["name"].upper():
			found = True
			remove(data, i)
			save_inv("inventory.json", data)
			print("item removed!")
			break
		i = i+1
	if not found:
		print("item could not be found are you sure you spelt it correctly?")

while True:
	print('''
1.) read the inventory
2.) add an item to the inventory
3.) remove item form inventory
4.) quit ''')
	action = input("enter option number ==> ")
	if action in ["1", "2", "3", "4"]:
		if action == "1":
			read_inv()
		if action == "2":
			add_item()
		if action == "3":
			remove_item()
		if action == "4":
			print("Exiting...")
			exit()
	else:
		print("input not recognised please try again")
