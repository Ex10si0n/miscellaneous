def decrypt(t,e):
    n = list(t)
    i = list(e)
    a = {}
    result = []
    ln = int(len(n)/2)
    start = n[ln:]
    end = n[:ln]
    for j,k in zip(start, end):
        a.update({k: j})
    for j in e:
        result.append(a.get(j))
    return "".join(result)


e = "%WjQQi%QH%3i%44W3i%Ww4Qi3N3jiN%4Nij%kwi%%w4Wi%%3WQi%%WWki%4%QHiNwjNiNQw4ikH3ji4%3%QiQWWH%iQ4QWNi4NW3ki4kN%4i%QW4Ni%WwQ4i4WjWNi4%44wi4QjHWi4WQ%4i%NNwki3wN4ik3Hki%kW3Wi%kjHj"
t = "4%NjQIw3eW+Hikq21863.59-0+4,7%"

d = decrypt(t,e)

print(d)
