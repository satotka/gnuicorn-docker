from influxdb import InfluxDBClient

def server(environ, start_response):
    print("1: influxdb client")
    client = InfluxDBClient(host='10.20.11.131',port=8086) # TODO: Change IP.

    print("2: influxdb switching database")
    client.switch_database('influxtest_erfanul')

    print("3: influxdb quering - connecting influxdb")
    result = client.query('select conversion_prediction from predicted_data limit 1')
        
    print("4: influxdb getting points")
    for point in result.get_points():
        conv = point['conversion_prediction']
    print(conv)

    data = b"Hello, Guicorn World!\n"
    print("5: replacing response")
    if conv:
        data = b"Hello, Influxdb!\n"

    print("6: starting response")
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])

    print("7: return response data")
    return iter([data])

if __name__ == '__main__':
    print("*** no using guniorn **** -- started")
    def mock_start_response(*args):
        print(args)

    server("", mock_start_response)

    print("*** no using guniorn **** -- completed")
