#### Slide หน้าที่ 24
'''
เขียนโปรแกรมในกำรรับข้อมูลประกอบไปด้วย ชื่อ เก็บไว้ที่ตัวแปร name อายุ เก็บไว้ที่ตัวแปร age
น้ำหนัก เก็บไว้ที่ตัวแปร weight และเก็บข้อมูลการจองพื้นที่ในกำรแสดงผลของข้อมูลทั้ง 3 โดยการ
จองพื้นที่สำหรับแสดงแข้อมูลแต่ละข้อมูลนั้นจะไม่เกิน 10 ช่อง
'''

# Coding 
print('Display data as your request')
name = input('Enter name: ')
age = int(input('Enter age: '))
height = int(input('Enter height: '))
print('Your name: %s' %(name))
print('Your age: %d' %(age))
print('Your height: %d' %(height))
space_name = input('Enter space for name: ')
space_name = '%' + space_name + 's'
space_age = input('Enter space for age: ')
space_age = '%' + space_age + 'd'
space_height = input('Enter space for height: ')
space_height = '%' + space_height + 'd'
print('1234567890' * 3)
print(space_name %(name), space_age %(age), space_height %(height), sep = '')
