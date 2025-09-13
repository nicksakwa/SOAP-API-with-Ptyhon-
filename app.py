from suds.client import Client

# The URL to the WSDL file of the web service.
# This one provides weather information.
wsdl_url = 'http://wsf.cdyne.com/WeatherWS/Weather.asmx?WSDL'

try:
    # Create a new SOAP client object with the WSDL URL.
    client = Client(wsdl_url)

    # Use a method from the web service.
    # The 'GetCityForecastByZIP' method takes a ZIP code as an argument.
    zip_code = '90210'
    response = client.service.GetCityForecastByZIP(zip_code)

    # Access the data from the SOAP response.
    # The structure of the response is defined in the WSDL.
    forecast_info = response.ForecastResult.Forecast[0]

    # Print the city and the weather forecast for the first day.
    print(f"Weather forecast for {response.GetCityForecastByZIPResult.City}:")
    print(f"Date: {forecast_info.Date}")
    print(f"Day: {forecast_info.Desciption}")
    print(f"High Temp: {forecast_info.Temperatures.MorningLow}°F, Low Temp: {forecast_info.Temperatures.MorningLow}°F")

except Exception as e:
    print(f"An error occurred: {e}")