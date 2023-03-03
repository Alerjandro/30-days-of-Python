t="Thirty"
d="Days"
o="Of"
p="Python"
space= " "
thirty_days_of_python=t + space + d + space + o + space + p
print(thirty_days_of_python)

c="Coding"
f="For"
a="All"
space= " "
coding_for_all=c + space + f + space + a
print(coding_for_all)

company="Coding For All"

print(len(company))

may = company.upper()
print (may)
min = company.lower()
print (min)
capital = company.capitalize()
print (capital)
tit = company.title()
print (tit)
swap = company.swapcase()
print (swap)
cut = slice(0, 6)
print (company[cut])

cod = 'Coding'
print (company.index(cod))
print (company.rindex(cod))
print (company.find(cod))                    
print (company.rfind(cod))                   

print (company.replace('python', 'coding'))

print (company.replace('Everyone', 'coding'))

company = 'Coding For All'
print (company. split()) # ['Coding', 'For', 'All']

print (company. split()) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print (company[0]) 

print  (company[-1])

print (company[10])

PFE = "Coding For All"
print (''.join(w[0] for w in PFE.split()))
print (''.join(w[0] for w in company.split()))

print (company.index('C'))

print (company.index('F'))

company = 'Coding For All People'
print (company.rfind('I'))

company = 'You cannot end a sentence with because because because is a conjunction'
print (company.index('because'))

company = 'You cannot end a sentence with because because because is a conjunction'
print (company.rindex('because'))

slicea = company [0:31]
sliceb = company [55:71]
print(slicea+sliceb)

