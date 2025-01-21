# Używamy obrazu Python jako bazy
FROM python:3.10-slim

# Ustawiamy katalog roboczy
WORKDIR /app

# Kopiujemy plik script.py do katalogu roboczego
COPY script.py .

# Dodajemy archiwum tar i rozpakowujemy je automatycznie
ADD archive.tar .

# Kopiujemy katalog data do /app/data
COPY data /app/data

# Uruchamiamy skrypt Python
CMD ["python", "script.py"]
