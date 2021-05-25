# your code goes here

employees=[
	
	{
		"Name":"Bappy",
		"Age": 25,
		"Salary": 33000
	},
	{
		"Name":"Mehedi",
		"Age": 23,
		"Salary": 32000
	},
	{
		"Name":"Sifat",
		"Age": 25,
		"Salary": 34000
	},
	{
		"Name":".Shuvo",
		"Age": 24,
		"Salary": 32000
	},
	{
		"Name":"Sohel",
		"Age": 23,
		"Salary": 32000
	},
	{
		"Name":"Avi",
		"Age": 24,
		"Salary": 34000
	}
]

# def get_name(employee):
#     return employee.get('Name')


# def get_age(employee):
#     return employee.get('Age')


# def get_salary(employee):
#     return employee.get('Salary')
    
# employees.sort(key = get_salary,reverse=True)
# print(employees, end='\n\n')

# print sorted(employees, key = lambda x : x['Salary'], reverse=True)

# list1=sorted(employees, key = lambda i: (-i["Salary"], -i["Age"],i["Name"]))
# print(list1)

employees.sort( key = lambda i: (-i["Salary"], -i["Age"],i["Name"]))
print(employees)



