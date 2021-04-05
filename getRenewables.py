'''
ijbd
4/2/2021

This is a complementary script providing an interface for accessing the capacity factors from `powGen-wtk-nsrdb.py` output.

'''
import numpy as np
import pandas as pd
import os

local_path = os.path.dirname(__file__)

def getRenewables(solar_filename, wind_filename):
    '''
    Args
    -------
        `solar_filename` (str) : Absolute path to the solar capacity factor file.
        `wind_filename` (wind) : Absolute path to the wind capacity factor file.

    Returns
    -------
        `renewableSites` (pd.Series) : Series of lat/lons
    '''
    solar = pd.read_csv(solar_filename,index_col=0)
    wind = pd.read_csv(wind_filename,index_col=0)

    # get locations
    solarLats = [float(c.split()[0]) for c in solar.columns]
    solarLons = [float(c.split()[1]) for c in solar.columns]
    windLats = [float(c.split()[0]) for c in wind.columns]
    windLons = [float(c.split()[1]) for c in wind.columns]

    # fill
    renewableSites = pd.DataFrame()
    renewableSites['Latitude'] = np.append(solarLats,windLats)
    renewableSites['Longitude'] = np.append(solarLons,windLons)

    # get generation 
    solarGen = solar.values.T
    windGen = wind.values.T

    renewableSites[range(len(solarGen))] = np.append(solarGen,windGen)

    return renewableSites

def main():
    solar_filename = 'output/solar_cf_NY_PA_OH_WV_KY_TN_VA_MD_DE_NC_NJ_0.5_2014.csv'
    wind_filename = 'output/wind_cf_NY_PA_OH_WV_KY_TN_VA_MD_DE_NC_NJ_0.5_2014.csv'

    renewableSites = getRenewables(solar_filename, wind_filename)
    print(renewableSites)

if __name__ == '__main__':
    main()