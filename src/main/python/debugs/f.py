import folium
import matplotlib
import numpy as np


def sample_data(shape=(73, 145)):
    nlats, nlons = shape

    lats = np.linspace(np.deg2rad(-21.211645), np.deg2rad(-21.246091), nlats)
    lons = np.linspace(np.deg2rad(-44.995876), np.deg2rad(-44.954157), nlons)

    lons, lats = np.meshgrid(lons, lats)

    lats = np.rad2deg(lats)
    lons = np.rad2deg(lons)
    data = np.random.randint(-200, -60, size=(nlats, nlons))

    return lons, lats, data


# -21.2262173,-44.9779183

lon, lat, data = sample_data(shape=(1000, 1000))
# lon -= 180

color_map = matplotlib.cm.get_cmap('rainbow')

normed_data = (data - data.min()) / (data.max() - data.min())
colored_data = color_map(normed_data)

m = folium.Map(location=[-21.2262173, -44.9779183], zoom_start=14)

folium.raster_layers.ImageOverlay(
    image=colored_data,
    bounds=[[lat.min(), lon.min()], [lat.max(), lon.max()]],
    mercator_project=True,

    opacity=0.6,
    interactive=True,
    cross_origin=False,
).add_to(m)

m.save('sample.html')
