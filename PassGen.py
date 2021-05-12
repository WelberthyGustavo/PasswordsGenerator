import random
import  time

#banner
print("""   🄿🄰🅂🅂🅆🄾🅁🄳🅂
   🄶🄴🄽🄴🅁🄰🅃🄾🅁 \n""")
time.sleep(0.8)

#open file
file = open("passwords.txt","a+")
file.write("\nPASSWORDS: \n\n")

#Pass Alphabet 
carac = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890/?$&@,+^-:!.()/\~<>*#}{][]}"

print("Generating passwords... \n")
time.sleep(1)

#pilha
y = 0

#Generating 5 passwords
while y < 5:
	quant = random.randint(8,16)
	passwd = ""
	x = 0
	#Generating password
	while x < quant:
		passwd += random.choice(carac)
		x += 1
	print("Pass: ",passwd,"\n")
	
	#Write in file txt
	file.write(passwd)
	file.write('\n')
	
  #add is pilha
	y += 1
	time.sleep(1)

#close file
file.close()

print("Saved in file passwords.txt \n")
time.sleep(1)

#end
print("   ___Finishing___")

#Development by Welberthy Gustavo
