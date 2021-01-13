import pandas as pd
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
    rides_cluster = pd.DataFrame()
    for trace in traces:
        trace = trace.assign(check=False)
        trace = trace.assign(counter=0)
        rides_cluster = rides_cluster.append(trace)
    rides_to_cluster = rides_cluster[:]


    rides = pd.DataFrame()
    for ind, road in rides_to_cluster.iterrows():
        rides_cluster = rides_to_cluster[:]
        for ind, trace in rides_cluster.iterrows():

            unattached_segments, road = check_trace_relation(road, trace)

            #old_roads.append(road_old)
            rides = add_segments_to_list(trace, unattached_segments)
            rides_to_cluster.remove(trace)
            rides_to_cluster.append(rides)
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
    for ind, dot in segment.iterrows():
        index, distance = find_the_perfect_index(road, dot)
        dot.check = add_dot_to_road(width_trace, distance)


        if dot.check:
            new_location = change_location(road, index, dot)
            #print(new_location)
    segment_false = unchecked_segments(segment)
    return segment_false, road

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
def find_the_perfect_index(main_trace, dot):

    return 1, 1
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

    counter = road.iloc[index].counter
    road.loc[index, 'counter'] = counter +1
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
