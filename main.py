from custom_modules.import_functions import import_cars_brand

selected_brands = input("Brands to import (seperate by whitespace ' '):\n")

selected_brands_list = selected_brands.split(" ")

for brand in selected_brands_list:
    print(f"🚗Importing {brand}")
    import_cars_brand(brand)