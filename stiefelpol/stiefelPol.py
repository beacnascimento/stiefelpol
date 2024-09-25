import numpy as np
from scipy.linalg import qr
import matplotlib.pyplot as plt

class Stiefel:

    @staticmethod
    def StiefelSample(n):

        random_matrix = np.random.randn(n, 2)
        
        # Realizando a decomposição QR
        orthogonal_matrix, _ = np.linalg.qr(random_matrix)
        
        # Garantir que a entrada (1, 1) seja positiva
        if orthogonal_matrix[0, 0] < 0:
            orthogonal_matrix[:, 0] = -orthogonal_matrix[:, 0]
        
        return orthogonal_matrix

    @staticmethod
    def FrameToEdges(frame):

        edges = []

        for i in range(len(frame)):
            y = complex(frame[i][0],frame[i][1])
            edge = y*y
            edges.append(edge)

        return edges

    @staticmethod
    def EdgesToVertices(edges):

        # Calculate cumulative sum of edges
        vertices = np.cumsum(edges, axis=0)

        # Normalize vertices to start at the origin
        vertices -= vertices[0]

        return vertices

    @staticmethod
    def FrameToVertices(frame):

        vertices = np.cumsum(frame.FrameToEdges(), axis=0)
        vertices -= vertices[0]
        return vertices

    @staticmethod
    def EdgesToFrame(edges):

        # Calculate square roots and extract real and imaginary parts
        frame = np.array([np.real(np.sqrt(complex(*edge))), np.imag(np.sqrt(complex(*edge)))] for edge in edges).T

        # Orthogonalize the frame using QR decomposition
        orthogonal_frame, _ = np.linalg.qr(frame)

        return orthogonal_frame

    @staticmethod
    def VerticesToEdges(vertices):
        # Calculate differences between consecutive vertices
        edges = np.diff(vertices, axis=0)
        return edges

    @staticmethod
    def VerticesToFrame(vertices):

        edges = Stiefel.VerticesToEdges(vertices)
       
        return Stiefel.EdgesToFrame(edges)
    
    @staticmethod
    def viewPolygon(vertices):
        for i in range(len(vertices)):
            x,y = vertices[i].real, vertices[i].imag
            plt.scatter(x,y)
            x_next, y_next = vertices[(i + 1) % len(vertices)].real, vertices[(i + 1) % len(vertices)].imag
            plt.plot([x, x_next], [y, y_next], color='black')
        plt.show()

