def calculate_gini(pass_count, fail_count):

    total = pass_count + fail_count

    if total == 0:
        return 0

    p_pass = pass_count / total
    p_fail = fail_count / total

    gini = 1 - (p_pass ** 2 + p_fail ** 2)

    return gini


result = calculate_gini(5, 5)

print("Gini Index:", result)