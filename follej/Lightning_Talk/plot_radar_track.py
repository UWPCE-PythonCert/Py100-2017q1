#!/usr/bin/env python

import pandas as pd
# import plotly.graph_objs as go
# import plotly.plotly as py
import matplotlib.pyplot as plt
import matplotlib.lines as lines

runway_lat_long = [37.628739, -122.393392]  # 10L
runway_lat_long = [37.613534, -122.357141]  # 28R

track_filename = 'track.csv'


def load_data(filename):
    track_data = pd.read_csv(track_filename)
    track_data.head()
    # print(track_data['LAT'])
    # print(track_data['LONG'])
    # print(track_data['AIRSPEED'])
    # print(track_data['ALT'])
    return track_data


def add_runway_plot():
    print(runway_lat_long)


def plot_track_data_2D(track_data):
    # trace1 = go.Scatter(
    #     x=track_data['LONG'], y=track_data['LAT'],
    #     mode='lines', name='Track'
    # )
    # layout = go.Layout(title='2D Plot from csv track data',
    #                    plot_bgcolor='rgb(230, 230,230)')
    # fig = go.Figure(data=[trace1], layout=layout)
    # py.iplot(fig, filename='simple-plot-from-csv')
    fig = plt.figure()

    l1 = lines.Line2D(track_data['LONG'], track_data['LAT'], transform=fig.transFigure, figure=fig)

    fig.lines.append(l1)
    plt.interactive(False)
    plt.pyplot.show()


def add_axis_labels_2D():
    pass


def plot_track_data_3D():
    pass


def add_axis_labels_3D():
    pass


if __name__ == '__main__':
    track_data = load_data(track_filename)
    add_runway_plot()
    plot_track_data_2D(track_data)
    add_axis_labels_2D()
    plot_track_data_3D()
    add_axis_labels_3D()
