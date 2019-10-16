D_alpha = 16.9

li=[
0.34,0.90,0.25,0.89,0.87,0.44,0.12,0.21,0.46,0.67,
0.83,0.79,0.79,0.64,0.70,0.81,0.94,0.74,0.22,0.74,
0.96,0.99,0.77,0.67,0.56,0.41,0.52,0.73,0.99,0.02,
0.47,0.30,0.17,0.82,0.56,0.05,0.45,0.31,0.78,0.05,
0.79,0.71,0.23,0.19,0.82,0.93,0.65,0.37,0.39,0.42,
0.99,0.17,0.99,0.46,0.05,0.66,0.10,0.42,0.18,0.49,
0.37,0.51,0.54,0.01,0.81,0.28,0.69,0.34,0.75,0.49,
0.72,0.43,0.56,0.97,0.30,0.94,0.96,0.58,0.73,0.05,
0.06,0.39,0.84,0.24,0.40,0.64,0.40,0.19,0.79,0.62,
0.18,0.26,0.97,0.88,0.64,0.47,0.60,0.11,0.29,0.78
]

print("The observation numer:\n",li)
print("Critical number :",D_alpha)

def frequecy_count(interval,li):
	frequecy_count_li=[]
	for i in range(len(interval)):
		count=0
		for j in interval[i]:
			for x in li:
				if j==x:
					count+=1
		frequecy_count_li.append(count)
			# print(j)
	return frequecy_count_li
	# exit()


print("number of observation : ",len(li))

n = int(input("Enter the Interval 10 : "))
start = 0
end = n
total_inverval = []
for i in range(n):
	interval_list = []
	for j in range(start,end):
		interval_number_div=(j+1)/100
		interval_list.append(interval_number_div)
	total_inverval.append(interval_list)
	start = end
	end = start + n
	
# print(total_inverval)

frequecy_list = frequecy_count(total_inverval,li)

# print(frequecy_list)
print("---------------------------------------------------------------------")
print("interval \t Oi \t Ei \t Oi-Ei \t (Oi-Ei)^2 \t (Oi-Ei)^2/Ei")
print("---------------------------------------------------------------------")

Ei_sum = 0
Ei_minus_Oi_sum = 0
result_sum = 0
for i in range(n):
	Ei= frequecy_list[i]-n
	Ei_squre= Ei**2
	Ei_squre_divi_Ei= Ei_squre/n
	Ei_minus_Oi_sum = Ei_minus_Oi_sum+Ei
	Ei_sum = Ei_sum+n
	result_sum = result_sum+Ei_squre_divi_Ei
	print(i+1,"\t\t",frequecy_list[i],"\t",n,'\t',Ei,"\t",Ei_squre,"\t\t",Ei_squre_divi_Ei)

print("---------------------------------------------------------------------")
print("\t\t",sum(frequecy_list),"\t",Ei_sum,"\t",Ei_minus_Oi_sum,"\t \t \t %0.2f"%(result_sum))
print("---------------------------------------------------------------------")

if Ei_squre_divi_Ei <= D_alpha:
	print("Uniform distribution is not rejected")
else:
	print("Uniform distribution is rejected")


