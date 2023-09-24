import pandas
import matplotlib.pyplot

df=pandas.read_csv('countries of the world.csv')
df=df.dropna()


matplotlib.pyplot.title('Зависимость рождаемости от образованности (грамотность)')

def literacy_apply(literacy):
    literacy=literacy.replace(',','.')
    return float(literacy)
df['Literacy (%)']=df['Literacy (%)'].apply(literacy_apply)
def birthrate_apply(birthrate):
    birthrate=birthrate.replace(',','.')
    return float(birthrate)
df['Birthrate']=df['Birthrate'].apply(literacy_apply)

high_lb=df[df['Literacy (%)']>=95.0]['Birthrate'].mean()
medium_lb=df[df['Literacy (%)']>=85.0]['Birthrate'].mean()
low_lb=df[df['Literacy (%)']<85.0]['Birthrate'].mean()

lb=pandas.Series(data=[high_lb,medium_lb,low_lb],index=['Высокая','Средняя','Низкая'])
lb.plot(kind='pie')
matplotlib.pyplot.show()


matplotlib.pyplot.title('Зависимость индустриализаций от уровня сервиса (индустриализация)')

def industry_apply(industry):
    industry=industry.replace(',','.')
    return float(industry)
df['Industry']=df['Industry'].apply(industry_apply)
def service_apply(service):
    service=service.replace(',','.')
    return float(service)
df['Service']=df['Service'].apply(service_apply)

high_si=df[df['Service']>=0.6]['Industry'].mean()
medium_si=df[df['Service']>=0.5]['Industry'].mean()
low_si=df[df['Service']<0.5]['Industry'].mean()

si=pandas.Series(data=[high_si,medium_si,low_si],index=['Высокая','Средняя','Низкая'])
si.plot(kind='pie')
matplotlib.pyplot.show()
