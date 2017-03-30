import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

# The data represents results of the "Software-Ergonomie Vertiefungsseminar" WS16/17, in which
# participants tested the UR Walking Application. The lists include the summed durations the
# participants took while pressing the "Erkannt"-button.
# Data for the following lists comes from the log-data.It is copied out of David Sinz' Excel
# file "ExcelDatenSoftwareErgo.xlsx" which is an ordered# version of the original
# log-data ("Logdaten aufsummiert WS1617.csv").
# See also .csv files in this project.


daten_m_karte = [213608, 263783, 187220, 336006, 140293, 155008, 351851, 246175, 352878, 418766, 264735,
                 277633, 122899, 227301, 607710, 103366, 338283, 813619, 284833, 435818, 58746, 224106,
                 190896, 120479, 121992, 62477, 851367, 188802, 286778, 207450, 163010]
daten_w_karte = [265439, 133959, 178182, 188284, 82364, 137957, 425347, 529344, 91525, 89626, 268989, 201326,
                 181335, 620709, 80469, 171428, 156562, 446669, 461113, 73525, 171033, 39377, 182595, 430826,
                 190066, 1057525, 108228, 305509, 108779, 373706]

daten_m_ohne = [93005, 293227, 66559, 325332, 154230, 104191, 276238, 108237, 859379, 146555, 205246, 222652, 89887,
                340494, 144779, 172487, 445102, 111875, 285103, 202620, 57565, 114240, 113312, 179771, 960466,
                212714, 471799, 110371, 105389, 66728, 149213]
daten_w_ohne = [229789, 241253, 151511, 176934, 80292, 351351, 94276, 226438, 281496, 161666, 444670, 88980, 240183,
                86949, 172679, 216532, 187514, 705171, 466370, 75442, 119466, 261893, 118660, 281618, 148705, 671131,
                135799, 146779, 91946, 315432]


def show_histogram_plots(show_histograms=False):
    """
    Show histograms of the data. Function starts when show_histograms is set true.
    """
    if show_histograms:
        print
        print "Histogramme oeffnen sich in neuen Fenstern."
        print "***********************************************************************"

        plt.hist([daten_m_karte, daten_w_karte], label=("Maennlich", "Weiblich"))
        plt.legend()
        plt.title("Verteilung - Probanden mit Karte")
        plt.xlabel("Duration")
        plt.ylabel("Frequency")
        plt.show()

        plt.hist([daten_m_ohne, daten_w_ohne], label=("Maennlich", "Weiblich"))
        plt.legend()
        plt.title("Verteilung - Probanden ohne Karte")
        plt.xlabel("Duration")
        plt.ylabel("Frequency")
        plt.show()


if __name__ == "__main__":
    print
    print "***********************************************************************"
    print "Auswertung der Daten"
    print "***********************************************************************"

    show_histogram_plots()

    # Shapiro-Wilk
    # Perform the Shapiro-Wilk test for normality.
    # The Shapiro-Wilk test tests the null hypothesis that the data was drawn from a normal distribution.
    # -> Has to be done with both groups.

    # Mann-Whitney
    # Computes the Mann-Whitney rank test on samples x and y.

    # For further explanation see documentation and:
    # http://www.methodenberatung.uzh.ch/de/datenanalyse.html

    print "Normalverteilungstests von Maennern und Frauen mit Karte:"
    print
    print "Shapiro-Ergebnisse (W - Die Test-Statistik, p-Wert des Hypothesentests):"
    print "Shapiro Maennlich m. Karte: ", scipy.stats.shapiro(daten_m_karte)
    print "Shapiro Weiblich  m. Karte: ", scipy.stats.shapiro(daten_w_karte)
    print
    print "Ergebnis Mann-Whitney-U-Test:"
    print
    print scipy.stats.mannwhitneyu(daten_m_karte, daten_w_karte)

    print
    print "***********************************************************************"
    print

    print "Normalverteilungstests von Maennern und Frauen ohne Karte:"
    print
    print "Shapiro-Ergebnisse (W - Die Test-Statistik, p-Wert des Hypothesentests):"
    print "Shapiro Maennlich o. Karte: ", scipy.stats.shapiro(daten_m_ohne)
    print "Shapiro Weiblich  o. Karte: ", scipy.stats.shapiro(daten_w_ohne)
    print
    print "Ergebnis Mann-Whitney-U-Test:"
    print
    print scipy.stats.mannwhitneyu(daten_m_ohne, daten_w_ohne)

    print
    print "***********************************************************************"
