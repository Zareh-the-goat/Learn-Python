import streamlit as st
st.title("Title")
st.header("Header")
st.subheader("Subheader")
st.text("Text")
st.markdown("Markdown")
st.write("Write")
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)
st.write(range(10))
if st.checkbox("Show/Hide"):
    st.info("Showing the widget")
status = st.radio("Select a gender:", ['Male','Female','Not telling'])
if status == 'Male':
    st.success("Male")
elif status == 'Female':
    st.success("Female")
else:
    st.success("No Problem")
hobby = st.selectbox("Select a hobby:", ['Dancing','Reading', 'Sports'])
st.write("Your Hobby is", hobby)
hobbies = st.multiselect("Select your hobbies", ['Dancing','Reading', 'Sports','Games','Sleep'])
st.write("You Selected", len(hobbies), "Hobbies")
st.title('Guess')
st.button("Click me! ho")
st.button("Click me! he")
st.button("Click me! (")
if st.button("Click me! (:"):
    st.subheader('Correct :)')
st.button("Click me! :(")
st.button("Click me!):")
st.button("Click me! hi")
name = st.text_input("Enter your name", "Type Here")
if st.button("Submit"):
    result = name.title()
    st.success(result)
level = st.slider("Choose you age", min_value=1, max_value = 1000000 )
st.write(f"Selected age: {level}")




