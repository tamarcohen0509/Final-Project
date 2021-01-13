import math_functions
import export_table, histogram
import pandas as pd
import matplotlib.pyplot as plt
import add_drive

def process_pls (df_trace):
    trace = df_trace[['pls_name', 'longitude', 'latitude', 'altitude', 's']].copy()
    trace_copy = df_trace[['pls_name', 'longitude', 'latitude', 'altitude', 's']].copy()
    df_segment = trace[(trace_copy['s'] < 10)]

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
    export_table.__p_type(hdf_table)  # print columns type

    df_all = pd.DataFrame(data=hdf_table)

    pls_names_list = export_table.__df_column_to_list(df_all, 'pls_name')
    pls_names_list = list(dict.fromkeys(pls_names_list))
    # print(pls_names_list)

    # print('========= plot all graphs')
    # multiple_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude'])
    # export_table.__f_on_groupby(df_all, multiple_graphs, True)

    # plot 1 graph
    df_first_trace = pd.DataFrame(data=hdf_table)
    df_first_trace = df_first_trace.loc[df_first_trace['pls_name'] == pls_names_list[0]]
    # __plot_graph(df_first_trace)
    # export_table.__p_data_frame(df_first_trace, ['pls_name', 'longitude', 'latitude', 's'])

    # plot graph #2:
    # TODO delete multiple dataframes
    df_second_trace = pd.DataFrame(data=hdf_table)
    df_second_trace = df_second_trace.loc[df_second_trace['pls_name'] == pls_names_list[1]]

    #### trace1
    return_values_dict = process_pls(df_first_trace)
    latitude_list = return_values_dict['long_lat'][0]
    longitude_list = return_values_dict['long_lat'][1]
    df_segment = return_values_dict['segment']
    export_table.__plot_data_points(latitude_list, longitude_list)  # plotting the points


    #### trace2
    return_values_dict2 = process_pls(df_second_trace)
    latitude_list2 = return_values_dict2['long_lat'][0]
    longitude_list2 = return_values_dict2['long_lat'][1]

    df_segment2 = return_values_dict2['segment']
    export_table.__plot_data_points(latitude_list2, longitude_list2, color='#C60B4B', m_color='#C60B50')  # plotting the points

    plt.show()


