from ge import foege
import time

#if check_ge()== True and check_attempt()==True:
#    x,y = check_arrow()
#    move_to_node(x,y)
#    click()
#    time.sleep(random.uniform(0.5,1.5))
#    a,b = check_att_nego_b(x,y)
#   move_to_att_nego(a,b)
#    click()

#x,y 1: 1012,818| 2:1008, 808| 3:1005, 804| 4:1012, 821| 5:1338, 820| 6:1570,823
#7:1376, 597| 8:1013, 491
x1, y1 = 1012, 818
x2, y2 = 1008, 808
x3, y3 = 1005, 804
x4, y4 = 1012, 821
x5, y5 = 1338, 820
x6, y6 = 1570, 823
x7, y7 = 1376, 597
x8, y8 = 1013, 491

#a,b 1:1008, 808 | 2:1005, 804| 3:1012, 821| 4:1094, 809| 5:1521, 819|6:1525, 753
#7:1165,531 , 8: 1012, 476
a1, b1 = 1008, 808
a2, b2 = 1005, 804
a3, b3 = 1012, 821
a4, b4 = 1094, 809
a5, b5 = 1521, 819
a6, b6 = 1525, 753
a7, b7 = 1165, 531 
a8, b8 = 1012, 476

def start_2nd_ge():
	time.sleep(1)
	foege.hit(x1,y1)
	foege.collect(a1,b1)
	time.sleep(0.5)

	foege.hit(x2,y2)
	foege.collect(a2,b2)
	time.sleep(0.5)

	foege.hit(x3,y3)
	foege.collect(a3,b3)
	time.sleep(0.5)

	foege.hit(x4,y4)
	foege.collect(a4,b4)
	time.sleep(0.5)

	foege.hit(x5,y5)
	foege.collect(a5,b5)
	time.sleep(0.5)

	foege.hit(x6,y6)
	foege.collect(a6,b6)
	time.sleep(0.5)

	foege.hit(x7,y7)
	foege.collect(a7,b7)
	time.sleep(0.5)

	foege.hit(x8,y8)
	foege.collect(a8,b8)
	time.sleep(0.5)
	print('done')
