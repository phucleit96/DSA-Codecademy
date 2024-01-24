from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

landmark_string = ""
stations_under_construction = ["Burrard"]

# Loop through the landmark_choices dictionary and add each landmark to the landmark_string
for letter, landmark in landmark_choices.items():
    landmark_string += "{0} - {1}\n".format(letter, landmark)


def greet():
    print("Hi there and welcome to SkyRoute!")
    print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)


def set_start_and_end(start_point, end_point):
    if start_point is not None:
        # If the start_point is already set, ask the user what they want to change
        change_point = input(
            "What would you like to change? You can enter 'o' for 'origin', 'd' for destination, or 'b' for 'both': ")
        if change_point == "b":
            # If the user wants to change both the start and end points, call the get_start and get_end functions
            start_point = get_start()
            end_point = get_end()
        elif change_point == "o":
            # If the user wants to change the start point, call the get_start function
            start_point = get_start()
        elif change_point == "d":
            # If the user wants to change the end point, call the get_end function
            end_point = get_end()
        else:
            print("Oops, that isn't 'o', 'd', or 'b' ... Please redo!")
            set_start_and_end(start_point, end_point)
    else:
        # If the start_point is not set, call the get_start and get_end functions to get the start and end points
        start_point = get_start()
        end_point = get_end()
    return start_point, end_point


def get_start():
    start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
    if start_point_letter in landmark_choices:
        # If the user's input is in the landmark_choices dictionary, set the start_point to the corresponding landmark
        start_point = landmark_choices[start_point_letter]
        return start_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_start()


def get_end():
    end_point_letter = input("Ok, where are you headed?: ")
    if end_point_letter in landmark_choices:
        # If the user's input is in the landmark_choices dictionary, set the end_point to the corresponding landmark
        end_point = landmark_choices[end_point_letter]
        return end_point
    else:
        print("Sorry, that's not a landmark we have data on. Let's try this again...")
        get_end()


def show_landmarks():
    see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
    if see_landmarks == "y":
        # If the user wants to see the landmarks again, print the landmark_string
        print(landmark_string)


def get_active_stations():
    update_metro = vc_metro
    for station_under_construction in stations_under_construction:
        for current_station, neighboring_station in vc_metro.items():
            if current_station != station_under_construction:
                # If the current station is not under construction, remove all stations under construction from its neighbors
                update_metro[current_station] -= set(stations_under_construction)
            else:
                # If the current station is under construction, set its neighbors to an empty set
                update_metro[current_station] = set([])
    return update_metro


def goodbye():
    print("Thanks for using Sky Route!")


def new_route(start_point=None, end_point=None):
    start_point, end_point = set_start_and_end(start_point, end_point)
    shortest_route = get_route(start_point, end_point)
    if shortest_route is not None:
        # If a shortest route is found, convert it to a string and print it
        shortest_route_string = '\n'.join(shortest_route)
        print(f"The shortest metro route from {start_point} to {end_point} is:\n{shortest_route_string}")
    else:
        print(f"Unfortunately, there is currently no path between {start_point} and {end_point} due to maintenance.")
    again = input("Would you like to see another route? Enter y/n: ")
    if again == "y":
        show_landmarks()
        new_route(start_point, end_point)


def get_route(start_point, end_point):
    start_stations = vc_landmarks[start_point]
    end_stations = vc_landmarks[end_point]
    routes = []
    for start_station in start_stations:
        for end_station in end_stations:
            metro_system = get_active_stations() if stations_under_construction else vc_metro
            if stations_under_construction:
                # If there are stations under construction, use depth-first search to find a possible route
                possible_route = dfs(metro_system, start_station, end_station)
                if possible_route is None:
                    return None
            # Use breadth-first search to find the shortest route
            route = bfs(metro_system, start_station, end_station)
            if route is not None:
                # If a route is found, add it to the list of routes
                routes.append(route)
    if routes:
        # If there are any routes, find the shortest one and return it
        shortest_route = min(routes, key=len)
        return shortest_route


def skyroute():
    greet()
    new_route()
    goodbye()


#  print(set_start_and_end(None, None))
# print(get_route('Marine Building', 'Robson Square'))
# active_stations = get_active_stations()
# for active_station, connection in active_stations.items():
#   print(active_station + " - " + str(connection))

skyroute()
