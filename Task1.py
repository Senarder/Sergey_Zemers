def filter_list(list):
    result = []
    for i in list:
        if type(i) == int:
            result.append(i)

    return result


print(filter_list([1, 2, 'a', 'b']))
print(filter_list([1, 'a', 'b', 0, 15]))
print(filter_list([1, 2, 'aasf', '1', '123', 123]))
