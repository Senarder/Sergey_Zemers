def sort_friend_list(s):
    split_list = []
    for i in s.split(';'):
        split_list.append(i.upper().split(':'))
    sorted_list = sorted(split_list, key=lambda x: (x[1], x[0]))
    return ''.join([f"({i[1]}, {i[0]})" for i in sorted_list])


string = "Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
print(sort_friend_list(string))
