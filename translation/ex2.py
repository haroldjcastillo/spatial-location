import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    T = np.array([[1, 0, 0, 6],
                  [0, 1, 0, -3],
                  [0, 0, 1, 8],
                  [0, 0, 0, 1]])
    r_uvw = np.array([[4], [4], [11], [1]])
    print("Translation matrix")
    print(T)
    print("Vector r")
    print(r_uvw)
    r_xyz = np.matmul(T, r_uvw).T
    print("Result")
    print(r_xyz)

    p = T[:3, 3]
    r = r_uvw[:3, 0].T
    f = r_xyz[0, :3]
    zeros = np.zeros(3)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.text2D(0.05, 0.95, "Translation  ex. 2", transform=ax.transAxes)

    x, y, z = zip(zeros, r)
    rr, = plt.plot(x, y, z, '-k', label="r", linewidth=2)
    label = '(%d, %d, %d)' % (x[0], y[0], z[0])
    ax.text(x[0], y[0], z[0], label)
    plt.legend(handles=[rr], loc=2)

    x, y, z = zip(zeros, f)
    rr_prime, = plt.plot(x, y, z, '-b', label="r'", linewidth=2)
    label = '(%d, %d, %d)' % (x[1], y[1], z[1])
    ax.text(x[1], y[1], z[1], label)
    plt.legend(handles=[rr_prime], loc=3)

    x, y, z = zip(r, f)
    pp, = plt.plot(x, y, z, '-g', label="p", linewidth=2)
    label = '(%d, %d, %d)' % (x[0], y[0], z[0])
    ax.text(x[0], y[0], z[0], label)
    plt.legend(handles=[pp], loc=4)

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 4])
    ax.set_zlim([0, 19])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


if __name__ == "__main__":
    main()
