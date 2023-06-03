### Slide หน้า 13
"""
เขียนโปรแกรมในการรับสตริง 1 จำนวน ซึ่งสตริงที่ประกอบไปด้วย a - z เก็บไว้ที่ตัวแปร str
หลังจากนั้นให้ทำการตรวจสอบดูว่าสตริงที่รับเข้ามานั้นมีสระ ซึ่งก็คือ a, e, i, o หรือ u หรือไม่
"""

# Coding
str = input('Enter a string: ')
print('\"%s\" constains vowel ==> %s' %(str, 'a' in str or 'e' in str or 'i' in str or 'o' in str or 'u' in str))