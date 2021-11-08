# 1. The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary.
# Find the total number of characters in the file and save to the variable num.

fileref = open("travel_plans.txt","r")
num = 0
for i in fileref:
    num += len(i)
fileref.close()

# 2. We have provided a file called emotion_words.txt that contains lines of words that describe emotions.
# Find the total number of words in the file and assign this value to the variable num_words.

num_words = 0
fileref = "emotion_words.txt"

with open(fileref, 'r') as file:
    for line in file:
        num_words += len(line.split())

print("number of words : ", num_words)

# 3. Assign to the variable num_lines the number of lines in the file school_prompt.txt.

num_lines = sum(1 for line in open('school_prompt.txt'))

# 4. Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

f = open('school_prompt.txt', 'r')
beginning_chars = f.read(30)
print(beginning_chars)

# 5. Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

three = []

with open('school_prompt.txt', 'r') as f:
    three = [line.split()[2] for line in f]
    print(three)

# 6. Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.

fileref = open ("emotion_words.txt","r")
line = fileref.readlines()
emotions = []
for words in line:
    word = words.split()
    emotions.append(word[0])
print (emotions)

# 7. Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

f = open('travel_plans.txt', 'r')
first_chars = f.read(33)
print(first_chars)

# 8. Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.

fileref = open('school_prompt.txt', 'r')
words = fileref.read().split()
p_words = [word for word in words if 'p' in word]

# 1. At the halfway point during the Rio Olympics, the United States had 70 medals, Great Britain had 38 medals, China had 45 medals, Russia had 30 medals, and Germany had 17 medals. Create a dictionary assigned to the variable medal_count with the country names as the keys and the number of medals the country had as each key’s value.

medal_count = {'United States': 70, 'Great Britain': 38, 'China': 45, 'Russia': 30, 'Germany': 17}
print(medal_count)

# 2. Given the dictionary swimmers, add an additional key-value pair to the dictionary with "Phelps" as the key and the integer 23 as the value. Do not rewrite the entire dictionary.

swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4}
swimmers['Phelps'] = 23
print(swimmers)

# 3. Add the string “hockey” as a key to the dictionary sports_periods and assign it the value of 3. Do not rewrite the entire dictionary.

sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2}
sports_periods['hockey'] = 3
print(sports_periods)

# 4. The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics. But today, Spain won 2 more gold medals. Update golds to reflect this information.

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds["Spain"] = 21
print(golds)

# 5. Create a list of the countries that are in the dictionary golds, and assign that list to the variable name countries. Do not hard code this.

golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
countries = golds

# 6. Provided is the dictionary, medal_count, which lists countries and their respective medal count at the halfway point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for "Belarus" to the variable belarus. Do not hardcode this.

medal_count = {'United States': 70, 'Great Britain':38, 'China':45, 'Russia':30, 'Germany':17, 'Italy':22, 'France': 22, 'Japan':26, 'Australia':22, 'South Korea':14, 'Hungary':12, 'Netherlands':10, 'Spain':5, 'New Zealand':8, 'Canada':13, 'Kazakhstan':8, 'Colombia':4, 'Switzerland':5, 'Belgium':4, 'Thailand':4, 'Croatia':3, 'Iran':3, 'Jamaica':3, 'South Africa':7, 'Sweden':6, 'Denmark':7, 'North Korea':6, 'Kenya':4, 'Brazil':7, 'Belarus':4, 'Cuba':5, 'Poland':4, 'Romania':4, 'Slovenia':3, 'Argentina':2, 'Bahrain':2, 'Slovakia':2, 'Vietnam':2, 'Czech Republic':6, 'Uzbekistan':5}

belarus = medal_count.get("Belarus")
print(belarus)

# 7. The dictionary total_golds contains the total number of gold medals that countries have won over the course of history. Use dictionary mechanics to find the number of golds Chile has won, and assign that number to the variable name chile_golds. Do not hard code this!

total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111, "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87, "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22, "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209, "Uganda": 7,  "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
chile_golds = total_golds.get("Chile")
print(chile_golds)

# 8. Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016, and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing" to a variable fencing_value. Remember, do not hard code this.

US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3, "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2, "Golf": 1, "Weightlifting": 1}
fencing_value = US_medals.get("Fencing")
print(fencing_value)

# 1. The dictionary Junior shows a schedule for a junior year semester.
# The key is the course name and the value is the number of credits.
# Find the total number of credits taken this semester and assign it to the variable credits.
# Do not hardcode this – use dictionary accumulation!

Junior = {'SI 206':4, 'SI 310':4, 'BL 300':3, 'TO 313':3, 'BCOM 350':1, 'MO 300':3}
credits = 0
for v in Junior.values():
    credits += v
    print(credits)
    
# 2. Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.

from collections import Counter

str1 = "peter piper picked a peck of pickled peppers"
freq = Counter(str1)

for i in str1:
    print(i, freq[i])
    
# 3. Provided is a string saved to the variable name s1.
# Create a dictionary named counts that contains each letter in s1 and the number of times it occurs.

s1 = "hello"

def char_frequency(s1):
    dict = {}
    for n in s1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

counts = char_frequency(s1)
print(counts)

# 4. Create a dictionary, freq_words, that displays each word in string str1 as the key and its frequency as the value.

str1 = "I wish I wish with all my heart to fly with dragons in a land apart"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

freq_words = word_count(str1)
print(freq_words)

# 5. Create a dictionary called wrd_d from the string sent,
# so that the key is a word and the value is how many times you have seen that word.

sent = "Singing in the rain and playing in the rain are two entirely different situations but both can be good"

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

wrd_d  = word_count(sent)
print(wrd_d)

# 6. Create the dictionary characters that shows each character from the string sally and its frequency.
# Then, find the most frequent letter based on the dictionary. Assign this letter to the variable best_char.

sally = "sally sells sea shells by the sea shore"
characters = {}
for i in sally:
    characters[i]=characters.get(i,0)+1
    
sorted(characters.items(), key=lambda x: x[1])
best_char = sorted(characters.items(), key=lambda x: x[1])[-1][0]

# 7. Do the same as above but now find the least frequent letter.
# Create the dictionary characters that shows each character from string sally and its frequency.
# Then, find the least frequent letter in the string and assign the letter to the variable worst_char.

sally = "sally sells sea shells by the sea shore and by the road"

characters = {}
for i in sally:
    characters[i]=characters.get(i,0)+1
    
sorted(characters.items(), key=lambda x: x[1])
worst_char = sorted(characters.items(), key=lambda x: x[1])[-13][0]

# 9. Create a dictionary called low_d that keeps track of all the characters in the string p
# and notes how many times each character was seen. Make sure that there are no repeats of characters as keys,
# such that “T” and “t” are both seen as a “t” for example.

import collections
p = p = "Summer is a great time to go outside. You have to be careful of the sun though because of the heat."
low_d  = collections.defaultdict(int)

for c in p:
    low_d[c] += 1
        
for c in sorted(low_d, key=low_d.get, reverse=True):
    if low_d[c] > 1:
        print('%s %d' % (c, low_d[c]))

#  Write a function called int_return that takes an integer as input and returns the same integer. 




def int_return(ib):
    return ib
print(int_return(5))






# Write a function called add that takes any number as its input and returns that sum with 2 added. 








def add(a):
    return a+2

print(add(5))









#  Write a function called change that takes any string, adds “Nice to meet you!” to the end of the argument given, and returns that new string.












def change(v):
    return v+'Nice to meet you!'

v=input("Enter the string: ")
change(v)















#  Write a function, accum, that takes a list of integers as input and returns the sum of those integers. 











def accum(lst):
    j=0
    for i in lst:
        j=j+i
    return j
lst=[1,2,3,4,5,6,7,8,9]
accum(lst)














#  Write a function, length, that takes in a list as the input. If the length of the list is greater than or equal to 5, return “Longer than 5”. If the length is less than 5, return “Less than 5”. 














def length(lst):
    if len(lst)>=5:
        return 'Longer than 5'
    else:
        return 'Less than 5'

lst1=[1,2,3]
l1=[1, 1, 1, 1, 1]
l2=[4, 4, 4, 3, 5, 6, 7, 8, 9]

print(length(l2))
print(length(lst1))
print(length(l1))














#  You will need to write two functions for this problem. The first function, divide that takes in any number and returns that same number divided by 2. The second function called sum should take any number, divide it by 2, and add 6. It should return this new number. You should call the divide function within the sum function. Do not worry about decimals. 









def divide(n):
    return n/2
def sum(n):
    return n/2+6

sum(divide(10))


#  Create a tuple called olympics with four elements: “Beijing”, “London”, “Rio”, “Tokyo”





olympics=('Beijing','London','Rio','Tokyo')











#   The list below, tuples_lst, is a list of tuples. Create a list of the second elements of each tuple and assign this list to the variable country. 












tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country=[]
for i in tuples_lst:
    country.append(i[1])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
#  With only one line of code, assign the variables city, country, and year to the values of the tuple olymp. 










olymp = ('Rio', 'Brazil', 2016)
city=olymp[0]
country=olymp[1]   
year=olymp[2]













#  Define a function called info with five parameters: name, gender, age, bday_month, and hometown. The function should then return a tuple with all five parameters in that order. 










def info(name,gender,age,bday_month,hometown):
    f=(name,gender,age,bday_month,hometown)
    return f
info('sanjay','male',23,10,'bhopal')










#  Given is the dictionary, gold, which shows the country and the number of gold medals they have earned so far in the 2016 Olympics. Create a list, num_medals, that contains only the number of medals for each country. You must use the .items() method. Note: The .items() method provides a list of tuples. Do not use .keys() method. 











gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals=[]
for i in gold.items():
    num_medals.append(i[1])


#Write a function, sublist, that takes in a list of numbers as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the number 5 (it should not contain the number 5).
def sublist(x):
    sub = []
    x = (num for num in x) 
    num = next(x, 5)  
    while num != 5:
        sub.append(num)
        num = next(x, 5)  
    return sub

x = [1, 3, 4, 5, 6, 7, 3]
print(sublist(x))

#Write a function called check_nums that takes a list as its parameter, and contains a while loop that only stops once the element of the list is the number 7. What is returned is a list of all of the numbers up until it reaches 7.
def check_nums(x):
    sub = []
    x = (num for num in x) 
    num = next(x, 7)  
    while num != 7:
        sub.append(num)
        num = next(x, 7)  
    return sub

x = [1, 3, 4, 5, 6, 7, 3]
print(check_nums(x))

#Write a function, sublist, that takes in a list of strings as the parameter. In the function, use a while loop to return a sublist of the input list. The sublist should contain the same values of the original list up until it reaches the string “STOP” (it should not contain the string “STOP”).
def sublist(list):
   i = 0
   while i < len(list):

       if (list[i] == 'STOP'):
           return list[0:i]
       i+=1
   return list[0:i]
print(sublist(['mujju','salman','yo','STOP']))

#Write a function called stop_at_z that iterates through a list of strings. Using a while loop, append each string to a new list until the string that appears is “z”. The function should return the new list.
def stop_at_z(list):
   i = 0
   while i < len(list):

       if (list[i] == 'z'):
           return list[0:i]
       i+=1
   return list[0:i]
print(stop_at_z(['a','b','c','z']))

#Below is a for loop that works. Underneath the for loop, rewrite the problem so that it does the same thing, but using a while loop instead of a for loop. Assign the accumulated total in the while loop code to the variable sum2. Once complete, sum2 should equal sum1.

sum1 = 0
sum2 = 0
i = 0
lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x
print(sum1)
while i < len(lst):

    sum2 += lst[i]
    i = i + 1
    


print(sum2)


#Challenge: Write a function called beginning that takes a list as input and contains a while loop that only stops once the element of the list is the string ‘bye’. What is returned is a list that contains up to the first 10 strings, regardless of where the loop stops. (i.e., if it stops on the 32nd element, the first 10 are returned. If “bye” is the 5th element, the first 4 are returned.) If you want to make this even more of a challenge, do this without slicing
lst = [65, 78, 21, 33]
sum2 = 0
i =0
while i < len(lst):

    sum2 += lst[i]
    i = i + 1
    
print(sum2)




# 1. Create a function called mult that has two parameters, the first is required and should be an integer,
# the second is an optional parameter that can either be a number or a string but whose default is 6.
# The function should return the first parameter multiplied by the second.

def mult(a, b=6):
    return a * b
    
# 2. The following function, greeting, does not work. Please fix the code so that it runs without error.
# This only requires one change in the definition of the function.

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

# 3. Below is a function, sum, that does not work. Change the function definition so the code works.
# The function should still have a required parameter, intx, and an optional parameter, intz with a defualt value of 5.

def sum(intx, intz=5):
    return intz + intx
    
# 4. Write a function, test, that takes in three parameters: a required integer,
# an optional boolean whose default value is True, and an optional dictionary,
# called dict1, whose default value is {2:3, 4:5, 6:8}. If the boolean parameter is True,
# the function should test to see if the integer is a key in the dictionary.
# The value of that key should then be returned. If the boolean parameter is False, return the boolean value “False”.

def test(x, abool = True, dict1 = {2:3, 4:5, 6:8}):
    return abool and dict1.get(x, False)
    
# 5. Write a function called checkingIfIn that takes three parameters.
# The first is a required parameter, which should be a string.
# The second is an optional parameter called direction with a default value of True.
# The third is an optional parameter called d that has a default value of
# {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}.
# Write the function checkingIfIn so that when the second parameter is True,
# it checks to see if the first parameter is a key in the third parameter;
# if it is, return True, otherwise return False.

# But if the second paramter is False, then the function should check to see if the first parameter is not a key of the third.'
# If it’s not, the function should return True in this case, and if it is, it should return False.

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return True 
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return False
            
# 6. We have provided the function checkingIfIn such that if the first input parameter is in the third,
# dictionary, input parameter, then the function returns that value, and otherwise, it returns False.
# Follow the instructions in the active code window for specific variable assignmemts.

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('peas')
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('apples', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans= checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('potatos', False, {'carrots': 1, 'peas': 9, 'potatos': 8, 'corn': 32, 'beans': 1})




#Sort the following string alphabetically, from z to a, and assign it to the variable sorted_letters.
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters, reverse = True)

#Sort the list below, animals, into alphabetical order, a-z. Save the new list as animals_sorted.

animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

#The dictionary, medals, shows the medal count for six countries during the Rio Olympics. Sort the country names so they appear alphabetically. Save this list to the variable alphabetical.

medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
alphabetical = sorted(medals)


#Given the same dictionary, medals, now sort by the medal count. Save the three countries with the highest medal count to the list, top_three.
top_three = []
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
def g(k,d):
    return d[k]
ks = medals.keys()
top_three = sorted(ks,key=lambda x : g(x,medals),reverse = True)[:3]   

#We have provided the dictionary groceries. You should return a list of its keys, but they should be sorted by their values, from highest to lowest. Save the new list as most_needed.
most_needed = []
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
def g(k,d):
    return d[k]
ks = groceries.keys()
most_needed = sorted(ks, key=lambda x:g(x,groceries), reverse = True)

#Create a function called last_four that takes in an ID number and returns the last four digits. For example, the number 17573005 should return 3005. Then, use this function to sort the list of ids stored in the variable, ids, from lowest to highest. Save this sorted list in the variable, sorted_ids. Hint: Remember that only strings can be indexed, so conversions may be needed.
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

def last_four(x):
    
    return (str(x)[-4:])
last_four(ids)

sorted_ids = sorted(ids, key=last_four )
print(sorted_ids)

#$Sort the list ids by the last four digits of each id. Do this using lambda and not using a defined function. Save this sorted list in the variable sorted_id.

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_id = sorted(ids, key=lambda x: str(x)[-4:])

#
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']

lambda_sort = sorted(ex_lst, key = lambda x: x[1])
print(lambda_sort)













