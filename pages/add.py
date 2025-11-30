import streamlit as st
from stocks import Stocks

st.title("Add Burger Ingredient")

ingredient_name = st.text_input("Ingredient Name")
ingredient_quantity = st.number_input("Quantity", min_value=0, step=1)
ingredient_price = st.number_input(
    "Price per Unit", min_value=0.0, format="%.2f", step=0.01)

if st.button("Add Ingredient"):
    # Validation
    if not ingredient_name:
        st.error("Please enter an ingredient name!")
    elif ingredient_quantity == 0:
        st.warning("Quantity should be greater than 0")
    elif ingredient_price == 0.0:
        st.warning("Price should be greater than 0")
    else:
        new_ingredient = Stocks(
            ingredient_name, ingredient_quantity, ingredient_price)

        st.success(f"Successfully added **{new_ingredient.getName()}**!")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Ingredient", new_ingredient.getName())
        with col2:
            st.metric("Quantity", f"{new_ingredient.getQuantity()}")
        with col3:
            st.metric("Price/Unit", f"${new_ingredient.getPrice():.2f}")
        with col4:
            st.metric("Total Value",
                      f"${new_ingredient.calculateTotalValue():.2f}")

        # TODO: Save the to a database or file system
