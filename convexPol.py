
from stiefelpol import Stiefel
import stiefelpol.utils as ut
import numpy as np
import matplotlib.pyplot as plt


def orderAngle(edges):

    edges_plane = []
    for i in range(len(edges)):
        x = edges[i].real
        y = edges[i].imag
        edges_plane.append((x,y))

    angles = []

    for i in range(len(edges_plane)):
        angle = ut.vector_angle(edges_plane[i], (1,0))
        angles.append((angle,i))

    sorted_angles = sorted(enumerate(angles), key=lambda x: x[1][0])

    indices_originais = [x[0] for x in sorted_angles]

    edges_plane_ordenado = [edges[i] for i in indices_originais]

    return edges_plane_ordenado

