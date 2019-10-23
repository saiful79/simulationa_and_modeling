# Random Number Generation
# Combined Linear Congruential Method
# Writer: nahid

def clcg(a1=40014, c1=0, m1=2147482563, a2=40692, c2=0, m2=2147483399):
	clcg.seed1 = (a1*clcg.seed1 + c1) % m1
	clcg.seed2 = (a2*clcg.seed2 + c2) % m2
	x = (clcg.seed1-clcg.seed2) % (m1-1)
	if x > 0:
		return x/m1
	else:
		return (m1-1)/m1

clcg.seed1 = int(input("Enter the seed 1 : "))
clcg.seed2 = int(input("Enter the seed 2 : "))

for i in range(10):
	print(clcg())