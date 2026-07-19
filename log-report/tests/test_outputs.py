import json
from pathlib import Path


def test_report_exists_and_valid_json():
    """1. The output file /app/report.json must exist and contain valid JSON."""
    path = Path("/app/report.json")
    assert path.exists(), "report.json does not exist"
    try:
        with open(path) as f:
            json.load(f)
    except json.JSONDecodeError:
        assert False, "report.json is not valid JSON"


def test_total_requests():
    """2. The "total_requests" key must correctly specify the total number of requests."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("total_requests") == 6, f"Expected total_requests to be 6, got {data.get('total_requests')}"


def test_unique_ips():
    """3. The "unique_ips" key must correctly count the unique IP addresses."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("unique_ips") == 3, f"Expected unique_ips to be 3, got {data.get('unique_ips')}"


def test_top_path():
    """4. The "top_path" key must correctly identify the most frequently requested path."""
    with open("/app/report.json") as f:
        data = json.load(f)
    assert data.get("top_path") == "/index.html", f"Expected top_path to be '/index.html', got {data.get('top_path')}"
