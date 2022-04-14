# Print each persons name and twitter handle etc., using groups, should look like:
#  [
#     ([first name] [last name],
#      email, 
#      phone,
#      title,
#      Twitter handle)
# ]

import re
file = open('./names.txt', encoding='utf-8')

data = file.read()

information = """Hawkins, Derek	derek@codingtemple.com	(555) 555-5555	Teacher, Coding Temple	@derekhawkins
Milliken, Connor	connor@codingtemple.com	(555) 555-5554	Teacher, Coding Temple
Johnson, Joe	joejohnson@codingtemple.com		Carter, Joel
Österberg, Sven-Erik	governor@norrbotten.co.se		Governor, Norrbotten	@sverik
, Tim	tim@killerrabbit.com		Enchanter, Killer Rabbit Cave
Butz, Ryan	ryanb@codingtemple.com	(555) 555-5543	CEO, Coding Temple	@ryanbutz
Doctor, The	doctor+companion@tardis.co.uk		Time Lord, Gallifrey
Exampleson, Example	me@example.com	555-555-5552	Example, Example Co.	@example
Obama, Barack	president.44@us.gov	555 555-5551	President, United States of America	@potus44
Patel, Ripal	ripalp@codingtemple.com	(555) 555-5553	Teacher, Coding Temple	@ripalp
Vader, Darth	darth-vader@empire.gov	(555) 555-4444	Sith Lord, Galactic Empire	@darthvader
Fernández de la Vega Sanz, María Teresa	mtfvs@spain.gov		First Deputy Prime Minister, Spanish Govt."""
   
info = re.findall('''
            (\s[\w]+\,\[\w]+)                  #first_name last_name
            (\s[\w\d]\W*@[\w][\w\d]+)        #email
            (\(?\d{3}\)?\s?-?\d{3}-\d{4})    #phone number
            (\s{2}[\w]+?\,\s[])               #title
            (@[a-z])                         #twitter
                ''', information, re.X)

names = []
for name in info: 
    person_name = {
        'flname' : name[0],
        'email' : name[1],
        'phone' : name[2],
        'title' : name[3],
        'twitter' : name[4]
    }
    names.append(person_name)

print(info)