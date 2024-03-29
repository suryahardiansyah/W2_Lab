#Surya Hardiansyah
#Unless otherwise noted, try solving these using class content and without searching online
print('Q1')
#1
#Modify this code so that when i is 5 it doesn't print anything (including Finished!)
#and instead moves directly onto 6, while leaving it unchanged for other values of i
i = 0
while i < 10:
    if i < 5:
        print('little')
    elif i ==5: # set special condition when i equals 5
        i += 1
        continue
    elif i > 5:
        print('big')
    else: # this code wouldn't be run since there is no such condition here
        print('what happened?')
    print('Finished!')
    i += 1
        
print('')
print('Q2')
#2
#Write a for loop that prints this pattern:
#HINT: you can write a for-loop inside of a for-loop

#1
#1 2
#1 2 3
#1 2 3 4
for row in range(1, 4 + 1): # outer loop (1st to 4th row)
    for item in range(1, row + 1): # inner loop (items in each row)
        print(item, end=' ') # use end =' ' to print respective items in a row
    print() # next line for new row
# inspired by: https://pynative.com/print-pattern-python-examples/

print('')
print('Q3')
#3
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]  
#NOTE:  The spacing is just to show which numbers are converted to which
#HINTS: There are three steps here: mapping, filtering, and flattening the nested lists
#       Try doing this in a for-loop, then try doing it in a list comprehension
#       You may need to check StackOverflow for how to flatten a nested list
print('Using for-loop:')
# Here goes the for-loop
# inspired by: https://www.programiz.com/python-programming/examples/flatten-nested-list
mapped = [] # convert items using mapping step e.g. divided by 2
for sublist in start_list:
    mapped_sublist = []
    for item in sublist:
        mapped_sublist.append(int(item/2))
    mapped.append(mapped_sublist)
print(mapped)

flattened = [] # flatten into one-line list
for sublist in mapped:
    for item in sublist:
        flattened.append(item)
print(flattened)

filtered = [] # i only want to get unique items
for item in flattened:
    if item in filtered:
        continue
    else:
        filtered.append(item)
print(filtered)

print('Using list comprehension:')
# Here goes the list comprehension
mapped = [[int(item/2) for item in sublist] for sublist in start_list]
print(mapped)
flattened = [item for sublist in mapped for item in sublist]
print(flattened)
filtered = [item for item in set(flattened)] 
# set(flattened) convert list to set and only show uniques
print(filtered)
# if/else filtered list comprehension reference:
# https://stackoverflow.com/questions/4260280/if-else-in-a-list-comprehension


print('')
print('Q4')
#4
import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime.datetime(1999, 2, 23),
#              'Sarah': datetime.datetime(2001, 9, 1),
#              'Zach': datetime.datetime(2005, 8, 8)}
#HINTS: The datetime library has a function that turns strings of the right format into dates
#       Again, start with a for-loop, but make a dictionary comprehension in the end
print('Using for-loop:')
from datetime import datetime
end_dict_keys =[]
end_dict_values =[]
for key, val in start_dict.items():
    end_dict_keys.append(key.capitalize())
    end_dict_values.append(datetime.strptime(val, '%m/%d/%Y').date())
# strings to datetimes reference: 
# https://www.datacamp.com/tutorial/converting-strings-datetime-objects
end_dict = {}
for key in end_dict_keys:
    for val in end_dict_values:
        end_dict[key] = val
        end_dict_values.remove(val)
        break
print(end_dict)
# 2 lists to dictionary reference:
# https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/

print('Using dictionary comprehension:')
# dictionary comprehension
end_dict = {key.capitalize() : datetime.strptime(val, '%m/%d/%Y').date() for key, val in start_dict.items()}
print(end_dict)
#1. datetime.strptime() gives me datetime.datetime(1999, 2, 23, 0, 0)
#2. adding .date() at the end gives me datetime.date(1999, 2, 23)
# i prefer the 2nd since we don't need to care about hours and minutes for DOB