import warnings
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

warnings.filterwarnings('ignore', category=FutureWarning)

def DataPerState(state, product):
    data_prince = pd.read_csv('./GasPricesinBrazil_2004-2019.csv', sep=';')
    return data_prince[
                          (data_prince['ESTADO'] == state) & 
                          (data_prince['PRODUTO'] == product)
                          ]

def FilterPrincePerYear(state, product):
    data_per_state = DataPerState(state, product)
    data_prince_per_year = pd.DataFrame(columns=['ANO', 'PREÇO'])
    for value in data_per_state.values:
        month = value[1].split('-')[1]
        year = value[1].split('-')[0]

        if month == '02' and year not in data_prince_per_year.values:
            new_row = pd.DataFrame({data_prince_per_year.columns[0]: [year], data_prince_per_year.columns[1]: value[8]})
            data_prince_per_year = pd.concat([data_prince_per_year, new_row], ignore_index=True)

    return data_prince_per_year

def PlotData(data):
    print(data)
    return plt.scatter(data['ANO'], data['PREÇO'])
    
data_util_PA_Etanol = FilterPrincePerYear('PARA', 'ETANOL HIDRATADO')
data_util_PA_Gasolina = FilterPrincePerYear('PARA', 'GASOLINA COMUM')
PlotData(data_util_PA_Etanol)
PlotData(data_util_PA_Gasolina)
plt.show()



# degree = 5
# model_poly = make_pipeline(PolynomialFeatures(degree), LinearRegression())
# X = data_util_PA[['ANO']].values   
# y = data_util_PA['PREÇO'].values

# model_poly.fit(X, y)

# y_pred = model_poly.predict(X)
# mae = mean_absolute_error(y, y_pred)

# predict_2025 = model_poly.predict([[2014]])

# predict_min = predict_2025 * (1 - mae)
# predict_max = predict_2025 * (1 + mae)

# print(data_util_PA)
# print(f'PREÇO MÍNIMO: {predict_min[0]:.2f}\nPREÇO MÁXIMO: {predict_max[0]:.2f}\nPREÇO MÉDIO: {predict_2025[0]:.2f}')

# print(f'Erro médio absoluto (MAE) do modelo: {mae:.4f}')

