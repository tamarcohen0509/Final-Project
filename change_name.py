import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import export_table

# get the center point (long, lat) from an input dataframe
def __get_center_point_from_trace(data_frame):
    df_len = len((data_frame.index))
    index_center = round(df_len/2) + data_frame.index[0]
    return export_table.__extract_from_data_frame(data_frame, None, index_center)


# get slope - TODO check it it calculates correctly (GEO points)
def __get_slope_between_two_points(point1, point2):
    lat1 = point1[1]
    long1 = point1[0]
    lat2 = point2[1]
    long2 = point2[0]
    slope = (long2 - long1) / (lat2 - lat1)
    return slope


def __get_reciprocal_slope(slope):
    if slope == 0:
        new_slope = -1
    else: new_slope = (1 / slope) * -1
    print(new_slope)
    return new_slope


def __get_y_axis_based_on_slope(point1, x_axis, slope):
    # calculate y=mx+n
    # find n
    n = point1[0] - slope*point1[1]
    # find y
    y = slope*x_axis + n
    return y


def __plot_vert_graph(slope, point1):
    r_slope = __get_reciprocal_slope(slope)
    point2 = [0,0]
    point2[1] = point1[1] -0.01 # latitude value
    point2[0] = __get_y_axis_based_on_slope(point1, point2[1], r_slope)
    point2 = tuple(point2)

    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, color='red')


