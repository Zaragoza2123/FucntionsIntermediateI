#Update Values in Dictionaries and list
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1.
x[1][0]=15

#2.
students[0]['last_name'] = 'Bryant'
#3.
sports_directory['soccer'][0] = 'Andres'
#4 
z[0]['y']=30

#2 Iterate through a list of dictionaries 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(some_list):
    for x in range(0,4):
        print("first_name - " + students[x]['first_name'] + ", last_name - " + students[x]['last_name'])

iterateDictionary(students)

#3 Get Values From a List of Dictionary 
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#4. Iterate Through a Dictionary With List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    
    for x in some_dict:
        print(f"{len(some_dict[x])} {x}")
        for i in range(0,len(some_dict[x])):
            print(some_dict[x][i])


printInfo(dojo)