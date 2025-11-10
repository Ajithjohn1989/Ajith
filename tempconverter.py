class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @classmethod
    def print_conversion(cls, celsius):
        fahrenheit = cls.celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C = {fahrenheit}°F")
TemperatureConverter.print_conversion(25)