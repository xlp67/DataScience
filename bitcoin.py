import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet  
from sklearn.metrics import mean_absolute_error

bitcoin_data = pd.read_csv('./bitcoin_historical_data.csv', sep=',', encoding='utf-8')

bitcoin_data['Date'] = pd.to_datetime(bitcoin_data['Date'], format='%m/%d/%Y')  
bitcoin_data['Price'] = bitcoin_data['Price'].str.replace(',', '').astype(float)  

df = bitcoin_data[['Date', 'Price']].rename(columns={'Date': 'ds', 'Price': 'y'})

model = Prophet(
    daily_seasonality=False, 
    yearly_seasonality=True, 
    weekly_seasonality=True,
    seasonality_prior_scale=10,  
    changepoint_prior_scale=0.05  
)

model.add_seasonality(name='monthly', period=30.5, fourier_order=8)  

model.add_country_holidays(country_name='US')  

model.fit(df)

future = model.make_future_dataframe(periods=730, freq='D')  
forecast = model.predict(future)

plt.figure(figsize=(12, 6))
plt.plot(df['ds'], df['y'], label="Dados Reais", color='blue', alpha=0.6)  
plt.plot(forecast['ds'], forecast['yhat'], label="Previsão", color='red')  
plt.fill_between(forecast['ds'], forecast['yhat_lower'], forecast['yhat_upper'], color='gray', alpha=0.2)  

plt.title('Previsão do Preço do Bitcoin (2025-2026) - Modelo Prophet', fontsize=14)
plt.xlabel('Tempo', fontsize=12)
plt.ylabel('Preço de Fechamento (USD)', fontsize=12)
plt.legend()
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout() 
plt.show()

y_true = df['y']
y_pred = forecast['yhat'][:len(df)]
mae = mean_absolute_error(y_true, y_pred)

print(f"Erro médio absoluto do modelo: {mae:.2f} USD")
