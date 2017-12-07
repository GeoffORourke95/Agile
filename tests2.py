#In this task I was asked to accpet a list of 12 inputs and remove the 6th and 9th value
#Makes sure that 12 entries are inputted.
#Deletes the 5th as the list start are [0].
#Then the 7th to acommpany the change made by first del command.
#Print out unalter list.
#Print out altered list.


def nosixnine(orginallist): 
    del orginallist[5] #Deletes the 6th value
    del orginallist[7] #Deletes the 9th value
    return orginallist
print('''Welcome to task 3,
This function will remove the 6th and 9th element of your list.
''')
while True:
    
    print('Please enter 12 entries to begin, seperated with a space')
    orginallist = [(x) for x in input().split()] #Gets the inputs of user
    if len(orginallist) != 12: #Makes sure there is 12 entries
        print('Incorrent amount of enteries, please enter 12')
    else:
        break
    continue
print('Orginal List: '+(str(orginallist))) #Print unaltered list
print('Changed List: '+(str(nosixnine(orginallist)))) #Print new list (without 6th and 9th)
