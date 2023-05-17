#### Slide หน้าที่ 19
''' 
เขียนโปรแกรมเพื่อรับสตริงเก็บไว้ที่ตัวแปร s แล้วแสดงการใช้เมธอดต่าง ๆ เพื่อแสดงผล
'''

# Coding
s = input('Enter a string: ')
print('You entered a string \"%s\"' %(s))
print('Capital only first character of each worsd ==> %s' %(s.title()))
print('All Uppercase ==> %s' %(s.upper()))
print('All Lowercase ==> %s' %(s.lower()))
print('Replace a space with \"---\" ==> %s' %(s.replace(' ', '---')))