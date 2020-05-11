weight = int (input('weight : '))
unit = input ('(L)bs or (K)g:')
if unit.upper() == "L":
    coverted = weight * 0.45
    print(f"You are {coverted} Kilos")
    # print("You are {} Kilos".format(str(coverted)))
else :
    coverted = weight /0.45
    print(f"You are {coverted} pounds")
i = 1
while i <= 5:
    print("*" * i)
    i = i + 1
is_hot = False
is_cold = False
if is_hot :
    print ("it's so hot !")
elif is_cold :
    print ("it's so code !")
else:
    print ("it's ok !")
print ("hello")
price = 100
has_good_credit = True
if has_good_credit :
    down_payment = 0.1 * price
else : down_payment = 1.2 * price
print (f"Down payment : ${down_payment}")

has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit :
    print("Eligible for loan"),
else :
    print("oui!")
temperature = 20
if temperature > 30 :
    print ("it's a good day")
elif temperature > 15 or temperature < 30 :
    print("it's ok ")
else :
    print ("it's a bad day")
name = "mingxuan"
print(len(name))
print((name)[5 : 8])
if len(name) < 3 :
    print ("you should be make 3 caractaire")
else :
    print(" you can login")
a,b = 1 ,2
while b < 10 :
    print(b ,end = " / ")
    a,b = b , a + b ,

age = int (input('your dag\'s age'))
print ("")
if age <= 0:
    print("are you kidding me")
elif age == 1 :
    print("he is a baby")
elif age == 2 :
    print("yes,he is 2 years old")
else:
    print("he is old")
number = 8.5
guess = -1
print("game for number")
while guess != number:
    guess = float(input('just mettre your number'))
    if guess == number:
        print("yes !! you win")
    elif guess < number:
        print("so small")
    elif guess > number:
        print ("so big")

a = 1
while a <= 10 :
    print(a)
    a += 2

n = 100
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 - %d total: %d" % (n,sum))
print('1- '+ str(n)+' total: '+ str(sum))
print((n,sum))
name = "your"
print("www.%s.com"% name)
print("www.%d %d.com" % (150 ,200))
print("www.%d.com"%(150))
langue = [ "c" , "c++" ,"PHP" ,"Python"]
for x in langue:
    print(x ,end = ".")
for i in range(-10,-101,-30) :
    print(i)
    # -30 espace



























