
x0 = 27
a = 17
c = 43
m = 100

print("Example 7.1 \n")
print("x0 : {} \na : {} \nc : {} \nm : {}".format(x0,a,c,m))

n = int(input("Enter the interation : "))
print("--------------------------")
print("xi \t\t Ri")
print("---------------------------")
for i in range(n):
	x = float(((a*x0)+c)%m)
	r = x / m
	x0 = x
	print(x,"\t\t", r)