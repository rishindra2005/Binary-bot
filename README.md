# Binary-bot

A collection of algorithmic trading bots for IQ Option platform using machine learning prediction models.

## Bot Scripts and Their Functionality

This project includes several trading bot implementations:

- **chainbot.py**: Multi-currency pair bot that analyzes EURUSD, USDJPY, and EURJPY simultaneously using RandomForest models.
- **IQ_linkbot.py**: Advanced version that combines predictions from multiple models and currency pairs.
- **iq_botml.py**: Specialized bot focusing on EURJPY with custom machine learning implementation.
- **botml_all.py**: Uses both RandomForest and DecisionTree models to provide combined signals.
- **iq_botcandle.py**: Real-time candle analysis bot that makes decisions based on price action patterns.
- **iq_try_OTC.py**: Specialized for OTC (Over The Counter) markets with adapted strategies.
- **iq(only_buy).py**: Simplified bot that only executes buy orders with a recovery strategy.

## Trading Strategy

These bots employ a combination of:

1. **Machine Learning Prediction**: Using pre-trained models (RandomForest, DecisionTree) to predict market direction.
2. **Technical Analysis**: Analyzing candlestick patterns and price action.
3. **Martingale Recovery**: Progressive stake adjustment strategy when trades are unsuccessful.

The average accuracy of these bots is around 60%, which provides an edge in binary options trading where the typical payout is 80%. The recovery strategy is designed to help manage losses when predictions are incorrect.

## Environment Variables

This project uses environment variables to securely manage credentials. Follow these steps to set up your environment:

1. Create a `.env` file in the root directory of the project
2. Add your credentials in the following format:
```
IQ_EMAIL=your_email@example.com
IQ_PASSWORD=your_password
```

3. The application will automatically load these credentials when it runs

## GUI Interface

The `linkbot` folder contains a graphical user interface that allows for:
- Easy login to IQ Option
- Setting trade parameters
- Monitoring balance and trade results
- Starting and stopping the bot

## Security Best Practices

- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude the `.env` file
- Keep your credentials secure and don't share them

## Risk Warning

Trading binary options involves significant risk. These bots are provided for educational purposes only and come with no guarantee of profit. Only trade with money you can afford to lose. 