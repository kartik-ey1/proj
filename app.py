import streamlit as st
def M2(M1):
    return ((1 + 0.2*M1*M1)/(1.4*M1*M1 - 0.2))**(0.5)

def d_ratio(M1):
    return (2.4*M1*M1)/(0.4*M1*M1 + 2)

def P_ratio(M1):
    return 1 + (1.1667)*(M1*M1 - 1)

def T_ratio(M1):
    return 1 + (0.13889)*(1.4*M1*M1 + 1)*(M1*M1 - 1)/(M1*M1)

def Ps_ratio(M1):
    return ((P_ratio(M1))**(-2.5))*(((2.4*M1*M1)/(0.4*M1*M1 + 2))**(3.5))

def a_ratio(M1):
    return (T_ratio(M1))**(0.5)

def M1_print(M1):
    st.write("M1 = " + str(abs(M1)))
    st.write("M2 = " + str(M2(M1)))
    st.write("P2/P1 = " + str(P_ratio(M1)))
    st.write("d2/d1 = " + str(d_ratio(M1)))
    st.write("T2/T1 = " + str(T_ratio(M1)))
    st.write("a2/a1 = " + str(a_ratio(M1)))
    st.write("p02/p01 = " + str(Ps_ratio(M1)))



s = st.selectbox('Select the variable',('M1', 'M2', 'rho2/rho1','P2/P1','p02/p01','a2/a1','T2/T1'))

if(s=='M1'):
    number = st.number_input('Insert a number',min_value=0.001, max_value=None)
    st.write('The current number is ', number)
    M1_print(number)

elif(s == 'M2'):

    x = st.number_input('enter', min_value=0.38, max_value=1.00)
    st.write('The current number is ', x)

    def f(M1, z):
        return M2(M1) - z

    def fx(M1, z):
        return (f(M1, z + 1e-5) - f(M1, z)) / (1e-5)

    def M1_f(z):
        M1 = 1
        x = 0
        while abs(x - M1) > 1e-5:
            x = M1
            M1 = x - f(M1, z) / fx(M1, z)
        return M1
    a = M1_f(x)
    M1_print(a)

elif s == "P2/P1":
    x = st.number_input('Insert a number', min_value=1.00, max_value=None)
    st.write('The current number is ', x)
    a = (((x - 1) / (1.1667)) + 1) ** (0.5)
    M1_print(a)

elif s == "T2/T1":
    x = st.number_input('Insert a number', min_value=1.04, max_value=None)
    st.write('The current number is ', x)
    def f(M1, z):
        return a_ratio(M1) - z
    def fx(M1, z):
        return (f(M1, z + 1e-5) - f(M1, z)) / (1e-5)
    def M1_f(z):
        M1 = 1
        x = 0
        while abs(x - M1) > 1e-5:
            x = M1
            M1 = x - f(M1, z) / fx(M1, z)
        return M1
    a = M1_f(x)
    a = a*a
    M1_print(a)

elif s == "rho2/rho1":
    x = st.number_input('Insert a number', min_value=1.14, max_value=5.992)
    st.write('The current number is ', x)
    def f(M1,z):
        return d_ratio(M1) - z
    def fx(M1,z):
        return (f(M1,z+1e-5) - f(M1,z))/(1e-5)
    def M1_f(z):
        M1 = 1
        x = 0
        while abs(x-M1) > 1e-5:
            x = M1
            M1 = x - f(M1,z)/fx(M1,z)
        return round(M1,2)
    a = M1_f(x)
    M1_print(a)

elif s == "p02/p01":
    x = st.number_input('Insert a number', min_value=0.1, max_value=1.0)
    st.write('The current number is ', x)
    def f(M1,z):
        return Ps_ratio(M1) - z
    def fx(M1,z):
        return (f(M1,z+1e-5) - f(M1,z))/(1e-5)
    def M1_f(z):
        M1 = 1
        x = 0
        while (x-M1) > 1e-5:
            x = M1
            M1 = x - f(M1,z)/fx(M1,z)
        return M1
    a = M1_f(x)
    M1_print(a)

elif s == "a2/a1":
    x = st.number_input('Insert a number', min_value=1.04, max_value=None)
    st.write('The current number is ', x)
    def f(M1,z):
        return a_ratio(M1) - z
    def fx(M1,z):
        return (f(M1,z+1e-5) - f(M1,z))/(1e-5)
    def M1_f(z):
        M1 = 1
        x = 0
        while abs(x-M1) > 1e-5:
            x = M1
            M1 = x - f(M1,z)/fx(M1,z)
        return M1
    a = M1_f(x)
    M1_print(a)
else:
    print("तुम से ना हो पाएगा")
