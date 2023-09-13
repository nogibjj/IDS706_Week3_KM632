import polars as pl
import matplotlib.pyplot as plt
import locale


def format_currency(value):
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    return locale.currency(value, grouping=True)


def find_mean(df):
    mean = format_currency(round(df["Loan Amount(in USD)"].mean()))
    return mean


def find_median(df):
    median = format_currency(round(df["Loan Amount(in USD)"].median()))
    return median


def find_std(df):
    std = format_currency(round(df["Loan Amount(in USD)"].std()))
    return std


def create_graph(df):
    country_expenses = df.group_by("School Country", maintain_order=True).agg(
        pl.sum("Loan Amount(in USD)").alias("Total Expenses")
    )
    x = country_expenses["School Country"]
    y = country_expenses["Total Expenses"]
    plt.bar(x, y, color="blue")
    plt.xlabel("School Country")
    plt.ylabel("Total Expenses")
    plt.title("Total Expenses by School Country")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("total_expenses_by_country.png")


def main():
    df = pl.read_excel("raw.xlsx")
    new_column_names = {
        "Эцэг /эх/-ийн нэр / Өөрийн нэр": "First and Last Name",
        "Суралцаж байгаа улс": "School Country",
        "Сургуулийн нэр": "School Name",
        "Мэргэжил": "Intended Major",
        "Суралцах хугацаа": "Study Duration(in years)",
        "Олгосон санхүүжил": "Loan Amount(in USD)",
    }
    df = df.rename(new_column_names)
    mean = find_mean(df)
    median = find_median(df)
    std = find_std(df)
    create_graph(df)
    print("Mean:", mean)
    print("Median:", median)
    print("Standard deviation:", std)


if __name__ == "__main__":
    main()
