import fnmatch
import numpy as np
import os
import mesa

profs=len(fnmatch.filter(os.listdir('./LOGS/'), 'profile*.data'))
X_c=np.zeros(profs)

for i in range(profs):
    prof=mesa.profile('./LOGS/profile'+str(i+1)+'.data')
    X=prof.x_mass_fraction_H
    os.rename('./LOGS/profile'+str(i+1)+'.data','./LOGS/X_'+str(X[-1])+'.data')
    X_c[i]=X[-1]


X_c=np.array(X_c)

steps=[1,0.95,0.9,0.85,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.45,0.4,0.35,0.3,0.25,0.2,0.15,0.1,0.05,0.0]
Xmin=np.zeros(len(steps))
Xdiff=np.zeros(len(steps))
for j in range(len(steps)):
    Xdiff[j]=np.min(np.absolute(X_c-steps[j]))
    if 0.001>=Xdiff[j]:
        Xmin[j]=X_c[np.argmin(np.absolute(X_c-steps[j]))]
    


for i in range(profs):
    if not(X_c[i] in Xmin):
        os.remove('./LOGS/X_'+str(X_c[i])+'.data') 

os.system('rm ./LOGS/profile* ./LOGS/history.data')

for i in range(len(steps)):
    if Xmin[i]!=0:
        os.rename('./LOGS/X_'+str(Xmin[i])+'.data','./LOGS/X_'+str(round(Xmin[i],2)).replace('.','_')+'.data')