#!/usr/bin/env python

import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

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
    fig = plt.figure()
    ax = fig.gca()
    ax.scatter(track_data['LONG'], track_data['LAT'], marker='.')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    plt.show()


def add_axis_labels_2D():
    pass


def plot_track_data_3D():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(track_data['LONG'], track_data['LAT'], track_data['ALT'], marker='.')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Altitude')
    plt.show()



if __name__ == '__main__':
    track_data = load_data(track_filename)
    add_runway_plot()
    plot_track_data_2D(track_data)
    plot_track_data_3D()
