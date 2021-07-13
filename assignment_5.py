names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

def split_names_list(names_list):
    even_nameslist = []
    odd_nameslist = []
    for name in names_list:
        if len(name) % 2 == 0:
            even_nameslist.append(name)
        else:
            odd_nameslist.append(name)
    for replacingwb in range(len(even_nameslist)):
        even_nameslist[replacingwb] = 'b' + even_nameslist[replacingwb][3:]
    for replacingwc in range(len(odd_nameslist)):
        odd_nameslist[replacingwc] = odd_nameslist[replacingwc][:-1] + 'c'
    print("even list = ", even_nameslist)
    print("odd list = ", odd_nameslist)
    return even_nameslist
print(split_names_list(names_list))
