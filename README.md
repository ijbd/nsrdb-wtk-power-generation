# powGen-wtk-nsrdb
3/31/2021

## Intro
The purpose of this program is to extract solar and wind resource data using the National Renewable Energy Laboratory's developer API, and then convert those resources into hourly capacity factors using the System Advisor Model. 

## Setup
1. Get an [NREL API Key](https://developer.nrel.gov/signup/):

2. Install dependencies:

        pip install numpy
        pip install pandas
        pip install argparse
        pip install geopandas
        pip install NREL-PySAM
        pip install shapely
        pip install requests
        pip install matplotlib
        
3. Clone repository:

        git clone https://github.com/ijbd/powGen-wtk-nsrdb.git


## CLI

When running from the command line, parameters should be passed as key-value pairs. For example:

    python powGen-wtk-nsrdb.py --year 2014 --api-key <my-key> --email <my-email> ...

**Important:** Some sites might fail due to an API issue. This program is set up such that if the same command (same parameters) is run twice, the original capacity factors will not be overwritten, and instead the missing coordinates will be filled. It is strongly suggested that the user confirms all sites have been properly downloaded! 

**Important:** This program maintains UTC across coordinates.

| Key   | Type | Options | Required | Description|
| ----- | ---- | --------| -------- | ---------- |
| `year`  | int  | 2007-2014| Yes     | Inclusive  |
| `api_key` | str |         | Yes     |            |
| `email`  | str  |         | Yes     |            |
| `geometry` | str | `point`, `grid`, `state` | Yes | Indicate the geometry of your desired sites. `point`: single lat/lon coordinate. `grid`: Every point in a grid from a min lat/lon to a max lat/lon. `state`: Grid bounded by one or multiple states.|
| `lat`   | float |         | If `point` |            |
| `lon`   | float |         | If `point` |            |
| `min_lat`   | float |         | If `grid` |            |
| `min_lon`   | float |         | If `grid` |            |
| `max_lat`   | float |         | If `grid` |            |
| `max_lon`   | float |         | If `grid` |            |
| `states`    | str |        | If `state` | State(s) to include. **Example:** `MI` for just Michigan; `MI IL OH` for Michigan, Illinois and Ohio |
| `deg_resolution` | float | >.04| If `grid` or `state` | Lat/lon resolution (in degrees). **Default:** .04 |
| `verbose` | no argument |      | No | If flagged, program will print additional information throughout. |

Example:

    python powGen-wtk-nsrdb.py --year 2014 --api_key <my-key> --email <my-email> --geometry state --deg_resolution .5 --states NY

## PySAM Parameters
**Table 1:** PV Parameters

| Parameter | Value |
| --------- | ----- |
| Axis Type | Fixed |
| Azimuth | South-Facing |
| Tilt | Latitude Angle |
| DC:AC | 1.1 |
| Inverter Efficiency | 96 % |
| Other System Losses | 14 % |

**Table 2:** Wind Turbine Parameters

| Parameters | Value |
| ---------- | ----- |
| Hub Height | 100 m |
| Turbine Diameter | 90 m |



Each site is categorized into three IEC wind turbine classes based on the median annual wind speed @ 100m for the year downloaded. This reflects more realistically the power output of specific turbines that *would* be built at each site.

| Wind Speed | IEC Turbine Class |
| ---------- | ----------------- |
| v<sub>med</sub> > 9 m/s | IEC Class I |
| 8 m/s < v<sub>med</sub> < 9 m/s | IEC Class II |
| v<sub>med</sub> < 8 m/s | IEC Class III
 


## Sources
1. [Solar Radiation Data](https://nsrdb.nrel.gov/) [1]

2. [Wind Resource Data](https://www.nrel.gov/grid/wind-toolkit.html) [2-5]

1. [State shapefiles](https://www.weather.gov/gis/USStates) [6]

4. [Generation Modelling](https://sam.nrel.gov/) [7,8]

## Citations
[1] Sengupta, M., Y. Xie, A. Lopez, A. Habte, G. Maclaurin, and J. Shelby. 2018. "The National Solar Radiation Data Base (NSRDB)." Renewable and Sustainable Energy Reviews  89 (June): 51-60.

[2] Draxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.

[3] Draxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. "The Wind Integration National Dataset (WIND) Toolkit." Applied Energy 151: 355366.

[4] Lieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.

[5] King, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.

[6] National Weather Service. 2016. U.S. States and Territories Shapefile.

[7] System Advisor Model Version 2020.11.29 (SAM 2020.11.29). National Renewable Energy Laboratory. Golden, CO. Accessed December 27, 2020. https://sam.nrel.gov.

[8] PySAM Version 2.2.0. National Renewable Energy Laboratory. Golden, CO. Accessed December 27, 2020. https://github.com/nrel/pysam.


