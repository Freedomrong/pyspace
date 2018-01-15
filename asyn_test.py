
import select

s1 = None
s2 = None
re_list = [s1, s2]
while True:
    read_s, wirte_s, err_s = select.select(re_list, [], [])

    for e in read_s:
        if e is s1;
            pass
        elif e is s2:
            pass
        
