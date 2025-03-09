import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_plastic_trends(file):
    df = pd.read_csv(file)

    total_plastic = df["Mismanaged plastic waste to ocean per capita (kg per year)"].sum()

    plt.figure(figsize=(12, 6))
    
    sns.lineplot(x=df["Entity"], y=df["Mismanaged plastic waste to ocean per capita (kg per year)"], marker="o", label="Per Capita Waste")
    
    plt.axhline(y=total_plastic, color='red', linestyle='--', label="Total Plastic Pollution")

    plt.title("Global Plastic Waste By Country")
    plt.xlabel("Country")
    plt.ylabel("Plastic Waste (kgs)")
    plt.xticks(rotation=45, ha='right')
    plt.legend()


    plt.savefig("Visualisations/plastic_per_country.png")
    plt.show()
    plt.close() 


if __name__ == "__main__":
    plot_plastic_trends("data/cleaned_plastic_pollution.csv")
