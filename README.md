# Download-organizer

Acest script în Python monitorizează folderul de descărcări și mută automat fișierele în subfoldere bazate pe extensia lor (PDF, DOCX, PNG etc.).

## Caracteristici
- Monitorizează în timp real folderul `Downloads`
- Mută fișierele automat în subfoldere în funcție de extensie
- Funcționează în fundal și organizează fișierele imediat ce sunt descărcate

## Instalare
1. Asigură-te că ai Python instalat (versiunea 3.x).
2. Instalează pachetul `watchdog`, necesar pentru monitorizarea fișierelor:
   ```bash
   pip install watchdog
   ```
3. Salvează scriptul Python (`auto_move.py`) într-un folder la alegere.

## Utilizare
1. Rulează scriptul:
   ```bash
   python auto_move.py
   ```
2. Lasă-l să ruleze în fundal. Când descarci un fișier, acesta va fi mutat automat într-un subfolder corespunzător.

## Personalizare
- Poți schimba folderul de descărcări modificând variabila `DOWNLOADS_FOLDER`.
- Folderul de destinație poate fi ajustat prin `DESTINATION_FOLDER`.



