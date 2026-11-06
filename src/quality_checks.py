import geopandas as gpd

wards = gpd.read_file("data/processed/wards.gpkg")
land = gpd.read_file("data/processed/land_parcels.gpkg")
assets = gpd.read_file("data/processed/property_assets.gpkg")

print("DATA QUALITY CHECKS")
print("=" * 45)

for name, layer in [("wards", wards), ("land", land), ("assets", assets)]:
    if layer.crs.to_epsg() == 27700:
        print(f"[PASS] {name}: coordinate system is British National Grid")
    else:
        print(f"[FAIL] {name}: wrong coordinate system ({layer.crs})")

for name, layer in [("wards", wards), ("land", land), ("assets", assets)]:
    missing = layer["ward_code"].isna().sum()
    print(f"[{'PASS' if missing == 0 else 'FAIL'}] {name}: {missing} missing ward_code values")

valid_wards = set(wards["ward_code"])
for name, layer in [("land", land), ("assets", assets)]:
    orphans = (~layer["ward_code"].isin(valid_wards)).sum()
    print(f"[{'PASS' if orphans == 0 else 'FAIL'}] {name}: {orphans} rows pointing to a ward that doesn't exist")

print("=" * 45)
print("Checks complete.")
