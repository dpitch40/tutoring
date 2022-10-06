from math import sin, cos, acos, radians

R_EARTH = 6378.137

CITIES = [
    # City, state, latitude, longitude
    ("New York", "New York", 40.66, 73.93),
    ("Los Angeles", "California", 34.01, 118.41),
    ("Chicago", "Illinois", 41.83, 87.68),
    ("Houston", "Texas", 29.78, 95.39),
    ("Phoenix", "Arizona", 33.57, 112.09),
    ("Philadelphia", "Pennsylvania", 40, 75.13),
    ("San Antonio", "Texas", 29.47, 98.52),
    ("San Diego", "California", 32.81, 117.13),
    ("Dallas", "Texas", 32.79, 96.76),
    ("San Jose", "California", 37.29, 121.81),
    ("Austin", "Texas", 30.3, 97.75),
    ("Jacksonville", "Florida", 30.33, 81.66),
    ("Fort Worth", "Texas", 32.78, 97.34),
    ("Columbus", "Ohio", 39.98, 82.98),
    ("Indianapolis", "Indiana", 39.77, 86.14),
    ("Charlotte", "North Carolina", 35.2, 80.83),
    ("San Francisco", "California", 37.72, 123.03),
    ("Seattle", "Washington", 47.62, 122.35),
    ("Denver", "Colorado", 39.76, 104.88),
    ("Oklahoma City", "Oklahoma", 35.46, 97.51),
    ("Nashville", "Tennessee", 36.17, 86.78),
    ("El Paso", "Texas", 31.84, 106.42),
    ("Washington", "District of Columbia", 38.9, 77.01),
    ("Boston", "Massachusetts", 42.33, 71.02),
    ("Las Vegas", "Nevada", 36.22, 115.26),
    ("Portland", "Oregon", 45.53, 122.65),
    ("Detroit", "Michigan", 42.38, 83.1),
    ("Louisville", "Kentucky", 38.16, 85.64),
    ("Memphis", "Tennessee", 35.1, 89.97),
    ("Baltimore", "Maryland", 39.3, 76.61),
    ("Milwaukee", "Wisconsin", 43.06, 87.96),
    ("Albuquerque", "New Mexico", 35.1, 106.64),
    ("Fresno", "California", 36.78, 119.79),
    ("Tucson", "Arizona", 32.15, 110.87),
    ("Sacramento", "California", 38.56, 121.46),
    ("Mesa", "Arizona", 33.4, 111.71),
    ("Kansas City", "Missouri", 39.12, 94.55),
    ("Atlanta", "Georgia", 33.76, 84.42),
    ("Omaha", "Nebraska", 41.26, 96.04),
    ("Colorado Springs", "Colorado", 38.86, 104.76),
    ("Raleigh", "North Carolina", 35.83, 78.64),
    ("Virginia Beach", "Virginia", 36.78, 76.02),
    ("Long Beach", "California", 33.8, 118.15),
    ("Miami", "Florida", 25.77, 80.2),
    ("Oakland", "California", 37.76, 122.22),
    ("Minneapolis", "Minnesota", 44.96, 93.26),
    ("Tulsa", "Oklahoma", 36.12, 95.9),
    ("Bakersfield", "California", 35.32, 119.01),
    ("Wichita", "Kansas", 37.69, 97.34),
    ("Arlington", "Texas", 32.7, 97.12),
]

def spherical_distance(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    angle = acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    return R_EARTH * angle

def test_spherical_distance():
    cities_dict = {city: (lat, lon) for city, _, lat, lon in CITIES}
    lat1, lon1 = cities_dict["New York"]
    lat2, lon2 = cities_dict["Minneapolis"]

    estimated = round(spherical_distance(lat1, lon1, lat2, lon2))
    actual = 1635
    assert abs(estimated - actual) / actual < 0.01, estimated

def verify_path(path):
    """Given a path as a list of indexes on CITIES, a 2-tuple whose first element is whether the path:
        1. Ends at its starting point
        2. Visits every city exactly once (aside from the starting point)
    And whose second element is the total length of the path in km.
    """
    raise NotImplementedError

def test_verify_path():
    path1 = list(range(50)) + [0]
    assert verify_path(path1)[0] is True

    path2 = list(range(50))
    assert verify_path(path2)[0] is False

    path3 = list(range(50)) + [0]
    path3[1] = 25
    assert verify_path(path3)[0] is False
