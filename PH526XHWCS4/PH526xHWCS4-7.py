region_cols = [region_colors[i] for i in whisky.Region.tolist()]
classification_cols = [cluster_colors[i] for i in whisky.Group.tolist()]

location_plot("Whisky Locations and Regions", region_cols)
location_plot("Whisky Locations and Groups", classification_cols)