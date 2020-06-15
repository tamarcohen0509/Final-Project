import matplotlib.pyplot as plt
import pandas as pd
from geopy import distance

def get_min_point_on_axis(data_frame, axis):
    sample = (data_frame.loc[data_frame[axis].idxmin()])
    print(sample['latitude'], sample['longitude'])
    return sample['latitude'], sample['longitude']


def get_max_point_on_axis(data_frame, axis):
    sample = (data_frame.loc[data_frame[axis].idxmax()])
    print(sample['latitude'], sample['longitude'])
    return sample['latitude'], sample['longitude']


def get_range(min, max):
    # normalize the points to the same axis value
    print(min[1],max[1])
    dist = distance.distance(min, max).km
    return dist
    # print(distance.distance(min, max).km)


# get number of equal-width bins in the range
def get_bins(range):
    return range/0.001


def sub_plots(data_frame, attr1, attr2, bins1, bins2):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Distributions of " + attr1 + " and " + attr2 + " in the dataset", fontsize = 16)
    ax1.hist(data_frame[attr1],  bins=bins1)
    ax1.set_xlabel(attr1, fontsize = 13)
    ax1.set_ylabel("Frequency", fontsize = 13)
    ax2.hist(data_frame[attr2], bins=bins2)
    ax2.set_xlabel(attr2, fontsize = 13)
    ax2.set_ylabel("Frequency", fontsize = 13);
    plt.show()


def hist2d_plt(data_frame, attr1, attr2, bins):
    plt.figure(figsize = (10,8))
    plt.hist2d(data_frame[attr1], data_frame[attr2], bins=50, cmap='gray')
    plt.colorbar().set_label("Number of properties")
    plt.xlabel("Latitude", fontsize=14)
    plt.ylabel("Longitude", fontsize=14)
    plt.title("hist2d", fontsize=17)
    plt.show()

