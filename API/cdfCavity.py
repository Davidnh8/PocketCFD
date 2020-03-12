import numpy as np


def update_pressure(p, u, v, dx, dy, dt, rho):
    pNew = p.copy()

    term1 = ((p[2:,1:-1] - p[:-2,1:-1])*dy**2 + (p[1:-1,2:] + p[1:-1,:-2])*dx**2 ) / (2*(dx**2 + dy**2))
    term2 = -(rho * dx**2 * dy**2)/(2*(dx**2 + dy**2))
    term3 = (rho * (1 / dt *
                    ((u[1:-1, 2:] - u[1:-1, 0:-2]) /
                     (2 * dx) + (v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy)) -
                    ((u[1:-1, 2:] - u[1:-1, 0:-2]) / (2 * dx))**2 -
                      2 * ((u[2:, 1:-1] - u[0:-2, 1:-1]) / (2 * dy) *
                           (v[1:-1, 2:] - v[1:-1, 0:-2]) / (2 * dx))-
                          ((v[2:, 1:-1] - v[0:-2, 1:-1]) / (2 * dy))**2))

    pNew[1:-1, 1:-1] = term1 + term2 * term3

    pNew[:, -1] = pNew[:, -2]
    pNew[0, :] = pNew[1, :]
    pNew[:, 0] = pNew[:, 1]
    pNew[-1:] = 0

    return pNew


def update_u(p, u, v, dx, dy, dt, rho, nu):
    uNew = u.copy()

    uNew[1:-1,1:-1] = (u[1:-1, 1:-1]-
                         u[1:-1, 1:-1] * dt / dx *
                        (u[1:-1, 1:-1] - u[1:-1, 0:-2]) -
                         v[1:-1, 1:-1] * dt / dy *
                        (u[1:-1, 1:-1] - u[0:-2, 1:-1]) -
                         dt / (2 * rho * dx) * (p[1:-1, 2:] - p[1:-1, 0:-2]) +
                         nu * (dt / dx**2 *
                        (u[1:-1, 2:] - 2 * u[1:-1, 1:-1] + u[1:-1, 0:-2]) +
                         dt / dy**2 *
                        (u[2:, 1:-1] - 2 * u[1:-1, 1:-1] + u[0:-2, 1:-1])))
    uNew[0, :] = 0
    uNew[:, 0] = 0
    uNew[:, -1] = 0
    uNew[-1, :] = 1

    return uNew


def update_v(p, u, v, dx, dy, dt, rho, nu):
    vNew = v.copy()

    vNew[1:-1,1:-1] = (v[1:-1, 1:-1] -
                        u[1:-1, 1:-1] * dt / dx *
                       (v[1:-1, 1:-1] - v[1:-1, 0:-2]) -
                        v[1:-1, 1:-1] * dt / dy *
                       (v[1:-1, 1:-1] - v[0:-2, 1:-1]) -
                        dt / (2 * rho * dy) * (p[2:, 1:-1] - p[0:-2, 1:-1]) +
                        nu * (dt / dx**2 *
                       (v[1:-1, 2:] - 2 * v[1:-1, 1:-1] + v[1:-1, 0:-2]) +
                        dt / dy**2 *
                       (v[2:, 1:-1] - 2 * v[1:-1, 1:-1] + v[0:-2, 1:-1])))
    vNew[0, :] = 0
    vNew[-1, :] = 0
    vNew[:, 0] = 0
    vNew[:, -1] = 0

    return vNew


def Iterate(count, p, u, v, dx, dy, dt, rho, nu):

    for i in range(count):
        uOld = u.copy()
        vOld = v.copy()

        p = update_pressure(p, u, v, dx, dy, dt, rho)
        u = update_u(p, uOld, vOld, dx, dy, dt, rho, nu)
        v = update_v(p, uOld, vOld, dx, dy, dt, rho, nu)
    return p, u, v

