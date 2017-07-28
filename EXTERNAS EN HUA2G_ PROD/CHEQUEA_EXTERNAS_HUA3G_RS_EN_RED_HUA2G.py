import sqlite3

db=sqlite3.connect('C:\\Desarrollo_Pablo\\CHEQUEO EXTERNAS\\dbext.db')
db.text_factory = str
cursor=db.cursor()

#EXT 3G_HUA2G
cursor.execute('''SELECT EXT_3G_HUA2G.ExternalUtranCellNameStandard, EXT_3G_HUA2G.GlobalRNCname, EXT_3G_HUA2G.TargetUtranCellId, EXT_3G_HUA2G.TargetUtranCellLac, EXT_3G_HUA2G.TargetUtranCellMcc, EXT_3G_HUA2G.TargetUtranCellMnc, EXT_3G_HUA2G.RA, EXT_3G_HUA2G.TargetUtranPsc,EXT_3G_HUA2G.GlobalVendor,EXT_3G_HUA2G.TargetUtranUARFCN_DL,EXT_3G_HUA2G.SourceBsc
FROM EXT_3G_HUA2G;''')

celdas=cursor.fetchall()

for celda in celdas:

    if celda[8]=='Orange-Huawei':
        externa_valida=1
        def_ext_valida=1
        try:
            externa_hua=celda[0]
            rnc_ext = celda[1]
            ci_ext=int(celda[2])
            lac_ext=int(celda[3])
            mcc_ext=int(celda[4])
            mnc_ext=int(celda[5])
            rac_ext=int(celda[6])
            psc_ext=int(celda[7])
            vendor_ext=celda[8]
            dl_uarfcn_ext = int(celda[9])
            bsc_origen = celda[10]
            externa_valida=1
        except:
            pass
            externa_valida=0

        cursor.execute('''
        SELECT HUA_3G_RS.LocalCellName,  HUA_3G_RS.UtranCellId,HUA_3G_RS.LAC, HUA_3G_RS.PSC,HUA_3G_RS.MCC,HUA_3G_RS.MNC, HUA_3G_RS.UARFCN_DL, HUA_3G_RS.RNC FROM HUA_3G_RS
         WHERE (((HUA_3G_RS.LocalCellName)="'''+externa_hua+'"));')
        try:
            def_externa_hua=cursor.fetchone()
            def_externa_hua_ci = int(def_externa_hua[1])
            def_externa_hua_lac=int(def_externa_hua[2])
            def_externa_hua_psc = int(def_externa_hua[3])
            def_externa_hua_mcc = int(def_externa_hua[4])
            def_externa_hua_mnc = int(def_externa_hua[5])
            def_externa_hua_uarfcndl = int(def_externa_hua[6])
            def_externa_hua_rnc = def_externa_hua[7]
            def_ext_valida = 1


        except:
            pass
            def_ext_valida=0

        if externa_valida==1 and def_ext_valida==1:

            if psc_ext-def_externa_hua_psc<>0: print 'BSC ORIGEN: '+bsc_origen+';PSC EN DEF EXTERNA: '+ externa_hua,str(psc_ext)+ '  PSC EN RED: '+ externa_hua, def_externa_hua_psc
            if lac_ext - def_externa_hua_lac <> 0: print 'BSC ORIGEN: '+bsc_origen+';LAC EN DEF EXTERNA: ' + externa_hua,str(lac_ext) + '  LAC EN RED: ' + externa_hua, def_externa_hua_lac
            if ci_ext - def_externa_hua_ci <> 0: print 'BSC ORIGEN: '+bsc_origen+';CI EN DEF EXTERNA: ' + externa_hua,str(ci_ext) + '  CI EN RED: ' + externa_hua, def_externa_hua_ci
            if mcc_ext - def_externa_hua_mcc <> 0: print 'BSC ORIGEN: '+bsc_origen+';MCC EN DEF EXTERNA: ' + externa_hua,str(mcc_ext) + '  MCC EN RED: ' + externa_hua, def_externa_hua_mcc
            if mnc_ext - def_externa_hua_mnc <> 0: print 'BSC ORIGEN: '+bsc_origen+';MNC EN DEF EXTERNA: ' + externa_hua,str(mnc_ext) + '  MNC EN RED: ' + externa_hua, def_externa_hua_mnc
            if rnc_ext <> def_externa_hua_rnc: print 'BSC ORIGEN: '+bsc_origen+';RNC EN DEF EXTERNA: ' + externa_hua, str(rnc_ext) + '  RNC EN RED: ' + externa_hua, def_externa_hua_rnc

db.commit()
db.close()