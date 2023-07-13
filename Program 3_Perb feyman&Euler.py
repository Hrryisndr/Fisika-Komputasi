import math
import matplotlib.pyplot as plt

# Variabel Input
d = 6e-2 # meter
m = 0.1 # kg
v0 = 25 # m/s
elv = 37 # derajat
cd = 0.0
rho = 1.2
g = 9.8
h = 0.05
t = 0.0
tmax = 2.85
xFN = 0.0
yFN = 0.0

# List data output untuk melakukan plot
tp = []
xFNp = []
yFNp = []

# Menghitung Nilai
K = (cd*rho*math.pi*d**2)/(8*m)
vFNx = v0*math.cos(math.radians(elv))
vFNy = v0*math.sin(math.radians(elv))

# Print nilai
print('xFN','yFN')

# Looping
while yFN>=0:
    v = math.sqrt(vFNx**2 + vFNy**2)
    aFNx = -K * v * vFNx
    aFNy = -g - K * v * vFNy

    # Metode FN
    xhalf = xFN + vFNx * h / 2
    yhalf = yFN + vFNy * h / 2
    vxhalf = vFNx + aFNx * h / 2
    vyhalf = vFNy + aFNy * h / 2
    vhalf = math.sqrt(vxhalf**2 + vyhalf**2)
    axhalf = -K * vhalf * vxhalf
    ayhalf = -g - K * vhalf * vyhalf
    xFN += h * vxhalf
    yFN += h * vyhalf
    vFNx += h * axhalf
    vFNy += h * ayhalf
    t += h
    xFNp.append(xFN)
    yFNp.append(yFN)

    # Print data
    print("{:.6f}".format(xFN),"{:.6f}".format(yFN))

plt.subplot(1,1,1)
plt.plot(xFNp, yFNp, '')
plt.plot(xFNp, yFNp, marker="o", markersize=5)
plt.xlabel('x(m)')
plt.ylabel('y(m)')
plt.grid(True)
plt.show()