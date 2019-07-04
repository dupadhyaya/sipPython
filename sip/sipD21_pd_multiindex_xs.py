#Cross - Section - Index
#-----------------------------
#%

d = {'num_legs': [4, 4, 2, 2],   'num_wings': [0, 0, 2, 2], 'class': ['mammal', 'mammal', 'mammal', 'bird'], 'animal': ['cat', 'dog', 'bat', 'penguin'], 'locomotion': ['walks', 'walks', 'flies', 'walks']}
d
df = pd.DataFrame(data=d)
df = df.set_index(['class', 'animal', 'locomotion'])
df

df.xs('mammal', axis=0)
