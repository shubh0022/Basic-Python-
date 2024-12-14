#find out the index vlue of 'm' using find () in strindg ( intyermitdet)
str1= "hi my name is maddy"
for index,char  in enumerate("str1"):
 print(index,char)

#find out the index vlue of 'm' using find () in strindg (simple)
str1= "hi my name is maddy"
print([ i for i,char in enumerate(str1) if char =='m'])
