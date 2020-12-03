#NOT FINISHED

class Calculate:
    def calculateValues(self, a):
        sumOfValues = int(a.getKliszt()) + int(a.getViz()) + int(a.getEleszto()) + int(a.getSo()) + int(a.getFliszt())
        timeToProduce = int(a.getIdo())
        allIncome = sumOfValues * timeToProduce
        profit = int(allIncome) - sumOfValues
        showTxt = f"Darabszám: {int(a.getDb())} Db\nBeruházás: {sumOfValues:,} Ft\nIdő: {timeToProduce} Óra\nBevétel: {allIncome:,} Ft\nProfit: {profit:,} Ft".replace(",", " ")
        return showTxt

    def storeValues(self, a, v_kliszt, v_viz, v_eleszto, v_so, v_fliszt, v_db, v_ido):
        a.setKliszt(v_kliszt)
        a.setViz(v_viz)
        a.setEleszto(v_eleszto)
        a.setSo(v_so)
        a.setFliszt(v_fliszt)
        a.setDb(v_db)
        a.setIdo(v_ido)