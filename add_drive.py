import math_functions, export_table
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
counter = 0
clusters = {}
num_cluster = -1

"""
input: traces
output: roads that are a clustering of this
        traces
    go over every couple of traces compare and find which dots can be connected and which can't.
    if would do this without any change would find for every dot to what traces it's related
    would get clusters which are group of all dots that are connected.
    the clustes aren't on the original traces it's on the common parts of the traces.
"""
def create_streets(traces):
    for trace in traces:
        check_trace_relation(trace)
    merge_points_in_clusters()

"""
input: trace and a list of tuples of index's where the trace
       wasn't matched to any road.
output: a new trace that contains only the dots tha were
        not a match to any road
"""
def add_segments_to_list(trace, unattached_segments):
    if unattached_segments is None:
        return None
    rides = []
    for value in unattached_segments:
        start_seg = value[0]
        end_seg = value[1]
        new_seg = trace[start_seg:end_seg]
        rides.append(new_seg)
    return rides

"""
This function gets a road and a segment.
it returns he new road according to the 
avg with the right points in trace and returns
a list with tuples of index's where trace wasn't
a match with road
"""
def check_trace_relation(segment):
    width_trace = 0.1
    segment = pd.DataFrame(segment)
    if segment.empty:
        return None, None
    for ind, dot in segment.iterrows():
        distance, index = find_the_perfect_index( (dot.latitude, dot.longitude, dot.pls_name))
        if (index != -1):
            segment.loc[ind,'check'] = add_dot_to_road(width_trace, distance) #belong dot only if it is in the road width


        if segment.loc[ind,'check']:
            cluster = add_to_cluster(index, dot)
            segment.loc[ind, 'cluster'] = cluster
            clusters[cluster].setdefault(dot['pls_name'], []).append(dot)
            merge_points_in_cluster(clusters[cluster])
        else:
            global num_cluster
            num_cluster+= 1
            segment.loc[ind, 'cluster'] = num_cluster
            # create a new cluster key in clusters dict
            clusters[num_cluster] = {dot['pls_name']: [segment.loc[ind]]}
            clusters[num_cluster]['avg_point'] = (segment.loc[ind]['latitude'], segment.loc[ind]['longitude'])



def add_to_cluster(index, dot):
    if dot.cluster is not None:
        print("dot has already a cluster it belongs to")
    else:
        dot.loc['cluster'] = index
    return dot.loc['cluster']

"""
This funcion runs on segmen an checks which dot are used 
in roas and which were not clustered yet. 
The ones that were not clustered are returned in list of indexes
"""
def unchecked_segments(trace):
    flag = trace.iloc[0].check
    segment_false = []
    for ind, dot in trace.iterrows():
        if dot.check != flag:
            index = trace.index(dot)
            if flag:
                segment_false.append(index)
            else:
                start_seg = segment_false[-1]
                segment_false[-1] = (start_seg, index - 1)
    if segment_false and segment_false[-1] is not tuple:
        start_seg = segment_false[-1]
        segment_false[-1] = (start_seg, len(trace) - 1)
    return segment_false

"""this function will be written by Tamar
 it returns the distance between dot and main_trace
  and the indefind_the_perfect_indexx of the dot in main trace 
  which is closest to the place in spline 
  where the distance was measured from
"""#horizontal and vertical are regarding to the vertivcal beween dot and trace herefore not sure if need this recursive
def find_the_perfect_index(dot):
    min_distance = 1000000  # initial value
    min_index = -1
    for index, item in clusters.items():
        if 'avg_point' in item:
            row_lat = item['avg_point'][0]
            row_long = item['avg_point'][1]
            print('---->>>avg', (row_lat, row_long), 'index', index)
            tmp_distance = math_functions.__distance(dot, (row_lat, row_long))
            print("tmp distance = ", tmp_distance)
            if tmp_distance < min_distance:
                if not if_road_in_cluster(item, dot[2]):
                    min_distance = tmp_distance
                    min_index = index
    return (min_distance, min_index)

def if_road_in_cluster(cluster, pls_name):
    print("FUNC", pls_name)
    for pls in cluster:
        if (pls == "avg_point"):
            continue
        if pls == pls_name:
            return True
    return False
"""
This function adds a given dot to a road if it matches-
if the distance is smaller then the width of the street.
"""
def add_dot_to_road(width_street, distance):
    if distance < 0: #???
        temp_dist = distance * (-1)
    else:
        temp_dist = distance
    if temp_dist < width_street:
        return True
    else:
        return False


"""
returns where to put the road in this specific index
so this dot should be located on the vertical in an 
average depending on how many traces is main road based on
"""
def change_location(road, index, dot):
    #counter counts how many rides is this road based on
    index = int(index)
    counter = road.iloc[index].counter + 1
    road.loc[index, 'counter'] = counter
    #wha is the distance between road and ride
    lat_dist = road.iloc[index].latitude - dot.latitude
    long_dist = road.iloc[index].longitude - dot.longitude
    # get average distance between the two points
    full_lat_dist = lat_dist * counter
    full_long_dist = long_dist * counter
    avg_lat_dist = full_lat_dist / (counter + 1)
    avg_long_dist = full_long_dist / (counter + 1)
    # move the road to correct place
    road.iloc[index].latitude = road.iloc[index].latitude - avg_lat_dist
    road.iloc[index].longitude = road.iloc[index].longitude - avg_long_dist
    return road.iloc[index]


def plot_cluster():
    for key, values in clusters.items():
        rgb = np.random.rand(3, )  # generate a random color
        if len(values) > 1:
            for key, dots in values.items():
                for dot in dots:
                    export_table.__plot_data_points(dot['latitude'], dot['longitude'], color=rgb, m_color=rgb)


def get_avg_in_pls(pls):
    points = []
    for point in pls:
        point_lat = point['latitude']
        point_long = point['longitude']
        point_alt = point['altitude']
        points.append((point_lat, point_long, point_alt))
    avg_point = math_functions.__get_avg_point(points)
    return avg_point


"""
merge the points in an input cluster to one point
using geometric avg. this will give us one road
"""
def merge_points_in_cluster(cluster):
    cluster_list = []
    for pls in cluster:
        if(pls == "avg_point"):
            continue
        if len(cluster[pls]) > 1:
            point_to_add = get_avg_in_pls(cluster[pls])
        else:
            point = cluster[pls][0]
            point_lat = point['latitude']
            point_long = point['longitude']
            point_alt = point['altitude']
            point_to_add = (point_lat, point_long, point_alt)
        cluster_list.append(point_to_add)
        avg_point = math_functions.__get_avg_point(cluster_list)
        cluster['avg_point'] = avg_point
    return avg_point

def merge_points_in_clusters():
    avg_points = []
    for cluster in clusters.values():
        if len(cluster) < 2:
            continue
        avg_points.append(cluster['avg_point'])
        export_table.__plot_data_points(cluster['avg_point'][0], cluster['avg_point'][1], color='#000000', m_color='#000000', marker='X')
