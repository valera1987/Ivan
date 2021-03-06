import requests

def test_location_day():
    resp = requests.get('https://www.metaweather.com//api/location/834463/2018/8/2/')
    assert resp.status_code == 200 

    resp_json = resp.json()
    assert resp_json[0]['predictability'] == 70
    assert resp_json[0]['visibility'] == 9.649894615445795
    assert resp_json[0]['humidity'] == 57 
    assert resp_json[0]['air_pressure'] == 1006.6 
    assert resp_json[0]['wind_direction'] == 103 
    assert resp_json[0]['wind_speed'] == 1.797998753943636 
    assert resp_json[0]['the_temp'] == 27 
    assert resp_json[0]['id'] == 6276757132935168 
    assert resp_json[0]['weather_state_name'] == 'Light Cloud' 
    assert resp_json[0]['weather_state_abbr'] == 'lc' 
    assert resp_json[0]['wind_direction_compass'] == 'ESE' 
    assert resp_json[0]['created'] == '2018-08-02T22:37:40.658750Z' 
    assert resp_json[0]['applicable_date'] == '2018-08-02' 
    assert resp_json[0]['min_temp'] == 16.575 
    assert resp_json[0]['max_temp'] == 27.94 








  
