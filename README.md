# Python-Project-PITP-MUET-Course
# main file 
from data_loader import read_csv
from data_cleaner import drop_missing, fill_missing
from data_analyzer import mean, median, maximum, minimum, most_popular_book
from data_visualizer import plot_histogram, plot_bar_chart
from data_report import data_summary

def main():
    filepath = "books.csv"
    data = read_csv(filepath)
    print("✅ Data Loaded Successfully!\n")

    # Clean data
    data = fill_missing(data, 'IssueCount', 10)
    data = drop_missing(data, 'IssueCount')

    # Report
    data_summary(data)

    # Analysis
    print("\n📈 Statistical Analysis:")
    print("Average Issues   :", round(mean(data, 'IssueCount'), 2))
    print("Median Issues    :", median(data, 'IssueCount'))
    print("Max Issues       :", maximum(data, 'IssueCount'))
    print("Min Issues       :", minimum(data, 'IssueCount'))

    title, count = most_popular_book(data)
    print(f"\n🏆 Most Popular Book: '{title}' with {count} issues.")

    # Visualization
    print("\nGenerating Charts...")
    plot_bar_chart(data)
    plot_histogram(data, 'IssueCount')

if __name__ == "__main__":
    main()

 # data Analyzer file
 def mean(data, column):
    values = [d[column] for d in data]
    return sum(values) / len(values)

def median(data, column):
    values = sorted([d[column] for d in data])
    n = len(values)
    mid = n // 2
    if n % 2 == 0:
        return (values[mid - 1] + values[mid]) / 2
    return values[mid]

def maximum(data, column):
    return max(d[column] for d in data)

def minimum(data, column):
    return min(d[column] for d in data)

def most_popular_book(data):
    top = max(data, key=lambda x: x['IssueCount'])
    return top['Title'], top['IssueCount']

# books csv file
BookID,Title,Author,IssueCount
1,Python Basics,John Smith,45
2,Data Science 101,Alice Brown,38
3,Machine Learning Guide,David Clark,60
4,Introduction to AI,Sarah Johnson,55
5,Web Development with JS,Emma Wilson,30
6,Database Management,Mark Lee,25

# data visulyzer
import matplotlib.pyplot as plt

def plot_bar_chart(data):
    titles = [d['Title'] for d in data]
    issues = [d['IssueCount'] for d in data]

    plt.bar(titles, issues)
    plt.xticks(rotation=45, ha='right')
    plt.title("Book Issue Count Comparison")
    plt.xlabel("Book Titles")
    plt.ylabel("Issue Count")
    plt.tight_layout()
    plt.show()

def plot_histogram(data, column):
    values = [d[column] for d in data]
    plt.hist(values, bins=5, edgecolor='black')
    plt.title(f"{column} Distribution")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.show()

# data cleaner
def drop_missing(data, column):
    return [d for d in data if d.get(column) not in (None, '', ' ')]

def fill_missing(data, column, value):
    for d in data:
        if not d.get(column):
            d[column] = value
    return data

# data report    
def data_summary(data):
    total = len(data)
    valid = sum(1 for d in data if d['IssueCount'] is not None)
    missing = total - valid
    print("✅ Data Summary Report:")
    print("Total Records     :", total)
    print("Valid Records     :", valid)
    print("Missing/Invalid   :", missing)

#  data loader
def read_csv(filepath):
    data = []
    with open(filepath, "r") as file:
        lines = file.readlines()[1:]  # skip header
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 4:
                book = {
                    "BookID": int(parts[0]),
                    "Title": parts[1],
                    "Author": parts[2],
                    "IssueCount": int(parts[3])
                }
                data.append(book)
    return data
