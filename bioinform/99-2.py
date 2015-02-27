dic = {'G': 57 ,    'A': 71,    'S': 87,    'P': 97,    'V': 99,    'T': 101,   'C': 103,   'I': 113,   'L': 113,   'N': 114,   'D': 115,   'K': 128,
       'Q': 128,    'E': 129,   'M': 131,   'H': 137,   'F': 147,   'R': 156,   'Y': 163,   'W': 186 }

list_prot = "GASPVTCILNDKQEMHFRYW"

M = 1024

def mass(prot):
    return sum([dic[i] for i in prot])

k = 7
num = 0
print len(list_prot)
while k < 8:
	tmp = [0]*k
	while tmp[-1] != len(list_prot)-1:
		index = 0
		for i in xrange(k):
			if tmp[i] != len(list_prot)-1:
				tmp[i] += 1
				index = i
				break
			elif i != k-1:
				tmp[i] = 0;

		cur_sum_protein = sum([dic[list_prot[i]] for i in tmp])
		if M == cur_sum_protein:
			num += 1
			print num, tmp
		#if cur_sum_protein > M:
		#	tmp[index] = len(list_prot)-1
		#if cur_sum_protein < M:
		#	if M - cur_sum_protein > 186:
		#		tmp[index] = len(list_prot)-1
		#print tmp

print num