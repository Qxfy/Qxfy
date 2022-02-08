def people():
    names = []
    while True:
        totalnumber = input('Please enter number of people involved: ')
        if totalnumber.isnumeric()== False or int(totalnumber)<=0:
            print('Please enter a valid number of people!')
        else:
            for i in range(int(totalnumber)):
                person = input(f"Please enter person {i+1}'s name : ")
                names.append(person)
            print('Here are the people you added:')
            for i in range(len(names)):
                print(names[i])
            return names
def foods():
    foodnames = []
    prices = []
    while True:
        flag = 1
        food = input('Please enter food name : ')
        while True:
            price = input('Please enter price of the food (eg: if $12 just enter 12): ')
            if price.isalpha():
                print('Please enter valid input!')
            elif float(price)>0:
                foodnames.append(food)
                prices.append(float(price))
                break
        while True:
            choice = input('To continue adding press 1 and to stop press 2 : ')
            if choice == '1':
                break
            elif choice == '2':
                flag = 2
                break
            else:
                print('Please enter a valid input!')
        if flag == 2:
            print('Here are the foods you added and its prices !')
            for i in range(len(foodnames)):
                print(f'{foodnames[i]} : ${prices[i]}')
            break
    return foodnames,prices
def whoeatwhat(names,foodnames):
    foodlist = []
    for i in range(len(foodnames)):
        foodlist.append([])
    for x in range(len(foodlist)):
        for e in range(len(names)):
            while True: 
                eatornot=input(f'Did {names[e]} eat {foodnames[x]}? Press 1 if Yes and 2 if No : ')
                if eatornot == '1':
                    foodlist[x].append(names[e])
                    break
                elif eatornot == '2':
                    break
                else:
                    print('Please enter a valid input!')
    print('====================Summary====================')
    for i in range(len(foodlist)):
        print(f'People who ate {foodnames[i]} : {foodlist[i]}')
    return foodlist
def calculate(foodlist,prices,names):
    gst = 0
    service = 0
    while True:
        gstunconf = input('Please enter the GST (eg: if $12 just input 12 or if none just 0 ) : ')
        if gstunconf.isalpha():
            print('Please enter valid input!')
        elif float(gst)>=0:
            gst+=float(gstunconf)
            break
    while True:
        serviceunconf = input('Please enter Service Charge (eg: if $12 just input 12 or if none just 0 ) : ')
        if serviceunconf.isalpha():
            print('Please enter valid input!')
        elif float(gstunconf)>=0:
            service+=float(serviceunconf)
            break
    costperperson = {}
    numppl = len(names)
    keys = range(numppl)
    for i in keys:
        costperperson[i] = 0
    for i in range(len(foodlist)):
        count =0
        if count == len(foodlist):
            break
        count2 = 0
        while True:
            if names[count2] == foodlist[i][count]:
                costperperson[count2]+=prices[i]/len(foodlist[i])
                count+=1
                count2+=1
            else:
                count2+=1
                continue
            if count == len(foodlist[i]):
                break       
    vals = list(costperperson.values())
    costperperson = {k: v for k, v in zip(names, vals)}
    print('Here is how much each person should pay : ')
    total = 0
    for i in costperperson:
        costperperson[i]+=(gst/len(names)+service/len(names))
        total+=costperperson[i]
    for i in costperperson:
        print(f'{i} : ${costperperson[i]}') 
    print(f'Total ${total}')
    print('Does this match with your receipt?')     
    print('Thanks for using this! Hope it helps!')
def main():
    print("""
Welcome to calculating how much each person should pay for their food ! (idk what to call this program)
""")
    names = people()
    foodnames,prices = foods()
    foodlist = whoeatwhat(names,foodnames)
    calculate(foodlist,prices,names)
    quit = input('Press anything to quit.')
main()