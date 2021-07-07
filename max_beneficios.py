import streamlit as st

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
from PIL import Image

import SessionState

st.set_page_config(
     page_title="deepsense|Marketing",
     page_icon="ICONO DEEPSENSE.png",
     layout="wide",
     initial_sidebar_state="expanded",
     )
def app():
    st.image(Image.open('ICONO DEEPSENSE.png'), width = 100)
    
    d = 0
    rango_camp = (2,3,4,5,6,7,8,9)

    st.title('Optimización de las campañas de Marketing con IA')


    s1, s2, s3 = st.beta_columns(3)


    d = s1.selectbox(
    "¿Cuantas estrategias has realizado?: ",
    rango_camp)
    d = int(d)
    N = s2.number_input("¿A cuantos contactos vas a lanzar la próxima campaña?: ", value = 100)
    N = int(N)
    producto = s3.number_input("Introduce el precio del producto: ", value = 1.0)
    producto = float(producto)

    """
    #### Introduce los datos de las estrategias anteriores:
    """

    c1, c2, c3 = st.beta_columns(3)
    b1, b2 = st.beta_columns(2)
    defect_value = 1


    if d == 2:
        """
        #### Número de contactos:
        """
        b1, b2 = st.beta_columns(2)
        N0= b1.number_input("Número de contactos con la estrategia 0: ", value = defect_value)
        N1= b2.number_input("Número de contactos con la estrategia 1: ", value = defect_value)
        """
        #### Número de conversiones:
        """
        b1, b2 = st.beta_columns(2)
        C0= b1.number_input("Número de conversiones con la estrategia 0: ", value = defect_value)
        C1= b2.number_input("Número de conversiones con la estrategia 1: ", value = defect_value)
        N0 = int(N0)
        N1 = int(N1)
        C0 = int(C0)
        C1 = int(C1)
        conversion_rates = [C0/N0, C1/N1]
    elif d == 3:
        """
        #### Número de contactos:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        N0= c1.number_input("Número de contactos con la estrategia 0: ", value = defect_value)
        N1= c2.number_input("Número de contactos con la estrategia 1: ", value = defect_value)
        N2= c3.number_input("Número de contactos con la estrategia 2: ", value = defect_value)
        """
        #### Número de conversiones:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        C0= c1.number_input("Número de conversiones con la estrategia 0: ", value = defect_value)
        C1= c2.number_input("Número de conversiones con la estrategia 1: ", value = defect_value)
        C2= c3.number_input("Número de conversiones con la estrategia 2: ", value = defect_value)
        N0 = int(N0)
        N1 = int(N1)
        N2 = int(N2)
        C0 = int(C0)
        C1 = int(C1)
        C2 = int(C2)
        conversion_rates = [C0/N0, C1/N1, C2/N2]
    elif d == 4:
        """
        #### Número de contactos:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        N0= b1.number_input("Número de contactos con la estrategia 0: ", value = defect_value)
        N1= b2.number_input("Número de contactos con la estrategia 1: ", value = defect_value)
        N2= b1.number_input("Número de contactos con la estrategia 2: ", value = defect_value)
        N3= b2.number_input("Número de contactos con la estrategia 3: ", value = defect_value)
        """
        #### Número de conversiones:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        C0= b1.number_input("Número de conversiones con la estrategia 0: ", value = defect_value)
        C1= b2.number_input("Número de conversiones con la estrategia 1: ", value = defect_value)
        C2= b1.number_input("Número de conversiones con la estrategia 2: ", value = defect_value)
        C3= b2.number_input("Número de conversiones con la estrategia 3: ", value = defect_value)
        N0 = int(N0)
        N1 = int(N1)
        N2 = int(N2)
        N3 = int(N3)
        C0 = int(C0)
        C1 = int(C1)
        C2 = int(C2)
        C3 = int(C3)
        conversion_rates = [C0/N0, C1/N1, C2/N2, C3/N3]
    elif d == 5:
        """
        #### Número de contactos:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        N0= c1.number_input("Número de contactos con la estrategia 0: ", value = defect_value)
        N1= c2.number_input("Número de contactos con la estrategia 1: ", value = defect_value)
        N2= c3.number_input("Número de contactos con la estrategia 2: ", value = defect_value)
        N3= c1.number_input("Número de contactos con la estrategia 3: ", value = defect_value)
        N4= c2.number_input("Número de contactos con la estrategia 4: ", value = defect_value)
        """
        #### Número de conversiones:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        C0= c1.number_input("Número de conversiones con la estrategia 0: ", value = defect_value)
        C1= c2.number_input("Número de conversiones con la estrategia 1: ", value = defect_value)
        C2= c3.number_input("Número de conversiones con la estrategia 2: ", value = defect_value)
        C3= c1.number_input("Número de conversiones con la estrategia 3: ", value = defect_value)
        C4= c2.number_input("Número de conversiones con la estrategia 4: ", value = defect_value)
        N0 = int(N0)
        N1 = int(N1)
        N2 = int(N2)
        N3 = int(N3)
        N4 = int(N4)
        C0 = int(C0)
        C1 = int(C1)
        C2 = int(C2)
        C3 = int(C3)
        C4 = int(C4)
        conversion_rates = [C0/N0, C1/N1, C2/N2, C3/N3, C4/N4]
    elif d == 6:
        """
        #### Número de contactos:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        N0= c1.number_input("Número de contactos con la estrategia 0: ", value = defect_value)
        N1= c2.number_input("Número de contactos con la estrategia 1: ", value = defect_value)
        N2= c3.number_input("Número de contactos con la estrategia 2: ", value = defect_value)
        N3= c1.number_input("Número de contactos con la estrategia 3: ", value = defect_value)
        N4= c2.number_input("Número de contactos con la estrategia 4: ", value = defect_value)
        N5= c3.number_input("Número de contactos con la estrategia 5: ", value = defect_value)
        """
        #### Número de conversiones:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        C0= c1.number_input("Número de conversiones con la estrategia 0: ", value = defect_value)
        C1= c2.number_input("Número de conversiones con la estrategia 1: ", value = defect_value)
        C2= c3.number_input("Número de conversiones con la estrategia 2: ", value = defect_value)
        C3= c1.number_input("Número de conversiones con la estrategia 3: ", value = defect_value)
        C4= c2.number_input("Número de conversiones con la estrategia 4: ", value = defect_value)
        C5= c3.number_input("Número de conversiones con la estrategia 5: ", value = defect_value)
        N0 = int(N0)
        N1 = int(N1)
        N2 = int(N2)
        N3 = int(N3)
        N4 = int(N4)
        N5 = int(N5)
        C0 = int(C0)
        C1 = int(C1)
        C2 = int(C2)
        C3 = int(C3)
        C4 = int(C4)
        C5 = int(C5)
        conversion_rates = [C0/N0, C1/N1, C2/N2, C3/N3, C4/N4, C5/N5]
    elif d == 7:
        """
        #### Número de contactos:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        N0= c1.number_input("Número de contactos con la estrategia 0: ", value = defect_value)
        N1= c2.number_input("Número de contactos con la estrategia 1: ", value = defect_value)
        N2= c3.number_input("Número de contactos con la estrategia 2: ", value = defect_value)
        N3= c1.number_input("Número de contactos con la estrategia 3: ", value = defect_value)
        N4= c2.number_input("Número de contactos con la estrategia 4: ", value = defect_value)
        N5= c3.number_input("Número de contactos con la estrategia 5: ", value = defect_value)
        N6= b1.number_input("Número de contactos con la estrategia 6: ", value = defect_value)
        """
        #### Número de conversiones:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        C0= c1.number_input("Número de conversiones con la estrategia 0: ", value = defect_value)
        C1= c2.number_input("Número de conversiones con la estrategia 1: ", value = defect_value)
        C2= c3.number_input("Número de conversiones con la estrategia 2: ", value = defect_value)
        C3= c1.number_input("Número de conversiones con la estrategia 3: ", value = defect_value)
        C4= c2.number_input("Número de conversiones con la estrategia 4: ", value = defect_value)
        C5= c3.number_input("Número de conversiones con la estrategia 5: ", value = defect_value)
        C6= b1.number_input("Número de conversiones con la estrategia 6: ", value = defect_value)
        N0 = int(N0)
        N1 = int(N1)
        N2 = int(N2)
        N3 = int(N3)
        N4 = int(N4)
        N5 = int(N5)
        N6 = int(N6)
        C0 = int(C0)
        C1 = int(C1)
        C2 = int(C2)
        C3 = int(C3)
        C4 = int(C4)
        C5 = int(C5)
        C6 = int(C6)
        conversion_rates = [C0/N0, C1/N1, C2/N2, C3/N3, C4/N4, C5/N5, C6/N6]
    elif d == 8:
        """
        #### Número de contactos:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        N0= c1.number_input("Número de contactos con la estrategia 0: ", value = defect_value)
        N1= c2.number_input("Número de contactos con la estrategia 1: ", value = defect_value)
        N2= c3.number_input("Número de contactos con la estrategia 2: ", value = defect_value)
        N3= c1.number_input("Número de contactos con la estrategia 3: ", value = defect_value)
        N4= c2.number_input("Número de contactos con la estrategia 4: ", value = defect_value)
        N5= c3.number_input("Número de contactos con la estrategia 5: ", value = defect_value)
        N6= c1.number_input("Número de contactos con la estrategia 6: ", value = defect_value)
        N7= c2.number_input("Número de contactos con la estrategia 7: ", value = defect_value)
        """
        #### Número de conversiones:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        C0= c1.number_input("Número de conversiones con la estrategia 0: ", value = defect_value)
        C1= c2.number_input("Número de conversiones con la estrategia 1: ", value = defect_value)
        C2= c3.number_input("Número de conversiones con la estrategia 2: ", value = defect_value)
        C3= c1.number_input("Número de conversiones con la estrategia 3: ", value = defect_value)
        C4= c2.number_input("Número de conversiones con la estrategia 4: ", value = defect_value)
        C5= c3.number_input("Número de conversiones con la estrategia 5: ", value = defect_value)
        C6= c1.number_input("Número de conversiones con la estrategia 6: ", value = defect_value)
        C7= c2.number_input("Número de conversiones con la estrategia 7: ", value = defect_value)
        N0 = int(N0)
        N1 = int(N1)
        N2 = int(N2)
        N3 = int(N3)
        N4 = int(N4)
        N5 = int(N5)
        N6 = int(N6)
        N7 = int(N7)
        C0 = int(C0)
        C1 = int(C1)
        C2 = int(C2)
        C3 = int(C3)
        C4 = int(C4)
        C5 = int(C5)
        C6 = int(C6)
        C7 = int(C7)
        conversion_rates = [C0/N0, C1/N1, C2/N2, C3/N3, C4/N4, C5/N5, C6/N6, C7/N7]
    elif d == 9:
        """
        #### Número de contactos:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        N0= c1.number_input("Número de contactos con la estrategia 0: ", value = defect_value)
        N1= c2.number_input("Número de contactos con la estrategia 1: ", value = defect_value)
        N2= c3.number_input("Número de contactos con la estrategia 2: ", value = defect_value)
        N3= c1.number_input("Número de contactos con la estrategia 3: ", value = defect_value)
        N4= c2.number_input("Número de contactos con la estrategia 4: ", value = defect_value)
        N5= c3.number_input("Número de contactos con la estrategia 5: ", value = defect_value)
        N6= c1.number_input("Número de contactos con la estrategia 6: ", value = defect_value)
        N7= c2.number_input("Número de contactos con la estrategia 7: ", value = defect_value)
        N8= c3.number_input("Número de contactos con la estrategia 8: ", value = defect_value)
        """
        #### Número de conversiones:
        """
        c1, c2, c3 = st.beta_columns(3)
        b1, b2 = st.beta_columns(2)
        C0= c1.number_input("Número de conversiones con la estrategia 0: ", value = defect_value)
        C1= c2.number_input("Número de conversiones con la estrategia 1: ", value = defect_value)
        C2= c3.number_input("Número de conversiones con la estrategia 2: ", value = defect_value)
        C3= c1.number_input("Número de conversiones con la estrategia 3: ", value = defect_value)
        C4= c2.number_input("Número de conversiones con la estrategia 4: ", value = defect_value)
        C5= c3.number_input("Número de conversiones con la estrategia 5: ", value = defect_value)
        C6= c1.number_input("Número de conversiones con la estrategia 6: ", value = defect_value)
        C7= c2.number_input("Número de conversiones con la estrategia 7: ", value = defect_value)
        C8= c3.number_input("Número de conversiones con la estrategia 8: ", value = defect_value)
        N0 = int(N0)
        N1 = int(N1)
        N2 = int(N2)
        N3 = int(N3)
        N4 = int(N4)
        N5 = int(N5)
        N6 = int(N6)
        N7 = int(N7)
        N8 = int(N8)
        C0 = int(C0)
        C1 = int(C1)
        C2 = int(C2)
        C3 = int(C3)
        C4 = int(C4)
        C5 = int(C5)
        C6 = int(C6)
        C7 = int(C7)
        C8 = int(C8)
        conversion_rates = [C0/N0, C1/N1, C2/N2, C3/N3, C4/N4, C5/N5, C6/N6, C7/N7, C8/N8]

    X = np.array(np.zeros([N, d]))
    for i in range(N):
        for j in range(d):
            if np.random.rand() <= conversion_rates[j]:
                X[i,j] = 1

    #OPEN SELECTION AND THOMPSON SAMPLING IMPLEMENTATION
    strategies_selected_rs = [] #random samplig
    strategies_selected_ts = [] #thompson sampling
    total_reward_rs = 0
    total_reward_ts = 0
    number_of_rewards_1 = [0] * d
    number_of_rewards_0 = [0] * d
    rewards_strategies_aleatory = [0] * d
    rewards_strategies_thompson = [0] * d
    regret_aleatory = []
    regret_thompson = []

    for n in range(0, N):
        #Aleatory selection
        strategy_rs = random.randrange(d)
        strategies_selected_rs.append(strategy_rs)
        reward_rs = X[n, strategy_rs]
        total_reward_rs += reward_rs
        # Best Strategy
        for i in range(0, d):
            rewards_strategies_aleatory[i] = rewards_strategies_aleatory[i] + X[n, i]
        total_reward_bs = max(rewards_strategies_aleatory)
        # Regret
        regret_aleatory.append(total_reward_bs - total_reward_rs)
        #Thompson sampling
        strategy_ts = 0
        max_random = 0
        for i in range(0, d):
            random_beta = random.betavariate(number_of_rewards_1[i]+1, number_of_rewards_0[i]+1)
            if random_beta > max_random:
                max_random = random_beta
                strategy_ts = i
        reward_ts = X[n, strategy_ts]
        if reward_ts == 1:
            number_of_rewards_1[strategy_ts] += 1
        else:
            number_of_rewards_0[strategy_ts] += 1
        strategies_selected_ts.append(strategy_ts)
        total_reward_ts += reward_ts
        # Best Strategy
        for i in range(0, d):
            rewards_strategies_thompson[i] = rewards_strategies_thompson[i] + X[n, i]
        total_reward_bs = max(rewards_strategies_thompson)
        # Regret
        regret_thompson.append(total_reward_bs - total_reward_ts)
    #Calculate absolut and relative return
    absolute_return = (total_reward_ts - total_reward_rs) * producto #supose that the price of product is 100 €
    relative_return = ((total_reward_ts - total_reward_rs) / total_reward_rs) * producto 

    """
    ### Resultados:
    """
    st.write('Rendimiento absoluto: {:.2f} €'.format(absolute_return))
    st.write('Rendimiento relativo: {:.2f} %'.format(relative_return))
    #st.write('estrategia seleccionada más veces con la estrategia de Thompson: ', np.max(strategies_selected_ts))

    st.set_option('deprecation.showPyplotGlobalUse', False)
    b1, b2 = st.beta_columns(2)

    plt.hist(strategies_selected_ts)
    plt.title('Histograma de selecciones')
    plt.xlabel('Estrategia')
    plt.ylabel('Número de veces que la estrategia es seleccionada')
    st.pyplot()


    plt.plot(regret_aleatory)
    plt.title('Regret Curve of Random Strategy')
    plt.xlabel('Round')
    plt.ylabel('Regret')
    b1.pyplot()

    plt.plot(regret_thompson)
    plt.title('Regret Curve of Thompson Strategy')
    plt.xlabel('Round')
    plt.ylabel('Regret')
    b2.pyplot()

ss = SessionState.get(x=1)
if ss.x<=1:
    st.image(Image.open('LOGO COLOR.png'), width = 300)
titulo_object = st.empty()
password_object = st.empty()
inicio_object = st.empty()
if ss.x <= 1:
    pass_real = pd.read_csv("./password_usecases.csv")["PASSWORD"][0]
    titulo_object.title('Introduce contraseña')
    password = password_object.text_input("Contraseña")
    inicio_sesion = inicio_object.button("INICIAR SESION")
    if password == pass_real and inicio_sesion:
        ss.x = ss.x + 1
else:
    titulo_object.empty()
    password_object.empty()
    inicio_object.empty()
    
    #la funcion app es donde debe meterse el codigo de la aplicacion que queremos ejecutar
    app()    
