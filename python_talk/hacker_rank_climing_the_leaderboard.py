ranked = [100,90,90,80]
player = [70,80,105]

combined = ranked + player;
unique = list(set(combined));
unique.sort(key=None, reverse=True);
output =[]

for i in range(len(unique)):
    for j in range(len(player)):
        if unique[i] == player[j]:
            output.append(i);
            break;

print(output.reverse())

for i in range(len(output)):
    if output[i]==0:
        output[i]=1

print(output)


