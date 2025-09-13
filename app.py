from suds.client import Client
wsdl_url ='http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL'

try:
    client =Client(wsdl_url)
    zip_code = '90210'
    response = client.service.getCityWeatherByZIP(zip_code)
    forecast = response.ForecastResult.Forecast[0]
    print(f"Weather forecast for  {response.GetCityWeatherByZIPResult.City}:")
    print (f"Date: {forecast.Date}")
    print (f"Day: {forecast.Description}")
    print (f"High: {forecast.Temperatures.High}°F", Low Temp: {forecast.Temperatures.Low}°F")

except Exception as e:
    print(f"An error occurred: {e}")
