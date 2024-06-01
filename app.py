import streamlit as st

# Introduction screen
def show_introduction():
    st.title("Anki Cards on Steroids: Revolutionize Your Study Routine with Custom Exercises")
    st.write("""
    Imagine transforming your study notes into a dynamic learning experience that goes beyond traditional flashcards. 
    Welcome to the world of Anki cards on steroids—a cutting-edge approach that takes your Anki cards to the next level. 
    With this innovative tool, you can scan your notes to generate custom exercises tailored to your learning needs. 
    Whether you’re looking to practice conversations, improve your listening skills, or engage in interactive exercises, 
    this method allows you to personalize your study sessions like never before. Say goodbye to monotonous repetition 
    and hello to a more engaging, effective way to master new information. Dive in and discover how you can supercharge 
    your learning with Anki cards on steroids!
    """)
    if st.button("Get Started"):
        st.session_state.page = "user_input"

# User input screen
def user_input():
    st.title("Tell Us About Yourself")
    
    native_language = st.selectbox("What's your native language?", ["English", "Japanese", "Spanish"])
    name = st.text_input("Name")
    learn_language = st.selectbox("What do you want to learn?", ["English", "Japanese", "Spanish"])
    knowledge_level = st.selectbox("Knowledge level", ["Beginner", "Intermediate", "Expert"])

    if st.button("Submit"):
        st.session_state.native_language = native_language
        st.session_state.name = name
        st.session_state.learn_language = learn_language
        st.session_state.knowledge_level = knowledge_level
        st.session_state.page = "confirmation"

# Confirmation screen
def confirmation():
    st.title("Confirmation")
    st.write(f"Name: {st.session_state.name}")
    st.write(f"Native Language: {st.session_state.native_language}")
    st.write(f"Language to Learn: {st.session_state.learn_language}")
    st.write(f"Knowledge Level: {st.session_state.knowledge_level}")

# Main function to control the app flow
def main():
    if 'page' not in st.session_state:
        st.session_state.page = "introduction"

    if st.session_state.page == "introduction":
        show_introduction()
    elif st.session_state.page == "user_input":
        user_input()
    elif st.session_state.page == "confirmation":
        confirmation()

if __name__ == "__main__":
    main()
