import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

def login():
    with open(r'pages\utils\user_config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)


    # Pre-hashing all plain text passwords once
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )

    cols = st.columns(2)

    #login [widget]
    with cols[0]:
        try:
            authenticator.login()
        except Exception as e:
            st.error(e)


    # #guest login button --> needs 2Oath implementation in password config (NOT IMPLEMENTED)
    # try:
    #     authenticator.experimental_guest_login('Login with Google',
    #                                            provider='google',
    #                                            oauth2=config['oauth2'])
    #     authenticator.experimental_guest_login('Login with Microsoft',
    #                                            provider='microsoft',
    #                                            oauth2=config['oauth2'])
    # except Exception as e:
    #     st.error(e)


    #authenticating users
    if st.session_state['authentication_status']:
        authenticator.logout(location="sidebar")
    elif st.session_state['authentication_status'] is False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] is None:
        st.warning('Please enter your username and password')


    #forgot password [widget]
    if not st.session_state['authentication_status']:
        with cols[1]:
            try:
                username_of_forgotten_password, \
                email_of_forgotten_password, \
                new_random_password = authenticator.forgot_password()
                if username_of_forgotten_password:
                    st.success('New password to be sent securely')
                    # The developer should securely transfer the new password to the user. (NOT IMPLEMENTED)
                elif username_of_forgotten_password == False:
                    st.error('Username not found')
            except Exception as e:
                st.error(e)

    #st.write("---")

    #register new users [widget]
    if not st.session_state['authentication_status']:
        try:
            email_of_registered_user, \
            username_of_registered_user, \
            name_of_registered_user = authenticator.register_user(pre_authorized=config['pre-authorized']['emails'])
            if email_of_registered_user:
                st.success('User registered successfully')
        except Exception as e:
            st.error(e)


    #Update user preferences

    #reset password [widget] --> MOVE TO SETTINGS (if we want to keep these)

    # if st.session_state['authentication_status']:
    #     try:
    #         if authenticator.reset_password(st.session_state['username']):
    #             st.success('Password modified successfully')
    #     except Exception as e:
    #         st.error(e)


    #create an updated user details [widget] --> MOVE TO SETTINGS TAB (if we want to keep these)

    # if st.session_state['authentication_status']:
    #     try:
    #         if authenticator.update_user_details(st.session_state['username']):
    #             st.success('Entries updated successfully')
    #     except Exception as e:
    #         st.error(e)


    #resaves to config file when contents are modified
    with open(r'pages\utils\user_config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
