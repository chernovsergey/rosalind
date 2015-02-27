__author__ = 'Sergey'

file = open('F:\Consensus&Profile.txt', 'r')
GCString = ""
GC_List = file.readlines()
for index in range(GC_List.__len__()):
    GCString += GC_List[index]
List_GC = GCString.split(">")
del List_GC[0]
for index in range(len(List_GC)):
    List_GC[index] = List_GC[index][13:]
    List_GC[index] = List_GC[index].replace("\n", "")

profile = {
    'A': [0 for i in range(len(List_GC[0]))],
    'G': [0 for i in range(len(List_GC[0]))],
    'C': [0 for i in range(len(List_GC[0]))],
    'T': [0 for i in range(len(List_GC[0]))]
}
#print(profile)
for cols in range(len(List_GC[0])):
    for row in range(len(List_GC)):
        profile[List_GC[row][cols]][cols] += 1

#print(profile)
consensus = ""
for index in range(len(List_GC[0])):
    max = 0
    cns_smb = ''
    for simb in ['A', 'C', 'G', 'T']:
        if (max < profile[simb][index]):
            max = profile[simb][index]
            cns_smb = simb
    consensus += cns_smb

print(consensus)
for simb in ['A', 'C', 'G', 'T']:
    s = ""
    for ind in range(len(profile[simb])):
        s += profile[simb][ind].__str__() + " "
    s = s.strip()
    print(simb + ": " + s)
