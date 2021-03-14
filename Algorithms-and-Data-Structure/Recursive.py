def f(n):
    if n == 0: 
        return 1
    if n == 1: 
        return 0
    return (n-1) * (f(n-2) + f(n-1))

def displacements(t_list):
    if len(t_list) == 0:
        return []
    if len(t_list) == 1:
        return 
    else:
        for i in range(1, len(t_list)):
            t_list[0], t_list[i] = t_list[i], t_list[0]
            sublist = displacements(t_list[1:i] + t_list[i+1:])
            return [t_list[0]] + sublist[:i] + [t_list[i]] + sublist[i+1:]
            t_list[0], t_list[i] = t_list[i], t_list[0]
            return [t_list[0]] + displacements(t_list[1:])
            



if __name__ == '__main__':
    n = 10
    _list = list(range(n))
    for i in displacements(_list):
        print(i)
    
