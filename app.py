from gettext import npgettext
import numpy
import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))


def predict_forest(oxygen, humidity, temparature):
    inputt = np.array([[oxygen, humidity, temparature]]).astype(np.float64)
    prediction = model.predict_proba(inputt)
    pred = '{0:.{1}f}'.format(prediction[0][0], 2)
    print(type(pred))
    return float(pred)


def main():
    st.title('stramlit')
html_temp = """ 
    <div style="background-color:#025246;padding:10px">
    <h2 style="color:white;text-align:center">Forest Fire Prediction ML App</h2>
    </div>   
    """

st.markdown(html_temp, unsafe_allow_html=True)

oxygen = st.text_input('Oxygen', 'Type Here')
humidity = st.text_input('Humidity', 'Type Here')
temparature = st.text_input('Temparature', 'Type Here')

safe_html = """
      <div style='background-color:#4D03F; padding:10px'>
        <h2 style="color:white;text-align:center">your forest is safe</h2>
        </div>
        
    """

danger_html = """
      <div style='background-color:#F00000; padding:10px'>
        <h2 style="color:black;text-align:center">your forest is in danger</h2>
         </div>
    
    """


if st.button('predict'):
    output = predict_forest(oxygen, humidity, temparature)
    st.success('The probability of fire taking place is {}' .format(output))
    if output > 0.5:
        st.markdown(danger_html, unsafe_allow_html=True)
    else:
        st.markdown(safe_html, unsafe_allow_html=True)
if __name__ == '__main__':
    main()
