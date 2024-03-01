names = open('names.txt', 'r')
dict = {}

for l in names:
    first = l.split()[0]
    last = l.split()[-1]

    if last in dict.keys():
        dict[last].append(first)
    else:
        lname = [first]
    dict[last] = lname

print(dict)
    

#dic={}
#for line in  names :
#    name= line.split()
#    firstname = name[0] 
#    lastname = name[-1]
#    if lastname in dic.keys():
#        lname.append(firstname)
#    else :
#        lname= [firstname]
#    dic[lastname]= lname
#print (dic)
    

