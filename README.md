## AI-Assisted Karate API Test Generator

Karate ile yazılmış manuel senaryoları, Python tarafında otomatik üretilen negatif Gherkin senaryolarıyla birleştiriyor ve mini bir web dashboard’ında PASS/FAIL özetini gösteriyorum.

---

## Proje Yapısı

- `karate-project/` – Maven + Karate kaynakları (`ReqResTest.java`, manuel feature’lar, JUnit runner)
- `ai_helper/` – `generate_karate_scenarios.py` script’i negatif senaryoları üretip `.feature` olarak kaydeder.
- `ui/` – `build_dashboard_data.py` + `index.html` ile statik dashboard.

---

## Hızlı Kullanım (PowerShell)

```powershell
cd ai_helper
pip install -r requirements.txt
py generate_karate_scenarios.py    # ai_generated_scenarios.feature güncellenir

cd ..\karate-project
mvn test                           # manuel + AI senaryoları birlikte koşar

cd ..
py ui\build_dashboard_data.py      # ui/dashboard-data.json güncellenir
```

Dashboard’ı görmek için `ui` klasöründe basit bir sunucu aç (ör. `py -m http.server 8000`) ve `http://localhost:8000/index.html` adresini aç. Kartlarda manuel sayısı, AI sayısı ve PASS/FAIL özeti yer alır.

---

## Özelleştirme

- `generate_karate_scenarios.py` içinde `endpoint`, `base_url`, `base_payload` değerlerini değiştirerek farklı API’ler için negatif senaryolar türetebilirsin.
- `Then status 400` satırlarını API’nin gerçek beklenen davranışına göre güncelle.
- Dashboard tasarımını `ui/index.html` üzerinden düzenleyebilirsin.

> NOT: `ui/dashboard-data.json` örnek bir veri setidir; kullanıcılar kendi ortamlarında `py ui\build_dashboard_data.py` komutuyla güncelleyebilir.
