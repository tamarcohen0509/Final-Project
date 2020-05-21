import pandas as pd
import matplotlib.pyplot as plt


def __p_type(table):
    print(table.dtypes)


def __p_data_frame(table, columns, index=None):
    if index is None:
        index = table.index
    print(pd.DataFrame(data=table, index=index, columns=columns))


def __plot_graph(data_frame, color='mediumvioletred'):
    data_frame.plot(x='longitude', y='latitude', kind='line', color=color)
    plt.show()


def __f_on_groupby(data_frame, func, plot=False, return_val=False):
    grouped_df = data_frame.groupby('pls_name')[['latitude', 'longitude']].apply(func)
    plt.show() if plot else 0
    return grouped_df if return_val else 0


if __name__ == "__main__":
    # open HDF file
    pd.set_option('max_colwidth', 400)
    hdf_table = pd.read_hdf("C:/Users/tamarcoh/FinalProject/HDF files/GPS traces/WOB.hdf")
    __p_data_frame(hdf_table, ['pls_name'])

    # plot 1 graph
    df_first_trace = pd.DataFrame(data=hdf_table)
    df_first_trace = df_first_trace.loc[df_first_trace['pls_name'] == '17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls']
    # __plot_graph(df_first_trace)

    df_all = pd.DataFrame(data=hdf_table)

    print('========= plot all graphs')
    multiple_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude'])
    # __f_on_groupby(df_all, multiple_graphs, True)

    print('========= plot X graphs:')
    graphs_names = ['17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls', '17-06-02_WOB_City01_Passat_OV_128800_0.pls']
    choose_graphs = lambda gr: plt.plot(gr['longitude'], gr['latitude']) if gr.name in graphs_names else 0
    __f_on_groupby(df_all, choose_graphs, True)

    print('========= print the graphs longtitude and latitude:')
    print_values = lambda gr: print(gr) if gr.name in graphs_names else 0
    # __f_on_groupby(df_all, print_values)
