import streamlit as st
import pickle
import csv
from matplotlib import pyplot as plt
from matplotlib import style
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image

with st.sidebar:
    selected = option_menu(
        menu_title='Main Menu',
        options=['Predictions','Past Data','Contact Us','About Us'],
        menu_icon='cast',
        icons=['activity','file-bar-graph','phone','file-person-fill'],
    )
if selected == 'Predictions':
    ## CSS
    st.title('Tourist Prediction Using ML')

    page_background='''<style>
    [data-testid="stAppViewContainer"]{
    background-color: lightblue;
    }
    #MainMenu{visibility: hidden;}
    footer{visibility: hidden;}
    </style>'''
    st.markdown(page_background,unsafe_allow_html=True)
    ## CSS - end 

    ## Variables
    opt1 = st.selectbox(
        'Select the Season',
        ('SUMMER', 'WINTER', 'MONSOON','AUTUMN'))
    # st.write('You selected:', opt1)
    opt2 = st.selectbox('Select a State', ['Andhra Pradesh', 'Arunachal Pradesh', 
                                            'Assam' , 'Bihar', 'Chhattisgarh', 'Goa', 
                                            'Gujarat', 'Himachal Pradesh', 'Haryana', 
                                            'Jharkhand', 'Jammu and Kashmir', 'Karnataka', 
                                            'Kerala', 'Maharashtra', 'Manipur', 'Meghalaya', 
                                            'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 
                                            'Sikkim', 'Telangana', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 
                                            'Uttar Pradesh', 'West Bengal'])
    ## Variables - end


    # TESTING CODE ## START
    season = {'SUMMER': 0, 'WINTER': 1, 'MONSOON': 2, 'AUTUMN': 3}
    seasons = season[opt1]
    states = {'Andhra Pradesh':'AP', 'Arunachal Pradesh':'AR', 'Assam':'AS', 'Bihar':'BR',
              'Chhattisgarh':'CG', 'Goa':'GA','Gujarat':'GJ', 'Himachal Pradesh':'HP', 'Haryana':'HR', 
              'Jharkhand':'JH', 'Jammu and Kashmir':'JK', 'Karnataka':'KA','Kerala':'KL', 'Maharashtra':'MH',
              'Meghalaya':'ML','Manipur':'MN', 'Madhya Pradesh':'MP','Mizoram':'MZ', 'Nagaland':'NL',
              'Odisha':'OR', 'Punjab':'PB', 'Rajasthan':'RJ','Sikkim':'SK', 'Telangana':'TG', 'Tamil Nadu':'TN',
              'Tripura':'TR', 'Uttarakhand':'UK','Uttar Pradesh':'UP', 'West Bengal':'WB'}
    state = states[opt2]
    fields = ['Year', 'Seasons', 'States', 'Visitors']
    rows = []

    array = ['AP', 'AR', 'AS', 'BR', 'CG', 'GA', 'GJ', 'HP',
             'HR', 'JH', 'JK', 'KA', 'KL', 'MH', 'ML', 'MN',         
             'MP', 'MZ', 'NL', 'OR', 'PB', 'RJ', 'SK', 'TG',
             'TN', 'TR', 'UK', 'UP', 'WB']

    constate=0 #converted state
    for i in array:
        if i==state:
            break
        constate+=1

    csv_file = csv.reader(open('CSVfiles//tourist_data.csv', 'r'))
    for i in csv_file:
        if i[1] == str(seasons) and i[2] == state:
            rows.append(i)

    with open('CSVfiles//Original_data.csv', 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    with open('Tourist_prediction.pkl', 'rb') as file:
        my = pickle.load(file)

    with open('CSVfiles//Predicted_data.csv', 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        for i in range(2001, 2024):
            prediction = int(my.predict([[i, seasons, constate]]))
            csvwriter.writerow([i, seasons, state, prediction])

    st.subheader('Predictions and Original Data')
    fig = plt.figure(figsize=(12, 6))
    original = pd.read_csv('CSVfiles//Original_data.csv')
    predicted = pd.read_csv('CSVfiles//Predicted_data.csv')
    plt.plot(original['Year'], original['Visitors'],'--b',color='r',label='Original Data')
    plt.plot(predicted['Year'], predicted['Visitors'], color='g',label='Predicted Data')
    plt.xlabel('Year')
    plt.ylabel('Visitors')
    plt.legend(bbox_to_anchor=(0.25,1),borderpad=2)
    plt.grid(True, color='k')
    plt.show()
    st.pyplot(fig)
    # TESTING CODE ## END



####################################################



if selected == 'Past Data':
    ## CSS
    st.title('Review Past Data Here')

    page_background='''<style>
    [data-testid="stAppViewContainer"]{
    background-color: lightblue;
    }
    #MainMenu{visibility: hidden;}
    footer{visibility: hidden;}
    </style>'''
    st.markdown(page_background,unsafe_allow_html=True)
    ## CSS - end 

    ## Variables
    opt1 = st.selectbox(
        'Select the Season',
        ('SUMMER', 'WINTER', 'MONSOON','AUTUMN'))
    # st.write('You selected:', opt1)
    opt2 = st.selectbox('Select a State', ['Andhra Pradesh', 'Arunachal Pradesh', 
                                            'Assam' , 'Bihar', 'Chhattisgarh', 'Goa', 
                                            'Gujarat', 'Himachal Pradesh', 'Haryana', 
                                            'Jharkhand', 'Jammu and Kashmir', 'Karnataka', 
                                            'Kerala', 'Maharashtra', 'Manipur', 'Meghalaya', 
                                            'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 
                                            'Sikkim', 'Telangana', 'Tamil Nadu', 'Tripura', 'Uttarakhand', 
                                            'Uttar Pradesh', 'West Bengal'])
    ## Variables - end


    # TESTING CODE ## START
    season = {'SUMMER': 0, 'WINTER': 1, 'MONSOON': 2, 'AUTUMN': 3}
    seasons = season[opt1]
    states = {'Andhra Pradesh':'AP', 'Arunachal Pradesh':'AR', 'Assam':'AS', 'Bihar':'BR',
              'Chhattisgarh':'CG', 'Goa':'GA','Gujarat':'GJ', 'Himachal Pradesh':'HP', 'Haryana':'HR', 
              'Jharkhand':'JH', 'Jammu and Kashmir':'JK', 'Karnataka':'KA','Kerala':'KL', 'Maharashtra':'MH',
              'Meghalaya':'ML','Manipur':'MN', 'Madhya Pradesh':'MP','Mizoram':'MZ', 'Nagaland':'NL',
              'Odisha':'OR', 'Punjab':'PB', 'Rajasthan':'RJ','Sikkim':'SK', 'Telangana':'TG', 'Tamil Nadu':'TN',
              'Tripura':'TR', 'Uttarakhand':'UK','Uttar Pradesh':'UP', 'West Bengal':'WB'}
    state = states[opt2]
    fields = ['Year', 'Seasons', 'States', 'Visitors']
    rows = []

    csv_file = csv.reader(open('CSVfiles//tourist_data.csv', 'r'))
    for i in csv_file:
        if i[1] == str(seasons) and i[2] == state:
            rows.append(i)

    with open('CSVfiles//Original_data.csv', 'w', newline='') as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)

    st.subheader('Past Data')
    fig = plt.figure(figsize=(12, 6))
    original = pd.read_csv('CSVfiles//Original_data.csv')
    plt.plot(original['Year'], original['Visitors'],color='r',label='Original Data')
    plt.xlabel('Year')
    plt.ylabel('Visitors')
    plt.grid(True, color='k')
    plt.show()
    st.pyplot(fig)
    # TESTING CODE ## END



#############################################




if selected == 'Contact Us':
    st.header(':mailbox: Get in touch with the creators!')

    page_background='''<style>
    [data-testid="stAppViewContainer"]{
    background-color: lightblue;
    }
    #MainMenu{visibility: hidden;}
    footer{visibility: hidden;}
    </style>'''
    st.markdown(page_background,unsafe_allow_html=True)
    ## CSS - end

    contact_form='''
    <form action="https://formsubmit.co/manojishan19@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Details of your problem"></textarea>
        <button type="submit">Send</button>
    </form>'''
    st.markdown(contact_form,unsafe_allow_html=True)

    #Use local css
    def local_css(file):
        with open(file) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

    local_css("style.css")



#############################################



if selected == 'About Us':
    ## CSS
    st.title("Meet the creators!")
    page_background='''<style>
    [data-testid="stAppViewContainer"]{
    background-color: lightblue;
    }
    #MainMenu{visibility: hidden;}
    footer{visibility: hidden;}
    .about-us-text {
        color: black;
    }
    .about-us-columns {
        color: black;
    }
    </style>'''
    st.markdown(page_background, unsafe_allow_html=True)
    ## CSS - end 

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('photos//Ishan.png', caption='Ishan    (210305105726)', width=100,)

    with col2:
        st.image('photos//priyanshul.png', caption='priyanshul  (210305105711)', width=100)

    with col3:
        st.image('photos//deepak.png', caption='deepak  (210305105709)', width=100)

    with col4:
        st.image('photos//dipanshu.png', caption='dipanshu   (210305105708)', width=100)

    st.markdown("<div class='about-us-columns'>Welcome to our Tourist Prediction System! We are a team of travel enthusiasts who are passionate about helping tourists make the most out of their trips. Our system uses advanced machine learning models to analyze tourist data.</div>", unsafe_allow_html=True)
    st.markdown("<div class='about-us-columns'>Our team has worked hard to create a system that is easy to use, accurate, and reliable. We have also developed our own algorithms to analyze this data and generate accurate predictions for each tourist.</div>", unsafe_allow_html=True)
    st.markdown("<div class='about-us-columns'>Our mission is to make travel planning easier and more enjoyable for everyone. We believe that travel is one of life's greatest experiences, and we want to help tourists make the most out of their trips. Whether you're planning a romantic getaway, a family vacation, or a solo adventure, our system can help you find the perfect destination which suits your preferences.</div>", unsafe_allow_html=True)
    st.markdown("<div class='about-us-columns'>We are committed to providing the best possible service to our users. If you have any questions or feedback about our system, please don't hesitate to contact us. We are always looking for ways to improve our system and make it even better for our users.</div>", unsafe_allow_html=True)
    st.markdown("<div class='about-us-columns'>Thank you for choosing our Tourist Prediction System for your travel planning needs. We hope you have a wonderful and unforgettable trip!</div>", unsafe_allow_html=True)
