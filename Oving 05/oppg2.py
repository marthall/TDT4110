# Takes input from user and checks for valid answer.
def user_input(question, valid_answer):
	old_valid_answer = valid_answer
	answer = input(question).lower()
	# Quit if the user types "hade"
	if answer == "hade":
		quit_program()
	# Converts answer to number if it is a number.
	if valid_answer == "num":
		try:
			answer = float(answer)
			valid_answer = [answer]
		except:
			None
	# Checks for valid answer and calls itself if not.
	if answer not in valid_answer:
			print("Ikke gyldig svar. Prov igjen")
			return(user_input(question, old_valid_answer))
	return answer

# gets the gender from the user.
def gender():
	gender = user_input("Hvilket kjonn(m/k) er du? ", ["m", "k"])
	return gender

# Checks if user is in the valid age group.
def is_valid_age():
	age = user_input("Hvor gammel er du? ", "num")
	if 15 < age < 25:
		return True
	else:
		print("Du er ikke i den tiltenkte malgruppen.")
		False

# Checks if user is active on social media.
def is_social_active():
	active = user_input("Er du aktiv i sosiale medier? ", ["ja", "nei"])
	if active == "ja":
		return True
	else:
		return False

# Checks if user is on facebook. 
def is_on_facebook(gender):
	if gender == "k":			# Different question dependent on gender.
		question = "Mellom 55-60% av Facebook sine brukere er kvinner. Er du en av disse? (ja/nei) "
	else:
		question = "Mellom 40-45% av Facebook sine brukere er menn. Er du en av disse? (ja/nei) "
	face = user_input(question, ["ja", "nei"])
	if face == "ja":
		return True
	else:
		return False
# Returns number of hours on social media per day.
def hours_active():
	hours = user_input("Hvor mange timer bruker du i snitt daglig pa sosiale medier? ", "num")
	return hours

# Prints out result and exits the program.
def quit_program():
	global num_male, num_female, num_face, num_sos, num_hours
	print("--------------------------------------")
	print("Antall menn:\t\t\t %i" % num_male)
	print("Antall kvinner:\t\t\t %i" % num_female)
	print("Antall sosiale medier:\t\t %i" % num_sos)
	print("Antall facebook:\t\t %i" % num_face)
	print("Antall timer sosiale medier:\t %i" % num_hours)
	print("--------------------------------------")
	exit()

def welcome():
	print("Velkommen til sporreundersokelse.")
	print("Du kan til enhver tid avslutte ved a skrive 'hade'")
	input("")

def main():
	while True:
		global num_male, num_female, num_face, num_sos, num_hours
		gen = gender()
		if not is_valid_age():
			print("\n" * 30)
			continue
		if is_social_active():
			hours = hours_active()
			on_face = is_on_facebook(gen)

			num_sos += 1
			if on_face:
				num_face += 1
			num_hours += hours
		
		if gen == "k":
			num_female += 1
		else:
			num_male += 1
		print("\n" * 30)

num_male = 0
num_female = 0
num_face = 0
num_sos = 0
num_hours = 0

print("\n" * 30)
welcome()
main()