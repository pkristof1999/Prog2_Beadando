#NOT FINISHED
#NOT FINISHED
#NOT FINISHED
#NOT FINISHED
#NOT FINISHED
#NOT FINISHED
class Calculate:
    def calculateValues(self, a):
        sumOfValues = int(a.getKliszt()) + int(a.getViz()) + int(a.getEleszto()) + int(a.getSo()) + int(a.getFliszt())
        timeToProduce = int(a.getIdo())
        allIncome = sumOfValues * timeToProduce
        profit = int(allIncome) - sumOfValues
        showTxt = f"Gyártásra fordított beruházás: {sumOfValues:,} Ft\nGyártásra fordított idő: {timeToProduce} Óra\nÖsszes bevétel: {allIncome:,} Ft\nEbből profit: {profit:,} Ft".replace(",", " ")
        return showTxt

    def storeValues(self, a, v_kliszt, v_viz, v_eleszto, v_so, v_fliszt, v_ido):
        a.setKliszt(v_kliszt)
        a.setViz(v_viz)
        a.setEleszto(v_eleszto)
        a.setSo(v_so)
        a.setFliszt(v_fliszt)
        a.setIdo(v_ido)


#{a.getKliszt()}{a.getViz()}{a.getEleszto()}{a.getSo()}{a.getFliszt()}{a.getIdo()}