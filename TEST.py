rates = input('Please Enter The Number of Supplier Rates')
rates = int(rates)

cities = []
id = []
prices = []

for x in range(0,rates+1):
    a = input('Enter Your City')
    cities.append(a)
    c = input('Enter your price')
    c = float(c)


    b = input('Enter your Supplier ID (A,B,C)')
    if b == 'A':
        check = input('How many days till check in?')
        if check == 1:
            c = c*0.5 + c
    elif b == 'B':
        check = input('How many days till check in?')
        if check<3:
            print('unable to book')
    elif b == 'C':
        check = input('How many days till check in?')
        if check>=7:
            c = c-(c*0.1)
    else:
        c = c+c*0.1


    id.append(b)
    prices.append(c)


queries = input('Enter user queries')
queries = int(queries)

q_cities = []
checkin = []

for x in range(0,queries+1):
    a = input('Enter City')
    q_cities.append(a)
    b = input('Enter days until checkin')
    checkin.append(b)


for x in queries:
    print(prices)