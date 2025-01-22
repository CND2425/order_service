
# Order Service

## Beschreibung
Der **Order Service** ist ein zentraler Bestandteil einer Microservices-basierten E-Commerce-Anwendung. Er bietet eine REST-API zur Verwaltung von Bestellungen und unterstützt die Kommunikation zwischen Services mithilfe von RabbitMQ.

### Hauptfunktionen:
1. **Bestellung erstellen**: Erstellung neuer Bestellungen und Speicherung in der Datenbank.
2. **Bestellungen abrufen**: Anzeigen aller Bestellungen oder einer spezifischen Bestellung.
3. **Bestellungen aktualisieren**: Ändern von Status und Details bestehender Bestellungen.
4. **Bestellungen löschen**: Entfernen von Bestellungen aus der Datenbank.

Dieser Service wurde mit **FastAPI** entwickelt, verwendet **MongoDB** für die Speicherung und **RabbitMQ** für asynchrone Nachrichtenkommunikation.

---

## Technologien
1. **FastAPI**: Framework für die API-Entwicklung.
2. **MongoDB**: NoSQL-Datenbank für die Speicherung von Bestelldaten.
3. **RabbitMQ**: Message-Broker für die Synchronisierung zwischen Services.
4. **Docker**: Containerisierung des Services.
5. **GitHub Actions**: CI/CD-Pipeline zur Qualitätssicherung.

---

## Verwendete Endpunkte
### Order Endpoints:
1. **POST** `/orders/` - Erstellt eine neue Bestellung.
2. **GET** `/orders/{id}` - Ruft eine spezifische Bestellung ab.
3. **GET** `/orders/` - Listet alle Bestellungen auf.
4. **GET** `/orders/me` - Ruft Bestellungen eines Benutzers ab.

---

## Installation und Verwendung
### Voraussetzungen
- **Python 3.9+**
- **Docker** und **Docker Compose**

### Lokale Ausführung
- **Repository klonen**:
  ```bash
  git clone <REPOSITORY_URL>
  cd order_service
  ```

- **Virtuelle Umgebung erstellen und aktivieren**:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Auf Windows: venv\Scripts\activate
  ```

- **Abhängigkeiten installieren**:
  ```bash
  pip install -r requirements.txt
  ```

- **Service starten**:
  ```bash
  uvicorn app.main:app --host 0.0.0.0 --port 8080
  ```

### Docker-Ausführung
- **Docker-Image erstellen und starten**:
  ```bash
  docker build -t order_service .
  docker run -p 8080:8080 order_service
  ```

- **Alternativ mit Docker Compose** (aus dem Compose-Repository):
  ```bash
  docker-compose up -d
  ```

### API-Dokumentation
FastAPI bietet eine automatisch generierte API-Dokumentation:
- Swagger UI: [http://localhost:8080/docs](http://localhost:8080/docs)
- ReDoc: [http://localhost:8080/redoc](http://localhost:8080/redoc)

---

## Datenbank
1. **MongoDB** wird verwendet, um Bestelldaten persistent zu speichern.
2. Standardmäßig verbindet sich der Service zu `mongodb://localhost:27017`.
3. Anpassung der URL über Umgebungsvariablen:
   ```bash
   MONGODB_URL=mongodb://<host>:<port>
   ```

---

## Nachrichtenkommunikation
1. **RabbitMQ** wird für die Nachrichtenübermittlung über Bestelländerungen verwendet.
2. Anpassung der RabbitMQ-URL über Umgebungsvariablen:
   ```bash
   RABBITMQ_URL=<rabbitmq_host>
   ```

---

## Tests
1. **Testumgebung installieren**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Tests ausführen**:
   ```bash
   pytest tests/
   ```

---

## CI/CD
1. Der Service verwendet **GitHub Actions**, um Tests und Linting automatisch bei jedem Commit auszuführen.
2. Die Konfiguration befindet sich in `.github/workflows/ci.yml`.

---

## Umgebungsvariablen
1. `MONGODB_URL`: MongoDB-Verbindungs-URL.
2. `RABBITMQ_URL`: RabbitMQ-Verbindungs-URL.
3. `SECRET_KEY`: Geheimer Schlüssel für sicherheitskritische Vorgänge.
4. `ACCESS_TOKEN_EXPIRE_MINUTES`: Token-Gültigkeitsdauer (in Minuten).

---

