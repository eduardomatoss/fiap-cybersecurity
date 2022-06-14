import streamlit as web


def create_form():
    web.title("🔍 Fraud Mitigation")

    form = web.form(key="form")
    form.form_submit_button("Search")
