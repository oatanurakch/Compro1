#### Slide หน้าที่ 20
'''
เขียนโปรแกรมในการรับข้อมูลประกอบไปด้วย ชื่อ – สกุล เก็บไว้ที่ตัวแปร
name อายุ (จ ำนวนเต็ม) เก็บไว้ที่ตัวแปร age น้ำหนัก (เลขจำนวนจริง) เก็บไว้
ที่ตัวแปร weight และเพศ (male หรือ female) เก็บไว้ที่ตัวแปร sex เก็บ แล้ว
แสดงผลของข้อมูลเหล่านั้นออกที่จอภาพ โดยใช้ %d, %f และ %s ในการ
แสดงผลข้อมูลของตัวแปรต่าง ๆ
'''

# Coding 
name = input('Name: ')
age = int(input('Age: '))
weight = float(input('Weight: '))
sex = input('Sex: ')
print('Hi, %s' %name)
print('You are %d years old and your weight is %f.' %(age, weight))
print('You are %s.' %sex)