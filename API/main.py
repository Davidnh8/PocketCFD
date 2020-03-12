import flask
from flask import send_file, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api

import numpy as np
import matplotlib.pyplot as plt
import cdfCavity as cf
import datetime

app = flask.Flask(__name__)
app.config["DEBUG"] = True
api = Api(app)
CORS(app)

class NavierStokes(Resource):
    def get(self):
        # dimensions
        ny = 41
        nx = 41
        dx = 2 / (nx - 1)
        dy = 2 / (ny - 1)
        x = np.linspace(0, 2, nx)
        y = np.linspace(0, 1, ny)
        X, Y = np.meshgrid(x, y)

        nu = 0.1
        rho = 1
        dt = 0.001

        u = np.zeros((ny, nx))
        v = np.zeros((ny, nx))
        p = np.zeros((ny, nx))

        p, u, v = cf.Iterate(500, p, u, v, dx, dy, dt, rho, nu)

        fig, ax = plt.subplots(figsize=(7, 3.5))
        ax.contourf(X, Y, p)
        ax.quiver(X[::2, ::2], Y[::2, ::2], u[::2, ::2], v[::2, ::2])
        filename = "Generated_%s" % datetime.datetime.utcnow().strftime('%Y-%m-%d-%H%M%S' + ".png")
        fig.savefig(filename)

        #return jsonify({"ab": "cd"})
        return send_file(filename, mimetype='image/png')

        #return jsonify({"x": X.tolist(), "y": Y.tolist(), "u": u.tolist(), "v": v.tolist()})


api.add_resource(NavierStokes, '/navierstokes')

if __name__ == '__main__':
    app.run(port=5002)

'''
# dimensions
ny = 41
nx = 41
dx = 2 / (nx-1)
dy = 2 / (ny-1)
x = np.linspace(0, 2, nx)
y = np.linspace(0, 1, ny)
X, Y = np.meshgrid(x, y)

nu = 0.1
rho = 1
dt = 0.001

u = np.zeros((ny, nx))
v = np.zeros((ny, nx))
p = np.zeros((ny, nx))


p, u, v = cf.Iterate(1000, p, u, v, dx, dy, dt, rho, nu)

fig ,ax = plt.subplots(figsize=(7, 3.5))
ax.contourf(X, Y, p)
ax.quiver(X[::2, ::2], Y[::2, ::2], u[::2, ::2], v[::2, ::2])

plt.show()
'''