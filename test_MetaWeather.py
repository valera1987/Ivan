import requests

def test_MetaWeather_API():
    resp = requests.get('https://www.metaweather.com//api/location/search/?query=minsk')
    assert resp.status_code == 200 

    resp_json = resp.json()
    assert resp_json[0]['latt_long'] == '53.90255,27.563101'
    assert resp_json[0]['woeid'] == 834463
    assert resp_json[0]['location_type'] == 'City' 
    assert resp_json[0]['title'] == 'Minsk' 
