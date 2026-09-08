# Broken API — PB1_PD21-22

Šis ir mācību projekts PB1 modulī, kurā kursants saņem nepabeigtu un bojātu Python/Flask API projektu. Uzdevums ir soli pa solim to salabot, palaist, notestēt un sakārtot dokumentāciju.

---

## 📌 Projekta apraksts

Broken API ir vienkāršs Flask serveris, kas atgriež sveiciena ziņu JSON formātā. Projekts sākotnēji satur vairākas kļūdas:

- nepareizu JSON struktūru,
- bojātu Docker konfigurāciju,
- kļūdainu README,
- nepareizu requirements.txt,
- neizpildāmus testus.

Darba mērķis ir salabot projektu un nodrošināt, ka tas strādā gan lokāli, gan Docker konteinerī, kā arī iziet CI pipeline.

---

## 📦 Instalācija

### 1. Klonē repozitoriju

```bash
git clone <repo-adrese>
cd broken-api
```

### 2. Instalē Python atkarības

```bash
pip install -r requirements.txt
```

---

## ▶️ Programmas palaišana lokāli

```bash
python app.py
```

Serveris startēs uz:

```
http://localhost:5000
```

Sagaidāmais rezultāts:

```json
{"msg": "Hello PB1"}
```

---

## 🧪 Testu palaišana

```bash
pytest
```

Sagaidāmais rezultāts:

```
1 passed
```

---

## 🐳 Docker palaišana

### 1. Izveido Docker image

```bash
docker build -t broken-api .
```

### 2. Palaid konteineru

```bash
docker run -p 5000:5000 broken-api
```

API būs pieejams:

```
http://localhost:5000
```

---

## 🔄 CI pipeline

Repo satur GitHub Actions konfigurāciju:

- instalē atkarības,
- palaiž testus,
- pārbauda projekta veselību.

CI iziet, ja testi ir zaļi.

---

## 📚 Failu struktūra

```
broken-api/
│ app.py
│ utils.py
│ requirements.txt
│ test_app.py
│ Dockerfile
│ docker-compose.yml
│ README.md
└── .github/workflows/ci.yml
```

---

# 🔥 Pilni projekta faili (koda fragmenti)

## app.py
```python
from flask import Flask
from utils import get_message

app = Flask(__name__)

@app.route("/")
def home():
    return {"msg": get_message()}

if __name__ == "__main__":
    app.run(port=5000)
```

---

## utils.py
```python
def get_message():
    return "Hello PB1"
```

---

## test_app.py
```python
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["msg"] == "Hello PB1"
```

---

## requirements.txt
```text
flask>=2.2
pytest
requests
```

---

## Dockerfile
```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
```

---

## docker-compose.yml
```yaml
version: "3"

services:
  api:
    build: .
    ports:
      - "5000:5000"
```

---

## .github/workflows/ci.yml
```yaml
name: CI

on: push

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

---

## ✔ Autors

Deniss Cvetkovs  
Grupa 73346
