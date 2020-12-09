class Calculate:
    def calculateValues(self, a):
        kliszt = a.getKliszt()
        viz = a.getViz()
        eleszto = a.getEleszto()
        so = a.getSo()
        fliszt = a.getFliszt()
        db = a.getDb()
        ido = a.getIdo()
        eladasi_ar = 500
        nyereseg = ""
        oradij = 300
        
        try:
            if kliszt == "0" or kliszt == "-0" or \
               viz == "0" or viz == "-0" or \
               eleszto == "0" or eleszto == "-0" or \
               so == "0" or so == "-0" or \
               fliszt == "0" or fliszt == "-0" or\
               db == "0" or db == "-0":
                raise Exception("Hiba! Egy vagy több értéknél 0 a megadott érték!\nHa mégis 0-val számolna, így adja meg: .0")

            if float(kliszt) < 0 or \
               float(viz) < 0 or \
               float(eleszto) < 0 or \
               float(so) < 0 or \
               float(fliszt) < 0 or \
               float(db) < 0:
                raise Exception("Hiba! Egy vagy több értéknél negatív a megadott érték!")

            if kliszt == ".0":
                kliszt = "0.0"
                kliszt = float(kliszt)
            if viz == ".0":
                viz = "0.0"
                viz = float(viz)
            if eleszto == ".0":
                eleszto = "0.0"
                eleszto = float(eleszto)
            if so == ".0":
                so = "0.0"
                so = float(so)
            if fliszt == ".0":
                fliszt = "0.0"
                fliszt = float(fliszt)
            if db == ".0":
                db == "0.0"
                db = float(db)
        
            calc_oradij = (1 - (int(ido)) / 15) * oradij + oradij
            calc_oradij = round(calc_oradij)
            ora_mennyiseg = int(db) / int(ido)
            ora_mennyiseg = round(ora_mennyiseg)
            osszeg = float(kliszt) + float(viz) + float(eleszto) + float(so) + float(fliszt)
            income = eladasi_ar * int(db)
            all_profit = income - (osszeg * int(db)) - (calc_oradij * int(ido))
            profit_hour = all_profit / int(ido)

            if profit_hour < 0:
                inc = "A cég óránként termelt vesztesége: "
            else:
                inc = "A cég óránként termelt nyeresége: "

            if all_profit == 0:
                balance = "A cég termelt nyeresége: "
                nyereseg = "Nem."
            elif all_profit < 0:
                balance = "A cég termelt vesztesége: "
                nyereseg = "Nem."
            else:
                balance = "A cég termelt nyeresége: "
                nyereseg = "Igen."
        
            showTxt = f"Darabszám: {int(db)} Db\n" \
                      f"Idő: {int(ido)} Óra\n" \
                      f"Beruházás: {float(osszeg):.2f} Ft\n" \
                      f"Óradíj: {int(calc_oradij)} Ft/Óra\n" \
                      f"{balance}{float(all_profit):.2f} Ft\n" \
                      f"{inc}{float(profit_hour):.2f} Ft\n" \
                      f"Nyereséges a kalkuláció? {nyereseg}"

        except ValueError as ve:
            return f"Hiba! Egy vagy több értéket kihagyott / rosszul adott meg!\n\n{ve}"
        except Exception as e:
            return f"{e}"

        return showTxt

    def storeValues(self, a, v_kliszt, v_viz, v_eleszto, v_so, v_fliszt, v_db, v_ido):
        a.setKliszt(v_kliszt)
        a.setViz(v_viz)
        a.setEleszto(v_eleszto)
        a.setSo(v_so)
        a.setFliszt(v_fliszt)
        a.setDb(v_db)
        a.setIdo(v_ido)