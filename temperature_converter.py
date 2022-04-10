"""Temperature converter."""
import math

def convert_temperature(celsius):
    """Convert Celsius to Fahrenheit or Kelvin."""
    return celsius * 9/5 + 32, celsius + 273.15

if __name__ == "__main__":
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit, kelvin = convert_temperature(celsius)
            print(f"Fahrenheit: {fahrenheit:.2f}", f"Kelvin: {kelvin:.2f}"`
        except ValueError:
            print("Invalid input. Try again!")