char=['a','b','s']

freq=[2,1,2]

l=[]

for c,f in zip(char,freq):
    l.extend([c]*f)

print(l)

def generate_comb(current,remainig,length):
    if len(current) >=length:
        results.add(''.join(current))
    if not remainig:
        return
    for i in range(len(remainig)):
        generate_comb(current+[remainig[i]],remainig[i+1:],length)

results=set()
min_len=3
max_len=len(l)

for length in range(min_len,max_len+1):
    generate_comb([],l,length)

all_comb=sorted(results)
print(all_comb)