import numpy as np
import matplotlib.pyplot as plt
import scipy.stats


'''
This file is made from knowledge of the course "Analysieren und
Visualisieren mit Python" by Manuel-Tonio Mueller, WS16/17
'''


# Erstellen zweier Probandengruppen (zu Testzwecken)
probandenGruppeA = np.random.randn(80) * 10 + 50
probandenGruppeB = np.random.randn(80) * 10 + 60
plt.hist([probandenGruppeA, probandenGruppeB])
# plt.show()


# Perform the Shapiro-Wilk test for normality.
# The Shapiro-Wilk test tests the null hypothesis that the data was drawn from a normal distribution.
# -> Has to be done with both groups.
print "Shapiro-Ergebnisse: (W - Die Test-Statistik, p-Wert des Hypothesentests)"
print "Shapiro Gruppe A: ", scipy.stats.shapiro(probandenGruppeA)
print "Shapiro Gruppe B: ", scipy.stats.shapiro(probandenGruppeB)


# Perform Levene test for equal variances.
# The Levene test tests the null hypothesis that all input samples are from populations with equal variances.
# Levene's test is an alternative to Bartlett's test bartlett in the case where there are significant deviations
# from normality.
print scipy.stats.levene(probandenGruppeA, probandenGruppeB)

