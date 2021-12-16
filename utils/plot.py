import matplotlib.pyplot as plt 

data = {}
with open("../results/t4_train.txt", 'r') as f:
    lines = f.readlines() 
    for line in lines:
        tokens = line.split(',')
        # model res50, batch_size 16, train_compute_tome 10.299044, total_time 10.511068
        modelname = tokens[0].split(' ')[-1]
        bz = int(tokens[1].split(' ')[-1])
        train_compute_time = float(tokens[2].split(' ')[-1])
        total_time = float(tokens[3].split(' ')[-1])
        if modelname not in data:
            data[modelname] = {'train':[], 'test':[], 'bz':[]}
        data[modelname]['train'].append(total_time)
        data[modelname]['bz'].append(bz)

with open("../results/t4_test.txt", 'r') as f:
    lines = f.readlines() 
    for line in lines:
        tokens = line.split(',')
        # model res50, batch_size 16, train_compute_tome 10.299044, total_time 10.511068
        modelname = tokens[0].split(' ')[-1]
        bz = int(tokens[1].split(' ')[-1])
        test_compute_time = float(tokens[2].split(' ')[-1])
        total_time = float(tokens[3].split(' ')[-1])
        data[modelname]['test'].append(total_time)

print(data)
fig, (ax1, ax2) = plt.subplots(1, 2)
for model in data:
    bz_len = min(len(data[model]['bz']), len(data[model]['train']))
    bz = data[model]['bz'][:bz_len]
    ax1.scatter(bz, data[model]['train'], label=model + "_train")
    ax1.plot(bz, data[model]['train'])
    
    bz_len = min(len(data[model]['bz']), len(data[model]['test']))
    bz = data[model]['bz'][:bz_len]
    ax2.scatter(bz, data[model]['test'], label=model + "_test")
    ax2.plot(bz, data[model]['test'])

ax1.legend()
ax2.legend()
fig.suptitle("t4", fontsize=20)
fig.set_size_inches(10, 5)
fig.savefig("t4.png")