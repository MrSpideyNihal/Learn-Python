"""Temperature converter."""

def convert_temperature(celsius):
    """Return Fahrenheit equivalent of Celsius temperature."""
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C is {convert_temperature(celsius)}°F")
