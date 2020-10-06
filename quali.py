from support.propagation_models import cost231_path_loss, fspl_path_loss, log_distance_model
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

    transmitted_frequency = 1872.500
    SENSITIVITY = -134

    n = 0.00

    n_lats, n_lons = (1000, 1000)
    lat_bounds = (-21.211645, -21.246091)  # lat_bounds[1]
    long_bounds = (-44.995876, -44.954157)  # long_bounds[0]

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

            tx_h = 56  # Base station height 30 to 200m
            rx_h = 1  # Mobile station height 1 to 10m
            mode = 2  # 1 = URBAN, 2 = SUBURBAN, 3 = OPEN

            path_loss = cost231_path_loss(transmitted_frequency, tx_h, rx_h, distance, mode)
            # received_power = transmitted_frequency - path_loss

            propagation_matrix[i][j] = path_loss
            # if received_power >= SENSITIVITY:
            #     propagation_matrix[i][j] = received_power
            # else:
            #     propagation_matrix[i][j] = 0

    distance_y = calc_distance((lat_bounds[0], long_bounds[0]), (lat_bounds[1], long_bounds[0]))  # |
    distance_x = calc_distance((lat_bounds[0], long_bounds[0]), (lat_bounds[0], long_bounds[1]))  # --
    print("Tamanho matrix de dados calculado: ", propagation_matrix.shape)
    print("Área: ", distance_y, "x", distance_x, "=", round(distance_y * distance_x, 2), "km2")
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
    # color_map = matplotlib.cm.get_cmap('rainbow_alpha') # custom
    # color_map = matplotlib.cm.get_cmap('gist_ncar')
    # color_map = matplotlib.cm.get_cmap('nipy_spectral')
    color_map = matplotlib.cm.get_cmap('jet')
    # color_map = matplotlib.cm.get_cmap('Wistia')
    # color_map = matplotlib.cm.get_cmap('copper')
    # color_map = matplotlib.cm.get_cmap('Oranges')

    normed_data = (propagation_matrix - propagation_matrix.min()) / \
                  (propagation_matrix.max() - propagation_matrix.min())
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


def table():
    distances = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    transmitted_frequency = 1872.500

    tx_h = 56  # Base station height 30 to 200m
    rx_h = 1  # Mobile station height 1 to 10m
    mode = 2  # 1 = URBAN, 2 = SUBURBAN, 3 = OPEN

    path_loss_cost231 = []
    path_loss_fspl = []
    path_loss_log_distance = []

    for distance in distances:
        # path_loss_cost231.append(cost231_path_loss(transmitted_frequency, tx_h, rx_h, distance, mode))
        # path_loss_fspl.append(fspl_path_loss(distance, transmitted_frequency))
        path_loss_log_distance.append(log_distance_model(distance, transmitted_frequency))

    fig, ax = plt.subplots()
    ax.plot(distances, path_loss_cost231)
    # ax.plot(distances, path_loss_fspl)

    ax.set(xlabel='Distancia (km)', ylabel='Path Loss (dB)',
           # title='Atenuação do Sinal - cost231'
           )
    ax.grid()
    plt.show()


if __name__ == '__main__':
    print_map()
    table()
