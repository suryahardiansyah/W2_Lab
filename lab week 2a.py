#Surya Hardiansyah

#### fix the following errors!
#### do not use any web-based resources to figure them out

#1
# x = '10'
x = 10  # remove the single-quotes so we can do math with x and y
y = 20
print(x + y)
# OR
x = '10'
y = '20'  # add single-quotes so we can concatenate x and y as a string
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list) # the length is 8
# print(my_list[my_list_len]) # this code doesn't work
# that also means print(my_list[8])
# there is no indexed-8 item in my_list
# remember [start:stop:step] so we can code like:
print(my_list[:my_list_len]) # start from beginning, stop before 8th index
print(my_list[::my_list_len]) # print 1st item and next items after 8 steps
print(my_list[my_list_len-1]) # print last item from the list

#3
my_string = 'hello world'
# print(my_string.upper) # the .upper() method lacks parentheses ()
print(my_string.upper())

#4
z = ['a', 'b', 'c'] # the list consists of 0th to 2nd item indexes
# z[3] = 'd' # there is no 3th index
z[2] = 'd' # we can alter the 2nd index item if you want
print(z) # ['a', 'b', 'd']

#5 run all these lines at once. why does the x not display 10, 
#followed by the 200?  Fix it so it does.
x = 10
x # it will show 10 if we only run this code alone, 
# not at once before another declaring code
print(x) # code to fix undisplaying x
y = 20
print(x * y)

#6
blue = 'blue' # need to define blue first
# color = 'My favorite color is {}, what is yours?' % blue 
# curly parentheses {} is not the pair of percent %
# the pairs are {} with .format(blue) and %s with % blue
color = 'My favorite color is %s, what is yours?' % blue
print(color)

#7
yellow = 'yellow' # don't forget to define yellow
color = 'My favorite color is {}, what is yours?'.format(yellow)
print(color)

#8
red = 'red' # define red before running the next code
color = f'My favorite color is {red}, what is yours?'
print(color)

#### answer the following questions by adding lines, but without changing the code given

#9 make the entries in this list unique
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools = set(schools) # redefine the list into set
print(schools) # printed set will only show unique value

#10 change the 'dog' entry to 'cat'
animals = tuple(['bird', 'horse', 'dog', 'fish']) 
# tuple object doesn't support item assignment
animals = list(animals) # redefine animals as a list
# animals = ['bird', 'horse', 'dog', 'fish'] 
animals[2] = 'cat'
print(animals)

#11 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'All that snow we had this winter sure was fun!'
print(my_sent.lower().split())
