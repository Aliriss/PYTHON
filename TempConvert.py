#TempConvert.py
TempStr=input("Please input tempresure with format (F(f)or C(c))")
if TempStr[-1] in['F','f']:
	C = ( eval ( TempStr [0:-1] ) - 32) / 1.8
	print("Transform is {:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
	F=1.8*eval(TempStr[0:-1])+32
	print("Transform is {:.2f}F".format(F))
else: print("ge shi cuo wu")
