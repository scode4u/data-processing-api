from app.main import app
def test_upload_csv_success(client):
    csv_content = "a,b,c\n1,2,3\n4,5,6\n"

    response = client.post(
        "/upload/",
        files={"file": ("test.csv", csv_content, "text/csv")}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["rows"] == 2
    assert data["columns"] == ["a","b","c"]
