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
    # __p_data_frame(hdf_table, ['pls_name','longitude', 'latitude', 'altitude'],list(range(0,5)))
    export_table.__p_data_frame(hdf_table, ['pls_name'])


    # ======= create histograms
    # print("========= create_histogram")
    #
    # # find min and max
    # min_lat = histogram.get_min_point_on_axis(df_all, 'latitude')
    # min_long = histogram.get_min_point_on_axis(df_all, 'longitude')
    # max_lat = histogram.get_max_point_on_axis(df_all, 'latitude')
    # max_long = histogram.get_max_point_on_axis(df_all, 'longitude')
    # print("min_lat=",  min_lat , "max_lat=" , max_lat , "min_long=" , min_long , "max_long=" , max_long)
    #
    # # find range
    # lat_range = histogram.get_range(min_lat, (max_lat[0], min_lat[1]))
    # long_range = histogram.get_range(min_long, (min_long[0], max_long[1]))
    # print("lat_range=", lat_range, "long_range", long_range)
    #
    #
    # lat_bins = round(histogram.get_bins(lat_range))
    # long_bits = round(histogram.get_bins(long_range))
    # print(lat_bins, long_bits)
    #
    # # histogram.sub_plots(df_all, 'longitude', 'latitude', lat_bins, long_bits)
    #
    # # 2D histogram
    # histogram.hist2d_plt(df_all, 'longitude', 'latitude', lat_bins * long_bits)

