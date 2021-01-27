import math_functions
import pandas as pd
import matplotlib.pyplot as plt
counter = 0
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
    roads = pd.DataFrame()
    rides_to_cluster = traces[:]
    i= 1
    j= 0
    for road in rides_to_cluster:
        traces = rides_to_cluster[:]
        for ind, dot in road.iterrows():
            print("lals")
            if road.iloc[ind].cluster is None:
                print(j)
                road.loc[ind, 'cluster'] = j
                j= j+1
        print(road)
        for trace in traces:
            if (trace is road):
                continue
            unattached_segments, road = check_trace_relation(road, trace)

            #old_roads.append(road_old)
            rides = add_segments_to_list(trace, unattached_segments)

            print("rides_to_cluster before remove")
            print(rides_to_cluster)
            print("rides_to_cluster before remove")
            rides_to_cluster.remove(trace)

            print("rides_to_cluster after remove")
            print(rides_to_cluster)
            print("rides_to_cluster after remove")
            rides = pd.DataFrame(rides)
            rides_to_cluster.append(rides)

            print("rides_to_cluster after append")
            print(rides_to_cluster)
            print("rides_to_cluster after append")
        roads.append(road)
    return roads

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
    #values = unattached_segments.split("(")
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

def check_trace_relation(road, segment):
    width_trace = 10
    segment = pd.DataFrame(segment)
    if segment.empty:
        print("no words in the segment")
        return None, None
    for ind, dot in segment.iterrows():
        distance, index = find_the_perfect_index(road, (dot.latitude, dot.longitude))
        print("index")
        print(index)
        segment.loc[ind,'check'] = add_dot_to_road(width_trace, distance)
        if segment.loc[ind,'check']:
            print("hereerere")
            cluster = add_to_cluster(road, index, dot)
            segment.loc[ind, 'cluster'] = cluster
            #new_location = change_location(road, index, dot)
            #print(new_location)
    #segment_false = unchecked_segments(segment)
    return segment_false, road

def add_to_cluster(road, index, dot):
    if dot.cluster is not None:
        print("dot has already a cluster it belongs to")
        print(f"and it is {dot.loc['cluster']}")
    else:
        print(f"cluster to be put is {road.iloc[index].cluster}")
        dot.loc['cluster'] = road.iloc[index].cluster
        print(f"cluster inputted is {dot.loc['cluster']}")
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
  and the index of the dot in main trace 
  which is closest to the place in spline 
  where the distance was measured from
"""#horizontal and vertical are regarding to the vertivcal beween dot and trace herefore not sure if need this recursive
def find_the_perfect_index(main_trace, dot):#point, df_segment):
        min_distance = 1000000  # initial value
        # distances = []
        for index, row in main_trace.iterrows():
            row_lat = row['latitude']
            row_long = row['longitude']
            # print("ROW = ", (row_lat, row_long))
            tmp_distance = math_functions.__distance(dot, (row_lat, row_long))
            # distances.append(tmp_distance)
            if tmp_distance < min_distance:
                min_distance = tmp_distance
                min_index = index
                min_row = (row_lat, row_long)

        print("Minimum distance = ", min_distance)
        # print(min(distances))
        print("INDEX = ", min_index)
        print("POINT ON df = ", (min_row[0], min_row[1]))
        plt.plot(min_row[0], min_row[1], marker='*', color='purple')
        return (min_distance, min_index)


    #if index + 1 < main_trace.length:
    #    if main_trace[index].dist_horizontal(dot) > main_trace[index + 1].dist_horizontal(dot):
    #        main_trace.find_the_perfect_index(main_trace, dot, index + 1)
    #if index - 1 >= 0:
    #    if main_trace[index].dist_horizontal(dot) > main_trace[index - 1].dist_horizontal(dot):
    #        main_trace.find_the_perfect_index(main_trace, dot, index - 1)
    #return index

"""
This function adds a given dot to a road if it matches-
if the distance is smaller then the width of the street.
"""
def add_dot_to_road(width_street, distance):
    if distance < 0:
        temp_dist =distance * (-1)
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
    #counter counts how many rides
    # is this road based on
    # print(road.iloc[index])
    # print(road.iloc[index].counter)
    #print(road.iloc[index])
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
