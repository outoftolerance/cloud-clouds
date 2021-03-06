#Input into Pi
import pywapi
import pprint
pp = pprint.PrettyPrinter(indent=4)
 
vancouver = pywapi.get_weather_from_weather_com('CAXX0518')
 
pp.pprint(vancouver)


# Solution:
{   'current_conditions': {   'barometer': {   'direction': u'steady',
                                               'reading': u'1026.08'},
                              'dewpoint': u'13',
                              'feels_like': u'17',
                              'humidity': u'80',
                              'icon': u'30',
                              'last_updated': u'6/14/14 11:25 AM BST',
                              'moon_phase': {   'icon': u'16',
                                                'text': u'Waning Gibbous'},
                              'station': u'Waddington, LIN, UK',
                              'temperature': u'17',
                              'text': u'Partly Cloudy',
                              'uv': {   'index': u'4', 'text': u'Moderate'},
                              'visibility': u'12.9',
                              'wind': {   'direction': u'50',
                                          'gust': u'N/A',
                                          'speed': u'12',
                                          'text': u'NE'}},
    'forecasts': [   {   'date': u'Jun 14',
                         'day': {   'brief_text': u'P Cloudy',
                                    'chance_precip': u'20',
                                    'humidity': u'72',
                                    'icon': u'30',
                                    'text': u'Partly Cloudy',
                                    'wind': {   'direction': u'32',
                                                'gust': u'N/A',
                                                'speed': u'19',
                                                'text': u'NNE'}},
                         'day_of_week': u'Saturday',
                         'high': u'18',
                         'low': u'10',
                         'night': {   'brief_text': u'M Clear',
                                      'chance_precip': u'10',
                                      'humidity': u'87',
                                      'icon': u'33',
                                      'text': u'Mostly Clear',
                                      'wind': {   'direction': u'16',
                                                  'gust': u'N/A',
                                                  'speed': u'17',
                                                  'text': u'NNE'}},
                         'sunrise': u'4:34 AM',
                         'sunset': u'9:31 PM'},
                     {   'date': u'Jun 15',
                         'day': {   'brief_text': u'P Cloudy',
                                    'chance_precip': u'10',
                                    'humidity': u'70',
                                    'icon': u'30',
                                    'text': u'Partly Cloudy',
                                    'wind': {   'direction': u'19',
                                                'gust': u'N/A',
                                                'speed': u'19',
                                                'text': u'NNE'}},
                         'day_of_week': u'Sunday',
                         'high': u'18',
                         'low': u'10',
                         'night': {   'brief_text': u'P Cloudy',
                                      'chance_precip': u'10',
                                      'humidity': u'87',
                                      'icon': u'29',
                                      'text': u'Partly Cloudy',
                                      'wind': {   'direction': u'23',
                                                  'gust': u'N/A',
                                                  'speed': u'16',
                                                  'text': u'NNE'}},
                         'sunrise': u'4:34 AM',
                         'sunset': u'9:31 PM'},
                     {   'date': u'Jun 16',
                         'day': {   'brief_text': u'Cloudy',
                                    'chance_precip': u'0',
                                    'humidity': u'76',
                                    'icon': u'26',
                                    'text': u'Cloudy',
                                    'wind': {   'direction': u'4',
                                                'gust': u'N/A',
                                                'speed': u'20',
                                                'text': u'N'}},
                         'day_of_week': u'Monday',
                         'high': u'15',
                         'low': u'10',
                         'night': {   'brief_text': u'Clear Late',
                                      'chance_precip': u'0',
                                      'humidity': u'78',
                                      'icon': u'29',
                                      'text': u'Clouds Early / Clearing Late',
                                      'wind': {   'direction': u'1',
                                                  'gust': u'N/A',
                                                  'speed': u'17',
                                                  'text': u'N'}},
                         'sunrise': u'4:34 AM',
                         'sunset': u'9:31 PM'},
                     {   'date': u'Jun 17',
                         'day': {   'brief_text': u'P Cloudy',
                                    'chance_precip': u'0',
                                    'humidity': u'75',
                                    'icon': u'30',
                                    'text': u'Partly Cloudy',
                                    'wind': {   'direction': u'13',
                                                'gust': u'N/A',
                                                'speed': u'20',
                                                'text': u'NNE'}},
                         'day_of_week': u'Tuesday',
                         'high': u'17',
                         'low': u'11',
                         'night': {   'brief_text': u'M Cloudy',
                                      'chance_precip': u'10',
                                      'humidity': u'82',
                                      'icon': u'27',
                                      'text': u'Mostly Cloudy',
                                      'wind': {   'direction': u'1',
                                                  'gust': u'N/A',
                                                  'speed': u'16',
                                                  'text': u'N'}},
                         'sunrise': u'4:34 AM',
                         'sunset': u'9:31 PM'},
                     {   'date': u'Jun 18',
                         'day': {   'brief_text': u'M Cloudy',
                                    'chance_precip': u'10',
                                    'humidity': u'75',
                                    'icon': u'28',
                                    'text': u'Mostly Cloudy',
                                    'wind': {   'direction': u'12',
                                                'gust': u'N/A',
                                                'speed': u'19',
                                                'text': u'NNE'}},
                         'day_of_week': u'Wednesday',
                         'high': u'19',
                         'low': u'10',
                         'night': {   'brief_text': u'P Cloudy',
                                      'chance_precip': u'0',
                                      'humidity': u'82',
                                      'icon': u'29',
                                      'text': u'Partly Cloudy',
                                      'wind': {   'direction': u'10',
                                                  'gust': u'N/A',
                                                  'speed': u'9',
                                                  'text': u'N'}},
                         'sunrise': u'4:34 AM',
                         'sunset': u'9:31 PM'}],
    'location': {   'lat': u'53.23',
                    'lon': u'-0.54',
                    'name': u'Lincoln, LIN, United Kingdom'},
    'units': {   'distance': u'km',
                 'pressure': u'mb',
                 'rainfall': u'mm',
                 'speed': u'km/h',
                 'temperature': u'C'}}