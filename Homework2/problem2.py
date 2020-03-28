text = input('The old string: ')
if len(text)>=7:
    print(text)
else :
    print('The value should be 7 or more characters long')
txt = (int(len(text)/2)-1)
print ('Middle 3 characters:', text[txt:txt+3])
middle = text[txt:txt+3]
print ('The new string: ', text[:txt]+middle.upper()+text[txt+3:])