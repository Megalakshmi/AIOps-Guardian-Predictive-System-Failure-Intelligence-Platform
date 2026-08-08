import streamlit as st
from analysis import run_analysis
from email_alert import send_email

st.set_page_config(page_title="AIOps Guardian")

st.title("🛡️ AIOps Guardian")

if "report" not in st.session_state:
    st.session_state.report = None

if st.button("Analyse System"):
    st.session_state.report = run_analysis()

if st.session_state.report:

    data = st.session_state.report

    st.text(data["summary"])

    st.subheader("Root Cause(s)")
    for c in data["root_causes"]:
        st.write(f"- {c}")

    st.subheader("Identified Error Type(s)")
    for e in data["error_types"]:
        st.write(f"- {e}")

    st.subheader("Recommended Action")
    st.write(data["action"])

    st.write("---")
    st.write("Did you resolve the issue?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("YES"):
            st.success("Issue resolved. No escalation required.")

    with col2:
        if st.button("NO"):
            st.error("Resolution Status: Automatic resolution not possible")
            st.write("Severity: CRITICAL")
            st.write("Escalation Required: YES")
            st.write("Assigned Team: Infrastructure / DevOps")

            send_email(data)

            st.success("Email sent successfully")