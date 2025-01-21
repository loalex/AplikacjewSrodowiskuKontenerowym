FROM python:3.10-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj kod do obrazu
COPY script.py /app/

# Polecenie główne
ENTRYPOINT ["python", "/app/script.py"]

# Domyślne argumenty
CMD ["default_arg1", "default_arg2"]
