EQUATION = "144/36=4"


def check_equation(input_eq: str) -> str:
    """
        n: not present
        w: wrong position
        c: correct
    """
    
    ret = [0, 0, 0, 0, 0, 0, 0, 0]

    count_dic = {}
    for i in EQUATION:
        if i in count_dic:
            count_dic[i] += 1
        else:
            count_dic[i] = 1


    for i in range(8):
        if input_eq[i] == EQUATION[i]:
            ret[i] =  "c"
            count_dic[input_eq[i]] -= 1
    
    for i in range(8):
        if input_eq[i] != EQUATION[i]:
            if input_eq[i] not in EQUATION:
                ret[i] = "n"
            else:
                if count_dic[input_eq[i]] > 0:
                    ret[i] = "w"
                    count_dic[input_eq[i]] -= 1
                else:
                    ret[i] = "n"
    return "".join(ret)
