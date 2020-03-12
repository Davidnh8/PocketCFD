import flask
from flask import send_file, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse

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

        parser = reqparse.RequestParser()
        parser.add_argument('xlength')
        parser.add_argument('ylength')
        parser.add_argument('nx')
        parser.add_argument('nu')
        parser.add_argument('rho')
        parser.add_argument('dt')
        parser.add_argument('iteration')

        args = parser.parse_args()

        Pxlength = args.get('xlength')
        Pylength = args.get('ylength')
        Pnx = args.get('nx')
        Pnu = args.get('nu')
        Prho = args.get('rho')
        Pdt = args.get('dt')
        Piteration = args.get('iteration')


        # Default Parameters

        nx = 41
        ny = 41
        if Pnx !='':
            nx = int(Pnx)
            ny = int(Pnx)

        xlength = 2
        ylength = 2
        if Pxlength != '':
            xlength = float(Pxlength)
        if Pylength != '':
            ylength = float(Pylength)

        dx = xlength / (nx - 1)
        dy = ylength / (ny - 1)

        nu = 0.1
        if Pnu != '':
            nu = float(Pnu)

        rho = 1
        if Prho != '':
            rho = float(Prho)

        dt = 0.001
        if Pdt != '':
            dt = float(Pdt)

        iteration= 500
        if Piteration != '':
            iteration = int(Piteration)

        x = np.linspace(0, xlength, nx)
        y = np.linspace(0, ylength, ny)
        X, Y = np.meshgrid(x, y)

        u = np.zeros((ny, nx))
        v = np.zeros((ny, nx))
        p = np.zeros((ny, nx))

        p, u, v = cf.Iterate(iteration, p, u, v, dx, dy, dt, rho, nu)

        fig, ax = plt.subplots(figsize=(5*xlength/ylength , 5))
        #ax.contourf(X, Y, p)
        ax.quiver(X[::2, ::2], Y[::2, ::2], u[::2, ::2], v[::2, ::2])
        ax.set_xlabel("x")
        ax.set_ylabel("y")
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