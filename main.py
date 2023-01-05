import time
import streamlit as st
import pickle
import pandas as pd
import requests
with st.sidebar:
        from PIL import Image
        image = Image.open('vitttaplogo.jpg')
        st.image(image,width=300)
    
        from streamlit_lottie import st_lottie
        from streamlit_lottie import st_lottie_spinner

        def load_lottieurl(url: str):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()
        lottie_url = "https://assets6.lottiefiles.com/packages/lf20_1pxqjqps.json"
        lottie_json = load_lottieurl(lottie_url)
        st_lottie(lottie_json)
# Our Team Guide and memebers
with st.sidebar:
    st.subheader(':red[Dr.Abdul Kalam Azad Sir]')
    st.subheader(':blue[BOLISETTY SURYA PRAKASH]')
    st.subheader(':blue[NAGA SAI SASI KIRAN KAKARAPARTHI]')
    st.subheader(':blue[ SOMU CHANDRA KIRAN REDDY]')
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=56e843adb999419e51c3da4b3df4410d&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500" + data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
    recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
    recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System 🎥')
selected_movie_name = st.selectbox(
'Enjoj your Movies',
movies['title'].values)
if st.button('Recommend "👈"'):
  names,posters= recommend(selected_movie_name)
  with st.spinner('Loading...'):
    time.sleep(3)
  with st.spinner('Grab a snacks'):
    time.sleep(3)
  with st.spinner('Still Loading..'):
    time.sleep(2)
  with st.spinner('Please Wait...'):
    time.sleep(2)
    st.success('Done!')
    st.success('Here is the relevant results!', icon="✅")
    col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
      st.text(names[0])
      st.image(posters[0])
  with col2:
      st.text(names[1])
      st.image(posters[1])

  with col3:
      st.text(names[2])
      st.image(posters[2])
  with col4:
      st.text(names[3])
      st.image(posters[3])
  with col5:
      st.text(names[4])
      st.image(posters[4])
st.write(""" audio """)
audio1 = open("ttsMP3.com_VoiceText_2022-11-25_14_41_10.mp3","rb")
st.audio(audio1)
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()
st.time_input('Meeting time')
