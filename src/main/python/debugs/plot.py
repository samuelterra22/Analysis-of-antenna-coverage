import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

FOs = [{'lat': -21.227515433313584, 'lng': -44.97664851579612, 'height': 39.2, 'power': 42.0, 'of': -117.58},
       {'lat': -21.227515433313584, 'lng': -44.97664851579612, 'height': 47.6, 'power': 42.0, 'of': -96.37599999999998},
       {'lat': -21.227515433313584, 'lng': -44.97664851579612, 'height': 56.0, 'power': 42.0, 'of': -73.88399999999996},
       {'lat': -21.227515433313584, 'lng': -44.97664851579612, 'height': 64.4, 'power': 42.0,
        'of': -51.692000000000036},
       {'lat': -21.227515433313584, 'lng': -44.97664851579612, 'height': 72.8, 'power': 42.0,
        'of': -29.196000000000026},
       {'lat': -21.22798114597635, 'lng': -44.97783152463657, 'height': 39.2, 'power': 42.0, 'of': -143.272},
       {'lat': -21.22798114597635, 'lng': -44.97783152463657, 'height': 47.6, 'power': 42.0, 'of': -122.47999999999996},
       {'lat': -21.22798114597635, 'lng': -44.97783152463657, 'height': 56.0, 'power': 42.0, 'of': -101.16799999999995},
       {'lat': -21.22798114597635, 'lng': -44.97783152463657, 'height': 72.8, 'power': 42.0, 'of': -54.879999999999995},
       {'lat': -21.2282480861869, 'lng': -44.97656893992344, 'height': 39.2, 'power': 42.0, 'of': -133.37199999999999},
       {'lat': -21.2282480861869, 'lng': -44.97656893992344, 'height': 39.2, 'power': 51.0, 'of': 202.5960000000001},
       {'lat': -21.2282480861869, 'lng': -44.97656893992344, 'height': 47.6, 'power': 42.0, 'of': -112.28000000000003},
       {'lat': -21.2282480861869, 'lng': -44.97656893992344, 'height': 56.0, 'power': 42.0, 'of': -88.93599999999998},
       {'lat': -21.2282480861869, 'lng': -44.97656893992344, 'height': 64.4, 'power': 42.0, 'of': -65.63999999999999},
       {'lat': -21.2282480861869, 'lng': -44.97656893992344, 'height': 64.4, 'power': 51.0, 'of': 320.84799999999996},
       {'lat': -21.2282480861869, 'lng': -44.97656893992344, 'height': 72.8, 'power': 42.0, 'of': -42.62399999999997},
       {'lat': -21.226531448063035, 'lng': -44.979663136823255, 'height': 39.2, 'power': 42.0, 'of': -129.824},
       {'lat': -21.226531448063035, 'lng': -44.979663136823255, 'height': 39.2, 'power': 51.0,
        'of': 201.14800000000002},
       {'lat': -21.226531448063035, 'lng': -44.979663136823255, 'height': 47.6, 'power': 42.0,
        'of': -111.14400000000003},
       {'lat': -21.226531448063035, 'lng': -44.979663136823255, 'height': 56.0, 'power': 42.0,
        'of': -90.68799999999996},
       {'lat': -21.226531448063035, 'lng': -44.979663136823255, 'height': 56.0, 'power': 60.0, 'of': 597.2079999999999},
       {'lat': -21.226531448063035, 'lng': -44.979663136823255, 'height': 64.4, 'power': 42.0,
        'of': -68.60400000000001},
       {'lat': -21.226531448063035, 'lng': -44.979663136823255, 'height': 72.8, 'power': 42.0,
        'of': -46.68800000000002},
       {'lat': -21.225154923450688, 'lng': -44.98194300811833, 'height': 39.2, 'power': 42.0,
        'of': -172.56000000000003},
       {'lat': -21.225154923450688, 'lng': -44.98194300811833, 'height': 39.2, 'power': 51.0, 'of': 109.904},
       {'lat': -21.225154923450688, 'lng': -44.98194300811833, 'height': 39.2, 'power': 78.0, 'of': 691.724},
       {'lat': -21.225154923450688, 'lng': -44.98194300811833, 'height': 47.6, 'power': 42.0, 'of': -152.464},
       {'lat': -21.225154923450688, 'lng': -44.98194300811833, 'height': 56.0, 'power': 42.0, 'of': -135.016},
       {'lat': -21.225154923450688, 'lng': -44.98194300811833, 'height': 56.0, 'power': 51.0, 'of': 186.81600000000003},
       {'lat': -21.225154923450688, 'lng': -44.98194300811833, 'height': 64.4, 'power': 42.0,
        'of': -118.03999999999999},
       {'lat': -21.225154923450688, 'lng': -44.98194300811833, 'height': 72.8, 'power': 42.0,
        'of': -100.17599999999999},
       {'lat': -21.228499150357965, 'lng': -44.98101226793093, 'height': 39.2, 'power': 42.0,
        'of': -121.71199999999999},
       {'lat': -21.228499150357965, 'lng': -44.98101226793093, 'height': 39.2, 'power': 51.0, 'of': 242.20800000000006},
       {'lat': -21.228499150357965, 'lng': -44.98101226793093, 'height': 47.6, 'power': 42.0, 'of': -98.52000000000001},
       {'lat': -21.228499150357965, 'lng': -44.98101226793093, 'height': 56.0, 'power': 42.0, 'of': -74.35200000000003},
       {'lat': -21.228499150357965, 'lng': -44.98101226793093, 'height': 64.4, 'power': 42.0,
        'of': -49.928000000000026},
       {'lat': -21.230586243120467, 'lng': -44.982217002426935, 'height': 39.2, 'power': 42.0, 'of': -190.812},
       {'lat': -21.230586243120467, 'lng': -44.982217002426935, 'height': 47.6, 'power': 42.0, 'of': -173.3},
       {'lat': -21.230586243120467, 'lng': -44.982217002426935, 'height': 64.4, 'power': 42.0,
        'of': -127.51200000000001},
       {'lat': -21.230586243120467, 'lng': -44.982217002426935, 'height': 72.8, 'power': 42.0, 'of': -101.392},
       {'lat': -21.22756826820764, 'lng': -44.9807051592169, 'height': 39.2, 'power': 42.0, 'of': -117.71999999999997},
       {'lat': -21.22756826820764, 'lng': -44.9807051592169, 'height': 47.6, 'power': 42.0, 'of': -96.05199999999999},
       {'lat': -21.22756826820764, 'lng': -44.9807051592169, 'height': 47.6, 'power': 51.0, 'of': 280.38800000000003},
       {'lat': -21.22756826820764, 'lng': -44.9807051592169, 'height': 47.6, 'power': 69.0, 'of': 679.7160000000001},
       {'lat': -21.22756826820764, 'lng': -44.9807051592169, 'height': 47.6, 'power': 78.0, 'of': 696.0719999999999},
       {'lat': -21.22756826820764, 'lng': -44.9807051592169, 'height': 56.0, 'power': 42.0, 'of': -72.99599999999998},
       {'lat': -21.22756826820764, 'lng': -44.9807051592169, 'height': 64.4, 'power': 42.0, 'of': -50.15999999999997},
       {'lat': -21.229645857443764, 'lng': -44.978913966510625, 'height': 39.2, 'power': 42.0,
        'of': -185.77200000000002},
       {'lat': -21.229645857443764, 'lng': -44.978913966510625, 'height': 47.6, 'power': 42.0, 'of': -169.276},
       {'lat': -21.229645857443764, 'lng': -44.978913966510625, 'height': 56.0, 'power': 42.0,
        'of': -149.50000000000003},
       {'lat': -21.229645857443764, 'lng': -44.978913966510625, 'height': 64.4, 'power': 42.0,
        'of': -126.68800000000002},
       {'lat': -21.229645857443764, 'lng': -44.978913966510625, 'height': 72.8, 'power': 42.0,
        'of': -102.46000000000004},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 39.2, 'power': 42.0, 'of': -160.56},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 47.6, 'power': 42.0, 'of': -139.924},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 47.6, 'power': 51.0, 'of': 200.78400000000005},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 47.6, 'power': 69.0, 'of': 678.044},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 47.6, 'power': 78.0, 'of': 696.7},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 56.0, 'power': 42.0,
        'of': -117.59999999999997},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 56.0, 'power': 51.0, 'of': 241.724},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 64.4, 'power': 42.0, 'of': -92.584},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 72.8, 'power': 42.0, 'of': -68.10000000000002},
       {'lat': -21.229708282418922, 'lng': -44.980324564582865, 'height': 39.2, 'power': 42.0, 'of': -170.052},
       {'lat': -21.229708282418922, 'lng': -44.980324564582865, 'height': 39.2, 'power': 51.0,
        'of': 156.64000000000004},
       {'lat': -21.229708282418922, 'lng': -44.980324564582865, 'height': 47.6, 'power': 42.0, 'of': -150.096},
       {'lat': -21.229708282418922, 'lng': -44.980324564582865, 'height': 56.0, 'power': 42.0,
        'of': -126.37599999999998},
       {'lat': -21.229708282418922, 'lng': -44.980324564582865, 'height': 64.4, 'power': 42.0, 'of': -101.536},
       {'lat': -21.229708282418922, 'lng': -44.980324564582865, 'height': 72.8, 'power': 42.0,
        'of': -76.11599999999996},
       {'lat': -21.228577385419886, 'lng': -44.983870698574215, 'height': 39.2, 'power': 42.0, 'of': -159.224},
       {'lat': -21.228577385419886, 'lng': -44.983870698574215, 'height': 47.6, 'power': 42.0, 'of': -135.624},
       {'lat': -21.228577385419886, 'lng': -44.983870698574215, 'height': 56.0, 'power': 42.0,
        'of': -109.48000000000002},
       {'lat': -21.228577385419886, 'lng': -44.983870698574215, 'height': 64.4, 'power': 42.0, 'of': -84.684},
       {'lat': -21.230899765411156, 'lng': -44.98224948231637, 'height': 39.2, 'power': 42.0,
        'of': -193.68400000000003},
       {'lat': -21.230899765411156, 'lng': -44.98224948231637, 'height': 56.0, 'power': 42.0, 'of': -154.704},
       {'lat': -21.23183489088755, 'lng': -44.97929579018264, 'height': 39.2, 'power': 42.0, 'of': -233.77599999999995},
       {'lat': -21.23183489088755, 'lng': -44.97929579018264, 'height': 47.6, 'power': 42.0, 'of': -222.044},
       {'lat': -21.23183489088755, 'lng': -44.97929579018264, 'height': 56.0, 'power': 42.0, 'of': -209.132},
       {'lat': -21.23183489088755, 'lng': -44.97929579018264, 'height': 64.4, 'power': 42.0, 'of': -195.812},
       {'lat': -21.231401847851636, 'lng': -44.98261596697181, 'height': 39.2, 'power': 42.0, 'of': -199.2},
       {'lat': -21.231401847851636, 'lng': -44.98261596697181, 'height': 47.6, 'power': 42.0, 'of': -182.344},
       {'lat': -21.231401847851636, 'lng': -44.98261596697181, 'height': 56.0, 'power': 42.0,
        'of': -160.90400000000002},
       {'lat': -21.231401847851636, 'lng': -44.98261596697181, 'height': 64.4, 'power': 42.0,
        'of': -138.05199999999996},
       {'lat': -21.231401847851636, 'lng': -44.98261596697181, 'height': 72.8, 'power': 42.0, 'of': -111.916},
       {'lat': -21.229327021727098, 'lng': -44.97616973519833, 'height': 47.6, 'power': 78.0, 'of': 696.7}]

# FOs = [
#     {'lat': -21.225128763766516, 'lng': -44.97471133268666, 'height': 39.2, 'power': 42.0, 'of': -144.51600000000002},
#     {'lat': -21.225128763766516, 'lng': -44.97471133268666, 'height': 47.6, 'power': 42.0, 'of': -121.77600000000002},
#     {'lat': -21.225128763766516, 'lng': -44.97471133268666, 'height': 56.0, 'power': 42.0, 'of': -104.36800000000002},
#     {'lat': -21.225128763766516, 'lng': -44.97471133268666, 'height': 64.4, 'power': 42.0, 'of': -86.27600000000001},
#     {'lat': -21.225128763766516, 'lng': -44.97471133268666, 'height': 72.8, 'power': 42.0, 'of': -63.74799999999999},
#     {'lat': -21.224173227350388, 'lng': -44.971201510003254, 'height': 39.2, 'power': 42.0, 'of': -96.892},
#     {'lat': -21.224173227350388, 'lng': -44.971201510003254, 'height': 47.6, 'power': 42.0, 'of': -76.06},
#     {'lat': -21.224173227350388, 'lng': -44.971201510003254, 'height': 56.0, 'power': 42.0, 'of': -55.352000000000004},
#     {'lat': -21.224173227350388, 'lng': -44.971201510003254, 'height': 64.4, 'power': 42.0, 'of': -33.640000000000015},
#     {'lat': -21.224173227350388, 'lng': -44.971201510003254, 'height': 72.8, 'power': 42.0, 'of': -8.496000000000038},
#     {'lat': -21.22454365944612, 'lng': -44.96853039204966, 'height': 39.2, 'power': 42.0, 'of': -34.18800000000002},
#     {'lat': -21.22454365944612, 'lng': -44.96853039204966, 'height': 56.0, 'power': 42.0, 'of': 15.344000000000023},
#     {'lat': -21.22454365944612, 'lng': -44.96853039204966, 'height': 64.4, 'power': 42.0, 'of': 41.036},
#     {'lat': -21.22454365944612, 'lng': -44.96853039204966, 'height': 72.8, 'power': 51.0, 'of': 585.86},
#     {'lat': -21.22454365944612, 'lng': -44.96853039204966, 'height': 72.8, 'power': 78.0, 'of': 699.968},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 39.2, 'power': 42.0, 'of': 1.8280000000000314},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 39.2, 'power': 51.0, 'of': 519.268},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 39.2, 'power': 60.0, 'of': 690.7},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 39.2, 'power': 69.0, 'of': 699.876},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 39.2, 'power': 78.0, 'of': 699.968},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 47.6, 'power': 42.0, 'of': 28.879999999999995},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 56.0, 'power': 42.0, 'of': 55.45600000000002},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 56.0, 'power': 78.0, 'of': 699.968},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 64.4, 'power': 42.0, 'of': 82.79200000000003},
#     {'lat': -21.228175026807506, 'lng': -44.96993261693371, 'height': 72.8, 'power': 42.0, 'of': 111.50799999999995},
#     {'lat': -21.224366637348407, 'lng': -44.96970521578067, 'height': 39.2, 'power': 42.0, 'of': -40.82400000000001},
#     {'lat': -21.224366637348407, 'lng': -44.96970521578067, 'height': 47.6, 'power': 42.0, 'of': -17.127999999999986},
#     {'lat': -21.224366637348407, 'lng': -44.96970521578067, 'height': 64.4, 'power': 42.0, 'of': 34.952000000000055},
#     {'lat': -21.224366637348407, 'lng': -44.96970521578067, 'height': 72.8, 'power': 42.0, 'of': 61.383999999999986},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 39.2, 'power': 42.0, 'of': -88.648},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 47.6, 'power': 42.0, 'of': -63.74400000000003},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 56.0, 'power': 42.0, 'of': -35.73200000000003},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 64.4, 'power': 42.0, 'of': -6.659999999999997},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 64.4, 'power': 51.0, 'of': 497.7720000000001},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 64.4, 'power': 60.0, 'of': 688.776},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 64.4, 'power': 69.0, 'of': 700.0},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 64.4, 'power': 78.0, 'of': 700.0},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 72.8, 'power': 42.0, 'of': 19.480000000000018},
#     {'lat': -21.228061705294735, 'lng': -44.97201083049632, 'height': 39.2, 'power': 42.0, 'of': -29.383999999999986},
#     {'lat': -21.228061705294735, 'lng': -44.97201083049632, 'height': 47.6, 'power': 42.0, 'of': -3.388000000000062},
#     {'lat': -21.228061705294735, 'lng': -44.97201083049632, 'height': 56.0, 'power': 42.0, 'of': 22.63999999999993},
#     {'lat': -21.228061705294735, 'lng': -44.97201083049632, 'height': 64.4, 'power': 42.0, 'of': 50.08000000000004},
#     {'lat': -21.228061705294735, 'lng': -44.97201083049632, 'height': 64.4, 'power': 69.0, 'of': 700.0},
#     {'lat': -21.228061705294735, 'lng': -44.97201083049632, 'height': 64.4, 'power': 78.0, 'of': 700.0},
#     {'lat': -21.228061705294735, 'lng': -44.97201083049632, 'height': 72.8, 'power': 42.0, 'of': 75.92399999999998},
#     {'lat': -21.228422316065295, 'lng': -44.974668055204695, 'height': 39.2, 'power': 42.0, 'of': -92.56400000000002},
#     {'lat': -21.228422316065295, 'lng': -44.974668055204695, 'height': 56.0, 'power': 42.0, 'of': -33.488},
#     {'lat': -21.228422316065295, 'lng': -44.974668055204695, 'height': 64.4, 'power': 42.0, 'of': -4.704000000000008},
#     {'lat': -21.228422316065295, 'lng': -44.974668055204695, 'height': 72.8, 'power': 42.0, 'of': 22.811999999999955},
#     {'lat': -21.229361867556527, 'lng': -44.97852487925566, 'height': 39.2, 'power': 42.0, 'of': -166.97199999999998},
#     {'lat': -21.229361867556527, 'lng': -44.97852487925566, 'height': 47.6, 'power': 42.0, 'of': -151.04399999999998},
#     {'lat': -21.229361867556527, 'lng': -44.97852487925566, 'height': 56.0, 'power': 42.0, 'of': -130.808},
#     {'lat': -21.229361867556527, 'lng': -44.97852487925566, 'height': 64.4, 'power': 42.0, 'of': -104.708},
#     {'lat': -21.229336522040555, 'lng': -44.97540113053806, 'height': 39.2, 'power': 42.0, 'of': -136.036},
#     {'lat': -21.229336522040555, 'lng': -44.97540113053806, 'height': 47.6, 'power': 42.0, 'of': -109.54000000000002},
#     {'lat': -21.229336522040555, 'lng': -44.97540113053806, 'height': 56.0, 'power': 42.0, 'of': -77.01600000000002},
#     {'lat': -21.229336522040555, 'lng': -44.97540113053806, 'height': 64.4, 'power': 42.0, 'of': -47.38399999999996},
#     {'lat': -21.229336522040555, 'lng': -44.97540113053806, 'height': 72.8, 'power': 42.0, 'of': -17.22800000000001},
#     {'lat': -21.229693874720486, 'lng': -44.974708741536894, 'height': 39.2, 'power': 42.0, 'of': -117.71600000000001},
#     {'lat': -21.229693874720486, 'lng': -44.974708741536894, 'height': 47.6, 'power': 42.0, 'of': -84.86000000000004},
#     {'lat': -21.229693874720486, 'lng': -44.974708741536894, 'height': 56.0, 'power': 42.0, 'of': -54.744},
#     {'lat': -21.229693874720486, 'lng': -44.974708741536894, 'height': 72.8, 'power': 42.0, 'of': 2.4280000000000257},
#     {'lat': -21.233177388771296, 'lng': -44.97434874274786, 'height': 39.2, 'power': 42.0, 'of': -184.52799999999996},
#     {'lat': -21.233177388771296, 'lng': -44.97434874274786, 'height': 47.6, 'power': 51.0, 'of': 196.33200000000005},
#     {'lat': -21.233177388771296, 'lng': -44.97434874274786, 'height': 56.0, 'power': 42.0, 'of': -145.56799999999998},
#     {'lat': -21.233177388771296, 'lng': -44.97434874274786, 'height': 64.4, 'power': 42.0, 'of': -123.39599999999996},
#     {'lat': -21.233052303859694, 'lng': -44.97240281517299, 'height': 39.2, 'power': 42.0, 'of': -184.59199999999998},
#     {'lat': -21.233052303859694, 'lng': -44.97240281517299, 'height': 39.2, 'power': 51.0, 'of': 147.86399999999998},
#     {'lat': -21.233052303859694, 'lng': -44.97240281517299, 'height': 47.6, 'power': 42.0, 'of': -166.90800000000002},
#     {'lat': -21.233052303859694, 'lng': -44.97240281517299, 'height': 47.6, 'power': 51.0, 'of': 194.84799999999998},
#     {'lat': -21.233052303859694, 'lng': -44.97240281517299, 'height': 56.0, 'power': 42.0, 'of': -144.876},
#     {'lat': -21.233052303859694, 'lng': -44.97240281517299, 'height': 64.4, 'power': 42.0, 'of': -122.988},
#     {'lat': -21.233052303859694, 'lng': -44.97240281517299, 'height': 72.8, 'power': 42.0, 'of': -98.94000000000003},
#     {'lat': -21.23602217789686, 'lng': -44.97010713879386, 'height': 39.2, 'power': 42.0, 'of': -138.484},
#     {'lat': -21.23602217789686, 'lng': -44.97010713879386, 'height': 47.6, 'power': 42.0, 'of': -120.09999999999997},
#     {'lat': -21.23602217789686, 'lng': -44.97010713879386, 'height': 56.0, 'power': 42.0, 'of': -98.27200000000002},
#     {'lat': -21.23602217789686, 'lng': -44.97010713879386, 'height': 64.4, 'power': 42.0, 'of': -71.29599999999999},
#     {'lat': -21.23602217789686, 'lng': -44.97010713879386, 'height': 72.8, 'power': 42.0, 'of': -41.99600000000001},
#     {'lat': -21.23741387135359, 'lng': -44.96991310438055, 'height': 39.2, 'power': 42.0, 'of': -123.656},
#     {'lat': -21.23741387135359, 'lng': -44.96991310438055, 'height': 47.6, 'power': 42.0, 'of': -100.412},
#     {'lat': -21.23741387135359, 'lng': -44.96991310438055, 'height': 56.0, 'power': 42.0, 'of': -74.804},
#     {'lat': -21.23741387135359, 'lng': -44.96991310438055, 'height': 72.8, 'power': 42.0, 'of': -15.044000000000011},
#     {'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 64.4, 'power': 69.0, 'of': 700.0}]

# 'lat': -21.226285918395124, 'lng': -44.97348526383644, 'height': 64.4, 'power': 69.0, 'of': 700
mp = 'COST231-Hata'  # 'HATA Path Loss'
success_i = 56  # 35

plot_height = [item['height'] for item in FOs]
plot_power = [item['power'] for item in FOs]

fig, (axs_height, axs_power) = plt.subplots(2, figsize=(10, 6))

fig.suptitle('Altura e potência por solução candidata (' + mp + ')')

axs_height.plot(plot_height, 'tab:blue')
axs_height.plot([39.2] * len(FOs), 'tab:blue', linestyle='dashed')
axs_height.plot([47.6] * len(FOs), 'tab:blue', linestyle='dashed')
axs_height.plot([56] * len(FOs), 'tab:blue', linestyle='dashed')
axs_height.plot([64.4] * len(FOs), 'tab:blue', linestyle='dashed')
axs_height.plot([72.8] * len(FOs), 'tab:blue', linestyle='dashed')

if success_i is not None:
    axs_height.axvline(x=success_i, c='r')

axs_height.text(len(plot_height) - 0.5, 39.2, '39.2')
axs_height.text(len(plot_height) - 0.5, 47.6, '47.6')
axs_height.text(len(plot_height) - 0.5, 56, '56')
axs_height.text(len(plot_height) - 0.5, 64.4, '64.4')
axs_height.text(len(plot_height) - 0.5, 72.8, '72.8')

axs_height.set(ylabel='Altura')

axs_power.plot(plot_power, 'tab:green')
axs_power.plot([42] * len(FOs), 'tab:green', linestyle='dashed')
axs_power.plot([51] * len(FOs), 'tab:green', linestyle='dashed')
axs_power.plot([60] * len(FOs), 'tab:green', linestyle='dashed')
axs_power.plot([69] * len(FOs), 'tab:green', linestyle='dashed')
axs_power.plot([78] * len(FOs), 'tab:green', linestyle='dashed')
axs_power.text(len(plot_power) - 0.5, 42, '42')
axs_power.text(len(plot_power) - 0.5, 51, '51')
axs_power.text(len(plot_power) - 0.5, 60, '60')
axs_power.text(len(plot_power) - 0.5, 69, '69')
axs_power.text(len(plot_power) - 0.5, 78, '78')
if success_i is not None:
    axs_power.axvline(x=success_i, c='r')
axs_power.set(ylabel='Potência')

plt.yscale('linear')

plt.xlabel('Solução candidata')
plt.gca().yaxis.set_minor_formatter(NullFormatter())
plt.show()
