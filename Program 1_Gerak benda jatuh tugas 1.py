import math
import matplotlib.pyplot as plt
import numpy as np

# Variabel Input
y = 2000 #m
v = 0.0 #m/s
g = 9.8 #m/s2
cd = 0.46
m = 3.9e-3 #kg
r = 7.5e-3
rho = 1.2
h = 0.1
t = 0
tmax= 25

# Rumus konstanta fenomena gerak benda jatuh
A = math.pi*r**2 # Luas penampang bola
K = (cd*rho*A)/2 # Rumus GJB

# Inisiasi Awal Metode Numerik
# Metode Euler
ve = v
ye = y
# Metode Feyman Newton
vFN = v # Kecepatan mula-mula
yFN = y # Jarak mula-mula

# List data output untuk melakukan plot
tp = []
yep = []
vep = []
aep = []
aFNp = []
vFNp = []
yFNp = []
vap = []
yap = []
ervnaep = []
erynaep = []
ervnaeFN = []
erynaeFN = []

# Print Untuk Header Data
print('t','Error VE(%)','Error VFN (%)','Eror YE(%)','Eror YFN(%)')

# Looping
while t<tmax:
    t += h
    tp.append(t)

    # Metode Analitik
    va = -np.sqrt(g*m/K)*np.tanh(t*np.sqrt(g*K/m))
    ya = y-(m/K)*np.log(np.cosh(t*np.sqrt(g*K/m)))
    vap.append(va)
    yap.append(ya)

    # Metode Numerik
    # Metode Euler
    ae = (K*ve**2)/m - g
    ve += ae*h
    ye += ve*h
    aep.append(ae)
    yep.append(ye)
    vep.append(ve)

    # Metode Feyman Newton
    aFN = (K*vFN**2)/m - g
    vhalf = vFN + aFN*h/2
    yhalf = yFN + vFN*h/2
    ahalf = (K*vhalf**2)/m - g
    vFN += h*ahalf
    yFN += h*vhalf
    aFNp.append(aFN)
    yFNp.append(yFN)
    vFNp.append(vFN)

    # Error Numerik vs Analitik
    # Metode Euler
    ervnae = np.abs((ve-va)/va)*100
    erynae = np.abs((ye-ya)/ya)*100
    ervnaep.append(ervnae)
    erynaep.append(erynae)
    # Metode Feyman Newton
    ervnaFN = np.abs((vFN-va)/va)*100
    erynaFN = np.abs((yFN-ya)/ya)*100
    ervnaeFN.append(ervnaFN)
    erynaeFN.append(erynaFN)

    # Print Output dari semua proses
    print("{:2f}".format(t),"{:.6f}".format(ervnae),"{:.6f}".format(ervnaFN),"{:.6f}".format(erynae),"{:.6f}".format(erynaFN))

print('\n----------SELESAI----------\n')

plt.subplot(2,2,1)
plt.plot(tp, ervnaep, '')
plt.plot(tp, ervnaeFN,'')
plt.xlabel('Waktu(s)')
plt.ylabel('Error Kecepatan(%)')
plt.grid(True)
plt.subplot(2,2,2)
plt.plot(tp, erynaep, '')
plt.plot(tp, erynaeFN, '')
plt.xlabel('Waktu(s)')
plt.ylabel('Error Posisi(%)')
plt.grid(True)
plt.show()