# import module
import streamlit as st
import os

# Title
st.title("SpotDL Web GUI")


# box to enter spotify link
link = st.text_input("Enter the link to a spotify song, album, or playlist.")


# choose the format for the songs
songFormat = st.selectbox("Audio Format: ", ['flac', 'mp3', 'wav', 'm4a', 'opus', 'ogg'])


# download location 
downLocation = st.text_input("Type the desired file output path", "/home/noah/Music/spotdl-streamlit")


# instructions for output format customization
st.write("Possible values for the output format:")
st.write("{artist}, {artists}, {title}, {album}, {ext}, {playlist}")


# output file format
outFormat = st.text_input("Output format: ", "'{artist}/{album}/{title} - {artist}.{ext}'")



THE_COMMAND = f"spotdl {link} --output-format {songFormat} --path-template {outFormat} --output {downLocation}"

if(st.button("run command")):
    # print(f"spotdl {link} --output-format {songFormat} --path-template {outFormat} --output {downLocation}")
    os.system(THE_COMMAND)


