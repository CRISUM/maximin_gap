import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon


def draw_result(interval_list, result, file_name):
    # Combine intervals, results, and indices into a single list of tuples
    combined_data = list(zip(interval_list, result))

    # Sort the combined data based on the result (scatter_x) values
    sorted_data = sorted(combined_data, key=lambda x: x[1])

    # Create empty lists for polygons, scatter x and y values
    polygons = []
    scatter_x = []
    scatter_y = []

    # Iterate over sorted data to create polygons and scatter points
    for idx, (interval, x_i) in enumerate(sorted_data):
        print('result=', idx, interval, x_i)
        scatter_x.append(x_i)
        scatter_y.append(idx)

        lb_x = interval[0]
        ub_x = interval[1]
        lb_y = idx - 0.3
        ub_y = idx + 0.3
        polygon = [[lb_x, lb_y], [lb_x, ub_y], [ub_x, ub_y], [ub_x, lb_y], [lb_x, lb_y]]
        polygons.append(polygon)

    fig, ax = plt.subplots()
    patches = [Polygon(polygon) for polygon in polygons]
    p = PatchCollection(patches,
                        facecolors='gray',
                        edgecolors='gray',
                        alpha=0.3)
    plt.scatter(scatter_x, scatter_y, s=2, c='red')
    ax.add_collection(p)

    plt.savefig('{}.jpg'.format(file_name), bbox_inches='tight', pad_inches=0)
    plt.savefig('{}.pdf'.format(file_name), bbox_inches='tight', pad_inches=0)
    return
