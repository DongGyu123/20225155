import i18n
import streamlit as st

from utils.init import init_once


if __name__ == '__main__':
    # Init
    init_once()

    # Show title
    st.title(i18n.t('Today \'s Fortune'))

    # Show page description
    st.write(i18n.t('Telling user\'s fortune of today with LLM in the guise of an fortune teller'))

    # Show github link
    st.write(f'* Github: {i18n.t('https://github.com/DongGyu123/20225155.git')}')
