# -*- coding: utf-8 -*-
# Zaktualizowana sieć rzeczna Polski (poprawione węzły i dopływy)

POLAND_BORDER = [
    [53.92, 14.25], [53.93, 14.45], [54.05, 15.00], [54.18, 15.58], [54.43, 16.41],
    [54.58, 16.86], [54.76, 17.55], [54.83, 18.20], [54.83, 18.33], [54.79, 18.40],
    [54.60, 18.80], [54.72, 18.41], [54.52, 18.54], [54.44, 18.57], [54.37, 18.67],
    [54.38, 19.45], [54.44, 19.64], [54.33, 20.50], [54.33, 21.50], [54.33, 22.30],
    [54.36, 22.79], [54.15, 23.55], [53.60, 23.85], [53.25, 23.95], [52.70, 23.85],
    [52.12, 23.53], [51.55, 23.55], [50.85, 24.15], [50.50, 24.00], [50.25, 23.50],
    [49.70, 22.90], [49.30, 22.80], [49.00, 22.85], [49.15, 22.50], [49.35, 21.90],
    [49.40, 21.60], [49.35, 20.95], [49.38, 20.48], [49.30, 20.15], [49.18, 20.08],
    [49.20, 19.85], [49.30, 19.82], [49.57, 19.52], [49.50, 18.98], [49.75, 18.63],
    [49.95, 18.30], [50.20, 17.80], [50.10, 16.65], [50.44, 16.24], [50.74, 15.74],
    [50.82, 15.44], [51.05, 15.00], [51.15, 15.00], [51.54, 14.74], [51.95, 14.70],
    [52.07, 14.63], [52.35, 14.55], [52.60, 14.62], [52.83, 14.12], [53.25, 14.48],
    [53.55, 14.55], [53.72, 14.28], [53.92, 14.25]
]

BASELINE_RIVERS = [
    {
        "id": "wisla",
        "name": "Wisła",
        "path": [
            [49.61, 18.99], [49.80, 18.79], [50.04, 19.20], [50.05, 19.94],
            [50.10, 20.22], [50.31, 20.93], [50.68, 21.75], [50.88, 21.85],
            [51.32, 21.95], [51.56, 21.84], [52.23, 21.01], [52.44, 20.68],
            [52.54, 19.70], [52.66, 19.06], [53.01, 18.60], [53.15, 18.17],
            [53.35, 18.42], [53.48, 18.75], [53.84, 18.83], [54.09, 18.79],
            [54.36, 18.94]
        ]
    },
    {
        "id": "odra",
        "name": "Odra",
        "path": [
            [49.92, 18.32], [50.09, 18.22], [50.35, 18.15], [50.67, 17.92],
            [50.86, 17.47], [51.11, 17.03], [51.66, 16.08], [51.80, 15.71],
            [52.05, 15.10], [52.59, 14.65], [52.88, 14.20], [53.25, 14.48],
            [53.43, 14.55], [53.75, 14.35]
        ]
    }
]

RIVERS_DATA = [
    {
        "id": "bug",
        "name": "Bug",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "lewy dopływ Narwi",
        "parentRiver": "Narew",
        "quadrant": "E",
        "quadrantName": "Wschód (E/NE)",
        "center": [51.90, 23.20],
        # Bug płynie wzdłuż wschodniej granicy i wpada do Narwi w Jeziorze Zegrzyńskim!
        "path": [
            [50.68, 24.15], [50.80, 23.95], [51.55, 23.55], [52.07, 23.60],
            [52.40, 22.65], [52.67, 22.32], [52.70, 21.97], [52.60, 21.45],
            [52.51, 21.07]
        ],
        "mouth": "wpada do Narwi w Jeziorze Zegrzyńskim (koło Serocka)",
        "keyTowns": ["Włodawa", "Terespol", "Drohiczyn", "Wyszków", "Serock"],
        "description": "Długa rzeka graniczna na wschodzie Polski. Płynie wzdłuż granicy z Ukrainą i Białorusią, po czym skręca na zachód i uchodzi do Narwi w Jeziorze Zegrzyńskim!",
        "mnemonic": "Bug płynie wzdłuż wschodniej granicy, skręca ku Warszawie i WPADA DO NARWI w Jeziorze Zegrzyńskim!",
        "hint": "Wschodnia granica Polski, wpada do Narwi pod Warszawą (Jezioro Zegrzyńskie)."
    },
    {
        "id": "narew",
        "name": "Narew",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "NE",
        "quadrantName": "Północny Wschód (NE)",
        "center": [53.05, 22.00],
        # Narew zbiera Biebrzę, potem Bug w Jeziorze Zegrzyńskim, Wkrę i wpada do Wisły w Modlinie
        "path": [
            [52.85, 23.75], [52.95, 22.95], [53.20, 22.77], [53.20, 22.40],
            [53.18, 22.06], [53.08, 21.57], [52.88, 21.42], [52.70, 21.09],
            [52.51, 21.07], [52.44, 20.71], [52.44, 20.68]
        ],
        "mouth": "wpada do Wisły w Nowym Dworze Mazowieckim (Modlin)",
        "keyTowns": ["Łomża", "Ostrołęka", "Pułtusk", "Serock", "Nowy Dwór Mazowiecki"],
        "description": "Rzeka wielokorytowa ('polska Amazonia'). W Wiznie przyjmuje Biebrzę, w Jeziorze Zegrzyńskim przyjmuje Bug, koło Modlina Wkrę i wpada do Wisły.",
        "mnemonic": "Narew zbiera wody Biebrzy, w Jeziorze Zegrzyńskim łączy się z Bugiem, a potem razem wpadają do Wisły w Modlinie!",
        "hint": "Północno-wschodnia Polska, zbiera Biebrzę i Bug, uchodzi do Wisły w Modlinie."
    },
    {
        "id": "biebrza",
        "name": "Biebrza",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Narwi",
        "parentRiver": "Narew",
        "quadrant": "NE",
        "quadrantName": "Północny Wschód (NE)",
        "center": [53.50, 22.75],
        "path": [
            [53.70, 23.50], [53.58, 22.95], [53.48, 22.65], [53.35, 22.45],
            [53.20, 22.40]
        ],
        "mouth": "wpada do Narwi koło Wizny",
        "keyTowns": ["Goniądz", "Osowiec-Twierdza", "Sztabin"],
        "description": "Królowa polskich bagien i ostoja łosi (Biebrzański Park Narodowy). Wpada do Narwi koło Wizny.",
        "mnemonic": "Biebrzańskie Bagna na północy Podlasia – rzeka Biebrza wpada bezpośrednio do Narwi pod Wizną!",
        "hint": "Skrajny północny wschód, wpada do Narwi koło Wizny."
    },
    {
        "id": "wkra",
        "name": "Wkra",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Narwi",
        "parentRiver": "Narew",
        "quadrant": "C",
        "quadrantName": "Północne Mazowsze (C/NE)",
        "center": [52.80, 20.40],
        # Wkra płynie z północy do Narwi tuż przed jej ujściem do Wisły
        "path": [
            [53.30, 20.50], [53.15, 20.30], [52.90, 20.30], [52.72, 20.45],
            [52.55, 20.60], [52.44, 20.71]
        ],
        "mouth": "wpada do Narwi w Nowym Dworze Mazowieckim (tuż przed Wisłą)",
        "keyTowns": ["Działdowo", "Mława", "Glinojeck", "Pomiechówek"],
        "description": "Płynie z północnego Mazowsza prosto na południe i uchodzi jako prawy dopływ do Narwi w Pomiechówku/Nowym Dworze Mazowieckim.",
        "mnemonic": "Wkra płynie z północy (od Mławy) i WPADA DO NARWI w Nowym Dworze Mazowieckim tuż przed Wisłą!",
        "hint": "Północne Mazowsze, wpada do Narwi tuż przed Modlinem."
    },
    {
        "id": "skrwa",
        "name": "Skrwa",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "C",
        "quadrantName": "Centrum / Mazowsze Płockie (C)",
        "center": [52.70, 19.60],
        # Skrwa płynie bezpośrednio do Wisły koło Płocka
        "path": [
            [52.88, 19.70], [52.82, 19.65], [52.70, 19.52], [52.58, 19.55]
        ],
        "mouth": "wpada bezpośrednio do Wisły koło Płocka (Zbiornik Włocławski)",
        "keyTowns": ["Sierpc", "Brudzeń Duży", "Płock (okolice)"],
        "description": "Rzeka Mazowsza Płockiego. Płynie przez Sierpc i Brudzeński Park Krajobrazowy, uchodząc bezpośrednio do Wisły pod Płockiem.",
        "mnemonic": "Skrwa płynie przez Sierpc i WPADA BEZPOŚREDNIO DO WISŁY koło Płocka (nie do Narwi!)",
        "hint": "Płynie przez Sierpc i uchodzi bezpośrednio do Wisły koło Płocka."
    },
    {
        "id": "dunajec",
        "name": "Dunajec",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "SE",
        "quadrantName": "Południe (SE/S)",
        "center": [49.80, 20.70],
        "path": [
            [49.48, 20.03], [49.43, 20.35], [49.42, 20.48], [49.62, 20.69],
            [49.83, 20.68], [49.96, 20.84], [50.13, 20.88], [50.24, 20.73]
        ],
        "mouth": "wpada do Wisły w Opatowcu",
        "keyTowns": ["Nowy Targ", "Szczawnica", "Nowy Sącz", "Tarnów"],
        "description": "Górska rzeka wypływająca z Tatr, przecinająca wapienne Pieniny słynnym Przełomem Dunajca i zaporami w Czorsztynie i Rożnowie.",
        "mnemonic": "Dunajec wypływa z Tatr, przecina Pieniny tratwami i płynie na północ przez Nowy Sącz i Tarnów do Wisły!",
        "hint": "Górski dopływ Wisły płynący z Tatr i Pienin."
    },
    {
        "id": "wisloka",
        "name": "Wisłoka",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "SE",
        "quadrantName": "Południowy Wschód (SE)",
        "center": [49.95, 21.45],
        "path": [
            [49.48, 21.43], [49.51, 21.50], [49.74, 21.47], [50.05, 21.41],
            [50.19, 21.48], [50.29, 21.42], [50.41, 21.36]
        ],
        "mouth": "wpada do Wisły koło Gawłuszowic (na północ od Mielca)",
        "keyTowns": ["Jasło", "Dębica", "Mielec"],
        "description": "Karpacki dopływ Wisły płynący z Beskidu Niskiego przez Podkarpacie, usytuowany pomiędzy dorzeczem Dunajca a Sanu.",
        "mnemonic": "Kolejność karpackich dopływów Wisły od zachodu do wschodu: DUNAJEC -> WISŁOKA -> SAN!",
        "hint": "Południowy wschód, leży dokładnie pomiędzy Dunajcem a Sanem."
    },
    {
        "id": "san",
        "name": "San",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "SE",
        "quadrantName": "Południowy Wschód (SE)",
        "center": [50.10, 22.40],
        "path": [
            [49.03, 22.87], [49.40, 22.45], [49.56, 22.21], [49.82, 22.23],
            [49.78, 22.77], [50.02, 22.68], [50.26, 22.42], [50.58, 22.06],
            [50.70, 21.84]
        ],
        "mouth": "wpada do Wisły na północ od Sandomierza",
        "keyTowns": ["Sanok", "Przemyśl", "Jarosław", "Stalowa Wola", "Sandomierz"],
        "description": "Największa rzeka południowo-wschodniej Polski. Źródła w Bieszczadach, tworzy Jezioro Solińskie i wpada do Wisły w Kotlinie Sandomierskiej.",
        "mnemonic": "San rodzi się w Bieszczadach (Solina), okrąża Przemyśl i zasila Wisłę pod Sandomierzem!",
        "hint": "Główna rzeka Bieszczadów i Podkarpacia, wpada do Wisły pod Sandomierzem."
    },
    {
        "id": "kamienna",
        "name": "Kamienna",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "lewy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "SE",
        "quadrantName": "Południowe Centrum (C/SE)",
        "center": [51.05, 21.20],
        "path": [
            [51.10, 20.75], [51.12, 20.87], [51.04, 21.07], [50.93, 21.39],
            [51.02, 21.54], [51.11, 21.78]
        ],
        "mouth": "wpada do Wisły w Solcu nad Wisłą",
        "keyTowns": ["Skarżysko-Kamienna", "Starachowice", "Ostrowiec Świętokrzyski", "Bałtów"],
        "description": "Rzeka Wyżyny Kieleckiej, oś Staropolskiego Okręgu Przemysłowego (hutnictwo, kopalnie rud żelaza) i jurajskiego parku w Bałtowie.",
        "mnemonic": "Kamienna płynie twardo przez Góry Świętokrzyskie (Skarżysko-Kamienna, Starachowice) prosto do Wisły!",
        "hint": "Wyżyna Kielecka, lewy dopływ Wisły poniżej Sandomierza."
    },
    {
        "id": "warta",
        "name": "Warta",
        "category": "river",
        "basin": "odra",
        "basinName": "Dorzecze Odry",
        "tributarySide": "prawy dopływ Odry",
        "parentRiver": "Odra",
        "quadrant": "NW",
        "quadrantName": "Centrum i Zachód (C/NW)",
        "center": [52.10, 17.50],
        "path": [
            [50.50, 19.50], [50.81, 19.12], [51.60, 18.73], [52.20, 18.64],
            [52.22, 18.25], [52.09, 17.02], [52.41, 16.94], [52.71, 16.38],
            [52.60, 15.51], [52.73, 15.24], [52.59, 14.62]
        ],
        "mouth": "wpada do Odry w Kostrzynie nad Odrą (Park Narodowy Ujście Warty)",
        "keyTowns": ["Częstochowa", "Sieradz", "Konin", "Poznań", "Gorzów Wielkopolski"],
        "description": "Trzecia najdłuższa rzeka Polski i największy dopływ Odry. Przecina całą Wielkopolskę potężnym łukiem.",
        "mnemonic": "Warta jest warta pamiętania – wypływa z Jury, przepływa przez Poznań i w Kostrzynie zasila Odrę!",
        "hint": "Główna rzeka Wielkopolski, największy prawy dopływ Odry."
    },
    {
        "id": "bobr",
        "name": "Bóbr",
        "category": "river",
        "basin": "odra",
        "basinName": "Dorzecze Odry",
        "tributarySide": "lewy dopływ Odry",
        "parentRiver": "Odra",
        "quadrant": "SW",
        "quadrantName": "Południowy Zachód (SW)",
        "center": [51.35, 15.50],
        "path": [
            [50.66, 15.91], [50.78, 16.03], [50.90, 15.73], [51.11, 15.59],
            [51.27, 15.57], [51.62, 15.32], [51.80, 15.24], [52.05, 15.08]
        ],
        "mouth": "wpada do Odry w Krośnie Odrzańskim",
        "keyTowns": ["Kamienna Góra", "Jelenia Góra", "Bolesławiec", "Żagań"],
        "description": "Najdłuższa górska rzeka Sudetów. Wypływa z Karkonoszy, płynie przez Dolny Śląsk i wpada do Odry.",
        "mnemonic": "Bóbr wypływa z Karkonoszy, mija ceramikę w Bolesławcu i płynie na północ do Odry!",
        "hint": "Południowy zachód, wypływa z Sudetów do Odry."
    },
    {
        "id": "pilica",
        "name": "Pilica",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "lewy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "C",
        "quadrantName": "Centrum (C)",
        "center": [51.45, 20.30],
        "path": [
            [50.47, 19.65], [50.63, 19.82], [51.09, 19.87], [51.35, 19.88],
            [51.53, 20.01], [51.62, 20.58], [51.65, 20.95], [51.78, 21.18],
            [51.85, 21.28]
        ],
        "mouth": "wpada do Wisły koło Czerska / Mniszewa",
        "keyTowns": ["Tomaszów Mazowiecki", "Nowe Miasto nad Pilicą", "Warka"],
        "description": "Najdłuższy lewy dopływ Wisły. Tworzy Zbiornik Sulejowski, słynie ze spływów kajakowych i sadów w Warce.",
        "mnemonic": "Pilica to NAJDŁUŻSZY lewy dopływ Wisły – płynie przez Zalew Sulejowski prosto do Warki!",
        "hint": "Najdłuższy lewy dopływ Wisły w centralnej Polsce."
    },
    {
        "id": "drweca",
        "name": "Drwęca",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "N",
        "quadrantName": "Północ (N/C)",
        "center": [53.35, 19.30],
        "path": [
            [53.58, 20.25], [53.70, 19.96], [53.42, 19.59], [53.25, 19.40],
            [53.11, 19.05], [53.01, 18.68]
        ],
        "mouth": "wpada do Wisły w Toruniu (Kaszczorek)",
        "keyTowns": ["Ostróda", "Nowe Miasto Lubawskie", "Brodnica", "Golub-Dobrzyń", "Toruń"],
        "description": "Czysta rzeka pojezierna, na całej długości będąca rezerwatem ichtiologicznym dla ryb łososiowatych. Płynie z Mazur prosto do Torunia.",
        "mnemonic": "Drwęca to wielki rezerwat ryb – płynie z Mazur przez Brodnicę do Torunia!",
        "hint": "Prawy dopływ Wisły łączący Pojezierze Mazurskie z Toruniem."
    },
    {
        "id": "wda",
        "name": "Wda (Wzórna)",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "lewy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "NW",
        "quadrantName": "Północ / Kaszuby (NW)",
        "center": [53.75, 18.20],
        "path": [
            [54.12, 17.75], [54.01, 17.93], [53.84, 18.10], [53.60, 18.34],
            [53.40, 18.47]
        ],
        "mouth": "wpada do Wisły w Świeciu",
        "keyTowns": ["Czarna Woda", "Tleń", "Świecie"],
        "description": "Nazywana też Czarną Wodą. Wypływa z jeziora Wdzydze na Kaszubach, przecina Bory Tucholskie i wpada do Wisły w Świeciu.",
        "mnemonic": "Wda to rzeka Borów Tucholskich płynąca z Kaszub na południe do Świecia!",
        "hint": "Lewy dopływ dolnej Wisły, płynie przez Bory Tucholskie do Świecia."
    },
    {
        "id": "wierzyca",
        "name": "Wierzyca",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "lewy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "NW",
        "quadrantName": "Północ / Kaszuby (NW)",
        "center": [53.95, 18.45],
        "path": [
            [54.12, 17.98], [53.98, 18.17], [53.96, 18.53], [53.92, 18.70],
            [53.84, 18.83]
        ],
        "mouth": "wpada do Wisły w Gniewie",
        "keyTowns": ["Kościerzyna", "Starogard Gdański", "Pelplin", "Gniew"],
        "description": "Rzeka Kociewia i Kaszub, płynąca na północ od rzeki Wdy, uchodząca do Wisły pod potężnym zamkiem krzyżackim w Gniewie.",
        "mnemonic": "Wierzyca płynie na północ od Wdy – mija Starogard i wpada do Wisły w GNIEWIE!",
        "hint": "Lewy dopływ dolnej Wisły, wpada do Wisły w Gniewie."
    },
    {
        "id": "osa",
        "name": "Osa",
        "category": "river",
        "basin": "wisla",
        "basinName": "Dorzecze Wisły",
        "tributarySide": "prawy dopływ Wisły",
        "parentRiver": "Wisła",
        "quadrant": "N",
        "quadrantName": "Północ (N)",
        "center": [53.50, 19.10],
        "path": [
            [53.60, 19.48], [53.54, 19.38], [53.47, 19.34], [53.45, 19.10],
            [53.52, 18.74]
        ],
        "mouth": "wpada do Wisły na północ od Grudziądza",
        "keyTowns": ["Biskupiec", "Łasin", "Grudziądz (okolice)"],
        "description": "Rzeka Pojezierza Iławskiego i Chełmińskiego, meandrująca głębokim wąwozem i wpadająca do Wisły tuż powyżej Grudziądza.",
        "mnemonic": "Osa żądli Wisłę tuż obok Grudziądza od wschodniej strony!",
        "hint": "Prawy dopływ Wisły na północ od Grudziądza."
    },
    {
        "id": "notec",
        "name": "Noteć",
        "category": "river",
        "basin": "odra",
        "basinName": "Dorzecze Odry",
        "tributarySide": "prawy dopływ Warty",
        "parentRiver": "Warta",
        "quadrant": "NW",
        "quadrantName": "Północny Zachód (NW)",
        "center": [52.95, 16.80],
        "path": [
            [52.33, 18.85], [52.68, 18.33], [52.95, 17.92], [53.14, 17.60],
            [53.06, 16.73], [52.90, 16.57], [52.88, 16.01], [52.74, 15.42]
        ],
        "mouth": "wpada do Warty w Santoku (koło Gorzowa Wlkp.)",
        "keyTowns": ["Kruszwica", "Nakło nad Notecią", "Piła (Ujście)", "Czarnków", "Drezdenko"],
        "description": "Główna rzeka pradoliny toruńsko-eberswaldzkiej. Wypływa na Kujawach, przepływa przez Gopło i łączy się z Wartą.",
        "mnemonic": "Noteć płynie Pradoliną Toruńsko-Eberswaldzką przez Nakło i Piłę, wpadając do Warty w Santoku!",
        "hint": "Największy dopływ Warty na północnym zachodzie."
    },
    {
        "id": "nysa_luzycka",
        "name": "Nysa Łużycka",
        "category": "river",
        "basin": "odra",
        "basinName": "Dorzecze Odry",
        "tributarySide": "lewy dopływ Odry",
        "parentRiver": "Odra",
        "quadrant": "SW",
        "quadrantName": "Zachód (Granica) (SW/W)",
        "center": [51.40, 14.90],
        "path": [
            [50.90, 14.83], [51.15, 15.00], [51.25, 15.05], [51.54, 14.74],
            [51.95, 14.72], [52.07, 14.75]
        ],
        "mouth": "wpada do Odry koło Kosarzyna / Ratzdorf",
        "keyTowns": ["Zgorzelec", "Łęknica", "Gubin"],
        "description": "Rzeka stanowiąca zachodnią granicę Polski z Niemcami (granica na Odrze i Nysie Łużyckiej).",
        "mnemonic": "Nysa ŁUŻYCKA to rzeka graniczna z Niemcami na zachodzie (Zgorzelec, Gubin)!",
        "hint": "Lewy dopływ Odry biegnący wzdłuż granicy z Niemcami."
    },
    {
        "id": "nysa_klodzka",
        "name": "Nysa Kłodzka",
        "category": "river",
        "basin": "odra",
        "basinName": "Dorzecze Odry",
        "tributarySide": "lewy dopływ Odry",
        "parentRiver": "Odra",
        "quadrant": "SW",
        "quadrantName": "Południowy Zachód (SW)",
        "center": [50.45, 17.00],
        "path": [
            [50.15, 16.80], [50.15, 16.66], [50.44, 16.66], [50.51, 16.74],
            [50.46, 17.17], [50.47, 17.33], [50.75, 17.62], [50.80, 17.67]
        ],
        "mouth": "wpada do Odry koło Skorogoszczy (między Opolem a Brzegiem)",
        "keyTowns": ["Kłodzko", "Bystrzyca Kłodzka", "Paczków", "Nysa", "Lewin Brzeski"],
        "description": "Górska rzeka Sudetów płynąca przez Kotlinę Kłodzką, tworząca Jezioro Otmuchowskie i Nyskie, po czym uchodząca do Odry.",
        "mnemonic": "Nysa KŁODZKA płynie przez Kotlinę Kłodzką w stronę Opola i Brzegu!",
        "hint": "Południowy zachód, płynie przez Kotlinę Kłodzką do Odry."
    }
]
