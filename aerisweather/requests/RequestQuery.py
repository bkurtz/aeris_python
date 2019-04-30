""" Defines the available query options for each Aeris API endpoint's requests.

    For details on the use of each query value, see the Queries secton of the corresponding endpoint, such
    as the Observations endpoint's queries found here:
    https://www.aerisweather.com/support/docs/api/reference/endpoints/observations/#queries.
"""
from collections import namedtuple


class RequestQuery:

    request_query = namedtuple('REQUEST_QUERY', ['AIR_QUALITY', 'ALERTS', 'OBSERVATIONS', 'OBSERVATIONS_SUMMARY',
                                                 'PLACES'])

    aqi = namedtuple('AIR_QUALITY', ['PM2P5', 'PM10', 'NO2', 'CO', 'SO2', 'O3', 'DT', 'ID', 'NAME', 'CITY',
                                     'STATE', 'COUNTRY'])
    AIR_QUALITY = aqi('pm2p5', 'pm10', 'no2', 'co', 'so2', 'o3', 'dt', 'id', 'name', 'city', 'state', 'country')

    alrt = namedtuple('ALERTS', ['ACTIVE', 'ADDED', 'BEGINS', 'COUNTRY', 'EMERGENCY', 'EXPIRES', 'ID', 'ISSUED',
                                 'LOC', 'NAME', 'SIG', 'SIGP', 'STATE', 'TYPE'])
    ALERTS = alrt('active', 'added', 'begins', 'country', 'emergency', 'expires', 'id', 'issued', 'loc', 'name',
                  'sig', 'sigp', 'state', 'type')

    lght = namedtuple('LIGHTNING', ['TYPE', 'PEAKAMP', 'HEIGHT', 'NUMSENSORS'])
    LIGHTNING = lght('type', 'peakamp', 'height', 'numsensors')

    lght_sum = namedtuple('LIGHTNING_SUMMARY', ['DT', 'TYPE', 'PEAKAMP', 'HEIGHT', 'NUMSENSORS'])
    LIGHTNING_SUMMARY = lght_sum('dt', 'type', 'peakamp', 'height', 'numsensors')

    obs = namedtuple('OBSERVATIONS', ['COUNTRY', 'DEWPT', 'ELEV', 'HAS_PRECIP', 'ID', 'GUST', 'NAME', 'PRECIP',
                                      'PRESSURE', 'QC', 'QC_CODE', 'RH', 'STATE', 'TEMP', 'WIND', 'WIND_DIR'])
    OBSERVATIONS = obs('country', 'dewpt', 'elev', 'hasprecip', 'id', 'gust', 'name', 'precip', 'pressure', 'qc',
                       'qccode', 'rh', 'state', 'temp', 'wind', 'winddir')

    obs_archive = namedtuple('OBSERVATIONS_ARCHIVE', ['TEMP', 'DEWPT', 'RH', 'PRESSURE', 'WIND', 'WIND_DIR',
                                                      'GUST', 'ID', 'DT', 'NAME', 'STATE', 'COUNTRY', 'HAS_PRECIP'])
    OBSERVATIONS_ARCHIVE = obs_archive('temp', 'dewpt', 'rh', 'pressure', 'wind', 'winddir', 'gust', 'id', 'dt',
                                       'name', 'state', 'country', 'hasprecip')

    obs_sum = namedtuple('OBSERVATIONS_SUMMARY', ['AVG_DEWPT', 'AVG_PRES', 'AVG_RH', 'AVG_VIS', 'AVGT', 'COUNT',
                                                  'COUNTRY', 'DATE', 'ELEV', 'GUST', 'HAS_PRECIP', 'ID',
                                                  'MAX_DEWPT', 'MAX_PRES', 'MAX_RH', 'MAX_VIS', 'MAXT', 'MIN_DEWPT',
                                                  'MIN_PRES', 'MIN_RH', 'MIN_VIS', 'MINT', 'NAME', 'PRECIP',
                                                  'PRECIPC', 'STATE', 'WIND'])
    OBSERVATIONS_SUMMARY = obs_sum('avgdewpt', 'avgp', 'avgrh', 'avgv', 'avgt', 'count', 'country', 'dt', 'elev',
                                   'gust', 'hasprecip', 'id', 'maxdewpt', 'maxp', 'maxrh', 'maxv', 'maxt', 'mindewpt',
                                   'minp', 'minrh', 'minv', 'mint', 'name', 'precip', 'precipc', 'state', 'wind')

    pl = namedtuple('PLACES', ['ALT_NAME', 'COUNTRY', 'NAME', 'POP', 'STATE'])
    PLACES = pl('altname', 'country', 'name', 'pop', 'state')

    tropcyc = namedtuple('TROPICAL_CYCLONE', ['ID', 'BASIN', 'ORIGIN', 'CURRENT_BASIN', 'YEAR', 'EVENT', 'NAME',
                                              'START_DATE', 'END_DATE', 'MAX_TYPE', 'MAX_CAT', 'MAX_WIND_SPEEDS',
                                              'MIN_PRESSURE', 'TEST', 'STORM_TYPE', 'STORM_CAT', 'WINDSPEED',
                                              'PRESSURE', 'STORM_DIR', 'STORM_SPEED', 'TRACK_STORM_TYPE',
                                              'TRACK_STORM_CAT', 'TRACK_WIND_SPEED', 'TRACK_PRESSURE', 'TRACK_STORM_DIR',
                                              'TRACK_STORM_SPEED', 'FC_STORM_TYPE', 'FC_STORM_CAT', 'FC_WIND_SPEED'])
    TROPICAL_CYCLONE = tropcyc('id', 'basic', 'origin', 'current_basin', 'year', 'event', 'name', 'start_date',
                               'end_date', 'max_type', 'max_cat', 'max_wind_speeds', 'min_pressure', 'test',
                               'storm_type', 'storm_cat', 'windspeed', 'pressure', 'storm_dir', 'storm_speed',
                               'track_storm_type', 'track_storm_cat', 'track_wind_speed', 'track_pressure',
                               'track_storm_dir', 'track_storm_speed', 'fc_storm_type', 'fc_storm_cat', 'fc_wind_speed')


