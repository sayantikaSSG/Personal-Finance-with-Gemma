import pandas as pd
from sklearn.metrics import mean_absolute_percentage_error

def prepare_monthly_series(df, category=None):
    """
    Prepare monthly time series for expenses, optionally by category.
    """
    df = df[df['type'] == 'expense']
    if category:
        df = df[df['category'] == category]
    monthly = df.groupby(df['date'].dt.to_period('M'))['amount'].sum().abs()
    monthly.index = monthly.index.to_timestamp()
    return monthly

def forecast_with_baseline(series, periods=3):
    """
    Forecast using baseline: average of last 3 months.
    """
    if len(series) < 3:
        return [series.mean()] * periods
    baseline = series.tail(3).mean()
    return [baseline] * periods

def forecast_with_prophet(series, periods=3):
    """
    Forecast using Prophet if available.
    """
    try:
        from prophet import Prophet
        df_prophet = pd.DataFrame({'ds': series.index, 'y': series.values})
        model = Prophet()
        model.fit(df_prophet)
        future = model.make_future_dataframe(periods=periods, freq='M')
        forecast = model.predict(future)
        return forecast['yhat'].tail(periods).tolist()
    except ImportError:
        print("Prophet not installed, using baseline")
        return forecast_with_baseline(series, periods)

def evaluate_forecast(actual, predicted):
    """
    Evaluate forecast with MAPE and RMSE.
    """
    mape = mean_absolute_percentage_error(actual, predicted)
    rmse = ((actual - predicted) ** 2).mean() ** 0.5
    return {"MAPE": mape, "RMSE": rmse}