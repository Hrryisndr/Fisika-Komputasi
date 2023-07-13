import matplotlib.pyplot as plt

#variabel yang diketahui
k = 0.9 #N/m
m = 1.0 # kg
c = 0.2  # kg/s
y = -2.0e-2 # meter
v = 0
h = 0.1
t = 0
tmax = 50

# Indentasi numerik
vFN = v
yFN = y

# List data output untuk melakukan plot
tp = []
vFNp = []
yFNp = []

# Print header
print ('t(s)', 'a(m/s^2)', 'v(m/s)', 'y(m)')

#Looping
while t < tmax:
    t+=h
    tp.append(t)

    #metode FN
    aFN = -(k*yFN + c*vFN)/m
    vhalf = vFN + aFN*h/2
    yhalf = yFN + vFN*h/2
    ahalf = -(k*yhalf + c*vhalf)/m
    vFN += ahalf*h
    yFN += vhalf*h
    yFNp.append(yFN)
    vFNp.append(vFN)

    print ("{:2f}".format(t),"{:.6f}".format(aFN),"{:.6f}".format(vFN),"{:.6f}".format(yFN))
print('\n----------SELESAI----------\n')

plt.subplot(2,2,1)
plt.plot(tp, vFNp, '')
plt.xlabel('Waktu(s)')
plt.ylabel('Kecepatan(m/s)')
plt.grid(True)
plt.subplot(2,2,2)
plt.plot(tp, yFNp, '')
plt.xlabel('Waktu(s)')
plt.ylabel('Posisi(m)')
plt.grid(True)
plt.show()