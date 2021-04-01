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

    python reGen.py --year 2014 --api-key <my-key> --email <my-email> ...

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

    python reGen.py --year 2014 --api_key <my-key> --email <my-email> --geometry state --deg_resolution .5 --states NY

## Sources
1. [State shapefiles](https://www.weather.gov/gis/USStates)

2. [Solar Radiation Data](https://nsrdb.nrel.gov/)

3. [Wind Resource Data](https://www.nrel.gov/grid/wind-toolkit.html)

4. [Generation Modelling](https://sam.nrel.gov/)

## Citations
**ADD NSRDB**

**ADD WTK**

**ADD PYSAM**


