import export_table, histogram
import pandas as pd
import matplotlib.pyplot as plt

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


    df_all = pd.DataFrame(data=hdf_table)

    print('========= plot all graphs')
    multiple_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude'])
    export_table.__f_on_groupby(df_all, multiple_graphs, True)

    print('========= plot X graphs:')
    graphs_names = ['17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls', '17-06-02_WOB_City01_Passat_OV_128800_0.pls']
    choose_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude']) if gr.name in graphs_names else 0
    #export_table.__f_on_groupby(df_all, choose_graphs, True)


    print('========= print the graphs longtitude and latitude values:')
    print_values = lambda gr: print(gr) if gr.name in graphs_names else 0
    export_table.__f_on_groupby(df_all, print_values)


    # ======= create histograms
    print("========= create_histogram")

    # find min and max
    min_lat = histogram.get_min_point_on_axis(df_all, 'latitude')
    min_long = histogram.get_min_point_on_axis(df_all, 'longitude')
    max_lat = histogram.get_max_point_on_axis(df_all, 'latitude')
    max_long = histogram.get_max_point_on_axis(df_all, 'longitude')
    print("min_lat=",  min_lat , "max_lat=" , max_lat , "min_long=" , min_long , "max_long=" , max_long)

    # find range
    lat_range = histogram.get_range(min_lat, (max_lat[0], min_lat[1]))
    long_range = histogram.get_range(min_long, (min_long[0], max_long[1]))
    print("lat_range=", lat_range, "long_range", long_range)


    lat_bins = round(histogram.get_bins(lat_range))
    long_bits = round(histogram.get_bins(long_range))
    print(lat_bins, long_bits)

    # histogram.sub_plots(df_all, 'longitude', 'latitude', lat_bins, long_bits)

    # 2D histogram
    histogram.hist2d_plt(df_all, 'longitude', 'latitude', lat_bins * long_bits)