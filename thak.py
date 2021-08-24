import fiona
from shapely.geometry import shape

collection = fiona.open('./TOWN_MOI_1100415.shp')

for mih in collection:
    sai, lam, tang, pak = shape(mih['geometry']).bounds
    king = (sai + tang) / 2
    ui = (lam + pak) / 2
    print(mih['properties']['TOWNCODE'], king, ui)
