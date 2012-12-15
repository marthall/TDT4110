elif er_superlaas:
    print("superlaas")
    if nokkel >= 2:
        laas_opp()
        nokkel -= 2
        hukommelse[n] = {"venstre": False, "hoyre": False, "venstre_tom": False, "hoyre_tom": False, "siste_steg": "", "blindvei": False}
        gaa_hoyre()
    else:
        gaa_tilbake()
        print("gaar tilbake")
elif er_laas:
    print("laas")
    if nokkel >= 1:
        laas_opp
        nokkel -= 1
        hukommelse[n] = {"venstre": False, "hoyre": False, "venstre_tom": False, "hoyre_tom": False, "siste_steg": "", "blindvei": False}
        gaa_hoyre()
    else:
        gaa_tilbake()
        print("gaar tilbake")


elif er_laas():
    print("Dette er en laas")

    if nokkel >= 1:
        if er_superlaas():
            print("SUPERLAAS")
            if nokkel >= 2:
                laas_opp()
                nokkel -= 2
        else:
            laas_opp()
            nokkel -= 1

        if hukommelse[n]["hoyre"] == False:
            gaa_hoyre()
        else:
            gaa_venstre()
        hukommelse[n] = {"venstre": False, "hoyre": False, "venstre_tom": False, "hoyre_tom": False, "siste_steg": "", "blindvei": False}
        print("gaar hoyre")
    else:
        gaa_tilbake()
        print("gaa tilbake")
