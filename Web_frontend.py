import streamlit as st
import functions_web

st.title("Members List Application")
st.subheader("Need to add the members list")

st.write("List of Members")

values = functions_web.get_names()

def Add_names():
    Adding = st.session_state['new_members'] + "\n"
    values.append(Adding)
    functions_web.write_names(values)

for index, i in enumerate(values):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        values.pop(index)
        functions_web.write_names(values)
        del st.session_state[i]
        st.experimental_rerun()

st.text_input(label='',placeholder='Add the members',on_change= Add_names,key='new_members')



