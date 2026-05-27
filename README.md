# Horse Biometric Analytics Pipeline (Benter Engine Core v1.0)
**Developer: Pray Patel**

## Project Overview
This software framework exploits a specific market inefficiency in sports handicapping pools. While standard public datasets rely completely on historical administrative variables (like past times and jockey weights), this engine quantifies real-time physical condition changes using alternative biometric features.

## System Architecture Layers
1. **AI Vision Pipeline (`test_vision.py`)**: Uses YOLOv8 neural networks to locate and isolate competitors within a bounding box matrix, slice specific muscle engine zones (hindquarters), and apply directional edge texture analysis to calculate a proprietary muscle condition index.
2. **Predictive Quant Engine (`benter_ultra_engine.py` / `benter_ml_elite.py`)**: Implements multi-variable non-linear decision scoring and a Stage-2 Logarithmic Blending algorithm to calculate true win probabilities across a field.
3. **Stochastic Simulator (`benter_monte_carlo.py`)**: Runs 10,000 parallel race simulations under normal distribution curves to model real-world chaotic track variance and calculate empirical returns.
4. **Relational Ledger Archive (`save_to_database.py`)**: Anchors calculations and text logs securely into local persistent SQLite database storage schemas.
5. **Settlement Auditor Core (`results_checker.py`)**: Parses pending bet matrices, applies contract multiplier math to official race results, and handles capital accounting tracking.
6. 
