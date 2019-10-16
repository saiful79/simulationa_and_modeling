
import math

D_alpha = 16.9

li=[
0.41,0.68,0.89,0.94,0.74,0.91,0.55,0.62,0.36,0.27,
0.19,0.72,0.75,0.08,0.54,0.02,0.01,0.36,0.16,0.28,
0.18,0.01,0.95,0.69,0.18,0.47,0.23,0.32,0.82,0.53,
0.31,0.42,0.73,0.04,0.83,0.45,0.13,0.57,0.63,0.29
]


def get_run(positive_run,negation_run):
	count_p_run = 1
	count_n_run = 1
	for i in range(len(positive_run)-1):
		if positive_run[i]< positive_run[i+1]:
			continue
		else:
			count_p_run+=1
	
	for i in range(len(negation_run)-1):
		if negation_run[i]< negation_run[i+1]:
			continue
		else:
			count_n_run+=1
	
	return count_p_run,count_n_run



def run_frequency_postive(text_li):
	positive_run = []
	negation_run = []
	p_count = 0
	n_count = 0
	for i in text_li:
		if i =="+":
			n_count+=1
			negation_run.append(n_count)
			p_count = 0
		else:
			p_count+=1
			positive_run.append(p_count)
			n_count = 0
	# print("positive:",positive_run,"\n negation_run :",negation_run)
	positive_run_number,negative_run_number = get_run(positive_run,negation_run)

	print("Positve run :",positive_run_number,"Negative run :",negative_run_number)
	total_run = positive_run_number+negative_run_number

	print("Total run :",total_run)

	mean = (2*len(li)-1)/3
	varience = ((16*len(li))-29)/90

	result =  (total_run-mean)/math.sqrt(varience)

	print("Ua : %0.2f\n Q^2 : %0.2f"%(mean,varience))
	print("Z0 : %0.2f" %(result))

	if result <= D_alpha:
		print("Uniform distribution is not rejected")
	else:
		print("Uniform distribution is rejected")



text_li = []
for i in range(len(li)-1):
	if li[i]<li[i+1]:
		text_li.append("+")
	else:
		text_li.append("-")
print(text_li)
run_frequency_postive(text_li)



