import mesa
import numpy as np

def thermdiff(profile):
    logT=np.array(profile.logT)
    logrho=np.array(profile.logRho)
    cp=np.array(profile.cp)
    kappa=np.array(profile.opacity)
    T=10**logT
    rho=10**logrho
    thermdiff=-(4*5.6704e-5*T**3)/(3*kappa*rho**2*cp)
    return thermdiff

def force(profile):
    eps=np.array(profile.eps_nuc)
    cp=np.array(profile.cp)
    force=eps/cp
    return force

def tempgrad(profile):
    Hp=np.array(profile.pressure_scale_height)
    gradT=np.array(profile.gradT)
    logT=np.array(profile.logT)
    T=10**logT
    tempgrad=-T*(gradT*Hp)
    return tempgrad

def subad(profile):
    Hp=np.array(profile.pressure_scale_height)
    Hp_cm=Hp*mesa.rsol
    logT=np.array(profile.logT)
    T=10**logT
    grada=np.array(profile.grada)
    gradT=np.array(profile.gradT)
    graddiff=grada-gradT
    subad=(T/Hp_cm)*graddiff
    return subad

def hrho(profile):
    chirho=np.array(profile.chiRho)
    Hp=np.array(profile.pressure_scale_height)
    hrho=1/(chirho*Hp)*-1
    hrho_cm=hrho/mesa.rsol
    return hrho_cm
