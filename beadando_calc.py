class Calculate:
    def calculateValues(self, a):
        kliszt = a.getKliszt()
        viz = a.getViz()
        eleszto = a.getEleszto()
        so = a.getSo()
        fliszt = a.getFliszt()
        db = a.getDb()
        ido = a.getIdo()
        
        try:
            if kliszt == "0" or \
               viz == "0" or \
               eleszto == "0" or \
               so == "0" or \
               fliszt == "0" or \
               db == "0":
                    raise Exception
            
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
        
            sumOfValues = (float(kliszt) + float(viz) + float(eleszto) + float(so) + float(fliszt)) * float(db)
            allIncome = sumOfValues * ido
            profit = float(allIncome) - sumOfValues
            showTxt = f"Darabszám: {int(db)} Db\nBeruházás: {sumOfValues:,} Ft\nIdő: {ido} Óra\nBevétel: {allIncome:,} Ft\nProfit: {profit:,} Ft".replace(",", " ")

        except ValueError:
            return "Hiba! Egy vagy több értéket kihagyott / rosszul adta meg!"
        except Exception:
            return "Hiba! Egy vagy több értéknél 0 a megadott érték!\nHa mégis 0-val számolna, így adja meg: .0"

        return showTxt

    def storeValues(self, a, v_kliszt, v_viz, v_eleszto, v_so, v_fliszt, v_db, v_ido):
        a.setKliszt(v_kliszt)
        a.setViz(v_viz)
        a.setEleszto(v_eleszto)
        a.setSo(v_so)
        a.setFliszt(v_fliszt)
        a.setDb(v_db)
        a.setIdo(v_ido)