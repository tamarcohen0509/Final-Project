import math_functions
import export_table, histogram
import pandas as pd
import matplotlib.pyplot as plt


def process_pls (df_trace):
    trace = df_trace[['pls_name', 'longitude', 'latitude', 'altitude', 's']].copy()
    trace_copy = df_trace[['pls_name', 'longitude', 'latitude', 'altitude', 's']].copy()
    df_segment = trace[(trace_copy['s'] < 40)]

    # export_table.__p_data_frame(df_segment, None)     # print data frame values
    # export_table.__plot_graph(df_segment)             # plotting

    # export_table.__p_data_frame(df_segment, ['longitude', 'latitude'])    # print long & lat
    longitude_list = export_table.__df_column_to_list(df_segment, 'longitude')
    print(longitude_list)
    latitude_list = export_table.__df_column_to_list(df_segment, 'latitude')
    print(latitude_list)

    return_values_dict = dict()
    return_values_dict['long_lat'] = latitude_list, longitude_list
    return_values_dict['segment'] = df_segment
    return return_values_dict



if __name__ == "__main__":
    # open HDF file
    pd.set_option('max_colwidth', 40)
    hdf_table = pd.read_hdf("C:/Users/tamarcoh/FinalProject/HDF files/GPS traces/WOB.hdf")
    export_table.__p_type(hdf_table)
    #__p_data_frame(hdf_table, ['pls_name','longitude', 'latitude', 'altitude'],list(range(0,5)))
    export_table.__p_data_frame(hdf_table, ['pls_name'])

    df_all = pd.DataFrame(data=hdf_table)

    print('========= plot all graphs')
    multiple_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude'])
    export_table.__f_on_groupby(df_all, multiple_graphs, True)

    # print('========= plot X graphs:')
    # graphs_names = ['17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls', '17-06-02_WOB_City01_Passat_OV_128800_0.pls']
    # choose_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude']) if gr.name in graphs_names else 0
    # # export_table.__f_on_groupby(df_all, choose_graphs, True)

    # print('========= print the graphs longtitude and latitude values:')
    # print_values = lambda gr: print(gr) if gr.name in graphs_names else 0
    # # export_table.__f_on_groupby(df_all, print_values)


    # plot 1 graph
    df_first_trace = pd.DataFrame(data=hdf_table)
    df_first_trace = df_first_trace.loc[df_first_trace['pls_name'] == '17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls']
    # __plot_graph(df_first_trace)

    # plot graph #2:
    # TODO delete multiple dataframes
    df_second_trace = pd.DataFrame(data=hdf_table)
    df_second_trace = df_second_trace.loc[df_second_trace['pls_name'] == '17-06-02_WOB_City01_Passat_OV_128800_0.pls']


    ############################################
    print("---> Road segment clustering")

    #### trace1
    return_values_dict = process_pls(df_first_trace)
    latitude_list = return_values_dict['long_lat'][0]
    longitude_list = return_values_dict['long_lat'][1]
    df_segment = return_values_dict['segment']
    export_table.__plot_data_points(latitude_list, longitude_list) # plotting the points


    #### trace2
    return_values_dict2 = process_pls(df_second_trace)
    latitude_list2 = return_values_dict2['long_lat'][0]
    longitude_list2 = return_values_dict2['long_lat'][1]

    # plot data points + linear spline
    f = math_functions.__get_linear_interpolation(latitude_list2, longitude_list2)
    math_functions.__plot_spline(latitude_list2, longitude_list2, f)
    # plt.plot(x, y, 'o', xnew, f(xnew), '-')


    # naming the x axis
    plt.xlabel('latitude - axis')
    # naming the y axis
    plt.ylabel('longitude - axis')





    print("---> TRACE1: get center point")
    center = math_functions.__get_center_point_from_trace(df_segment)
    center_long = center['longitude'].to_numpy()
    center_lat = center['latitude'].to_numpy()
    print("CENTER longitude" , center_long)
    print("CENTER latitude" , center_lat)
    plt.plot(center_lat, center_long, marker = '*', color = 'red')

    print("---> get slope")
    center_points = center

    df = export_table.__extract_from_data_frame(df_segment, None, (center.index[0], center.index[0]+1))
    points_to_slope = export_table.__df_to_tuples(df)
    points_to_slope[0] = points_to_slope[0][1:]
    points_to_slope[1] = points_to_slope[1][1:]
    print(points_to_slope[0], points_to_slope[1])
    slope = math_functions.__get_slope_between_two_points(points_to_slope[0], points_to_slope[1])
    print(slope)

    print("---> get horizontal")
    math_functions.__plot_hor_graph(slope, points_to_slope[0])

    print("---> get vertical")
    vert_graph = math_functions.__plot_vert_graph(slope, points_to_slope[0])

    plt.show()



