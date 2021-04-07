import math_functions
import export_table, histogram
import pandas as pd
import matplotlib.pyplot as plt
import add_drive

def process_pls (df_trace, val):
    trace = df_trace[['pls_name', 'longitude', 'latitude', 'altitude', 's']].copy()
    trace_copy = df_trace[['pls_name', 'longitude', 'latitude', 'altitude', 's']].copy()
    df_segment = trace[:]
    longitude_list = export_table.__df_column_to_list(df_segment, 'longitude')
    latitude_list = export_table.__df_column_to_list(df_segment, 'latitude')

    return_values_dict = dict()
    return_values_dict['long_lat'] = latitude_list, longitude_list
    return_values_dict['segment'] = df_segment
    return return_values_dict

if __name__ == "__main__":
    # open HDF file
    pd.set_option('max_colwidth', 40)
    hdf_table = pd.read_hdf(r"C:/Users/HM/Documents/porject_end_degree/test_to_start/WOB.hdf")
    export_table.__p_type(hdf_table)  # print columns type

    df_all = pd.DataFrame(data=hdf_table)

    pls_names_list = export_table.__df_column_to_list(df_all, 'pls_name')
    pls_names_list = list(dict.fromkeys(pls_names_list))
    print("pls_names_list")
    df_segments =[]
    for pls_names in pls_names_list:
        df_trace = pd.DataFrame(data=hdf_table)
        df_trace = df_trace.loc[df_trace['pls_name'] == pls_names]
        return_values_dict = process_pls(df_trace, 1)
        latitude_list = return_values_dict['long_lat'][0]
        longitude_list = return_values_dict['long_lat'][1]
        df_segment = return_values_dict['segment']
        df_segment = df_segment.assign(check=False)
        df_segment = df_segment.assign(counter=0)

        df_segment = df_segment.assign(cluster=None)
        df_segments.append(df_segment)
        export_table.__plot_data_points(latitude_list, longitude_list)  # plotting the points
    plt.show()
    road = add_drive.create_streets(df_segments)