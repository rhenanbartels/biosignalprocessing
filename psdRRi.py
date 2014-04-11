#-------------------------------
# Name:        psdRRi
# Purpose:     Estimates the  PSD of given RRi serie and its AUC.
# Author:      Rhenan Bartels Ferreira
# Created:     06/03/2014
# Copyright:   (c) Rhenan 2013
# Licence:     <your licence>
#-------------------------------

import matplotlib.pyplot as plt

from numpy import arange, cumsum, logical_and
from scipy.signal import welch
from scipy.interpolate import splrep, splev


#Open RRi file

rri = [int(rri.strip()) for rri in open('filename') if rri.strip()]


#Create time array
t = cumsum(rri) / 1000.0
t -= t[0]

#Evenly spaced time array (4Hz)
tx = arange(t[0], t[-1], 1.0 / 4.0)

#Interpolate RRi serie
tck = splrep(t, rri, s=0)
rrix = splev(tx, tck, der=0)

#Number os estimations
P = int((len(tx) - 256 / 128)) + 1

#PSD with Welch's Method
Fxx, Pxx = welch(rrix, fs=4.0, window="hanning", nperseg=256, noverlap=128,
                 detrend="linear")

#Plot the PSD
plt.plot(Fxx, Pxx)
plt.xlabel("Frequency (Hz)")
plt.ylabel(r"PSD $(ms^ 2$/Hz)")
plt.title("PSD")

#Calculates the Confidence interval

from scipy.stats import chi2

#95% probability
probability = 0.95

alfa = 1 - probability
v = 2 * P
c = chi2.ppf([1 - alfa / 2, alfa / 2], v)
c = v / c

Pxx_lower = Pxx * c[0]
Pxx_upper = Pxx * c[1]

plt.plot(Fxx, Pxx_lower, 'k--')
plt.plot(Fxx, Pxx_upper, 'k--')


#Calculates the AUC of the PSD
def psdauc(Fxx, Pxx, vlf=0.04, lf=0.15, hf=0.4):
    df = Fxx[1] - Fxx[0]
    vlf = sum(Pxx(Fxx <= vlf)) * df
    lf = sum(Pxx[logical_and(Fxx >= vlf, Fxx < lf)]) * df
    hf = sum(Pxx[logical_and(Fxx >= lf, Fxx < hf)]) * df
    return vlf, lf, hf
