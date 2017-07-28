import sqlite3

db=sqlite3.connect('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

#EXT 3G_EN RED 3G SHARING
cursor.execute('''SELECT EXT3G_3GSHARING.ExternalUtranCellId, EXT3G_3GSHARING.rncid, EXT3G_3GSHARING.cid, EXT3G_3GSHARING.lac, EXT3G_3GSHARING.mcc, EXT3G_3GSHARING.mnc, EXT3G_3GSHARING.PRIMARYSCRAMBLINGCODE,EXT3G_3GSHARING.uarfcndl
FROM EXT3G_3GSHARING;''')

celdas = cursor.fetchall()

for celda in celdas:
    externa_valida = 1
    def_ext_valida = 1
    try:
        externa_eri = celda[0]
        ci_ext = int(celda[2])
        lac_ext = int(celda[3])
        mcc_ext = int(celda[4])
        mnc_ext = int(celda[5])
        psc_ext = int(celda[6])
        uarfcn_ext = int(celda[7])
        externa_valida = 1
    except:
        pass
        externa_valida = 0
    cursor.execute('''
        SELECT ERI_3G.LocalCellName, ERI_3G.UtranCellId, ERI_3G.Lac, ERI_3G.PSC, ERI_3G.Mcc, ERI_3G.Mnc, ERI_3G.UARFCN_DL, ERI_3G.Rnc
        FROM ERI_3G WHERE(((ERI_3G.LocalCellName) = "''' + externa_eri + '"));')
    try:
        def_externa_eri = cursor.fetchone()
        def_externa_eri_ci = int(def_externa_eri[1])
        def_externa_eri_lac = int(def_externa_eri[2])
        def_externa_eri_psc = int(def_externa_eri[3])
        def_externa_eri_mcc = int(def_externa_eri[4])
        def_externa_eri_mnc = int(def_externa_eri[5])
        def_externa_eri_uarfcndl = int(def_externa_eri[6])
        def_externa_eri_rnc = def_externa_eri[7]
        def_ext_valida = 1
    except:
        pass
        def_ext_valida = 0

    if externa_valida == 1 and def_ext_valida == 1:

        if psc_ext - def_externa_eri_psc <> 0: print 'PSC EN DEF EXTERNA: ' + externa_eri, str(psc_ext) + '  PSC EN RED: ' + externa_eri, def_externa_eri_psc
        if lac_ext - def_externa_eri_lac <> 0: print 'LAC EN DEF EXTERNA: ' + externa_eri, str(lac_ext) + '  LAC EN RED: ' + externa_eri, def_externa_eri_lac
        if ci_ext - def_externa_eri_ci <> 0: print 'CI EN DEF EXTERNA: ' + externa_eri, str(ci_ext) + '  CI EN RED: ' + externa_eri, def_externa_eri_ci
        if mcc_ext - def_externa_eri_mcc <> 0: print 'MCC EN DEF EXTERNA: ' + externa_eri, str(mcc_ext) + '  MCC EN RED: ' + externa_eri, def_externa_eri_mcc
        if mnc_ext - def_externa_eri_mnc <> 0: print 'MNC EN DEF EXTERNA: ' + externa_eri, str(mnc_ext) + '  MNC EN RED: ' + externa_eri, def_externa_eri_mnc

    cursor.execute('''
         SELECT HUA_3G.LocalCellName,  HUA_3G.UtranCellId,HUA_3G.LAC, HUA_3G.PSC,HUA_3G.MCC,HUA_3G.MNC, HUA_3G.UARFCN_DL, HUA_3G.RNC FROM HUA_3G
          WHERE (((HUA_3G.LocalCellName)="''' + externa_eri + '"));')
    try:
        def_externa_hua = cursor.fetchone()
        def_externa_hua_ci = int(def_externa_hua[1])
        def_externa_hua_lac = int(def_externa_hua[2])
        def_externa_hua_psc = int(def_externa_hua[3])
        def_externa_hua_mcc = int(def_externa_hua[4])
        def_externa_hua_mnc = int(def_externa_hua[5])
        def_externa_hua_uarfcndl = int(def_externa_hua[6])
        def_externa_hua_rnc = def_externa_hua[7]
        def_ext_valida = 1

    except:
        pass
        def_ext_valida = 0

    if externa_valida == 1 and def_ext_valida == 1:

        if psc_ext - def_externa_hua_psc <> 0: print 'PSC EN DEF EXTERNA: ' + externa_eri, str(psc_ext) + '  PSC EN RED: ' + externa_eri, def_externa_hua_psc
        if lac_ext - def_externa_hua_lac <> 0: print 'LAC EN DEF EXTERNA: ' + externa_eri, str(lac_ext) + '  LAC EN RED: ' + externa_eri, def_externa_hua_lac
        if ci_ext - def_externa_hua_ci <> 0: print 'CI EN DEF EXTERNA: ' + externa_eri, str(ci_ext) + '  CI EN RED: ' + externa_eri, def_externa_hua_ci
        if mcc_ext - def_externa_hua_mcc <> 0: print 'MCC EN DEF EXTERNA: ' + externa_eri, str(mcc_ext) + '  MCC EN RED: ' + externa_eri, def_externa_hua_mcc
        if mnc_ext - def_externa_hua_mnc <> 0: print 'MNC EN DEF EXTERNA: ' + externa_eri, str(mnc_ext) + '  MNC EN RED: ' + externa_eri, def_externa_hua_mnc

db.commit()
db.close()