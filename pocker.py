"""
3 Digit Poker Test
Writer: Sagor Sarker
"""

def calculate_probability():
    p_3_diff_digit = (9/10*8/10)
    p_3_like_digit = (1/10*1/10)
    p_exact_one_pair = 1 - p_3_diff_digit - p_3_like_digit
    p_list = [p_3_diff_digit, p_3_like_digit, p_exact_one_pair]
    return p_list

def calculate_d(p_list, ob_list):
    Ei = [x*ob_total for x in p_list]
    Ei_diff = [x1-x2 for (x1, x2) in zip(ob_list, Ei)]
    Ei_diff_sq = [x**2 for x in Ei_diff]
    d_list = [x1/x2 for (x1, x2) in zip(Ei_diff_sq, Ei)]
    d = sum(d_list)
    return Ei, Ei_diff, d_list, d


if __name__=="__main__":
    ob_list = [680, 31, 289]
    ob_total = sum(ob_list)
    print(ob_total)
    
    p_list = calculate_probability()
    print(p_list)
    Ei, Ei_diff, d_list, d = calculate_d(p_list, ob_list)
    print("---------------------------------------------------------------------")
    print("combination \t Oi \t Ei \t Oi-Ei \t (Oi-Ei)^2/Ei")
    print("---------------------------------------------------------------------")

    # combination = ['3 Different Digit', '3 Like Digit', 'Exact one pair']
    for i in range(3):
        print(i+1,"\t\t",ob_list[i],"\t",Ei[i],'\t',Ei_diff[i], '\t', d_list[i])
        
    print("\n---------------------------------------------------------------------")
    print("\t\t",sum(ob_list),"\t",int(sum(Ei)),"\t",sum(Ei_diff),"\t%0.2f"%(sum(d_list)))
    print("---------------------------------------------------------------------")
        
    d_alpha = 5.99

    print('='*50)
    print('Independence of the random number is: ')
    if d<d_alpha:
        print('Accepted')
    else:
        print('Rejected')