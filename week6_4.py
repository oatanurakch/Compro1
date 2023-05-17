#### Slide หน้าที่ 22

'''
เขียนโปรแกรมเพื่อรับสตริง รับอินเด็กซ์ จุดเริ่มต้น จุดสิ้นสุด ลำดับขั้น
ในการเลื่อน แล้วแสดงผลออกที่จอภาพ
'''

# Coding
s = input('Enter a string: ')
start = int(input('Display data at index: '))
print('Data at index %d is \'%s\'' %(start, s[start]))
start = int(input('Start display data at index: '))
stop = int(input('Stop display data at index: '))
step = int(input('Step to move: '))
print('Data from index %d to %d is \'%s\'' %(start, stop, s[start:stop:step]))