import pandas as pd
import numpy as np

def preprocess_features(df):
    df['Значение счетчика моточасов, час:мин'] = df['Значение счетчика моточасов, час:мин'].apply(lambda x: float(str(x).split(':')[0]))

    df['Полож.пед.акселер.,%'] = df['Полож.пед.акселер.,%'].apply(lambda x: float(str(x).split(',')[0]))

    df['Обор.двиг.,об/мин'] = df['Обор.двиг.,об/мин'].apply(lambda x: float(str(x).split(',')[0]))

    df['Сост.пед.сцепл.'].replace('Отпущ.', 0, inplace = True)
    df['Сост.пед.сцепл.'].replace('Нажат.', 1, inplace = True)

    df['Нейтраль КПП (spn3843)'].replace('1', 1, inplace = True)
    df['Нейтраль КПП (spn3843)'].replace('0', 0, inplace = True)

    df['Стояночный тормоз (spn3842)'].replace('1', 1, inplace = True)
    df['Стояночный тормоз (spn3842)'].replace('0', 0, inplace = True)

    df['Засоренность воздушного фильтра (spn3840)'].replace('0', 0, inplace = True)
    df['Засоренность воздушного фильтра (spn3840)'].replace('1', 1, inplace = True)

    df['Засоренность фильтра КПП (spn3847)'].replace('1', 1, inplace = True)
    df['Засоренность фильтра КПП (spn3847)'].replace('0', 0, inplace = True)

    df['Засоренность фильтра ДВС (spn3845)'].replace('0', 0, inplace = True)
    df['Засоренность фильтра ДВС (spn3845)'].replace('1', 1, inplace = True)

    df['Засоренность фильтра рулевого управления (spn3844)'].replace('1', 1, inplace = True)
    df['Засоренность фильтра рулевого управления (spn3844)'].replace('0', 0, inplace = True)

    df['Засоренность фильтра навесного оборудования (spn3851)'].replace('1', 1, inplace = True)
    df['Засоренность фильтра навесного оборудования (spn3851)'].replace('0', 0, inplace = True)

    df['Недопустимый уровень масла в гидробаке (spn3850)'].replace('1', 1, inplace = True)
    df['Недопустимый уровень масла в гидробаке (spn3850)'].replace('0', 0, inplace = True)

    df['Аварийная температура масла в гидросистеме (spn3849)'].replace('1', 1, inplace = True)
    df['Аварийная температура масла в гидросистеме (spn3849)'].replace('0', 0, inplace = True)

    df['Аварийная температура охлаждающей жидкости (spn3841)'].replace('1', 1, inplace = True)
    df['Аварийная температура охлаждающей жидкости (spn3841)'].replace('0', 0, inplace = True)

    df['Аварийное давление в I контуре тормозной системы (spn3848)'].replace('1', 1, inplace = True)
    df['Аварийное давление в I контуре тормозной системы (spn3848)'].replace('0', 0, inplace = True)

    df['Аварийное давление в II контуре тормозной системы (spn3855)'].replace('1', 1, inplace = True)
    df['Аварийное давление в II контуре тормозной системы (spn3855)'].replace('0', 0, inplace = True)

    df['Зарядка АКБ (spn3854)'].replace('1', 1, inplace = True)
    df['Зарядка АКБ (spn3854)'].replace('0', 0, inplace = True)

    df['Отопитель (spn3853)'].replace('1', 1, inplace = True)
    df['Отопитель (spn3853)'].replace('0', 0, inplace = True)

    df['Выход блока управления двигателем (spn3852)'].replace('1', 1, inplace = True)
    df['Выход блока управления двигателем (spn3852)'].replace('0', 0, inplace = True)

    df['Включение тормозков (spn3859)'].replace('1', 1, inplace = True)
    df['Включение тормозков (spn3859)'].replace('0', 0, inplace = True)

    df['Засоренность фильтра слива (spn3858)'].replace('1', 1, inplace = True)
    df['Засоренность фильтра слива (spn3858)'].replace('0', 0, inplace = True)

    df['Аварийное давление масла КПП (spn3857)'].replace('1', 1, inplace = True)
    df['Аварийное давление масла КПП (spn3857)'].replace('0', 0, inplace = True)

    df['Аварийная температура масла ДВС(spn3856)'].replace('1', 1, inplace = True)
    df['Аварийная температура масла ДВС(spn3856)'].replace('0', 0, inplace = True)

    df['Аварийное давление масла ДВС (spn3846)'].replace('1', 1, inplace = True)
    df['Аварийное давление масла ДВС (spn3846)'].replace('0', 0, inplace = True)

    df['Неисправность тормозной системы (spn3863)'].replace('1', 1, inplace = True)
    df['Неисправность тормозной системы (spn3863)'].replace('0', 0, inplace = True)

    df['Термостарт (spn3862)'].replace('1', 1, inplace = True)
    df['Термостарт (spn3862)'].replace('0', 0, inplace = True)

    df['Разрешение запуска двигателя (spn3861)'].replace('1', 1, inplace = True)
    df['Разрешение запуска двигателя (spn3861)'].replace('0', 0, inplace = True)

    df['Низкий уровень ОЖ (spn3860)'].replace('1', 1, inplace = True)
    df['Низкий уровень ОЖ (spn3860)'].replace('0', 0, inplace = True)

    df['Аварийная температура масла ГТР (spn3867)'].replace('1', 1, inplace = True)
    df['Аварийная температура масла ГТР (spn3867)'].replace('0', 0, inplace = True)

    df['Необходимость сервисного обслуживания (spn3866)'].replace('1', 1, inplace = True)
    df['Необходимость сервисного обслуживания (spn3866)'].replace('0', 0, inplace = True)

    df['Подогрев топливного фильтра (spn3865)'].replace('1', 1, inplace = True)
    df['Подогрев топливного фильтра (spn3865)'].replace('0', 0, inplace = True)

    df['Вода в топливе (spn3864)'].replace('1', 1, inplace = True)
    df['Вода в топливе (spn3864)'].replace('0', 0, inplace = True)

    df['Холодный старт (spn3871)'].replace('1', 1, inplace = True)
    df['Холодный старт (spn3871)'].replace('0', 0, inplace = True)
    return df


blank_cols = ['Нагрузка на двигатель, %',
 'iButton2',
 'Крутящий момент (spn513), Нм',
 'Положение рейки ТНВД (spn51), %',
 'Расход топлива (spn183), л/ч',
 'ДВС. Температура наддувочного воздуха, °С',
 'Давление наддувочного воздуха двигателя (spn106), кПа',
 'Текущая передача (spn523)',
 'Температура масла гидравлики (spn5536), С',
 'Педаль слива (spn598)']
def preprocess_data(df):
    df.replace('-', np.nan, inplace=True)
    df.replace('        -', np.nan, inplace=True)
    df['Дата и время'] = pd.to_datetime(df['Дата и время'], format="%d/%m/%Y %H:%M:%S")
    df.drop(columns=blank_cols, inplace=True)
    df = preprocess_features(df)
    return df
