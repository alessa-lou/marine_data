import pandas as pd

def analyze_data(file):
    df = pd.read_csv(file)

    print("\n Data Overview:")
    print(df.describe())

    total_plastic_in_year = df.groupby("Year")["Mismanaged plastic waste to ocean per capita (kg per year)"].sum()
    print(f"Total plastic Waste By Year: {int(total_plastic_in_year.iloc[0])}kg")

if __name__ == "__main__":
    analyze_data("data/cleaned_plastic_pollution.csv")
