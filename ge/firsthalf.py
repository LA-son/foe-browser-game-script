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

#x,y 1: 380,596| 2:873,598 , 3:1009,428, 4:1011,469| 5:1008,817| 6: 1015,806
#7:778,820| 8:999,800| 9:1002,816
x1, y1 = 380, 596
x2, y2 = 873, 598
x3, y3 = 1009, 428
x4, y4 = 1011,469
x5, y5 = 1008,817
x6, y6 = 1015,806
x7, y7 = 778,820
x8, y8 = 999,800

#a,b 1st:534,618| 2:1014, 531| 3:1009,411| 4:1013,686| 5:1015,806| 6:970,810
#7:786,810| 8:1012,800
a1, b1 = 603, 614
a2, b2 = 1014, 531
a3, b3 = 1009,411
a4, b4 = 1013,686
a5, b5 = 1015,806
a6, b6 = 970,810
a7, b7 = 786,810
a8, b8 = 1012,800

def start_1st_ge():
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
