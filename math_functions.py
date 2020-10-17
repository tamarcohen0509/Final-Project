import matplotlib.pyplot as plt
import numpy as np
import export_table
from scipy.interpolate import interp1d


# get the center point (long, lat) from an input dataframe
def __get_center_point_from_trace(data_frame):
    df_len = len((data_frame.index))
    print("df_len", df_len)
    index_center = round(df_len/2) + data_frame.index[0]
    print("index_center", index_center)
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

def __plot_hor_graph(slope, point1):
    x = np.linspace(point1[1] - 0.001, point1[1] + 0.001, 5)
    n = point1[0] - (slope * point1[1])
    y = slope * x + n
    plt.plot(x, y, '-r', color = 'black')
    return y

def __plot_vert_graph(slope, point1):
    r_slope = __get_reciprocal_slope(slope)
    point2 = [0,0]
    # point3 = [0,0]
    point2[1] = point1[1] -0.001 # latitude value
    point2[0] = __get_y_axis_based_on_slope(point1, point2[1], r_slope)
    point2 = tuple(point2)

    # point3[1] = point1[1] + 0.1  # latitude value
    # point3[0] = __get_y_axis_based_on_slope(point1, point3[1], r_slope)
    # point3 = tuple(point3)

    # print(point2)

    # y_values = [point1[0], point2[0], point3[0]]
    # x_values = [point1[1], point2[1], point3[0]]

    # y_values = [point1[0], point2[0]]
    # x_values = [point1[1], point2[1]]
    #
    # print(x_values, y_values)

    # plt.plot(x_values, y_values, color='red')
    # plt.axline((0, 0.5), slope=0.25, color="black", linestyle=(0, (5, 5)))
    x = np.linspace(point1[1]-0.001, point1[1]+0.001, 5)
    n = point1[0] - (r_slope * point1[1])
    y = r_slope * x + n
    plt.plot(x, y, '-r')
    return y


def __get_linear_interpolation(x, y):
    f = interp1d(x, y, fill_value="extrapolate")  # linear spline
    return f


def __plot_spline(x, y, func):
    plt.plot(x, y, 'o', x, func(x), '-')    # plot data points + linear spline
