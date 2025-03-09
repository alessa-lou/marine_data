import pandas as pd
import os

new_file_path = "data/cleaned_plastic_pollution.csv"

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file)

    df.fillna(0, inplace=True)

    if "year" in df.columns:
        df["year"] = pd.to_datetime(df["year"], format="%Y")

    df.rename(columns={"Plastic Waste (tonnes)": "plastic_waste_tonnes"}, inplace=True)

    df.to_csv(output_file, index=False)
    if os.path.exists(new_file_path):
        print(f"✅ Cleaned data saved to {output_file}")
    else:
        print("error")

if __name__ == "__main__":
    clean_data("data/plastic-waste-emitted-to-the-ocean-per-capita.csv", "data/cleaned_plastic_pollution.csv")
