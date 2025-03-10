# Detekce správného provedení dřepů

Tento projekt slouží k detekci správného provedení dřepů z videozáznamu. Využívá knihoven **OpenCV**, **MediaPipe** a dalších nástrojů pro výpočet úhlů mezi klíčovými body postavy a následné vyhodnocení správnosti dřepů.

## Struktura souborů

### SquatDetector.py
- Obsahuje třídu **SquatDetector**, která spravuje počítání a vyhodnocování správných a špatných dřepů.  
- Metoda `detect_squat` vyhodnocuje, zda je uživatel ve správném rozsahu úhlů, aby byl dřep považován za správný.  
- Uchovává počty správně a špatně provedených dřepů v rámci jedné série.  

### CalculateAngle.py
- Definuje metody pro výpočet úhlů mezi třemi body.  
- Umožňuje spočítat úhel trupu, kyčle, kolene a kotníku na základě souřadnic klíčových bodů (např. rameno, kyčel, koleno, kotník).  
- Využívá knihovny **numpy** pro vektorové operace.  

### video_analytics.py
- Slouží k načtení videa, zpracování každého snímku pomocí knihovny **MediaPipe**, výpočtu úhlů (využitím `CalculateAngle.py`) a detekci dřepů (využitím `SquatDetector.py`).  
- Video je zpracováváno mezi stanoveným startovacím a koncovým časem (např. od 20. vteřiny do 60. vteřiny).  
- Zobrazuje na obrazovce úhly klíčových kloubů a také statistiku správných a špatných dřepů.  
- Klávesa **mezerník (space)** pozastaví či spustí přehrávání.  

### youtube.py
- Pomocí knihovny **yt_dlp** stáhne YouTube video podle zadané URL.  
- Výsledné video se uloží do souboru `video4.mp4`, který pak může zpracovat skript `video_analytics.py`.  

### requirements.txt
- Obsahuje seznam požadovaných knihoven (včetně jejich verzí), které je nutné nainstalovat před spuštěním kódu (např. `yt-dlp`, `numpy`, `mediapipe`, `opencv-python`).
