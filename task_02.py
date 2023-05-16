def coincidence(list = [], range = ()):

    ran = set(range)
    set_list = set(list)
    intersect = (set_list & ran)

    fl = []
    for i in set_list:

        if type(i) == float:
            int(round(i)) <=i < (int(round(i)) + 1)
            intersect.add(i)

    
    return sorted(intersect)
    
    
coincidence([1,2,3,4,5], range(3,6))
coincidence()
coincidence([None,1,'foo',4,2,2.5], range(1,4))