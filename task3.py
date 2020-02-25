import folium
from folium.plugins import MarkerCluster
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


def color_change(elev):
    if(elev < 3):
        return('green')
    elif(3 <= elev < 7):
        return('orange')
    else:
        return('red')


def build_map(user_name):
    '''
    Builds map with user's friends locations.
    '''
    print('')
    users_info = twitter2.get_json(user_name)['users']
    
    locations = {}
    for i in range(len(users_info)):
        location = users_info[i]['location']
        if location not in locations and location != '':
            locations[location] = users_info[i]['name']
        elif location != '':
            locations[location] = \
            locations[location] + \
            ', ' + users_info[i]['name']
  
    dicti_coor = {}
    for i in locations:
        coor = get_coordinates(i)
        if coor not in dicti_coor and coor != None:
            dicti_coor[coor] = locations[i]
        elif coor != None:
            dicti_coor[coor] = dicti_coor[coor] + ', ' + locations[i]

    user_map = folium.Map(tiles = "CartoDB dark_matter")
    
    marker_cluster = MarkerCluster().add_to(user_map)
    for loc in dicti_coor:
        try:
            location = loc
            folium.CircleMarker(
                location=[float(location[0]),
                float(location[1])],
                color=color_change(len(dicti_coor[loc].split(', '))),
                popup=dicti_coor[loc],
                fill_color='black', fill_opacity = 0.9,
                radius = 10,
                title=str(len(dicti_coor[loc].split(', ')))).add_to(marker_cluster)
        except:
            continue

    user_map.save('templates/friends.html')


# build_map('notworthcandle')