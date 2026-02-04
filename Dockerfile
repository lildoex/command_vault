# 1. Základní obraz: Použijeme lehký Python na Linuxu
FROM python:3.11-slim

# 2. Nastavení pracovního adresáře uvnitř kontejneru
WORKDIR /app

# 3. Zkopírování seznamu knihoven a jejich instalace
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Zkopírování celého tvého kódu do kontejneru
COPY . .

# 5. Port, na kterém aplikace poběží
EXPOSE 5000

# 6. Příkaz pro spuštění aplikace
CMD ["python", "app.py"]