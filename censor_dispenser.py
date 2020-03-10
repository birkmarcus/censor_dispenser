# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

sentence_1 = "learning algorithms"

def email_splitter(email):
	email = email.split()
	return email


email_one = email_one.replace('learning algorithms', '**** ****')
print(email_one)