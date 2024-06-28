def ip_to_tuple(ip):
    return tuple(map(int, ip.split('.')))

def tuple_to_ip(t):
    return '.'.join(map(str, t))

def sort_ips(ip_list):
    return sorted(ip_list, key=ip_to_tuple)

with open("zaip.txt", 'r') as f:
    ips = f.read().splitlines()
sorted_ips = sort_ips(ips)
with open('ip.txt', 'w') as f1:
    for ip in sorted_ips:
        f1.write(ip+'\n')
a = ["1","255","0"]
b = []
def same_c_network(ipA, ipB):
    partsA = ipA.split('.')
    partsB = ipB.split('.')
    if int(partsB[3])-int(partsA[3]) >10 or int(partsA[3])-int(partsB[3]) >10:
        return False
    if len(partsA) != 4 or len(partsB) != 4:
        raise ValueError("不正确的ip格式")
    c_segmentA = '.'.join(partsA[:3])
    c_segmentB = '.'.join(partsB[:3])
    return c_segmentA == c_segmentB

def qian_hou(ip):
    in_qh = []
    parts = ip.split('.')
    qian = parts[0]+'.'+parts[1]+'.'+parts[2]
    hou = parts[3]
    in_qh.append(qian)
    in_qh.append(hou)
    return in_qh

with open("ip.txt", "r") as f:
    ff = f.read().splitlines()
for i in range(0,len(ff)):
    if i+1 != len(ff):
        if(same_c_network(ff[i],ff[i+1])):
            db = qian_hou(ff[i])
            if db[0] not in a:
                a[0] = db[0]
            db2 = qian_hou(ff[i+1])
            if db[1] < db2[1]:
                if int(db[1]) < int(a[1]):
                    a[1] = db[1]
                if int(db2[1]) > int(a[2]):
                    a[2] = db2[1]
            else:
                if int(db2[1]) < int(a[1]):
                    a[1] = db2[1]
                if int(db[1]) > int(a[2]):
                    a[2] = db[1]
        else:
            db = qian_hou(ff[i])
            if db[0] not in a:
                a[0] = db[0]
            if int(db[1]) < int(a[1]):
                a[1] = db[1]
            if int(db[1]) > int(a[2]):
                a[2] = db[1]
            if a[1] == a[2]:
                b.append(a[0] + "." + a[1])
            else:
                b.append(a[0] + "." + a[1] + "-" + a[2])
            a = ["1","255","0"]
    else:
        if (same_c_network(ff[i], ff[i - 1])):
            db = qian_hou(ff[i])
            if db[0] not in a:
                a[0] = db[0]
            db2 = qian_hou(ff[i - 1])
            if db[1] < db2[1]:
                if int(db[1]) < int(a[1]):
                    a[1] = db[1]
                if int(db2[1]) > int(a[2]):
                    a[2] = db2[1]
            else:
                if int(db2[1]) < int(a[1]):
                    a[1] = db2[1]
                if int(db[1]) > int(a[2]):
                    a[2] = db[1]
            if a[1] == a[2]:
                b.append(a[0] + "." + a[1])
            else:
                b.append(a[0] + "." + a[1] + "-" + a[2])
        else:
            a = ["1", "255", "0"]
            db = qian_hou(ff[i])
            if db[0] not in a:
                a[0] = db[0]
            if int(db[1]) < int(a[1]):
                a[1] = db[1]
            if int(db[1]) > int(a[2]):
                a[2] = db[1]
            if a[1] == a[2]:
                b.append(a[0] + "." + a[1])
            else:
                b.append(a[0] + "." + a[1] + "-" + a[2])

# with open('ip_duan.txt', 'w+') as f1:
with open('ip_quan_duan.txt', 'w') as ff_qu:
    for i in b:
        # f1.write(i+'\n')
        if "-" in i:
            ff_qu.write(i+'\n')
def expand_ip_range(ip_range):
    parts = ip_range.split('.')
    start_ip = parts[-1].split('-')[0]
    end_ip = parts[-1].split('-')[1]
    base_ip = '.'.join(parts[:-1])

    start = int(start_ip)
    end = int(end_ip)

    ip_list = []
    for num in range(start, end + 1):
        ip_list.append(f"{base_ip}.{num}")

    return ip_list

with open('ip_quan_duan.txt', 'r') as ff_end:
    ff_end1 = ff_end.read().splitlines()
with open('ip_not_in.txt',"w") as f_not:
    for ip_xiao_duan in ff_end1:
        expanded_ips = expand_ip_range(ip_xiao_duan)
        with open('ip.txt', 'r') as f1_end:
            ff1_end = f1_end.read().splitlines()
            for ip in expanded_ips:
                if ip not in ff1_end:
                    f_not.write(ip+"\n")