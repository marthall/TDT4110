from skumleskogen import *

hukommelse = {}
nokkel = 0
n = 0

# while not er_utgang():
for i in range(80):

    forrige_n = n
    n = nummer()

    print("Node nr: \t%i" % n)
    print("Antall nøkler: \t%i" % nokkel)

    if n not in hukommelse:
        hukommelse[n] = {"venstre": False, "hoyre": False, "venstre_tom": False, "hoyre_tom": False, "siste_steg": "", "blindvei": False}

    if hukommelse[forrige_n]["blindvei"]:
        if hukommelse[n]["siste_steg"] == "hoyre":
            hukommelse[n]["hoyre_tom"] == True
        elif hukommelse[n]["siste_steg"] == "venstre":
            hukommelse[n]["venstre_tom"] == True

    if (n == forrige_n) and (n != 0):
        hukommelse[n]["blindvei"] = True

    if er_nokkel():
        print("Dette er en nokkel")

        plukk_opp()
        nokkel += 1
        gaa_tilbake()
        print("gaar tilbake")
        hukommelse[n]["blindvei"] = True
        for n in hukommelse:
            hukommelse[n]["hoyre"] = False
            hukommelse[n]["venstre"] = False

    elif er_superlaas():
        print("superlaas")
        if nokkel >= 2:
            laas_opp()
            nokkel -= 2
            hukommelse[n] = {"venstre": False, "hoyre": False, "venstre_tom": False, "hoyre_tom": False, "siste_steg": "", "blindvei": False}
            gaa_hoyre()
        else:
            gaa_tilbake()
            print("gaar tilbake")
    elif er_laas():
        print("laas")
        if nokkel >= 1:
            laas_opp()
            nokkel -= 1
            hukommelse[n] = {"venstre": False, "hoyre": False, "venstre_tom": False, "hoyre_tom": False, "siste_steg": "", "blindvei": False}
            gaa_hoyre()
        else:
            gaa_tilbake()
            print("gaar tilbake")

    elif er_stank():
        print("Dette er stank")
        gaa_tilbake()
        hukommelse[n]["blindvei"] = True

    elif er_vanlig() or er_inngang():
        if not (hukommelse[n]["hoyre"] or hukommelse[n]["hoyre_tom"] or hukommelse[n]["blindvei"]):
            hukommelse[n]["siste_steg"] = "hoyre"
            hukommelse[n]["hoyre"] = True
            gaa_hoyre()
            print("hoyre")
        elif not (hukommelse[n]["venstre"] or hukommelse[n]["venstre_tom"] or hukommelse[n]["blindvei"]):
            hukommelse[n]["siste_steg"] = "venstre"
            hukommelse[n]["venstre"] = True
            gaa_venstre()
            print("venstre")
        else:
            hukommelse[n]["blindvei"] = True
            gaa_tilbake()
            if hukommelse[forrige_n]["siste_steg"] == "hoyre":
                hukommelse[forrige_n]["hoyre_tom"] = True
            else:
                hukommelse[forrige_n]["venstre_tom"] = True
            print("gaar tilbake")

    if n == 46 or n == 48:
        print(hukommelse[n])

    print("")

gaa_ut()
