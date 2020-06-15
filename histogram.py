import matplotlib.pyplot as plt

def sub_plots(table, attr1, attr2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Distributions of " + attr1 + " and " + attr2 + " in the dataset", fontsize = 16)
    ax1.hist(table[attr1])
    ax1.set_xlabel(attr1, fontsize = 13)
    ax1.set_ylabel("Frequency", fontsize = 13)
    ax2.hist(table[attr2])
    ax2.set_xlabel(attr2, fontsize = 13)
    ax2.set_ylabel("Frequency", fontsize = 13);
    plt.show()