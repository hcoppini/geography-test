# 🇵🇱 Polska: Regiony i Rzeki — Trener Mapy Geograficznej

Interaktywna, w 100% offline aplikacja webowa do nauki i błyskawicznego zapamiętywania **24 krain geograficznych (regionów fizycznogeograficznych)** oraz **19 rzek i dopływów** Polski (+ Wisła i Odra) przed sprawdzianem z geografii.

Aplikacja dostępna bezpośrednio w przeglądarce — zero zewnętrznych zależności, zero serwerów, działa również offline!

---

## 🌟 Główne Funkcje

1. **Sesja Egzaminacyjna (86 pytań / 2x każdy obiekt)**:
   - Dokładnie 86 pytań w pełnej sesji ($43 \text{ obiekty} \times 2 = 86$).
   - Inteligentny algorytm tasowania (Fisher-Yates) z blokadą sąsiedztwa gwarantuje, że ten sam obiekt nigdy nie pojawi się dwa razy z rzędu.
   - Pasek postępu na żywo (`Pytanie X / 86`) oraz licznik punktów i skuteczności.
   - Końcowy raport z oceną szkolną (od 4 do 6), listą błędów, przypomnieniem mnemoników oraz przyciskiem do powtórzenia samych pomyłek.

2. **Ochrona przed missclickiem (Wybór + Zatwierdzenie SPACJĄ)**:
   - **Krok 1**: Kliknięcie na mapie tylko zaznacza obiekt na błękitno (`Wybrano: [Nazwa]`). Możesz klikać dowolną liczbę razy i poprawiać wybór bez utraty punktów!
   - **Krok 2**: Zatwierdzenie odpowiedzi następuje dopiero po wciśnięciu klawisza **SPACJA** (lub kliknięciu przycisku).
   - **Krok 3**: Kolejne wciśnięcie **SPACJI** natychmiast przenosi do następnego pytania.

3. **Dokładna Geografia i Wyraźne Granice**:
   - **Pieniny**: powiększone i wyodrębnione w dolinie Dunajca, renderowane na najwyższej warstwie (brak kolizji z Beskidami i rzeką).
   - **Wyżyna Śląska vs. Jura (Wyżyna Krakowsko-Częstochowska)**: ułożone poprawnie obok siebie (Śląsk na zachodzie, Jura jako skośne pasmo na wschód od Częstochowy po Kraków).
   - **Karpaty**: Beskidy wzdłuż całego łuku granicy południowej z Bieszczadami u źródeł Sanu; Tatry jako najwyższy masyw w środku granicy.
   - **Węzły rzeczne**: Bug wpada do Narwi w Jeziorze Zegrzyńskim, Narew do Wisły pod Modlinem, Wkra do Narwi, a Skrwa bezpośrednio do Wisły pod Płockiem.

4. **Widok Mapy Konturowej (SVG) oraz Satelitarnej (Leaflet)**:
   - Domyślna, szkolna mapa wektorowa SVG ze stabilnym kadrem całej Polski (brak uciążliwego automatycznego zoomowania).
   - Wysokorozdzielcza mapa satelitarna **Esri World Imagery (ArcGIS)**, Google Satellite oraz CARTO Voyager.

5. **Mnemoniki i Zasady Pamięciowe**:
   - Każdy obiekt posiada dedykowaną wskazówkę pamięciową (np. *„Kamienna tłucze Skarżysko-Kamienną i Starachowice pod Górami Świętokrzyskimi”*).

---

## 🚀 Jak uruchomić

### 1. Lokalnie (w przeglądarce):
Wystarczy dwukrotnie kliknąć plik `index.html` (lub na systemie Windows uruchomić `Uruchom_Mape_Polski.bat`). Nie wymaga instalacji żadnych programów ani serwera.

### 2. Przez GitHub Pages:
1. W repozytorium przejdź do zakładki **Settings** ➔ **Pages**.
2. W sekcji **Branch** wybierz gałąź `main` (lub `master`) oraz katalog `/ (root)`.
3. Kliknij **Save**. Twoja strona będzie dostępna publicznie pod adresem:
   `https://hcoppini.github.io/geography-test/`

---

## ⌨️ Skróty Klawiszowe

- **Spacja**: Zatwierdzenie wyboru na mapie / Przejście do następnego pytania
- **1, 2, 3, 4**: Wybór odpowiedzi w quizie wyboru 1 z 4
- **H**: Pokaż podpowiedź geograficzną i ćwiartkę
- **R**: Pokaż prawidłowe położenie na mapie (Reveal)
- **M**: Przełącz widok (Mapa wektorowa SVG / Satelita)
- **L**: Włącz/wyłącz podpisy obiektów na mapie

---

## 📄 Licencja
Projekt stworzony do celów edukacyjnych i przygotowania do sprawdzianu z geografii Polski.
