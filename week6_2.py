#### Slide หน้าที่ 13
''' 
เขียนโปรแกรมเพื่อรับสตริงเก็บไว้ที่ตัวแปร s แล้วแสดงออกที่จอภาพ
ในรูปแบบต่าง ๆ โดยการระบุลำดับที่
'''

# Coding
s = input('Enter a string: ')
print('You entered \"%s\"' %(s))
print('There are %d characters.' %(len(s)))
print('The first character is \'%s\'.' %(s[0]))
print('The last character is \'%s\'.' %(s[-1]))
print('The first five-characters is \'%s\'.' %(s[:5]))
print('\"%s\" is reversed to \"%s\".' %(s, s[::-1]))
