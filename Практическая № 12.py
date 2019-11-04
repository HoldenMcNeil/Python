# myFile=open("re.txt","r")
# data=myFile.read()
# line= "О в ы из ц е н т ра "
# for line in :
#     line.strip('')
# print()
your_string ='ANDREWS VS BALL JA-15-0050 D0015 JUDGE EDWARD A ROBERTS'
print re.sub(r'\s{2,}','|',your_string.strip())