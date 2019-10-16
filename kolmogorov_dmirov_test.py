print("Example 7.6 ")

D_alpha = 0.565

r =[0.81,0.14,0.44,0.93,0.05]

print("Given that : \n",r)
print("Critical value : ",D_alpha)
list1 = sorted(r, key=float)
number_of_len = len(r)

D_plus = []
D_minus = []
print("--------------------------------------------")
print("Ri \t i/N \t i/N-Ri \t Ri-(i-1)/N")
print("--------------------------------------------")
for i in range(number_of_len):
	i_div_n =(i+1)/number_of_len

	i_div_n_minus_r = i_div_n - list1[i]
	r_minus_i_minus_1_div_n = list1[i] - (i/number_of_len)

	D_plus.append(i_div_n_minus_r)
	D_minus.append(r_minus_i_minus_1_div_n)
	print('%.2f \t %.2f \t %.2f \t\t %.2f'% (list1[i],i_div_n,i_div_n_minus_r,r_minus_i_minus_1_div_n))
print("--------------------------------------------")

D_plus_max = max(D_plus)
D_minus_max =max(D_minus)
D_result = max(D_plus_max,D_minus_max)


print("output result :%.2f "%(D_result))

# print ("Ri : ",list1)
# print("i/N-Ri : ",D_plus)
# print("Ri-(i-1)/N",D_minus)

if D_result <= D_alpha:
	print("uniform distribution not rejected")
else:
	print("uniform distribution rejected")