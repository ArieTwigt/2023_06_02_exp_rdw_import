import requests
import pandas as pd

def import_cars_brand(brand):

    # uppercase the brand
    brand_upper = brand.upper()

    # define the endpoint
    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={brand_upper}"

    # execute the request
    response = requests.get(endpoint)

    # get the data
    data = response.json()

    if len(data) == 0:
        print(f"No data for {brand}")
        return None

    # convert the data to a pandas data frame
    data_df = pd.DataFrame(data)

    # export the data frame
    data_df.to_csv(f"{brand}_export.csv", sep=";", index=False)

    print(f"✅ Succesfully imported {brand}")