import streamlit as st
st.title("BMI Calculator")
st.balloons()

Weight=st.number_input("Enter the weight in Kg")
height=st.radio("Select ur height:",('cm','feet'))

if height=='cm':
    h=st.number_input("Centimeter")
    try:
        BMI=Weight/((h/100)**2)
    except:
        st.text('Enter some weight')
else:
    h=st.number_input('Feet')
    try:
        BMI=Weight/((h/3.28)**2)
    except:
        st.text("enter some values")
if(st.button('Calculate ur BMI')):
    st.text("Your BMI is{}".format(BMI))
    
    if BMI<16:
        st.error('YOU ARE EXTREMELY UNDERWEIGHT,EAT WELL')
    elif BMI >=16 and BMI<18.5:
        st.warning("You are underweight, eat healthy to gain weight")
    elif BMI >=18.5 and BMI<25:
        st.success("HEALTHY, Stay fit")
    elif BMI>=25 and BMI<30:
        st.warning("Overweight, Do workouts")
    elif BMI>=30:
        st.error("OBESITY")
