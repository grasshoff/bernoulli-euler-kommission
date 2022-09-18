import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

hide_st_style = """
    <style>
    MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .css-18e3th9 {
                padding: 0rem 0rem 0rem;
            }
    .css-1v3fvcr {
                margin-top: -20px;
                padding: 0rem 0rem 0rem;
            }
    .css-12oz5g7 {
                margin-top: -0px;
                padding: 0rem 0rem 0rem;
                max-width: 146rem
            }
    </style>
    """
st.markdown(hide_st_style, unsafe_allow_html=True)

if st.session_state.get('series', None) is None:
    st.session_state['series'] = "Series I"


df = pd.read_json("eulerOO_df.json")
df= df[["vol", "title", "editor", "year", "publ", "isbn_neu", "pages"]]



def ag_opt(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    #gb.configure_default_column(enablePivot=True, enableValue=True, enableRowGroup=True)
    gb.configure_pagination(paginationAutoPageSize=True)
    #gb.configure_auto_height(autoHeight=True)
    gb.configure_selection(selection_mode="multiple", use_checkbox=False, rowMultiSelectWithClick=True, suppressRowDeselection=False)

    gb.configure_side_bar()
    return gb.build()


st.session_state.series=st.radio("",["Series I","Series II","Series III","Series IV"],horizontal=True)

sels = {"Series I": f"^I \d", "Series II": f"^II \d", "Series III": f"^III \d", "Series IV": "^IV"}

selst=sels[st.session_state.series]

dfs=df[df["vol"].str.contains(selst,regex=True)]
go=ag_opt(dfs)
res=AgGrid(dfs,gridOptions=go,height=400,
    theme='streamlit')
st.write("Selection",res["selected_rows"])