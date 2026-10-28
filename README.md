# Horse Biometric Analytics Pipeline

**Developer:** Pray Patel  
**Language:** Python

## Overview

The Horse Biometric Analytics Pipeline is an experimental project that combines computer vision, probability modelling and Monte Carlo simulation to explore horse-racing predictions.

The goal is to analyse image features, estimate race outcomes and organise prediction data in one software system.

## Features

- **Computer Vision:** Uses YOLOv8, OpenCV and NumPy to analyse images and calculate image-feature scores.
- **Prediction Engines:** Calculates and combines estimated win probabilities.
- **Monte Carlo Simulation:** Simulates 10,000 races to explore possible outcomes.
- **Database:** Uses SQLite to store and retrieve race records.
- **Results Checker:** Compares entered race results with simulated records.
- **Analytics:** Generates charts to visualise example data.

## Project Files

| File | Purpose |
|---|---|
| `test_vision.py` | Image analysis |
| `benter_ultra_engine.py` | Probability calculations |
| `benter_ml_elite.py` | Prediction modelling |
| `benter_ensemble_elite.py` | Combines prediction approaches |
| `benter_monte_carlo.py` | Race simulations |
| `save_to_database.py` | Reads race records from the database |
| `results_checker.py` | Checks results and calculates settlements |
| `generate_analytics.py` | Generates charts |
| `master_control.py` | Main control menu |

## Technologies

- Python
- OpenCV
- NumPy
- YOLOv8
- SQLite
- Matplotlib

## Current Status

The prediction and simulation scripts have been tested with example data. The complete pipeline has not yet been validated end-to-end.

The model's predictive accuracy and the relationship between image features and physical condition require further testing against suitable data.

## Future Improvements

- Connect the modules into a complete workflow.
- Test predictions against historical race results.
- Measure prediction accuracy against a baseline.
- Improve data storage and reproducibility.
- Document results and limitations.

## Disclaimer

This project is for educational and research purposes. Its predictions are experimental and should not be considered reliable racing forecasts or financial advice.
