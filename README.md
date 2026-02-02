# Schwimmbad Wien: Metric
This small project allows to collect data and create metrics on how many people are in the swimming pool.
It is gathering numbers once a minute from a website and stores it in this repository.

This is a test graph:

```mermaid
---
config: 
  xyChart: 
    width: 900 
    height: 600 
    showDataLabel: true
    showTitle: false
  themeVariables: 
    xyChart:
      backgroundColor: "#999999"
      titleColor: "#ff0000"
      xAxisLineColor: "#ff0000"
      yAxisLineColor: "#ff0000"
---
xychart-beta
  title "Stadthallenbad"
  x-axis ["10:14", "10:15", "10:16", "10:17", "10:18", "10:19", "10:20", "10:18"]
  y-axis "People"
  line [60,60,59,62,61,61,61,61]
```
