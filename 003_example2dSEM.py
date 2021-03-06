# This script performs 2D Seismic Wave and Shot Simulation using Spectral Element Method
# Tested under Ubuntu 18.04.5 LTS
# Developed by GAIA (Center for Geosciences Artifical Intelligence and Advanced Computing)
# Agus Abdullah, Ph.D. Waskito Pranowo, M.T. Dicky Ahmad Zaky, M.T.
# Universitas Pertamina - Indonesia  2021
# HOW TO RUN
# Step1: Define parameterization in  seismic2dsem.par   (Parameters are from  row 21 to 38 !)
# Step2: Run this Python script via Python IDE or Ubuntu Terminal:  python  001_example2dSEM.py
# Input:  seismic2dsem.par  and velocityoneshot2d.npy (size: nx,nz  numpy format)

import subprocess
import numpy as np
import matplotlib.pyplot as plt
subprocess.run(["./seismic2dsem"])

filein = np.genfromtxt('seismic2dsem.par', dtype=str, skip_header=20)
xmax= float(filein[0])
zmax= float(filein[1])
dx= float(filein[2])
dz= float(filein[3])
model= filein[10]
path= filein[11]
shotfile= filein[17]

model = np.load(model)
nx = int(xmax / dx)  # number of grid points in x-direction
nz = (int)(zmax / dz)
v = 0.0000005
shot = np.load('%s/%s.npy' % (path,shotfile))
plt.imshow(shot, aspect='auto', interpolation='bilinear', cmap='bwr', vmin=-v,vmax=v)
plt.suptitle('2D SHOT RECORD SPECTRAL ELEMENT METHOD')
plt.ylim(300, 25)
plt.show()

fig = plt.figure(figsize=(7, 7))
plt.tight_layout()

extent = [0.0, xmax, zmax, 0.0]
plt.imshow(model.T, cmap='jet', interpolation='bilinear', extent=extent, alpha=1)
p = np.zeros((nx, nz))
image = plt.imshow(p.T, animated=True, cmap="Greys", extent=extent, interpolation='bilinear', vmin=-v, vmax=v,alpha=0.5)
plt.title('2D Wavefield')
plt.xlabel('x [m]')
plt.ylabel('z [m]')
plt.ion()
plt.show(block=False)

for i in range(300):
    p = np.load('%s/wavefieldSEM_%s.npy' % (path, int(i+1)))
    image.set_data(p.T)
    fig.canvas.draw()
