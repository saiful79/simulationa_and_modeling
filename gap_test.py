print("Gap test 7.4.4")
D_alpha= 0.136
li = [
4,1,3,5,1,7,2,8,2,0,7,9,1,3,5,2,7,9,4,1,6,3,
3,9,6,3,4,8,2,3,1,9,4,4,6,8,4,1,3,8,9,5,5,7,
3,9,5,9,8,5,3,2,2,3,7,4,7,0,3,6,3,5,9,9,5,5,
5,0,4,6,8,0,4,7,0,3,3,0,9,5,7,9,5,1,6,6,3,8,
8,8,9,2,9,1,8,5,4,4,5,0,2,3,9,7,1,2,0,3,6,3
]

gap_list_f = []
def get_gap_extend(list_value):
	# print(list_value)
	gap_list_f.extend(list_value)

def get_frequecy(i,obser_list):
	li_=[]
	for j in range(len(obser_list)):
		if i ==obser_list[j]:
			li_.append(j)
	li_map = [i,li_]
	return li_map

def gap_frequency(list_of_gap):
	print(list_of_gap)
	freq = {} 
	for item in list_of_gap: 
		if (item in freq): 
			freq[item] += 1
		else: 
			freq[item] = 1

	return freq

def main(interval):
	total_list = []
	for i in range(0,10):
		f = get_frequecy(i,li)
		if len(f[1]) !=0:
			total_list.append(f)

	print(total_list,"\n")

	value_and_gap_marge=[]

	for index in range(len(total_list)):
		gap_list = []
		for gap_in in range(len(total_list[index][1])-1):
			gap = total_list[index][1][gap_in+1]-total_list[index][1][gap_in]-1
			gap_list.append(gap)

		# index_and_gap=[]
		get_gap_extend(gap_list)

		print(total_list[index][0],"- Digit and Gap : ",len(gap_list))
		# print()
		value_and_gap=[total_list[index][0],gap_list]
		value_and_gap_marge.append(value_and_gap)

	print("maximu value: ",max(gap_list_f))

	uper_value = max(gap_list_f)

	unuse_value = []
	for u in range(uper_value):
		if u not in gap_list_f:
			sublist = [u,0]
			unuse_value.append(sublist)
	print("add unseen ",unuse_value,"\n")



	interation = (max(gap_list_f))/4
	if (interation-int(interation))> 0.5 :
		interation=int(interation)+1
	else:
		interation= int(interation)- 1

	# print(interation)

	freq = gap_frequency(gap_list_f)
	# print(freq)
	
	list_value_=[]
	for key, value in freq.items():
		x=[key,value]
		list_value_.append(x)

	# print(list_value_)

	final_result_list = list_value_ + unuse_value

	# print("fnal",final_result_list)

	value_touple = [b for a,b in sorted((tup[0], tup) for tup in final_result_list)]
	
	# print(value_touple)


	final_frequency = []
	start = 0
	end = interval
	print("---------------------------------------------------------------------------------------------")
	print("Gap lenght \t Frequency \t R.F \tC.F SN(x) \t F(x) \t|F(x)-SN(x)|")
	print("---------------------------------------------------------------------------------------------")
	C_R_sum = 0
	r_f = []
	for i in range(interation):
		sum_of_fre = 0 
		for j in range(start,end):
			sum_of_fre = sum_of_fre + value_touple[j][1]
			C_R = sum_of_fre/100
		final_frequency.append(C_R)
		C_R_sum=C_R_sum+C_R
		s = float(start)
		e =float(end-1)

		F_x = 1-(0.9)**end
		result_final=abs(F_x-C_R_sum)
		r_f.append(result_final)
		print("%0.2f/%0.2f"%(s,e),"\t",sum_of_fre,'\t\t',C_R,"\t",C_R_sum,'\t\t',"%0.4f"%(F_x),"\t",result_final)
		start = end
		end = start + interval
	# print(final_frequency)

	result_final_max_value=max(r_f)
	print("max value :",result_final_max_value)

	if result_final_max_value <= D_alpha:
		print("Uniform distribution is not rejected")
	else:
		print("Uniform distribution is rejected")



if __name__=="__main__":
	interval =int(input("Please inter interval 4 : "))
	main(interval)