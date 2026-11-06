import geopandas as gpd
from shapely.geometry import Polygon, Point
import os

BNG = "EPSG:27700"
os.makedirs("data/processed", exist_ok=True)

# --- wards ---
wards_data = [
    {"ward_code": "NW01", "ward_name": "Bulwell", "housing_need_index": 77,
     "geometry": Polygon([(454000, 339000), (456000, 339000), (456000, 341000), (454000, 341000)])},
    {"ward_code": "NW02", "ward_name": "Clifton", "housing_need_index": 54,
     "geometry": Polygon([(456000, 339000), (458000, 339000), (458000, 341000), (456000, 341000)])},
    {"ward_code": "NW03", "ward_name": "Aspley", "housing_need_index": 78,
     "geometry": Polygon([(458000, 339000), (460000, 339000), (460000, 341000), (458000, 341000)])},
]
wards = gpd.GeoDataFrame(wards_data, crs=BNG)
print(wards)
wards.to_file("data/processed/wards.gpkg", driver="GPKG")
print("Saved wards to data/processed/wards.gpkg")

# --- land parcels ---
land_data = [
    {"parcel_id": "LP001", "ward_code": "NW01", "status": "Available",
     "area_ha": 3.5, "est_capacity_homes": 105,
     "geometry": Polygon([(454400, 339400), (454700, 339400), (454700, 339700), (454400, 339700)])},
    {"parcel_id": "LP002", "ward_code": "NW02", "status": "Allocated",
     "area_ha": 2.0, "est_capacity_homes": 60,
     "geometry": Polygon([(456500, 339500), (456700, 339500), (456700, 339700), (456500, 339700)])},
    {"parcel_id": "LP003", "ward_code": "NW03", "status": "Under development",
     "area_ha": 4.2, "est_capacity_homes": 130,
     "geometry": Polygon([(458300, 339300), (458600, 339300), (458600, 339600), (458300, 339600)])},
]
land = gpd.GeoDataFrame(land_data, crs=BNG)
print(land)
land.to_file("data/processed/land_parcels.gpkg", driver="GPKG")
print("Saved land parcels to data/processed/land_parcels.gpkg")

# --- property assets ---
assets_data = [
    {"asset_id": "PA001", "ward_code": "NW01", "property_type": "House", "condition": "Good",
     "geometry": Point(454300, 339300)},
    {"asset_id": "PA002", "ward_code": "NW01", "property_type": "Flat", "condition": "Fair",
     "geometry": Point(454600, 339600)},
    {"asset_id": "PA003", "ward_code": "NW02", "property_type": "Bungalow", "condition": "Poor",
     "geometry": Point(456700, 339700)},
    {"asset_id": "PA004", "ward_code": "NW03", "property_type": "House", "condition": "Good",
     "geometry": Point(458400, 339400)},
]
assets = gpd.GeoDataFrame(assets_data, crs=BNG)
print(assets)
assets.to_file("data/processed/property_assets.gpkg", driver="GPKG")
print("Saved property assets to data/processed/property_assets.gpkg")
