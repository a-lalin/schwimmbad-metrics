# 🏊 Stadthallenbad Vienna - Live Pool Capacity Monitor

**Real-time monitoring system for Vienna's Stadthallenbad swimming pool occupancy**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/yourusername/schwimmbad-metrics)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Workflow Status](https://img.shields.io/badge/Workflow-Active-brightgreen)]()
[![Update Frequency](https://img.shields.io/badge/Updates-Minutely-blue)]()

## 📊 Live Dashboard

**Current Pool Occupancy:** [View Live Chart](./graphs/metric_last_hour.md)

The chart updates automatically every minute with the latest visitor data.

## 🌟 About This Project

This automated system monitors and visualises the occupancy levels of Vienna's Stadthallenbad swimming pool. While the pool doesn't provide a public API for real-time visitor counts, this project demonstrates how such a monitoring system could work, with simulated data collection that can be easily replaced with actual data sources.

### 🔄 How It Works

1. **Data Collection** (Every minute (in ver. 1.0))
   - Simulates visitor count collection
   - Stores data in organised JSON files
   - Handles duplicates and errors gracefully

2. **Automated Processing** (Every hour)
   - Generates visual charts of the last hour's data
   - Creates Mermaid.js diagrams for easy embedding
   - Updates the live dashboard automatically

3. **Visualization** (Always available)
   - Interactive line charts showing occupancy trends
   - Color-coded for easy readability
   - Responsive design for all devices

## 📁 Project Structure

```
schwimmbad-metrics/
├── .github/workflows/           # GitHub Actions automation
│   ├── update-logs.yml          # Runs every minute to collect data
│   └── generate-chart.yml       # Runs every hour to update charts
├── code/                        # Source code
│   ├── update_logs.py           # Data collection script
│   └── generate_chart.py        # Chart generation script
├── logs/                        # Historical data (automatically maintained)
│   └── YYYY-MM-DD/              # Organized by date
├── graphs/                      # Generated visualizations
│   └── metric_last_hour.md      # Always-updated live chart
└── README.md                    # This documentation
```

## 📈 Understanding the Data

### Data Format
Each data point includes:
- **Timestamp**: Exact minute of measurement
- **People Amount**: Collected from official [Twitch Video](https://www.twitch.tv/wienersportstaetten)

### Chart Features
- **Real-time updates**: Chart refreshes every hour
- **Historical context**: Shows last 60 minutes of data
- **Zero-data handling**: Graceful display even when no data is available
- **Consistent scaling**: Y-axis always shows 0-100 for comparison

## 🤝 Contributing

This project is open for contributions! Areas where you can help:

1. **Real data integration**: Connect to actual pool occupancy systems
2. **Enhanced visualizations**: Additional chart types and metrics
3. **Mobile optimization**: Better display on smartphones
4. **Historical analysis**: Long-term trend visualization
5. **Multi-pool support**: Expand to other Vienna swimming pools

### Quick Start for Contributors
1. Fork the repository
2. Test the workflow by enabling GitHub Actions
3. Submit a pull request with your improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- **Stadthallenbad Vienna**: For inspiring this monitoring solution
- **Mermaid.js**: For the excellent charting library
- **GitHub Actions**: For the powerful automation platform
- **Open Source Community**: For continuous inspiration and support

## 📬 Contact

Have ideas for improving this system or want to integrate real data?
- **GitHub Issues**: [Open an issue](https://github.com/yourusername/schwimmbad-metrics/issues)
- **Feature Requests**: Submit via discussions or issues

---

*Note: This project currently uses simulated data. We're actively seeking partnerships with Stadthallenbad or relevant authorities to integrate real occupancy data.*

---


Montag*:	08:00 - 21:30 Uhr
Dienstag*:	06:30 - 21:30 Uhr
Mittwoch*:	08:00 - 17:30 Uhr
Donnerstag*:	06:30 - 21:30 Uhr
Freitag*:	08:00 - 21:30 Uhr
Samstag*:	07:00 - 21:30 Uhr
Sonn- & Feiertag:	07:00 - 18:00 Uhr
*außer Feiertag