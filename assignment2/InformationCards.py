import requests
import streamlit as st

response = requests.get("https://restcountries.com/v3/all")

if response.status_code == 200:
    dataa = response.json()
    print(dataa)
else:
    print("Invalid API key")

def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3/name/{country_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data.get("capital", ["No capital information available"])[0]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data.get("currencies", "No currency information available")
        region = country_data["region"]
        return name, capital, population, area, currency, region
    else:
        return None

def main():
    st.title("Country Information App")
    country_name = st.text_input("Enter country name: ")

    if country_name:
        country_info = fetch_country_data(country_name)
        if country_info:
            name, capital, population, area, currency, region = country_info
            st.subheader("Country Information")
            st.write(f"**Name**: {name}")
            st.write(f"**Capital**: {capital}")
            st.write(f"**Population**: {population}")
            st.write(f"**Area**: {area} square kilometers")
            st.write(f"**Currency**: {currency}")
            st.write(f"**Region**: {region}")
        else:
            st.write("Country data not found")
            st.error("Error: Country data not found")

if __name__ == "__main__":
    main()
