import folium
import twitter2
from geopy.geocoders import Nominatim



def get_coordinates(location):
    '''
    (str) -> (tuple)
    Transforms the address into coordinates.
    '''
    try:
        geolocator = Nominatim(user_agent='Me', timeout=10)
        location = geolocator.geocode(location)
        user_location = (location.latitude, location.longitude)
        return user_location
    except:
        return None


def build_map(user_name):
    '''
    Builds map with user's friends locations.
    '''
    print('')
    users_info = twitter2.get_json(user_name)['users']
    locations = [(users_info[i]['screen_name'], users_info[i]['location'])
           for i in range(len(users_info))]

    lst = [(locations[i][0], get_coordinates(locations[i][1]))
           for i in range(len(locations))
           if locations[i][0] != '' and locations[i][1] != '']
    for el in lst:
        if el[1] is None:
            lst.pop(lst.index(el))
    user_map = folium.Map()
    for i in range(len(lst)):
        location = lst[i][1]
        user_map.add_child(folium.Marker(location=[float(location[0]),
                                         float(location[1])],
                                         popup=lst[i][0],
                                         icon=folium.Icon(color='green')))

    user_map.save('friends.html')

# if __name__ == "__main__":
#     build_map('DrewTurko')
