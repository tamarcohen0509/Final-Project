
"""
input: traces
output: roads that are a clustering of this
        traces
"""

def create_streets(traces):
    roads = None
    rides_to_cluster = traces[:]
    for road in rides_to_cluster:
        traces = rides_to_cluster[:]
        for trace in traces:
            unattached_segments, road = check_trace_relation(road, trace)
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
    for dot in segment:
        index, distance = road.find_the_perfect_index(dot)
        dot.checked = road.add_dot_to_road(width_trace, distance)
        if dot.checked:
            new_location = road.change_location(index, dot)
            print(new_location)
    segment_false = unchecked_segments(segment)
    return segment_false, road

"""
This funcion runs on segmen an checks which dot are used 
in roas and which were not clustered yet. 
The ones that were not clustered are returned in list of indexes
"""
def unchecked_segments(trace):
    flag = trace[0].checked
    segment_false = []
    for dot in trace:
        if dot.checked != flag:
            index = trace.index(dot)
            if flag:
                segment_false.append(index)
            else:
                start_seg = segment_false[-1]
                segment_false[-1] = (start_seg, index - 1)
    if segment_false[-1] is not None and not tuple:
        start_seg = segment_false[-1]
        segment_false[-1] = (start_seg, len(trace) - 1)
    return segment_false

"""this function will be written by Tamar
 it returns the distance between dot and main_trace
  and the index of the dot in main trace 
  which is closest to the place in spline 
  where the distance was measured from
"""#horizontal and vertical are regarding to the vertivcal beween dot and trace herefore not sure if need this recursive
def find_the_perfect_index(main_trace, dot, index):
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
    counter = road.index.counter
    road.index.counter = road.index.counter + 1
    #wha is the distance between road and ride
    lat_dist = road[index][1] - dot[1]
    long_dist = road[index][0] - dot[0]
    # get average distance between the two points
    full_lat_dist = lat_dist * counter
    full_long_dist = long_dist * counter
    avg_lat_dist = full_lat_dist / (counter + 1)
    avg_long_dist = full_long_dist / (counter + 1)
    # move the road to correct place
    road[index][1] = road[index][1] - avg_lat_dist
    road[index][0] = road[index][10] - avg_long_dist
    return road[index]
