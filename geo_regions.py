# -*- coding: utf-8 -*-
# 24 Regiony fizycznogeograficzne Polski (poprawiona topologia wyżyn i łańcucha górskiego)

REGIONS_DATA = [
    {
        "id": "pobrzeze_slowinskie",
        "name": "Pobrzeże Słowińskie / Koszalińskie",
        "category": "region",
        "belt": "pobrzeza",
        "beltName": "Pas Pobrzeży",
        "quadrant": "NW",
        "quadrantName": "Północny Zachód (NW)",
        "center": [54.55, 17.10],
        "polygon": [
            [54.18, 15.58], [54.43, 16.41], [54.58, 16.86], [54.76, 17.55],
            [54.83, 18.33], [54.72, 18.41], [54.54, 17.75], [54.46, 17.03],
            [54.19, 16.18], [54.05, 15.80], [54.18, 15.58]
        ],
        "keyCities": ["Kołobrzeg", "Koszalin", "Słupsk", "Ustka", "Łeba"],
        "description": "Pas nadmorski wzdłuż Bałtyku ze Słowińskim Parkiem Narodowym, jeziorami przybrzeżnymi (Łebsko, Gardno) oraz ruchomymi wydmami.",
        "mnemonic": "Pobrzeże Słowińskie to wydmy ruchome w Łebie i pas plaż od Kołobrzegu aż po Władysławowo!",
        "hint": "Skrajna północna linia brzegowa Polski, na zachód od Zatoki Gdańskiej."
    },
    {
        "id": "nizina_szczecinska",
        "name": "Nizina Szczecińska",
        "category": "region",
        "belt": "pobrzeza",
        "beltName": "Pas Pobrzeży i Nizin Przymorskich",
        "quadrant": "NW",
        "quadrantName": "Północny Zachód (NW)",
        "center": [53.45, 14.80],
        "polygon": [
            [53.92, 14.25], [53.97, 14.77], [53.70, 15.10], [53.34, 15.04],
            [53.15, 14.89], [52.93, 14.87], [52.96, 14.42], [53.25, 14.48],
            [53.55, 14.55], [53.72, 14.28], [53.92, 14.25]
        ],
        "keyCities": ["Szczecin", "Stargard", "Świnoujście", "Goleniów", "Police"],
        "description": "Rozległe obniżenie wokół Zalewu Szczecińskiego, dolnej Odry i jeziora Dąbie. Kraina portowa o klimacie łagodnym morskim.",
        "mnemonic": "Nizina Szczecińska to 'brama do Bałtyku' wokół dolnej Odry i Zalewu Szczecińskiego na granicy z Niemcami.",
        "hint": "Skrajny północny zachód Polski, ujście rzeki Odry."
    },
    {
        "id": "kaszuby",
        "name": "Kaszuby",
        "category": "region",
        "belt": "pojezierza",
        "beltName": "Pas Pojezierzy",
        "quadrant": "NW",
        "quadrantName": "Północny Zachód / Północ (NW)",
        "center": [54.28, 18.05],
        "polygon": [
            [54.54, 17.75], [54.60, 18.24], [54.45, 18.45], [54.33, 18.40],
            [54.12, 18.25], [53.95, 18.05], [54.00, 17.65], [54.17, 17.49],
            [54.35, 17.60], [54.54, 17.75]
        ],
        "keyCities": ["Kartuzy", "Kościerzyna", "Bytów", "Wejherowo", "Żukowo"],
        "description": "Malownicza kraina 'Szwajcarii Kaszubskiej' z najwyższym wzniesieniem Niżu Polskiego (Wieżyca 329 m n.p.m.). Źródła rzek Wda i Wierzyca.",
        "mnemonic": "Kaszuby leżą na południowy zachód od Trójmiasta. Pamiętaj: z Kaszub wypływają dwie siostrzane rzeki – Wda i Wierzyca!",
        "hint": "Na zachód od Gdańska, kraina jezior i wzgórza Wieżyca."
    },
    {
        "id": "pojezierze_pomorskie",
        "name": "Pojezierze Pomorskie",
        "category": "region",
        "belt": "pojezierza",
        "beltName": "Pas Pojezierzy",
        "quadrant": "NW",
        "quadrantName": "Północny Zachód (NW)",
        "center": [53.70, 16.60],
        "polygon": [
            [54.05, 15.80], [54.19, 16.18], [54.46, 17.03], [54.17, 17.49],
            [54.00, 17.65], [53.79, 17.97], [53.59, 17.86], [53.45, 17.20],
            [53.40, 16.30], [53.34, 15.04], [53.70, 15.10], [54.05, 15.80]
        ],
        "keyCities": ["Drawsko Pomorskie", "Szczecinek", "Chojnice", "Człuchów", "Połczyn-Zdrój"],
        "description": "Szeroki pas wzgórz morenowych i setek polodowcowych jezior (Pojezierze Drawskie, Bytowskie, Krajeńskie) oraz lasów Borów Tucholskich.",
        "mnemonic": "Pojezierze Pomorskie leży tuż pod Pobrzeżem – tworzy pas jezior od Drawska po Chojnice!",
        "hint": "Pomiędzy Pobrzeżem Słowińskim a Niziną Wielkopolską/Kujawami."
    },
    {
        "id": "zulawy_wislane",
        "name": "Żuławy Wiślane",
        "category": "region",
        "belt": "pobrzeza",
        "beltName": "Pas Pobrzeży",
        "quadrant": "NE",
        "quadrantName": "Północ (NE/NW)",
        "center": [54.20, 19.05],
        "polygon": [
            [54.37, 18.67], [54.38, 19.45], [54.25, 19.50], [54.16, 19.40],
            [54.04, 19.03], [54.09, 18.79], [54.26, 18.64], [54.37, 18.67]
        ],
        "keyCities": ["Nowy Dwór Gdański", "Malbork", "Elbląg", "Tczew", "Pruszcz Gdański"],
        "description": "Płaska jak stół aluwialna delta Wisły. Znajduje się tu najniższy punkt Polski (depresja w Raczkach Elbląskich -1.8 m) oraz zamek krzyżacki w Malborku.",
        "mnemonic": "Żuławy to żyzne mady w trójkącie delty Wisły i najgłębsza polska depresja!",
        "hint": "Trójkątne ujście Wisły do Zatoki Gdańskiej koło Malborka i Elbląga."
    },
    {
        "id": "pojezierze_mazurskie",
        "name": "Pojezierze Mazurskie",
        "category": "region",
        "belt": "pojezierza",
        "beltName": "Pas Pojezierzy",
        "quadrant": "NE",
        "quadrantName": "Północny Wschód (NE)",
        "center": [53.85, 21.40],
        "polygon": [
            [54.33, 20.50], [54.33, 21.50], [54.33, 22.30], [54.10, 22.45],
            [53.83, 22.36], [53.50, 22.00], [53.56, 20.99], [53.58, 20.28],
            [53.78, 20.48], [54.12, 20.58], [54.33, 20.50]
        ],
        "keyCities": ["Olsztyn", "Giżycko", "Mikołajki", "Mrągowo", "Ełk", "Szczytno"],
        "description": "Kraina Tysiąca Jezior z największymi jeziorami Polski (Śniardwy i Mamry). Obejmuje Pojezierze Olsztyńskie, Mrągowskie, Krainę Wielkich Jezior i Pojezierze Ełckie.",
        "mnemonic": "Mazury = Kraina Wielkich Jezior (Śniardwy i Mamry) w północno-wschodniej Polsce!",
        "hint": "Północny wschód Polski, kraina największych jezior."
    },
    {
        "id": "nizina_podlaska",
        "name": "Nizina Podlaska",
        "category": "region",
        "belt": "niziny",
        "beltName": "Pas Nizin Środkowopolskich",
        "quadrant": "NE",
        "quadrantName": "Północny Wschód / Wschód (NE)",
        "center": [53.10, 23.00],
        "polygon": [
            [53.83, 22.36], [54.15, 23.55], [53.60, 23.85], [53.25, 23.95],
            [52.70, 23.85], [52.43, 22.86], [52.65, 22.40], [53.05, 22.20],
            [53.50, 22.00], [53.83, 22.36]
        ],
        "keyCities": ["Białystok", "Bielsk Podlaski", "Hajnówka", "Sokółka", "Łomża"],
        "description": "Płaska nizina wschodniej Polski z unikalnymi puszczami (Białowieska, Knyszyńska, Augustowska) oraz dolinami rzek Biebrzy i Narwi.",
        "mnemonic": "Podlasie to żubry w Białowieży i dzika rzeka Narew przy granicy z Białorusią.",
        "hint": "Wschód Polski wokół Białegostoku, doliny Narwi i Biebrzy."
    },
    {
        "id": "nizina_mazowiecka",
        "name": "Nizina Mazowiecka",
        "category": "region",
        "belt": "niziny",
        "beltName": "Pas Nizin Środkowopolskich",
        "quadrant": "C",
        "quadrantName": "Centrum (C / E)",
        "center": [52.30, 21.00],
        "polygon": [
            [53.11, 20.38], [53.08, 21.57], [53.05, 22.20], [52.65, 22.40],
            [52.17, 22.28], [51.63, 21.93], [51.40, 21.15], [51.70, 20.50],
            [52.10, 19.80], [52.54, 19.70], [52.85, 19.67], [53.11, 20.38]
        ],
        "keyCities": ["Warszawa", "Radom", "Płock", "Siedlce", "Ciechanów", "Ostrołęka"],
        "description": "Największy region nizinny w centrum kraju, kotlina zbiegu najważniejszych rzek: Wisły, Narwi, Bugu, Pilicy i Bzury.",
        "mnemonic": "Mazowsze to serce Polski z Warszawą, gdzie wszystkie wielkie rzeki spotykają się z Wisłą!",
        "hint": "Środek i wschód Polski, otacza stolicę – Warszawę."
    },
    {
        "id": "polesie_lubelskie",
        "name": "Polesie Lubelskie",
        "category": "region",
        "belt": "niziny",
        "beltName": "Pas Nizin Środkowopolskich",
        "quadrant": "SE",
        "quadrantName": "Wschód (SE)",
        "center": [51.45, 23.30],
        "polygon": [
            [51.85, 23.40], [51.55, 23.55], [51.16, 23.81], [51.13, 23.47],
            [51.30, 22.88], [51.64, 22.90], [51.85, 23.40]
        ],
        "keyCities": ["Włodawa", "Parczew", "Łęczna", "Urszulin"],
        "description": "Kraina rozległych torfowisk, bagien i jezior krasowych (Poleski Park Narodowy) wzdłuż rzeki Bug na wschodniej granicy.",
        "mnemonic": "Polesie Lubelskie = Poleski Park Narodowy z żółwiem błotnym i bagnami nad rzeką Bug!",
        "hint": "Pomiędzy Niziną Mazowiecką a Wyżyną Lubelską, przy wschodniej granicy."
    },
    {
        "id": "pojezierze_wielkopolskie",
        "name": "Pojezierze Wielkopolskie",
        "category": "region",
        "belt": "pojezierza",
        "beltName": "Pas Pojezierzy",
        "quadrant": "NW",
        "quadrantName": "Zachód / Centrum (NW)",
        "center": [52.45, 17.20],
        "polygon": [
            [52.81, 17.20], [52.75, 17.49], [52.65, 17.95], [52.32, 17.58],
            [52.15, 17.10], [52.30, 16.50], [52.61, 16.58], [52.81, 17.20]
        ],
        "keyCities": ["Poznań", "Gniezno", "Wągrowiec", "Września", "Szamotuły"],
        "description": "Kolebka państwa polskiego z jeziorem Gopło, Gnieznem i Poznaniem. Rzeźba polodowcowa z pagórkami morenowymi i jeziorami rynnowymi.",
        "mnemonic": "Pojezierze Wielkopolskie to historyczny początek Polski (Gniezno, Ostrów Lednicki) na północ od Warty.",
        "hint": "Wokół Poznania i Gniezna, na zachód od Kujaw."
    },
    {
        "id": "kujawy",
        "name": "Kujawy",
        "category": "region",
        "belt": "pojezierza",
        "beltName": "Pas Pojezierzy / Nizin",
        "quadrant": "C",
        "quadrantName": "Północne Centrum (C)",
        "center": [52.70, 18.60],
        "polygon": [
            [52.90, 18.41], [52.88, 18.79], [52.65, 19.07], [52.50, 18.80],
            [52.45, 18.35], [52.65, 17.95], [52.79, 18.26], [52.90, 18.41]
        ],
        "keyCities": ["Inowrocław", "Włocławek", "Kruszwica", "Ciechocinek", "Radziejów"],
        "description": "Kraina w 'kolanie Wisły' słynąca z wyjątkowo żyznych czarnych ziem kujawskich, tężni solankowych w Inowrocławiu i Ciechocinku oraz Mysiej Wieży w Kruszwicy.",
        "mnemonic": "Kujawy leżą w kolanie Wisły – zapamiętaj: żyzne czarne ziemie i sól w Ciechocinku!",
        "hint": "Na zachód od Wisły pomiędzy Toruniem, Bydgoszczą a Włocławkiem."
    },
    {
        "id": "nizina_wielkopolska",
        "name": "Nizina Wielkopolska",
        "category": "region",
        "belt": "niziny",
        "beltName": "Pas Nizin Środkowopolskich",
        "quadrant": "NW",
        "quadrantName": "Zachód (NW/C)",
        "center": [51.80, 17.60],
        "polygon": [
            [52.15, 17.10], [52.32, 17.58], [52.22, 18.25], [52.20, 18.64],
            [51.85, 18.70], [51.60, 18.50], [51.45, 17.80], [51.55, 16.90],
            [51.84, 16.58], [52.09, 16.65], [52.15, 17.10]
        ],
        "keyCities": ["Kalisz", "Konin", "Ostrów Wielkopolski", "Leszno", "Krotoszyn"],
        "description": "Rolnicza równina w dorzeczu Warty i Prosny, na południe od Pojezierza Wielkopolskiego. Kalisz uznawany jest za najstarsze miasto w Polsce.",
        "mnemonic": "Nizina Wielkopolska rozciąga się wzdłuż Warty i Prosny wokół najstarszego Kalisza i Leszna!",
        "hint": "Południowa Wielkopolska, na południe od Poznania i na północ od Śląska."
    },
    {
        "id": "nizina_slaska",
        "name": "Nizina Śląska",
        "category": "region",
        "belt": "niziny",
        "beltName": "Pas Nizin Środkowopolskich",
        "quadrant": "SW",
        "quadrantName": "Południowy Zachód (SW)",
        "center": [50.95, 17.20],
        "polygon": [
            [51.66, 16.08], [51.55, 16.90], [51.11, 17.50], [50.67, 18.10],
            [50.35, 18.21], [50.09, 18.22], [50.32, 17.58], [50.70, 16.90],
            [51.05, 16.19], [51.40, 16.20], [51.66, 16.08]
        ],
        "keyCities": ["Wrocław", "Opole", "Legnica", "Lubin", "Brzeg", "Oława"],
        "description": "Ciepła, urodzajna nizina w dolinie Odry z najdłuższym okresem wegetacyjnym w Polsce. Bogata w czarnoziemy i zabytki Wrocławia.",
        "mnemonic": "Nizina Śląska = Wrocław i rzeka Odra. Najcieplejszy region nizinny w Polsce!",
        "hint": "Wzdłuż biegu Odry na południowym zachodzie wokół Wrocławia i Opola."
    },
    {
        "id": "sudety",
        "name": "Sudety",
        "category": "region",
        "belt": "gory",
        "beltName": "Pas Gór (Sudety)",
        "quadrant": "SW",
        "quadrantName": "Południowy Zachód (SW)",
        "center": [50.60, 16.10],
        "polygon": [
            [50.91, 15.34], [51.05, 16.19], [50.70, 16.90], [50.44, 16.88],
            [50.15, 16.85], [50.15, 16.66], [50.44, 16.24], [50.74, 15.74],
            [50.82, 15.44], [50.91, 15.34]
        ],
        "keyCities": ["Wałbrzych", "Jelenia Góra", "Kłodzko", "Karpacz", "Szklarska Poręba"],
        "description": "Góry zrębowe na granicy z Czechami z Karkonoszami (Śnieżka 1603 m), Górami Stołowymi (Szczeliniec Wielki) i Kotliną Kłodzką.",
        "mnemonic": "Sudety to góry na południowo-zachodniej granicy: Śnieżka, Karkonosze i Kotlina Kłodzka!",
        "hint": "Południowo-zachodnia granica z Czechami."
    },
    {
        "id": "wyzyna_slaska",
        "name": "Wyżyna Śląska",
        "category": "region",
        "belt": "wyzyny",
        "beltName": "Pas Wyżyn Polskich",
        "quadrant": "SW",
        "quadrantName": "Południe / Śląsk (SW/S)",
        "center": [50.28, 18.80],
        # Wyżyna Śląska leży NA ZACHÓD od Jury (obok siebie, zachód-wschód!)
        "polygon": [
            [50.55, 18.50], [50.52, 18.95], [50.45, 19.10], [50.25, 19.15],
            [50.08, 19.00], [49.98, 18.85], [50.05, 18.45], [50.25, 18.35],
            [50.45, 18.40], [50.55, 18.50]
        ],
        "keyCities": ["Katowice", "Gliwice", "Bytom", "Zabrze", "Rybnik", "Tychy", "Tarnowskie Góry"],
        "description": "Górnośląski Okręg Przemysłowy. Leży NA ZACHÓD od Jury Krakowsko-Częstochowskiej. Bogate złoża węgla kamiennego, cynku i ołowiu.",
        "mnemonic": "Wyżyna Śląska leży NA ZACHÓD od Jury: Katowice i przemysł węglowy sąsiadują od wschodu ze skałkami Jury!",
        "hint": "Południowa Polska wokół Katowic – leży na zachód od Wyżyny Krakowsko-Częstochowskiej."
    },
    {
        "id": "wyzyna_krakowsko_czestochowska",
        "name": "Wyżyna Krakowsko-Częstochowska",
        "category": "region",
        "belt": "wyzyny",
        "beltName": "Pas Wyżyn Polskich",
        "quadrant": "C",
        "quadrantName": "Południowe Centrum (SW/C)",
        "center": [50.45, 19.50],
        # Wąski pas skośny biegnący od Częstochowy (NW) do Krakowa (SE), NA WSCHÓD od Wyżyny Śląskiej!
        "polygon": [
            [50.85, 19.12], [50.78, 19.38], [50.60, 19.62], [50.40, 19.72],
            [50.18, 19.88], [50.06, 19.95], [50.08, 19.68], [50.25, 19.45],
            [50.48, 19.20], [50.72, 19.05], [50.85, 19.12]
        ],
        "keyCities": ["Częstochowa", "Zawiercie", "Ogrodzieniec", "Olkusz", "Ojców", "Kraków (północ)"],
        "description": "Wąski pas wapiennych skałek i jaskiń (Jura) ciągnący się od Częstochowy na południowy wschód do Krakowa. Przylega od wschodu do Wyżyny Śląskiej!",
        "mnemonic": "Jura Krakowsko-Częstochowska to wąski pas skałek biegnący SKOŚNIE od Częstochowy do Krakowa – leży NA WSCHÓD od Wyżyny Śląskiej!",
        "hint": "Wąski pas skałek wapiennych od Częstochowy do Krakowa, na wschód od Śląska."
    },
    {
        "id": "wyzyna_kielecka",
        "name": "Wyżyna Kielecka",
        "category": "region",
        "belt": "wyzyny",
        "beltName": "Pas Wyżyn Polskich",
        "quadrant": "SE",
        "quadrantName": "Południowe Centrum (C/SE)",
        "center": [50.90, 20.90],
        "polygon": [
            [51.19, 20.41], [51.12, 20.87], [51.04, 21.35], [50.90, 21.65],
            [50.68, 21.75], [50.65, 21.10], [50.75, 20.50], [50.95, 20.40],
            [51.19, 20.41]
        ],
        "keyCities": ["Kielce", "Ostrowiec Świętokrzyski", "Starachowice", "Skarżysko-Kamienna", "Sandomierz"],
        "description": "Obejmuje pradawne Góry Świętokrzyskie z gołoborzami kwarcytowymi (Łysica 614 m) oraz dolinę rzeki Kamiennej (Staropolski Okręg Przemysłowy).",
        "mnemonic": "Wyżyna Kielecka to Góry Świętokrzyskie, Łysica, gołoborza i rzeka Kamienna!",
        "hint": "Wokół Kielc, pomiędzy Wisłą a Niecką Nidziańską."
    },
    {
        "id": "niecka_nidzianska",
        "name": "Niecka Nidziańska",
        "category": "region",
        "belt": "wyzyny",
        "beltName": "Pas Wyżyn Polskich",
        "quadrant": "C",
        "quadrantName": "Południe / Centrum (C/SE)",
        "center": [50.50, 20.40],
        # Obniżenie wzdłuż Nidy między Wyżyną Krakowsko-Częstochowską a Kielecką
        "polygon": [
            [50.80, 19.85], [50.72, 20.45], [50.62, 20.95], [50.36, 20.89],
            [50.25, 20.50], [50.30, 20.05], [50.52, 19.80], [50.80, 19.85]
        ],
        "keyCities": ["Pińczów", "Busko-Zdrój", "Jędrzejów", "Kazimierza Wielka"],
        "description": "Obniżenie między Wyżyną Krakowsko-Częstochowską a Kielecką, w dolinie rzeki Nidy. Słynie ze złóż gipsu i uzdrowisk z wodami siarczkowymi.",
        "mnemonic": "Niecka Nidziańska leży W OBNAŻENIU (niecce) wzdłuż Nidy, pomiędzy Jurą a Kielcami – słynie z gipsu i Buska-Zdroju!",
        "hint": "Obniżenie terenu między Wyżyną Krakowsko-Częstochowską a Wyżyną Kielecką."
    },
    {
        "id": "wyzyna_lubelska",
        "name": "Wyżyna Lubelska",
        "category": "region",
        "belt": "wyzyny",
        "beltName": "Pas Wyżyn Polskich",
        "quadrant": "SE",
        "quadrantName": "Południowy Wschód (SE)",
        "center": [51.10, 22.70],
        "polygon": [
            [51.42, 21.97], [51.30, 22.88], [51.13, 23.47], [50.65, 23.50],
            [50.54, 22.72], [50.88, 21.85], [51.32, 21.95], [51.42, 21.97]
        ],
        "keyCities": ["Lublin", "Chełm", "Zamość", "Puławy", "Kazimierz Dolny", "Kraśnik"],
        "description": "Falista wyżyna pokryta grubą warstwą lessu z malowniczymi wąwozami (Kazimierz Dolny), uprawą chmielu i buraków oraz renesansowym Zamościem.",
        "mnemonic": "Wyżyna Lubelska = lessowe wąwozy w Kazimierzu Dolnym, Lublin i twierdza Zamość na wschód od Wisły!",
        "hint": "Na wschód od doliny środkowej Wisły, wokół Lublina i Zamościa."
    },
    {
        "id": "kotlina_sandomierska",
        "name": "Kotlina Sandomierska",
        "category": "region",
        "belt": "kotliny",
        "beltName": "Pas Kotlin Podkarpackich",
        "quadrant": "SE",
        "quadrantName": "Południowy Wschód (SE)",
        "center": [50.25, 21.80],
        "polygon": [
            [50.68, 21.75], [50.58, 22.06], [50.30, 22.70], [50.02, 22.68],
            [49.95, 21.60], [49.97, 20.43], [50.24, 20.73], [50.41, 21.36],
            [50.68, 21.75]
        ],
        "keyCities": ["Rzeszów", "Tarnobrzeg", "Stalowa Wola", "Tarnów", "Mielec", "Dębica"],
        "description": "Trójkątne zapadlisko podkarpackie u zbiegu Wisły i Sanu. Obejmuje doliny Wisłoki i Sanu oraz Puszczę Sandomierską.",
        "mnemonic": "Kotlina Sandomierska to wielki trójkąt u stóp Karpat, gdzie San i Wisłoka wpływają do Wisły!",
        "hint": "Trójkątne obniżenie na południowym wschodzie, pod Karpatami, wokół Rzeszowa."
    },
    {
        "id": "karpaty",
        "name": "Karpaty",
        "category": "region",
        "belt": "gory",
        "beltName": "Pas Gór (Karpaty)",
        "quadrant": "SE",
        "quadrantName": "Południe (SE/S)",
        "center": [49.50, 21.00],
        "polygon": [
            [49.75, 18.63], [49.82, 19.05], [49.74, 19.59], [49.97, 20.43],
            [49.95, 21.60], [49.78, 22.77], [49.30, 22.80], [49.00, 22.85],
            [49.15, 22.50], [49.35, 21.90], [49.40, 21.60], [49.35, 20.95],
            [49.38, 20.48], [49.18, 20.08], [49.57, 19.52], [49.50, 18.98],
            [49.75, 18.63]
        ],
        "keyCities": ["Zakopane", "Nowy Sącz", "Sanok", "Krosno", "Bielsko-Biała", "Krynica-Zdrój"],
        "description": "Potężny łańcuch młodych gór fałdowych ciągnący się wzdłuż całej południowo-wschodniej granicy Polski. Składa się z Karpat Zachodnich i Wschodnich.",
        "mnemonic": "Karpaty to cały południowy łańcuch górski: od Beskidu Śląskiego przez Tatry aż po Bieszczady!",
        "hint": "Cały południowy łuk górski wzdłuż granicy ze Słowacją i Ukrainą."
    },
    {
        "id": "tatry",
        "name": "Tatry",
        "category": "region",
        "belt": "gory",
        "beltName": "Pas Gór (Karpaty)",
        "quadrant": "SE",
        "quadrantName": "Południe (S)",
        "center": [49.27, 20.00],
        # Najwyższe skaliste pasmo alpejskie dokładnie na granicy wokół Zakopanego (wewnątrz granic Polski!)
        "polygon": [
            [49.32, 19.80], [49.34, 20.00], [49.32, 20.20], [49.22, 20.22],
            [49.19, 20.08], [49.20, 19.85], [49.32, 19.80]
        ],
        "keyCities": ["Zakopane", "Kościelisko", "Bukowina Tatrzańska"],
        "description": "Najwyższe góry Polski o rzeźbie alpejskiej (Rysy 2499 m n.p.m.). Skalisty masyw dokładnie pośrodku południowej granicy z Zakopanem i Morskim Okiem.",
        "mnemonic": "Tatry to najwyższe polskie góry alpejskie z Rysami i Zakopanem – skaliste serce na południowej granicy!",
        "hint": "Skrajne południe Polski pośrodku łuku Karpat wokół Zakopanego, najwyższe szczyty."
    },
    {
        "id": "pieniny",
        "name": "Pieniny",
        "category": "region",
        "belt": "gory",
        "beltName": "Pas Gór (Karpaty)",
        "quadrant": "SE",
        "quadrantName": "Południe (SE/S)",
        "center": [49.43, 20.42],
        # Wapienny pas skałkowy tuż na wschód od Tatr, wzdłuż przełomu Dunajca!
        # Wyraźny, łatwy do zaznaczenia obszar pomiędzy Tatrami a Beskidem Sądeckim
        "polygon": [
            [49.52, 20.22], [49.53, 20.48], [49.48, 20.65], [49.36, 20.62],
            [49.33, 20.38], [49.36, 20.22], [49.52, 20.22]
        ],
        "keyCities": ["Szczawnica", "Krościenko nad Dunajcem", "Czorsztyn", "Niedzica"],
        "description": "Malownicze wapienne pasmo skałkowe leżące TUŻ NA WSCHÓD OD TATR, słynące ze spływu tratwami Przełomem Dunajca i szczytu Trzy Korony.",
        "mnemonic": "Pieniny leżą TUŻ NA WSCHÓD OD TATR wzdłuż Dunajca – Trzy Korony i spływ tratwami!",
        "hint": "Tuż na wschód od Tatr, w dolinie rzeki Dunajec (Szczawnica, Trzy Korony)."
    },
    {
        "id": "beskidy_bieszczady",
        "name": "Beskidy / Bieszczady",
        "category": "region",
        "belt": "gory",
        "beltName": "Pas Gór (Karpaty)",
        "quadrant": "SE",
        "quadrantName": "Południe i Południowy Wschód (SE)",
        "center": [49.55, 21.20],
        # Beskidy rozciągają się wzdłuż CAŁEGO łuku karpackiego (od Beskidu Śląskiego/Żywieckiego na zachodzie, przez Gorce, Beskid Sądecki i Niski, aż po dzikie Bieszczady na skrajnym wschodzie!)
        "polygon": [
            [49.75, 18.63], [49.80, 19.20], [49.75, 19.65], [49.65, 20.50],
            [49.68, 21.50], [49.72, 22.40], [49.50, 22.65], [49.03, 22.85],
            [49.18, 22.45], [49.40, 21.60], [49.42, 20.95], [49.50, 20.65],
            [49.55, 20.48], [49.54, 20.20], [49.40, 19.70], [49.50, 18.98], [49.75, 18.63]
        ],
        "keyCities": ["Wisła", "Szczyrk", "Żywiec", "Krynica-Zdrój", "Dukla", "Ustrzyki Górne", "Cisna"],
        "description": "Potężny pas gór fliszowych ciągnący się od Beskidu Śląskiego i Żywieckiego na zachodzie, przez Beskid Sądecki i Niski, po Bieszczady na wschodzie ze źródłami rzeki San!",
        "mnemonic": "Beskidy tworzą szeroki łuk wzdłuż całej granicy karpackiej, a ich skrajny wschodni kraniec to Bieszczady ze źródłami Sanu!",
        "hint": "Ciągną się szerokim łukiem przez całą południową granicę od Wisły po Bieszczady na wschodzie."
    }
]
