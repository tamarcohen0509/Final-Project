import pandas as pd

def __avg_speed(data_frame, index):
    data_frame.mean(axis=0, skipna=True)

if __name__ == "__main__":
    pd.set_option('max_colwidth', 400)
    hdf_table = pd.read_hdf("C:/Users/tamarcoh/FinalProject/HDF files/GPS traces/WOB.hdf")
    graph1 = '17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls'
    graph2 = '17-06-02_WOB_City01_Passat_OV_128800_0.pls'

    df = pd.DataFrame(data=hdf_table)
    df_first_trace = df.loc[df['pls_name'] == graph1]
    df_sec_trace = df.loc[df['pls_name'] == graph2]

    print(df_first_trace['speed'].index(range(0,1000)))

