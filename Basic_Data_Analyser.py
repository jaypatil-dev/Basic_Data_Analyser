import numpy as np
number_list_str = input("Enter your data points (e.g., 10, 20, 30, 40): ")
number_list = number_list_str.split(",")
data = [float(num) for num in number_list]
data_array = np.array(data)

def analyze_data(data):
    analysis = {}
    analysis['mean'] = np.mean(data)
    analysis['median'] = np.median(data)
    analysis['std_dev'] = np.std(data)
    analysis['var'] = np.var(data)
    analysis['min'] = np.min(data)
    analysis['max'] = np.max(data)

    return analysis
results = analyze_data(data_array)
print(f"Mean (Average): {results['mean']:.2f}")
print(f"Median: {results['median']:.2f}")
print(f"Standard Deviation: {results['std_dev']:.2f}")
print(f"Variance: {results['var']:.2f}")
print(f"Minimum: {results['min']:.2f}")
print(f"Maximum: {results['max']:.2f}")