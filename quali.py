from support.propagation_models import cost231_path_loss
import io
import sys
import random
import folium
import numpy as np
import matplotlib
import matplotlib.cm
from haversine import haversine, Unit
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap


def calc_distance(point_1, point_2, unit=Unit.METERS):
    return haversine(point_1, point_2, unit=unit)


def print_map():
    ERB_LOCATION = (-21.226244, -44.978407)

    transmitted_power = 74.471580313
    SENSITIVITY = -134

    n = 0.00

    n_lats, n_lons = (100, 100)
    lat_bounds = (-21.211645, -21.246091)
    long_bounds = (-44.995876, -44.954157)

    lats_deg = np.linspace((lat_bounds[0]), (lat_bounds[1]), n_lats)
    lons_deg = np.linspace((long_bounds[0]), (long_bounds[1]), n_lons)

    lats_in_rad = np.deg2rad(lats_deg)
    longs_in_rad = np.deg2rad(lons_deg)

    lons_mesh, lats_mesh = np.meshgrid(longs_in_rad, lats_in_rad)

    lats_mesh_deg = np.rad2deg(lats_mesh)
    lons_mesh_deg = np.rad2deg(lons_mesh)

    propagation_matrix = np.empty([n_lats, n_lons])
    for i, point_long in enumerate(lons_deg):
        for j, point_lat in enumerate(lats_deg):
            point = (point_lat, point_long)
            distance = calc_distance(ERB_LOCATION, point)

            path_loss = cost231_path_loss(transmitted_power, 30, 1, distance, 2)
            received_power = transmitted_power - path_loss

            propagation_matrix[i][j] = received_power
            # if received_power >= SENSITIVITY:
            #     propagation_matrix[i][j] = received_power
            # else:
            #     propagation_matrix[i][j] = 0

    print(propagation_matrix.shape)

    # ------------------------------------------------------------------------------------------------------------------
    # get colormap
    ncolors = 512
    color_array = plt.get_cmap('gist_ncar')(range(ncolors))

    # change alpha values
    color_array[:, -1] = np.linspace(0.0, 1.0, ncolors)

    # create a colormap object
    map_object = LinearSegmentedColormap.from_list(name='rainbow_alpha', colors=color_array)

    # register this new colormap with matplotlib
    plt.register_cmap(cmap=map_object)

    # show some example data
    f, ax = plt.subplots()
    h = ax.imshow(np.random.rand(100, 100), cmap='rainbow_alpha')
    plt.colorbar(mappable=h)
    # ------------------------------------------------------------------------------------------------------------------


    # color_map = matplotlib.cm.get_cmap('YlOrRd')
    # color_map = matplotlib.cm.get_cmap('plasma')
    # color_map = matplotlib.cm.get_cmap('spring')
    # color_map = matplotlib.cm.get_cmap('summer')
    color_map = matplotlib.cm.get_cmap('rainbow_alpha')
    # color_map = matplotlib.cm.get_cmap('gist_ncar')
    # color_map = matplotlib.cm.get_cmap('nipy_spectral')
    # color_map = matplotlib.cm.get_cmap('jet')
    # color_map = matplotlib.cm.get_cmap('Wistia')
    # color_map = matplotlib.cm.get_cmap('copper')
    # color_map = matplotlib.cm.get_cmap('Oranges')

    normed_data = (propagation_matrix - propagation_matrix.min()) / ( propagation_matrix.max() - propagation_matrix.min())
    colored_data = color_map(normed_data)

    m = folium.Map(
        location=ERB_LOCATION,
        zoom_start=16,
        control_scale=True
    )

    folium.raster_layers.ImageOverlay(
        image=colored_data,
        bounds=[[lats_mesh_deg.min(), lons_mesh_deg.min()], [lats_mesh_deg.max(), lons_mesh_deg.max()]],
        mercator_project=True,

        opacity=0.4,
        interactive=True,
        cross_origin=False,
    ).add_to(m)

    folium.Marker(
        location=ERB_LOCATION,
        popup='Estação Rádio Base Vivo',
        draggable=False,
        icon=folium.Icon(prefix='glyphicon', icon='tower')
    ).add_to(m)

    # data = io.BytesIO()
    # m.save(data, close_file=False)
    # self.web_view.setHtml(data.getvalue().decode())
    m.save("quali.html")
    print("batata")

if __name__ == '__main__':
    print_map()