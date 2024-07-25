import streamlit as st
import pickle
import numpy as np
import sklearn
# pipe=pickle.load(open('pipe.pkl','rb'))
# df=pickle.load(open('df.pkl','rb'))

# st.title("Laptop Price Predictor")

# company=st.selectbox("Brand",df['Company'].unique())

# type=st.selectbox("Type",df['TypeName'].unique())

# ram=st.selectbox("Ram(in GB)",[2,4,6,8,12,16,32,64])

# weight=st.number_input("Weight")

# touchscreen = st.selectbox("TouchScreen",['No','Yes'])

# IPS = st.selectbox("IPS",['No','Yes'])

# screen_size = st.number_input("Screen Size")

# resolution= st.selectbox("Resolution",['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2800x1800','2560x1600','2560x1440','2304x1440'])

# cpu=st.selectbox("CPU",df['Cpu Brand'].unique())

# hdd=st.selectbox("HDD(in GB)",[0,128,256,512,1024,2048])

# sdd=st.selectbox("SDD(in GB)",[0,8,128,256,512,1024])

# gpu=st.selectbox("GPU",df['Gpu_Brand'].unique())

# os=st.selectbox("OS Type",df['os'].unique())

# if st.button('Predict'):
#     ppi=None
#     if touchscreen=="Yes":
#         touchscreen=1
#     else:
#         touchscreen=0
#     if IPS == "Yes":
#         IPS=1
#     else: 
#         IPS=0
# X_res=int(resolution.spli('x')[0])
# Y_res=int(resolution.spli('x')[1])
# ppi=((X_res**2)+(Y_res**2))**0.5/screen_size
# query=np.array([company,type,ram,weight,touchscreen,IPS,ppi,cpu,hdd,sdd,gpu,os])

# query =query.reshape(1,12)
# st.title("the predicted price of this laptop is "+ str(int(np.exp(pipe.predict(query)[0]))))

print(f"NumPy version: {np.__version__}")
print(f"scikit-learn version: {sklearn.__version__}")