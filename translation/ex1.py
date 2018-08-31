import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
    T = np.array([[1, 0, 0, 6],
                 [0, 1, 0, -3],
                 [0, 0, 1, 8],
                 [0, 0, 0, 1]])
    r_uvw = np.array([[-2], [7], [3], [1]])
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
    ax.text2D(0.05, 0.95, "Translation  ex. 1", transform=ax.transAxes)

    x, y, z = zip(zeros, p)
    plt.plot(x, y, z, '-k', linewidth=2)
    label = '(%d, %d, %d)' % (x[0], y[0], z[0])
    ax.text(x[0], y[0], z[0], label)

    x, y, z = zip(p, r)
    plt.plot(x, y, z, '-b', linewidth=2)
    label = '(%d, %d, %d)' % (x[0], y[0], z[0])
    ax.text(x[0], y[0], z[0], label)

    x, y, z = zip(r, f)
    plt.plot(x, y, z, '-g', linewidth=2)
    label = '(%d, %d, %d)' % (x[0], y[0], z[0])
    ax.text(x[0], y[0], z[0], label)

    x, y, z = zip(zeros, f)
    plt.plot(x, y, z, '-r', linewidth=1)
    label = '(%d, %d, %d)' % (x[1], y[1], z[1])
    ax.text(x[1], y[1], z[1], label)

    ax.set_xlim([-3, 8])
    ax.set_ylim([-4, 4])
    ax.set_zlim([0, 12])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()


if __name__ == "__main__":
    main()