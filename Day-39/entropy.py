import math

def calculate_entropy(pass_count , fail_count):

    total = pass_count + fail_count

    if total ==0:
        return 0

    p_pass = pass_count / total    
    p_fail = fail_count / total

    entropy = 0

    if p_pass > 0:
     entropy -= p_pass *math.log2(p_pass)

    if p_fail > 0:
     entropy -= p_fail *math.log2(p_fail)

     return entropy


result= calculate_entropy(4,5)
print("Entropy:",result)