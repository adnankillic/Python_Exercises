def flatten_list(f_list):
    flat_list = []
    for i in f_list:
        if type(i) is list:
            for k in i:
                flat_list.append(k)
        else:
            flat_list.append(i)
            
    return flat_list

nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10],11,12,13]
print('Original List', nested_list)
print('Transformed Flat List', flatten_list(nested_list))
            