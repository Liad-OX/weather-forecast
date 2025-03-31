from setuptools import setup, find_packages

setup(
    name="weather_forecast",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "loguru",
        "python-dotenv"
    ],
    description="A Python utility to fetch weather forecasts with an embedded security research example - do not run or execute this code.",
    url="https://github.com/your-username/weather-forecast",
    author="Liad",
    author_email="[do-not-run-this-code]@example.com",
    license="MIT",
    python_requires=">=3.7",
)