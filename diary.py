import datetime

def create_entry():

	now = datetime.datetime.now()
	date_string = now.strftime("%m-%d-%Y")
	file_name = f"diary_entry_{date_string}.txt"

	with open(file_name, "a") as f:
		f.write(f"\n\n{date_string}\n")
		while True:
			entry = input("Write your entry (type 'q' to quit): ")
			if entry == "q":
				break
			f.write(entry + "\n")

	print("Diary Entry Saved!")

def read_entry():

	date_string = input("Enter date (MM-DD-YYYY): ")
	file_name = f"diary_entry_{date_string}.txt"

	try:
		with open(file_name, "r") as f:
			print(f.read())
	except FileNotFoundError:
		print("No Entry Found For That Date.")

while True:
	choice = input("Do you want to (1) create a new entry, (2) read an entry, or (3) quit? ")
	if choice == "1":
		create_entry()
	elif choice == "2":
		read_entry()
	elif choice == "3":
		break
	else:
		print("Invalid choice.")