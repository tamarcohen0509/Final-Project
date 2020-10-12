import change_name
import export_table, histogram
import pandas as pd
import matplotlib.pyplot as plt
from shapely.geometry import LineString

if __name__ == "__main__":
    # open HDF file
    pd.set_option('max_colwidth', 40)
    hdf_table = pd.read_hdf("C:/Users/tamarcoh/FinalProject/HDF files/GPS traces/WOB.hdf")
    export_table.__p_type(hdf_table)
    #__p_data_frame(hdf_table, ['pls_name','longitude', 'latitude', 'altitude'],list(range(0,5)))
    export_table.__p_data_frame(hdf_table, ['pls_name'])

    # plot 1 graph
    df_first_trace = pd.DataFrame(data=hdf_table)
    df_first_trace = df_first_trace.loc[df_first_trace['pls_name'] == '17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls']
    # __plot_graph(df_first_trace)

    # plot graph #2:
    # TODO delete multiple dataframes
    df_second_trace = pd.DataFrame(data=hdf_table)
    df_second_trace = df_second_trace.loc[df_second_trace['pls_name'] == '17-06-02_WOB_City01_Passat_OV_128800_0.pls']


    df_all = pd.DataFrame(data=hdf_table)

    print('========= plot all graphs')
    multiple_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude'])
    export_table.__f_on_groupby(df_all, multiple_graphs, True)

    print('========= plot X graphs:')
    graphs_names = ['17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls', '17-06-02_WOB_City01_Passat_OV_128800_0.pls']
    choose_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude']) if gr.name in graphs_names else 0
    # export_table.__f_on_groupby(df_all, choose_graphs, True)


    print('========= print the graphs longtitude and latitude values:')
    print_values = lambda gr: print(gr) if gr.name in graphs_names else 0
    # export_table.__f_on_groupby(df_all, print_values)


    ############################################
    print("---> Road segment clustering")
    df_trace_long_lat = export_table.__extract_long_lat_from_DF(df_first_trace)
    # export_table.__p_data_frame(df_trace_long_lat, None)

    ########## trace1
    # data_frame[['longitude', 'latitude']].copy()
    trace1 = df_first_trace[['pls_name','longitude', 'latitude', 'altitude', 's']].copy()
    trace1_copy = df_first_trace[['pls_name','longitude', 'latitude', 'altitude', 's']].copy()
    # df_segment = trace1[(trace1_copy['s'] < 15)]
    df_segment = trace1[(trace1_copy['s'] < 40)]

    # export_table.__p_data_frame(df_segment, None)
    # export_table.__plot_graph(df_segment)  ###plotting

    print("---> first trace long and lat")
    # export_table.__p_data_frame(df_segment, ['longitude', 'latitude'])
    longitude_list = df_segment['longitude'].tolist()
    print(longitude_list)
    latitude_list = df_segment['latitude'].tolist()
    print(latitude_list)

    # plotting the points
    plt.plot(latitude_list, longitude_list, color='steelblue', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='lightblue', markersize=6)
    ########## trace1 ##########


    ########## trace2
    # data_frame[['longitude', 'latitude']].copy()
    trace2 = df_second_trace[['pls_name', 'longitude', 'latitude', 'altitude', 's']].copy()
    trace2_copy = df_second_trace[['pls_name', 'longitude', 'latitude', 'altitude', 's']].copy()
    # df_segment2 = trace2[(trace2_copy['s'] < 15)]
    df_segment2 = trace2[(trace2_copy['s'] < 40)]

    # export_table.__p_data_frame(df_segment2, None)
    # export_table.__plot_graph(df_segment) ### plotting

    print("---> Second trace long and lat")
    # export_table.__p_data_frame(df_segment2, ['longitude', 'latitude'])
    longitude_list2 = df_segment2['longitude'].tolist()
    print(longitude_list2)
    latitude_list2 = df_segment2['latitude'].tolist()
    print(latitude_list2)

    # plotting the points
    plt.plot(latitude_list2, longitude_list2, color='purple', linestyle='dashed', linewidth=3,
             marker='o', markerfacecolor='plum', markersize=6)
    ########## trace2 ##########

    # setting x and y axis range
    # plt.ylim(10, 11)
    # plt.xlim(52, 53)

    # naming the x axis
    plt.xlabel('latitude_list - axis')
    # naming the y axis
    plt.ylabel('longitude - axis')

    # plt.show()


    # print("---> print segment")
    # df_segment = df_trace_long_lat[(df_trace_long_lat['longitude'] >= 10.7690) & (df_trace_long_lat['longitude'] <= 10.7695)
    #                                 & (df_trace_long_lat.index.values >= 4878)]
    # export_table.__p_data_frame(df_segment, None)
    # export_table.__plot_graph(df_segment)
    # print(len(df_segment.index)) # get dataframe length

    print("---> TRACE1: get center point")
    center = change_name.__get_center_point_from_trace(df_segment)
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
    slope = change_name.__get_slope_between_two_points(points_to_slope[0], points_to_slope[1])
    print(slope)

    print("---> get horizontal")
    change_name.__plot_hor_graph(slope, points_to_slope[0])

    print("---> get vertical")
    change_name.__plot_vert_graph(slope, points_to_slope[0])


    plt.show()









