import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('max_colwidth', 400)
hdf_table = pd.read_hdf("C:/Users/tamarcoh/FinalProject/HDF files/GPS traces/WOB.hdf")
print('======= TYPE')
print(type(hdf_table))
print('=============')
print('======= Table of types')
print(hdf_table.dtypes)
print('=============')
print('======= Table of values')
print(pd.DataFrame(data=hdf_table, index=(0,1), columns=['longitude', 'latitude', 'altitude']))
print(pd.DataFrame(data=hdf_table, columns=['pls_name'])) #index=list(range(0,6000))))
a = pd.DataFrame(data=hdf_table, columns=['pls_name']) #index=list(range(0,6000))))
print('=============')


df_first_trace = pd.DataFrame(data=hdf_table)
df_first_trace = df_first_trace.loc[df_first_trace['pls_name'] == '17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls']
# df_first_trace.plot(x='longitude', y='latitude', kind = 'line', color='mediumvioletred')
#plt.show()

df_second_trace = pd.DataFrame(data=hdf_table)
df_second_trace = df_second_trace.loc[df_second_trace['pls_name'] == '17-06-02_WOB_City01_Passat_OV_128800_0.pls']
# df_second_trace.plot(x='longitude', y='latitude', kind = 'line', color='crimson')
#plt.show()

def plot_func(gr, pls_names):
    plt.plot(gr['longitude'], gr['latitude']) if gr['pls_name'] in pls_names else 0


print('Group-by:')
df_all = pd.DataFrame(data=hdf_table)
table_by_pls = df_all.groupby('pls_name')[['latitude', 'longitude']].apply(lambda gr: plt.plot(gr['longitude'], gr['latitude']))
plt.show()
print("=================================================")

print('2 graphs:')
graphs_names = ['17-06-13_WOB_City01_Passat_OV_loop11_lane1_130640_0.pls', '17-06-02_WOB_City01_Passat_OV_128800_0.pls']
df_all.groupby('pls_name')[['latitude', 'longitude']].apply(lambda gr: plt.plot(gr['longitude'], gr['latitude']) if gr.name in graphs_names else 0)
df_all.groupby('pls_name')[['latitude', 'longitude']].apply(lambda gr: print(gr) if gr.name in graphs_names else 0)
plt.show()

