def Pass1(local_baskets):
	baskets = list(local_baskets)
	local_num = len(local_baskets)
	local_thre = threshold*(local_num/baskets_num)
	candidates = []
	C1 = set()
	L1 = []
	count_table = collections.defaultdict(int)
	
	for each in baskets:
		for i in each:
			C1.add(i)
	for item in C1:
		for basket in baskets:
			if item in basket:
				count_table[item] += 1
		if count_table[item] >= local_thre:
			candidates.append([item])
			L1.append([item])

	Lksub1 = L1
	k = 2

	while(len(Lksub1)>=1):
		Lk = []
		Ck = create_Ck(Lksub1, k)
		for each in Ck:
			for basket in baskets:
				if set(each).issubset(set(basket)):
					count_table[each] += 1
			if count_table[each] >= local_thre:
				candidates.append(each)
				Lk.append(each)
		Lksub1 = Lk
		k = k + 1
	


	def create_Ck(Lksub1, k):

	    Ck = []
	    len_Lksub1 = len(Lksub1)
	    # list_Lksub1 = list(Lksub1)
	    for i in range(len_Lksub1):
	        for j in range(i+1, len_Lksub1):
	            l1 = list(Lksub1[i])
	            l2 = list(Lksub1[j])
	            l1.sort()
	            l2.sort()
	            if l1[0:k-2] == l2[0:k-2]:
	                Ck_item = Lksub1[i] | Lksub1[j]
	                if is_apriori(Ck_item, Lksub1):
	                    Ck.append(Ck_item)
	    return Ck

	def is_apriori(Ck_item, Lksub1):

	    for item in Ck_item:
	        sub_Ck = Ck_item.remove(item)
	        if sub_Ck not in Lksub1:
	            return False
	    return True

def Pass2(local_baskets):
	baskets = list(local_baskets)
	count_table = collections.defaultdict(int)
    for candidate in candidates:
        for basket in baskets:
        	if(set(candidate).issubset(basket)):
                    count_table[candidate] += 1
     return count_table.items()

