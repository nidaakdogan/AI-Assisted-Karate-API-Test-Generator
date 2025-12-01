## AI-Assisted Karate API Test Generator

**Kısa Özet (TR)**  
Karate ile yazılmış manuel senaryoları, Python tabanlı mini "AI" script'in ürettiği negatif senaryolarla birleştiriyor ve sonuçları tek bir dashboard ekranında görselleştiriyoruz.

**Short Summary (EN)**  
Manual Karate tests plus a lightweight Python helper that generates negative cases; everything is summarised on a minimal dashboard for quick sharing.

---

## Proje Yapısı / Project Structure

- `karate-project/` – Maven + Karate kaynakları  
  - `pom.xml`, `src/test/java/.../ReqResTest.java`, `src/test/resources/features/*.feature`
- `ai_helper/` – Python senaryo üreticisi (`generate_karate_scenarios.py`)
- `ui/` – Statik dashboard (`index.html`, `dashboard-data.json`, `build_dashboard_data.py`)

---

## Teknolojiler

- Java 17, Maven, Karate, JUnit 5
- Python 3.10+ (harici AI servisi olmadan kural tabanlı üretim)
- Vanilla HTML/CSS/JS ile tek sayfa dashboard

---

## Çalışma Adımları (PowerShell)

1. **Python ortamı**  
   ```powershell
   cd ai_helper
   pip install -r requirements.txt
   ```

2. **AI senaryolarını üret**  
   ```powershell
   py generate_karate_scenarios.py
   ```
   Çıktı: `karate-project/src/test/resources/features/ai_generated_scenarios.feature`

3. **Karate testlerini çalıştır**  
   ```powershell
   cd ..\karate-project
   mvn test
   ```

4. **Dashboard verisini güncelle**  
   ```powershell
   cd ..
   py ui\build_dashboard_data.py
   ```
   Komut, `ui/dashboard-data.json` dosyasını manuel sayısı, AI sayısı ve son PASS/FAIL özetiyle günceller.  
   - `manualScenarioCount` → `manual_*.feature` içindeki `Scenario:` satırlarının toplamı  
   - `aiScenarioCount` → `ai_generated_scenarios.feature` içindeki senaryolar  
   - `lastRun` → `karate-project/target/karate-reports/karate-summary-json.txt` mevcutsa PASS/FAIL bilgisi

5. **Dashboard’ı görüntüle**  
   - En pratik yol: `ui` klasörünü VS Code Live Server veya `npx serve ui` gibi basit bir statik sunucu ile açmak.  
   - Alternatif olarak tarayıcıda `ui/index.html` dosyasını açıp ekran görüntüsü alabilirsiniz.  
   - Kartlar:
     - Manuel senaryo sayısı (lacivert)
     - AI üretimli senaryo sayısı (yeşil)
     - Son test çalışması PASS/FAIL (kırmızı/yeşil rozet)

---

## English Quick Guide

1. `cd ai_helper && pip install -r requirements.txt`
2. `py generate_karate_scenarios.py`
3. `cd ..\karate-project && mvn test`
4. `cd .. && py ui\build_dashboard_data.py`
5. Open `ui/index.html` with any static server (Live Server, `npx serve ui`, etc.) and capture the dashboard.

---

## Özelleştirme / Customization

- `ai_helper/generate_karate_scenarios.py` içindeki `endpoint`, `base_url` ve `base_payload` değerlerini değiştirerek farklı API’ler için negatif senaryolar üretebilirsiniz.
- `Then status 400` satırlarını kendi API beklenen davranışına göre güncelleyebilirsiniz.
- Dashboard tasarımı sade tutuldu; isterseniz `ui/index.html` içinde renkleri ve kart düzenini güncelleyebilirsiniz.
NOT: ui/dashboard-data.json örnek bir veri setidir, kullanıcılar kendi ortamlarında py ui\build_dashboard_data.py komutuyla güncelleyebilir.