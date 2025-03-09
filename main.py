import os

print("\n Running Data Cleaning...")
os.system("python scripts/data_cleaning.py")

print("\n Running Data Analysis...")
os.system("python scripts/analysis.py")

print("\n Generating Visualisations...")
os.system("python scripts/visualisation.py")

print("\n✅ All tasks completed!")
