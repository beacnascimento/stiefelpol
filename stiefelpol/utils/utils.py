import numpy as np
import matplotlib.pyplot as plt


def to_complex(tuples_list):
    return [complex(x, y) for x, y in tuples_list]

def viewPolygon(vertices):
    for i in range(len(vertices)):
        x,y = vertices[i].real, vertices[i].imag
        plt.scatter(x,y)
        x_next, y_next = vertices[(i + 1) % len(vertices)].real, vertices[(i + 1) % len(vertices)].imag
        plt.plot([x, x_next], [y, y_next], color='black')
    plt.show()

def vector_angle(v1, v2):

    #Calcula o ângulo entre dois vetores.
    cos_theta = np.dot(v1, v2) / ((np.linalg.norm(v1) * np.linalg.norm(v2)))
    angle = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # Calcular o ângulo

    # Verifica se o ângulo é negativo, ajustando para o intervalo [0, 2pi]
    if np.cross(v1, v2) < 0:  # Se o vetor v1 está abaixo de v2 em relação ao eixo X
        angle =   2*np.pi - angle

    return angle

def vector_angle2(v1, v2):
    #Calcula o ângulo entre dois vetores.
    cos_theta = np.dot(v1, v2) / ((np.linalg.norm(v1) * np.linalg.norm(v2)))
    angle = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # Calcular o ângulo
    
    return(angle)