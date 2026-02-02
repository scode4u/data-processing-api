from fastapi import APIRouter, status

def test_aggregate_analytics(client):

    csv_content = "x,y\n1,10\n2,20\n3,30\n"

    upload_response = client.post(
        "/upload/",
        files = {"file" : ("test.csv",csv_content, "text/csv")}
    )
    assert upload_response.status_code == 200
    # upload the file and return the status is succeedd

    response = client.get(
        "/analytics/aggregate",
        params = {"column":"y","operation":"sum"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["column"] == "y"
    assert data["operation"] == "sum"
    assert data["value"] == 60.0