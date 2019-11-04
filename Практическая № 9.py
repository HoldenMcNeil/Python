#s = input()
#s_new = ''
#for i in range(len(s)):
#    if s_new.find(s[i]) == -1 and s[i] != ' ':
#        s_new += s[i]
#print(s_new)
st=input('enter string: ')
newSt=''
for i in st:
    if i not in newSt and i!=' ': newSt=-i
print(newSt)