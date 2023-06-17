import csv
"""
Hello
This
Proud Ding
"""
##print("Enter a number:")
##num=input()
##print(type(num))
##
##print("Double number:",2*int(num))
##
##x=input()
##if x==5:
##    print("x is 5")
##elif x==7:
##    print("x is 7")
##else:
##    print("x is not 5 and not 7")
##
##for character in "python":
##    print(character)
##
##for i in range(2,42,2):
##    print(i)
##    
##i =2
##while i<=40:
##    print(i,end=" ")
##    i+=2

##def fun1(i,j,step):
##    for a in range(i,j,step):
##        print(a,end=" ")
##
##def cicle_area(radius):
##    area=3.1415926*radius**2
##    return area
##print(cicle_area(5))

##---lists---
##list_ints = [10,4,-2,9]
##print(list_ints)
##print(list_ints[1],list_ints[-3])
##
##list_ints[0]=4000
##print(list_ints)
##
####int数组可以加字符串
##list_ints[-1]="this is proud"
##print(list_ints)
##
##print(len(list_ints))
##list_ints.append(42)
##print(list_ints)
##
##empty_list=[]
##print(len(empty_list))
##嵌套数组
##nested_list=[[0,1],[2,3],[],[8]]
##print(nested_list)
##print(nested_list[1])
##
##print(nested_list[1][1])

##cities=["Hangzhou","Wenzhou","beijing","shanghai"]
##for city in cities:
##    print(city)
##i=0
##while i<len(cities):
##     print(cities[i])
##     i += 1
##
##cities +=["shenzhen","chongqing"]
##print(cities)
##
##repeated_list = 3*["guangzhou","tianjin"]
##print(repeated_list)
##print(cities)
####1,2不包括3
##print(cities[1:3])
####1-2
##print(cities[:2])
####2-end
##print(cities[2:])
##
##cities_copy = cities[:]
##print("copy-1:",cities_copy)
##
##cities_copy[0] = "HANGZHOU"
##print("copy-2:",cities_copy)
##
##print("original",cities)
##
##cities.append("new york city")
##print(cities)
##
##cities.remove("shanghai")
##print(cities)
####pop() delete based on index
##cities.pop(-1)
##print(cities)

##string_list = ["Z","I","M","E"]
##one_string ="-".join(string_list)
##print(one_string)
##
####comma_separated_value_string ="My-Name，is，Proud,Ding"
##
##sp = one_string.split("-")
##print(sp)

filename = "data.csv"
infile = open(filename,"r")
reader = csv.reader(infile)
table= []
header= []

for row in reader:
    
        print(row)        
   
##        table.append(row)

infile.close()
##print(header)
##print(table)
