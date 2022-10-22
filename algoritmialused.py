class algo_alused:
    def yl_60():

        #60 Politsei ja kurjategia autode vahemaa on 240 meetri. Politsei auto kiirus on
        #A m/s, kurjategija auto - B m/s. Kui kiiresti politsei saab kurjategija kätte?

        distance = 240
        try:                # Proovime kas vastavad andmed on numbrid või mitte.
            speed_ment = int(input('Mendi kiirus: '))
            speed_krim = int(input('krimi kiirus: '))
        except(ValueError): # kukkus läbi, jätab vahele selle.
            print('antud Str väärtus, peab olema int.')
            return

        maths = distance/(speed_ment-speed_krim) #lihtne arvutus.

        if maths <=0: print(f'ment ei jõua järgi.') # Kui kiirus on 0 või väiksem, siis politsei loogiliselt ei jõuaks järgi.
        else: print(f'aja distantsiga {maths}s')


    def yl_79():

        #79 Esimene brigaad värvis t1 tunniga A m2
        #seina ja teine brigaad t2 tunniga värvis B m2. Millises meeskonnas on tootlikkus kõrgem ja kui palju?

        try:
            t1 = int(input('brigaad.1 aeg: '))
            m21 = int(input('brigaad.1 m2: '))
            t2 = int(input('brigaad.2 aeg: '))
            m22 = int(input('brigaad.2 m2: '))
        except(ValueError):
            print('Antud Str väärtus, peab olema int.')
            return

        brig1 = m21/t1
        brig2 = m22/t2

        # olen 100% kindel et seda saaks teha kompaktsemalt, aga ma ei ole kindel kuidas.
        if brig1 > brig2: print(f'brigaad 1 on effektiivsem kiirusega {brig1} m2/h.\n{brig1-brig2} m2/h kiirem kui brigaad 2 kiirusega {brig2} m2/h')
        elif brig1 < brig2: print(f'brigaad 2 on effektiivsem kiirusega {brig2} m2/h.\n{brig2-brig1} m2/h kiirem kui brigaad 1 kiirusega {brig1} m2/h')
        else: print(f'mõlemad brigaadid on sama kiired, töötavad kiirusega {brig1} m2/h')


    def yl_155():
        
        #155 On antud täisarvud 35 kuni 87. Leida ja trükkida välja need arvud, mis 7-
        #ga jagamisel annavad jäägi 1, 2 või 5.
        #ma ei teadnud kas Modulus arvutusega või oli vaja komakohaga seda. tegin mõlemad.

        a1, a2, jag = 35, 87, 7 # kolm variable'i yhel real, mis on tunduvalt kompaktsem ja ilusam.
        acceptable = (1,2,5) # panin aktsepteeritavad numbrid Tupple'i sisse, kuna me ei hakka muutma seda ja siis saame kasutada in funtkiooni if statmentis.

        print(f'float koma tagune arv.')
        while a1 <= a2: # Selles While loopis me arvutame a1 / 7 ja ümardame selle arvu kahe koma kohani.
            math = round(a1/jag, 2) # arvutus, ja ümardus kahe koma kohani.

            temp_list = [char for char in str(math)] # loome for loopi list'i sisse, mis trükib iga karakteri sellest arvust mis saime.
            for popping in range(temp_list.index('.')): temp_list.pop(popping) # siin me viskame välja kõik numbrid kuni me leiame nimekirjas '.'

            if int(temp_list[1]) in acceptable: # kontrollime kas positsioonil [1] on number 1, 2 või 3
                print(f'{a1} val > {math}') # prindime väärtuse millega arvutati, ja selle koma koha väärtusega.
            a1 += 1
        
        print(f'modulus arv.')
        a1 = 35 # peame uuesti 35 peale panema kuna eelmine while loop pani selle arvu alguseks 87.
        while a1 <= a2: 
            math = a1%jag # Leiame Modulusiga ülejääva arvu summa.
            if math in acceptable: # Kui arv on Tupple'is siis ta prindib järgnevat.
                print(f'{a1} val > {math}')
            a1 += 1

algo_alused.yl_60()
algo_alused.yl_79()
algo_alused.yl_155()