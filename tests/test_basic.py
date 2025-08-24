import pytest
from fastapi.testclient import TestClient
from main import app
from code_quality_checker import analyze_code

client = TestClient(app)

# -----------------------------
# בדיקות ל-CodeQualityChecker
# -----------------------------

def test_empty_file():
    alerts, func_lengths = analyze_code("")
    assert alerts == []
    assert func_lengths == []

def test_function_with_docstring():
    code = '''
def foo():
    """This is a docstring"""
    x = 1
    return x
'''
    alerts, func_lengths = analyze_code(code)
    assert alerts == []
    assert func_lengths == [2]

def test_function_missing_docstring():
    code = '''
def foo():
    x = 1
    return x
'''
    alerts, func_lengths = analyze_code(code)
    assert any("missing a docstring" in alert for alert in alerts)
    assert func_lengths == [2]

# -----------------------------
# בדיקות ל-FastAPI endpoints
# -----------------------------

def test_analyze_endpoint(tmp_path):
    file_path = tmp_path / "sample.py"
    file_path.write_text("def foo():\n    pass\n")

    with open(file_path, "rb") as f:
        response = client.post("/analyze", files={"files": (file_path.name, f, "text/plain")})

    assert response.status_code == 200
    json_data = response.json()
    assert "sample.py" in json_data["results"]
    assert isinstance(json_data["results"]["sample.py"], int)

def test_alerts_endpoint(tmp_path):
    file_path = tmp_path / "sample.py"
    file_path.write_text("def foo():\n    pass\n")

    with open(file_path, "rb") as f:
        response = client.post("/alerts", files={"files": (file_path.name, f, "text/plain")})

    assert response.status_code == 200
    json_data = response.json()
    assert "sample.py" in json_data["alerts"]
    assert isinstance(json_data["alerts"]["sample.py"][0], list)
