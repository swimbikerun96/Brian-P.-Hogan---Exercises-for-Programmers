#Dictionary for speakers & quotes
q_list = []
s_list = []
#Handle multiple inputs
for i in range(3):
    q = input('What is the quote? ')
    s = input('Who said it? ')
    q_list.append(q)
    s_list.append(s)

for i in range(len(q_list)):
    print(f'{s_list[i]} says, "{q_list[i]}".')
    
