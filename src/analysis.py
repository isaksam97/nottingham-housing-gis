import geopandas as gpd
import matplotlib.pyplot as plt
import os

wards = gpd.read_file("data/processed/wards.gpkg")
land = gpd.read_file("data/processed/land_parcels.gpkg")
assets = gpd.read_file("data/processed/property_assets.gpkg")

pipeline = land.groupby("ward_code")["est_capacity_homes"].sum()
asset_count = assets.groupby("ward_code").size()

summary = wards[["ward_code", "ward_name", "housing_need_index"]].set_index("ward_code")
summary["pipeline_homes"] = pipeline
summary["asset_count"] = asset_count
summary = summary.fillna(0)

print("WARD SUMMARY")
print(summary)

os.makedirs("outputs", exist_ok=True)
summary.to_csv("outputs/ward_summary.csv")
print("Saved outputs/ward_summary.csv")

os.makedirs("outputs/maps", exist_ok=True)
fig, ax = plt.subplots(figsize=(8, 8))
wards.plot(column="housing_need_index", cmap="OrRd", legend=True,
           edgecolor="white", linewidth=1, ax=ax)
for _, row in wards.iterrows():
    centre = row.geometry.centroid
    ax.annotate(row["ward_name"], (centre.x, centre.y), ha="center", fontsize=9)
ax.set_title("Housing Need Index by Ward (Nottingham - synthetic)")
ax.set_axis_off()
fig.savefig("outputs/maps/housing_need_by_ward.png", dpi=130, bbox_inches="tight")
print("Saved outputs/maps/housing_need_by_ward.png")
