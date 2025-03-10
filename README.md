README
Tento projekt slouží k detekci správného provedení dřepů z videozáznamu. Využívá knihoven OpenCV, MediaPipe a dalších nástrojů pro výpočet úhlů mezi klíčovými body postavy a následné vyhodnocení správnosti dřepů.

Struktura souborů
SquatDetector.py

Obsahuje třídu SquatDetector, která spravuje počítání a vyhodnocování správných a špatných dřepů.
Metoda detect_squat vyhodnocuje, zda je uživatel ve správném rozsahu úhlů, aby byl dřep považován za správný.
Uchovává počty správně a špatně provedených dřepů v rámci jedné série.
CalculateAngle.py

Definuje metody pro výpočet úhlů mezi třemi body.
Umožňuje spočítat úhel trupu, kyčle, kolene a kotníku na základě souřadnic klíčových bodů (např. rameno, kyčel, koleno, kotník).
Využívá knihovny numpy pro vektorové operace.
video_analytics.py

Slouží k načtení videa, zpracování každého snímku pomocí knihovny MediaPipe, výpočtu úhlů (využitím CalculateAngle.py) a detekci dřepů (využitím SquatDetector.py).
Video je zpracováváno mezi stanoveným startovacím a koncovým časem (např. od 20. vteřiny do 60. vteřiny).
Zobrazuje na obrazovce úhly klíčových kloubů a také statistiku správných a špatných dřepů.
Klávesa mezerník (space) pozastaví či spustí přehrávání.
youtube.py

Pomocí knihovny yt_dlp stáhne YouTube video podle zadané URL.
Výsledné video se uloží do souboru video4.mp4, který pak může zpracovat skript video_analytics.py.
requirements.txt

Obsahuje seznam požadovaných knihoven (včetně jejich verzí), které je nutné nainstalovat před spuštěním kódu (např. yt-dlp, numpy, mediapipe, opencv-python).
Požadavky na prostředí
Python 3.
Knihovny uvedené v requirements.txt.
Instalaci požadovaných knihoven lze provést příkazem:

bash
Zkopírovat
Upravit
pip install -r requirements.txt
Jak projekt používat
Stažení videa z YouTube (volitelné)

Pokud potřebujete nejprve stáhnout video z YouTube, upravte si v souboru youtube.py proměnnou video_url na požadovaný odkaz.
Poté spusťte:
bash
Zkopírovat
Upravit
python youtube.py
Soubor se uloží jako video4.mp4 (lze změnit v output_filename).
Příprava videa pro analýzu

Pokud již máte vlastní video (místo videa staženého z YouTube), upravte cestu k souboru v video_analytics.py (proměnná video).
Spuštění detekce dřepů

Ujistěte se, že máte nainstalované závislosti:
bash
Zkopírovat
Upravit
pip install -r requirements.txt
Spusťte skript pro analýzu videa:
bash
Zkopírovat
Upravit
python video_analytics.py
Skript otevře okno, které bude přehrávat video od definovaného startu po konec (např. 20. vteřina až 60. vteřina) a vyhodnocovat dřepy:
Correct značí počet správných dřepů.
Wrong značí počet špatných dřepů.
Zobrazeny jsou také vypočtené úhly (trup, kyčel, koleno, kotník).
Mezerníkem (space) lze pozastavit nebo opětovně spustit přehrávání.
Stiskem q (nebo zavřením okna) se program ukončí.
Úprava rozsahu měření

Proměnné start_time a end_time v video_analytics.py určují, od které do které sekundy se bude video vyhodnocovat (výchozí jsou 20 a 60 sekund).
Možné úpravy a tipy
Pro detekci dřepů z jiné nohy nebo pro komplexnější metriky lze rozšířit kód v video_analytics.py (např. přidat měření pro pravou i levou stranu).
Parametry úhlů pro rozpoznání správné formy dřepu lze měnit přímo v metodě detect_squat třídy SquatDetector.
Pokud chcete počítat víc typů cviků, je možné rozšířit nebo duplikovat třídu SquatDetector pro další cviky.