# Binary-bot

Binary-bot is a collection of algorithmic trading bots designed for the IQ Option platform, leveraging machine learning models to predict market movements with approximately 60% accuracy. This edge, combined with proper risk management, can be profitable in binary options markets offering 80% payouts.

## Key Features

- **Multiple Bot Implementations**: Specialized bots for different trading styles and asset classes
- **Machine Learning Prediction**: Pre-trained RandomForest and DecisionTree models for market direction forecasting
- **Multi-Currency Analysis**: Combined signals from EURUSD, USDJPY, and EURJPY for enhanced accuracy
- **Advanced Recovery Strategy**: Sophisticated Martingale implementation to manage unsuccessful trades
- **Real-Time Technical Analysis**: Candlestick pattern recognition and price action evaluation
- **Graphical User Interface**: User-friendly dashboard for monitoring and controlling bot operations
- **Secure Credential Management**: Environment variables for API credentials with no hardcoded sensitive data

## Bot Varieties

- Strategy bots for standard market hours
- OTC (Over The Counter) specialized bots
- Single-currency and multi-currency implementations
- Pure technical analysis and ML-hybrid approaches

The project includes a complete trading system with signal generation, execution logic, position sizing, and loss recovery mechanisms. The modular design allows for customization and enhancement of individual components.

This system demonstrates how machine learning can be applied to financial markets using Python, pandas for data manipulation, scikit-learn for ML models, and the IQ Option API for execution.

DISCLAIMER: Trading binary options involves significant risk. This software is provided for educational purposes only with no guarantee of profitability. Always practice responsible risk management. 