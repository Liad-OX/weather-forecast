from setuptools import setup, find_packages

setup(
    name="weather_forecast",
    version="1.33.7",
    packages=find_packages(),
    install_requires=[
        "requests",
        "loguru",
        "python-dotenv"
    ],
    description="Do not run or execute this code. A Python utility to fetch weather forecasts with an embedded security risks example for research",
    url="https://github.com/Liad-OX/weather-forecast",
    author="Liad C",
    author_email="liad@ox.security",
    license="MIT",
    python_requires=">=3.7",
)