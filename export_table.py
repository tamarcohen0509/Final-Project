import pandas as pd
import matplotlib.pyplot as plt


def __p_type(table):
    print(table.dtypes)


def __p_data_frame(table, columns, index=None):
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    pd.set_option('display.width', 1000)
    if index is None:
        index = table.index
    print(pd.DataFrame(data=table, index=index, columns=columns))


def __extract_from_data_frame(table, columns, index=None):
    if index is None:
        index = table.index
    return pd.DataFrame(data=table, index=index, columns=columns)


def __plot_graph(data_frame, color='mediumvioletred'):
    data_frame.plot(x='longitude', y='latitude', kind='line', color=color)
    # plt.show()


def __plot_data_points(latitude_list, longitude_list, color='steelblue', m_color='lightblue', marker='o'):
    # plotting the points
    plt.plot(latitude_list, longitude_list, color=color, linestyle='dashed', linewidth=3,
             marker=marker, markerfacecolor=m_color, markersize=6)


def __f_on_groupby(data_frame, func, plot=False, return_val=False):
    grouped_df = data_frame.groupby('pls_name')[['latitude', 'longitude']].apply(func)
    plt.show() if plot else 0
    return grouped_df if return_val else 0


def __extract_long_lat_from_DF(data_frame):
    return data_frame[['longitude', 'latitude']].copy()


# output: list of tuples
def __df_to_tuples(data_frame):
    return [tuple(r) for r in data_frame.to_numpy()]


def __df_column_to_list(df_segment, column):
    return df_segment[column].tolist()


