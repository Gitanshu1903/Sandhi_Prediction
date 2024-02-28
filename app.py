import streamlit as st
import yfinance as yf
import pandas as pd


def sandhi_splitter(mystring):
    mylist = list()
    mydic = dict()
    for x in [5,4,3,2,1]:
        for i in df[df['c'].str.len() == x].c:
            if i in mystring:
                repc = df[df['c'] == i]['a'] + ' ' + df[df['c'] == i]['b']
                repc2 = ' '.join(repc.tolist())
                mylist.append(mystring.replace(i, repc2))
    return set(mylist)

def _sandhi_builder(my):
    mylist = list()
    for i in my.split():
        mylist.append(i)
        
    final = list()
    nelist = list()
    check = mylist[0] + ' ' + mylist[1]
    for i in [8,7,6,5,4,3,2,1]:
        for p in [0,1,2,3,4,5,6,7]:
            x = mylist[0][-i:]
            y = mylist[1][:p]
            if len(x) > 0 and len(y) > 0:
                try:
                    z = df[(df['a'] == x) & (df['b'] == y)]['c']
                    if len(z) > 0:
                        for myr in z:
                            myt = [mylist[0][-i:], mylist[1][:p]]
                            final.append(check.replace(' '.join(myt), myr))
                except:
                    pass
    return set(final)

r_upsarg = ['प्र', 'परि', 'प्रति', 'दुर्', 'निर्']

def sandhi_builder(x):
    sandhi_long = x.split()
    
    for i in r_upsarg:
        if sandhi_long[0] == i:
            sandhi_long[1] = sandhi_long[1].replace('न', 'ण')
    
    return_set = set([sandhi_long[0]])  # Initialize with the first word

    for lr in range(1, len(sandhi_long)):
        tmp_list = []
        for eachv in return_set:
            return_set2 = _sandhi_builder(eachv + ' ' + sandhi_long[lr])
            if return_set2:
                tmp_list.extend(return_set2)
            else:
                tmp_list.append(eachv + sandhi_long[lr])
        return_set = set(tmp_list)

    return return_set

if __name__ == "__main__":
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1528715471579-d1bcf0ba5e83?q=80&w=2093&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    background-size: cover;  
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    st.title("Sandhi Prediction App")
    input_text = st.text_input("Enter Sanskrit Words", "श्रीमत् हि")

    if st.button("Prediction"):
        df = pd.read_csv('data_v1.txt', delim_whitespace=True, low_memory=True, header=None)
        df.columns = ['a', 'b','c', 'd', 'e']

        final_result = sandhi_builder(input_text)
        st.write("Final Result:")
        st.code(final_result)

