import matplotlib.pyplot as plt
import pandas as pd

def create_year_boxplot_from_csv(csv_filepath, output_svg_filepath):
    """
    Creates a box and whisker plot of years from dates in the 8th column of a CSV.

    Args:
        csv_filepath (str): Path to the input CSV file.
        output_svg_filepath (str): Path to save the output SVG file.
    """
    try:
        df = pd.read_csv(csv_filepath, header=None)
        dates = pd.to_datetime(df.iloc[:, 7], format='%Y-%m-%d', errors='coerce')
        years = dates.dt.year.dropna()
        boxplot("DOB Histogram of Employee Population", "YOB", "people_boxplot.svg")
    except FileNotFoundError:
        print(f"Error: CSV file not found at {csv_filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

def boxplot(title, xlabel, outpath, data):
    plt.figure(figsize=(8, 6))
    plt.boxplot(data, vert=False)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.savefig(outpath, format='svg')
    plt.close()

csv_file = "people.csv"
svg_file = "people_boxplot.svg"

create_year_boxplot_from_csv(csv_file, svg_file)