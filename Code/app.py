import streamlit as st
import time

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(
    page_title="Project Unlock Portal",
    page_icon="🚀",
    layout="wide"
)

# -------------------------
# HEADER
# -------------------------
st.title("🚀 Welcome to the Learning Project Portal")
st.subheader("Register to unlock exciting projects!")

st.write("---")

# -------------------------
# SESSION STATE
# -------------------------
if "registered" not in st.session_state:
    st.session_state.registered = False

# -------------------------
# REGISTRATION FORM
# -------------------------
if not st.session_state.registered:

    col1, col2 = st.columns([1,1])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
            width=True
        )

    with col2:

        with st.form("registration_form"):

            st.subheader("📝 Registration Form")

            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            profession = st.selectbox(
                "Profession",
                ["Student", "Engineer", "Developer", "Data Scientist", "Other"]
            )

            experience = st.slider(
                "Python Experience (Years)",
                0,10,1
            )

            interest = st.multiselect(
                "Areas of Interest",
                ["AI", "Cloud", "DevOps", "Data Science", "Web Apps"]
            )

            bio = st.text_area("Tell us about yourself")

            submit = st.form_submit_button("🚀 Unlock Projects")

        if submit:
            st.session_state.registered = True
            st.session_state.name = name
            st.balloons()

            st.success("Registration successful!")

            time.sleep(1)
            st.rerun()

# -------------------------
# AFTER REGISTRATION
# -------------------------
else:

    st.success(f"🎉 Congratulations {st.session_state.name}!")

    st.header("You unlocked some amazing projects!")

    st.write(
        """
        You now have access to some exciting learning projects.
        Watch the videos below to start building powerful apps!
        """
    )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📚 Project 1")
        st.video("https://youtu.be/6Vx4DuW_g4A")

    with col2:
        st.subheader("📚 Project 2")
        st.video("https://youtu.be/dMAqqhX3Esk")

    st.write("---")

    if st.button("Register another user"):
        st.session_state.registered = False
        st.rerun()