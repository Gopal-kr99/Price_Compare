import serpapi
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def compare(med_name):
    params ={
  "engine": "google_shopping",
  "q": med_name,
  "api_key": "73522f26406a5fb42f87524cd33e74abe98b45a68a0a8a3350c405de96e5b9c9",
  "gl":"in"
  }
    search = serpapi.GoogleSearch(params)
    results = search.get_dict()
    shopping_results = results["shopping_results"]
    return shopping_results
    
c1,c2= st.columns(2)
c1.image("e_pharmacy.png")
c2.header("E-pharmacy price comparision system")

# """------------------------------------------------------------"""


st.sidebar.title("Enter name of medicine:")
med_name = st.sidebar.text_input("Enter name here:")
number = st.sidebar.text_input("Enter number of obtains here:")
medcine_comp= []
med_price=[]

if med_name is not None:
    if st.sidebar.button("price compare"):

        shopping_results = compare(med_name)
        lowest_price = float((shopping_results[0].get("price").replace("₹","").replace(",","")))
        print(lowest_price)
        lowest_price_index = 0
        st.sidebar.image(shopping_results[0].get("thumbnail"))


        for i in range(int(number)):
            current_price = float((shopping_results[i].get("price").replace("₹","").replace(",","")))
            medcine_comp.append(shopping_results[i].get("source"))
            med_price.append(float((shopping_results[i].get("price").replace("₹","").replace(",",""))))

            # ------------------------------------------------
            st.title(f"option{i+1}")

            c1,c2= st.columns(2)
            c1.write("Company:")
            c2.write(shopping_results[i].get("source"))

            c1.write("Title:")
            c2.write(shopping_results[i].get("title"))

            c1.write("Price:")
            c2.write(shopping_results[i].get("price"))

            url=shopping_results[i].get("product_link")
            c1.write("Buy Link:")
            c2.write("[Link](%s)"%url)
            """__________________________________________________"""
            if (current_price<lowest_price):
                lowest_price=current_price
                lowest_price_index = i

        # this is best option
        st.title("Best option:")

        c1,c2= st.columns(2)
        c1.write("Company:")
        c2.write(shopping_results[lowest_price_index].get("source"))

        c1.write("Title:")
        c2.write(shopping_results[lowest_price_index].get("title"))

        c1.write("Price:")
        c2.write(shopping_results[lowest_price_index].get("price"))

        url=shopping_results[lowest_price_index].get("product_link")
        c1.write("Buy Link:")
        c2.write("[Link](%s)"%url)

        #---------------------------------------
        # graph comparisions
        df = pd.DataFrame(med_price,medcine_comp)
        st.title("Chat Comparison:")
        st.bar_chart(df)

        fig,ax = plt.subplots()
        ax.pie(med_price,labels=medcine_comp,shadow=True)
        ax.axis("equal")
        st.pyplot(fig)

        
          


