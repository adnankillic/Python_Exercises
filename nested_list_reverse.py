a = [[1,2], [3,4],[5,6,7]]

def reverse_list(r_list):
    
    result = list()
    
    for i in r_list:
        if type(i) is list:
            result.append(i[::-1])
        else:
            result.append(i)
    return print(result[::-1])

reverse_list(a)