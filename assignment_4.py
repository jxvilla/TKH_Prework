def namelist(name1,name2,name3,):
    big_name = ''
    list = [name1,name2,name3,]
    for name in list:
        if len(name) > len(big_name):
            big_name = name
    return big_name
print(namelist('michael jackson','kid cudi','young thug'))