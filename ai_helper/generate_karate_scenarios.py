import json
from pathlib import Path
from textwrap import indent


def generate_negative_payloads(base_payload: dict) -> list[tuple[str, dict]]:
    """
    Basit, kural tabanlı 'AI' benzeri yardımcı:
    - Eksik alan
    - Yanlış tip
    - Boş body
    """
    scenarios: list[tuple[str, dict]] = []

    # Eksik alan senaryoları
    for key in base_payload.keys():
        payload = base_payload.copy()
        payload.pop(key)
        scenarios.append((f"missing_{key}", payload))

    # Yanlış tip senaryoları (string ise sayı, sayı ise string vb.)
    for key, value in base_payload.items():
        wrong_value: object
        if isinstance(value, str):
            wrong_value = 123
        elif isinstance(value, (int, float)):
            wrong_value = "invalid_type"
        else:
            wrong_value = None
        payload = base_payload.copy()
        payload[key] = wrong_value
        scenarios.append((f"wrong_type_{key}", payload))

    # Boş body senaryosu
    scenarios.append(("empty_body", {}))

    return scenarios


def to_karate_json(obj: dict) -> str:
    """
    Python dict'i Karate'nin request gövdesi için uygun JSON string'e çevirir.
    """
    return json.dumps(obj, ensure_ascii=False)


def build_feature_content(endpoint: str, base_url: str, base_payload: dict) -> str:
    scenarios = generate_negative_payloads(base_payload)

    lines: list[str] = []
    lines.append("Feature: AI generated negative scenarios for ReqRes POST /users")
    lines.append("")
    lines.append("  Background:")
    lines.append(f"    * url '{base_url}'")
    lines.append(f"    * def endpoint = '{endpoint}'")
    lines.append("")

    for name, payload in scenarios:
        pretty_name = name.replace("_", " ")
        lines.append(f"  Scenario: Negative POST /users - {pretty_name}")
        lines.append("    Given path endpoint")
        lines.append(f"    And request {to_karate_json(payload)}")
        lines.append("    When method post")
        # ReqRes çoğu hatalı body'de yine de 201/200 dönebiliyor;
        # burada örnek olsun diye 400 bekliyoruz, isterseniz README'den kolayca değiştirebilirsiniz.
        lines.append("    Then status 400")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    """
    Basit kullanım:
      - Endpoint: api/users
      - Base URL: https://reqres.in
      - Örnek body: {\"name\": \"Nida\", \"job\": \"QA Engineer\"}
    """
    endpoint = "api/users"
    base_url = "https://reqres.in"
    base_payload = {"name": "Nida", "job": "QA Engineer"}

    feature_content = build_feature_content(endpoint, base_url, base_payload)

    # Karate test kaynak dizini altına kaydet
    base_dir = Path(__file__).resolve().parents[1] / "karate-project"
    out_dir = base_dir / "src" / "test" / "resources" / "features"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "ai_generated_scenarios.feature"
    out_file.write_text(feature_content, encoding="utf-8")

    print(f"AI generated feature written to: {out_file}")


if __name__ == "__main__":
    main()


