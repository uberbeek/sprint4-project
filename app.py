# Import packages
import streamlit as st
import pandas as pd
import plotly.express as px


# Convert integer columns to a type that supports missing values
df['model_year'] = df['model_year'].astype('Int64')
df['cylinders'] = df['cylinders'].astype('Int64')
df['odometer'] = df['odometer'].astype('Int64')
df['is_4wd'] = df['is_4wd'].astype('Int64')


# Import data and extract manufacturer from model column
df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].str.split().str[0]
df['design'] = df['model'].str.split().str[1:].str.join(' ')


# Display the dataframe
st.header('Vehicle Data')
st.dataframe(df)


# Display bar chart of manufacturer by condition
st.header('Manufacturer by Condition')
st.write(px.histogram(df, x='manufacturer', color='condition'))


# Display bar chart of vehicly type by paint color
st.header('Vehicle Type by Paint Color')
category_order = {
    "paint_color": ["custom", "black", "grey", "silver", "white", "brown", "purple", "blue", "green", "yellow", "orange", "red"]
}
color_map = {
    "red": "red",
    "orange": "orange",
    "yellow": "yellow",
    "green": "green",
    "blue": "blue",
    "purple": "purple",
    "brown": "brown",
    "white": "#f0f0f0",
    "silver": "silver",
    "grey": "grey",
    "black": "black",
    "custom": "pink"
}
st.write(px.histogram(df, x='type', color='paint_color',
         color_discrete_map=color_map, category_orders=category_order))


# Display histogram of odometer by type with a checkbox for outlyers > 300,000 miles
st.header('Histogram of Odometer by Type')

show_outliers = st.checkbox('Include outliers with > 300,000 miles')
df_filtered_by_odometer = df if show_outliers else df[df['odometer'] < 300000]

st.write(px.histogram(df_filtered_by_odometer, x='odometer', color='type'))


# Display scatterplot of price by model year with a checkbox for model years since 1960
st.header('Scatter Plot of Price by Model Year')

show_before_1960 = st.checkbox('Include vehicles from before 1960')
df_filtered_by_year = df if show_before_1960 else df[df['model_year'] >= 1960]

st.write(px.scatter(df_filtered_by_year,
         x='model_year', y='price'))


# Display histograms for designs of the selected manufacturer and type
st.header(
    'Compare the Price Distribution for Designs of Selected Manufacturer and Type')

manufac_list = sorted(df['manufacturer'].unique())
manufacturer_selected = st.selectbox('Select Manufacturer',
                                     manufac_list, index=manufac_list.index('chevrolet'))

eligible_types = sorted(
    df[df['manufacturer'] == manufacturer_selected]['type'].unique())
if 'type_selected' not in st.session_state or st.session_state['type_selected'] not in eligible_types:
    st.session_state['type_selected'] = eligible_types[0]
type_selected = st.selectbox('Select Vehicle Type', eligible_types,
                             index=eligible_types.index(st.session_state['type_selected']))
st.session_state['type_selected'] = type_selected

mask_filter = (df['manufacturer'] == manufacturer_selected) & (
    df['type'] == type_selected)
df_filtered_by_make_type = df[mask_filter]

normalize = st.checkbox('Normalize histogram', value=True)
histnorm = 'percent' if normalize else None

st.write(px.histogram(df_filtered_by_make_type,
                      x='price',
                      nbins=30,
                      color='design',
                      histnorm=histnorm,
                      barmode='overlay'))
