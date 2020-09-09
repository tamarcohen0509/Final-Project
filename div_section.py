import pandas as pd
import matplotlib.pyplot as plt
import export_table
import pandas as pd

def __avg_speed(data_frame, index):
    data_frame.mean(axis=0, skipna=True)


def __div_by_s():
    pd.set_option('max_colwidth', 400)
    hdf_table = pd.read_hdf("C:/Users/H&M/Documents/porject_end_degree/test_to_start/WOB.hdf")
    graph1 = '17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls'
    graph2 = '17-06-02_WOB_City01_Passat_OV_128800_0.pls'

    df = pd.DataFrame(data=hdf_table)
    df_first_trace = df.loc[df['pls_name'] == graph1]
    df_sec_trace = df.loc[df['pls_name'] == graph2]

    # print(df_first_trace['speed'].index(range(0, 1000)))
    # avg_speed = __avg_speed(df_first_trace['speed'].max_index(1000), list(range(0,1000)))
    # print(avg_speed)


    df_first_trace = df_first_trace.sort_values('s')
    df_sec_trace = df_sec_trace.sort_values('s')
    df_first_trace = df_first_trace.head(n=100000)
    df_sec_trace = df_sec_trace.head(n=100000)
    return df_first_trace, df_sec_trace




