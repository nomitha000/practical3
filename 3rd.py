import random 
length = int(input("Enter the  length of password required :"))
fh=open('output3.txt','w')
char_included = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^~&*123456790"
i = 0
password = ' '
while (i < length) :
    password =password + random.choice(char_included)
    i = i +1
print('Password = ',password)  
fh.write(f'your password is {str(password)}')
fh.close()
