# Learning Notes: Data Manipulation with Python CSV and Pandas

This document summarizes key concepts, troubleshooting experiences, and technical insights gained while working with the native Python `csv` library and the `pandas` library.

---

## 1. Native Python `csv` Library

### Understanding the `csv.reader` Object
When printing a `csv.reader` instance directly, Python outputs a reference similar to `<_csv.reader object at 0x...>` rather than the actual file contents. 
* **Reason:** The `csv.reader` function creates an iterable object designed to read data row by row, minimizing memory usage.
* **Solution:** To access or display the actual data, you must iterate through the object using a loop or convert it into a standard list.

```python
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # Approach 1: Iteration
    for row in data:
        print(row)
        
    # Approach 2: List Conversion (for small datasets)
    # data_list = list(data)