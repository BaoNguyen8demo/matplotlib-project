import matplotlib.pyplot as plt
import csv

def main():
    countries = []
    scores = []
    upper = []
    lower = []

    with open("World-happiness-report-2024.csv", encoding = "utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)

        for i, row in enumerate(reader):
            if i >= 15:
                break
            countries.append(row[0])
            scores.append(float(row[2]))
            upper.append(float(row[3]))
            lower.append(float(row[4]))

    error = []
    for score, lw, uw, in zip(scores, lower, upper):
        error.append([score - lw, uw - score])
    error = list(zip(*error))

    plt.figure(figsize = (10, 6))
    plt.bar(countries, scores, yerr = error, capsize = 5, color = "skyblue", edgecolor = "black")
    plt.xlabel("Country")
    plt.ylabel("Happiness Score")
    plt.title("Top 15 Happiest Countries (2024)")
    plt.xticks(rotation = 45, ha = "right")
    plt.grid(axis = "y", linestyle = "--", alpha = 0.7)
    plt.show()

    regions = {}
    region_counts = {}

    with open("World-happiness-report-2024.csv", encoding = "utf-8") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            country = row[0]
            region = row[1]
            score = float(row[2])

            if region not in regions:
                regions[region] = []
                region_counts[region] = 0

            regions[region].append(score)
            region_counts[region] += 1

    region_avg = {}
    for region, scores_list in regions.items():
        region_avg[region] = sum(scores_list) / len(scores_list)

    sorted_regions = sorted(region_avg.items(), key = lambda x: x[1], reverse = True)

    region_names = []
    for r in sorted_regions:
        region_names.append(r[0])

    region_scores = []
    for r in sorted_regions:
        region_scores.append(r[1])

    plt.figure(figsize = (12, 8))
    bars = plt.barh(region_names, region_scores, color = "lightgreen", edgecolor = "black")

    for i, region in enumerate(region_names):
        plt.text(0.5, i, f"(n = {region_counts[region]})", va = "center", fontsize = 9)

    for i, bar in enumerate(bars):
        plt.text(bar.get_width() + 0.05, bar.get_y() + bar.get_height()/2, f"{region_scores[i]:.2f}", va = "center")

    plt.xlabel("Average Happiness Score")
    plt.title("Average Happiness Score Across Regions (2024)")
    plt.grid(axis = "x", linestyle = "--", alpha = 0.7)
    plt.show()
    
if __name__ == "__main__":
    main()