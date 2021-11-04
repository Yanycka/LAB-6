import csv
zag=0
pr=0
my_list=[]
my_list1=[]
filename='The_Martian.txt'

fd=open(filename,'r')
for row in fd:
    pr=pr+row.count(' ')
    zag=zag+len(row)
    slova=row.split(' ')
    my_list.append(slova)

fd.close()
print('zagal`na cil`cist` sumvoliv=',zag)
print('cil`cist` probiliv=',pr)
print('slova=',len(my_list))

L=len(my_list)
L1=0
vsi_slova=0
uniq_slova=0
for i in range (L):
    L1=len(my_list[i])
    for j in range (L1):
        elem=my_list[i][j]
        vsi_slova=vsi_slova+1
        if elem in my_list1:
            continue
        else:
           my_list1.append(elem)
uniq_slova=len(my_list1)
print('vsi slova=', vsi_slova)
print('unikal`ni slova=', uniq_slova)