import streamlit as st
from stpages import dashboard, signup, login, personalization, expense_page, chatbot
import tools
import remove_footer
if __name__ == "__main__":
    # Initialization
    if 'page' not in st.session_state:
        st.set_page_config(page_title="AI Finance")
        st.session_state.page = 'dashboard'
    page = st.session_state.page

    if page == 'dashboard':
        dashboard.run()
    elif page == 'signup':
        signup.run()
    elif page == 'login':
        login.run()
    elif page == 'personalization':
        personalization.run()
    elif page == 'expense_page':
        expense_page.run()
    elif page == 'chatbot':
        chatbot.run()

    if page == 'signup' or page == 'login':
        st.sidebar.button("Introduction", on_click=tools.change_page('dashboard'))
        #st.sidebar.markdown("Authentication")
        st.sidebar.button("Login Form", on_click=tools.change_page('login'))
        st.sidebar.button("Sign Up Form", on_click=tools.change_page('signup'))
        st.sidebar.button("Personalization", on_click=tools.change_page('personalization'))
        st.sidebar.button("Expense Allocation", on_click=tools.change_page("expense_page"))
    remove_footer.run()