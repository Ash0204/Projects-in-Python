def update_list(l1,l2,x):
    """
    Assumes l1 sorted in increasing order and l2 sorted in decreasing order, where l1 and l2 are lists
    and x is an incoming integer. It compares x with these two lists and
    updates them by appending x to the list under the constraint of
    maintaing the overall ordering of the list w.r.t magnitude of its elements   
    """
    mono_inc=l1[:]
    mono_dec=l2[:]
    if l1==[]:
        if x>l2[len(l2)-1]:
            mono_dec=[]
            mono_inc.append(l2[len(l2)-1])
            mono_inc.append(x)
        elif x==l2[len(l2)-1]:
            mono_inc.append(l2[len(l2)-1])
            mono_inc.append(x)
            mono_dec.append(x)
        else:
            mono_dec.append(x)
    elif l2==[]:
        if x>l1[len(l1)-1]:
            mono_inc.append(x)
        elif x==l1[len(l1)-1]:
            mono_dec.append(l1[len(l1)-1])
            mono_dec.append(x)
            mono_inc.append(x)
        else:
            mono_inc=[]
            mono_dec.append(l1[len(l1)-1])
            mono_dec.append(x)
    else:
        if x==l1[len(l1)-1] and x==l2[len(l2)-1]:
            mono_inc.append(x)
            mono_dec.append(x)
        elif x>l1[len(l1)-1]:
            mono_inc.append(x)
            mono_dec=[]
        else:
            mono_inc=[]
            mono_dec.append(x)
    return (mono_inc,mono_dec)
            
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first. Does not modify the list.
    Returns the sum of the longest run. 
    """
    if len(L)>2:
        L_init = L[0:2]
        L_rest = L[2:]
        result_list = []
        len_list = []
        for j in range(len(L_rest)+1):
            result_list.append([0,0])
            len_list.append(0)
        if sorted(L_init)==L_init and sorted(L_init,reverse=True)!=L_init:
            l1=L_init
            l2=[]
        elif sorted(L_init,reverse=True)==L_init and sorted(L_init)!=L_init:
            l1=[]
            l2=L_init
        elif sorted(L_init)==L_init and sorted(L_init,reverse=True)==L_init:
            l1=L_init
            l2=L_init
        result_list[0][0]=l1
        result_list[0][1]=l2
        len_list[0] = max(len(l1),len(l2))
        for i in range(len(L_rest)):
            l1 = result_list[i][0]
            l2 = result_list[i][1]
            f=update_list(l1,l2,L_rest[i])
            result_list[i+1][0]=f[0]
            result_list[i+1][1]=f[1]
            len_list[i+1] = max(len(f[0]),len(f[1]))
        index_max_len = len_list.index(max(len_list))
        if len(result_list[index_max_len][0])==max(len_list):
            return sum(result_list[index_max_len][0])
        else:
            return sum(result_list[index_max_len][1])
    elif len(L)==2:
        return sum(L)
