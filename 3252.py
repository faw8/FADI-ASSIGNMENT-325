#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import io
import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import scipy as sp
import plotly.graph_objects as go
import plotly.figure_factory as ff
import plotly as plt
import matplotlib.pyplot as pl

df = pd.read_csv("2015.csv")
Nav = st.sidebar.radio("Navigation", ["Introduction","Look at Dataframe", "Null Values", "Happiness Bar", "Govermental factors of Happiness", "Life Quality factors of Happiness", "Cultural Values Horizontal Bar", "Animated ScatterPlot","3D Model","ScatterPlot", "Freedom and GovTrust Histogram", "Findings Summary", "Dataset Visualizations"])
if Nav== "Introduction":
    
 st.header("Introduction")
 st.subheader("Fadi Wassouf 325 Assignment")   
 col1,col2,col3 = st.columns([1000,10,900])
 with col1:
  st.markdown("""Welcome to my first Streamlit App! Today we're going to take a glance about what mostly affects Happiness among countries and regions.
     Is it monetary value? Is it Family precense? Or is it more related to freedom and trusting the leaders of your country? 
     And finally, are there any differences in the importance of these values among different cultures?""")
  with col3:
   st.image('happiness.jpg')
  choose_one = st.multiselect("Which one is your happiness source:",('Money','Family','Freedom','Goverm.Trust')) 
  st.write("Your choice is:", choose_one)  
if Nav == "Look at Dataframe":

 st.title("World Happiness Indicators")
 st.header('1. Table of The DataFrame')

#Table
#Only the First 15 rows where chosen to reduce the space on Streamlit
 table = ff.create_table(df.head(15))
 st.write(table)
 st.markdown("Only the first 15 rows where chosen inorder to save space")

if Nav== "Null Values":

#To make sure we dont have Null values
 st.header("2. Checking for Null Values")
 st.write(df.isna().any())

 st.markdown("There are no Null Values in the Dataframe")

if Nav == "Happiness Bar":

 st.header("3. A Bar Graph Displaying the Countries with their Relative Happiness Score ")
 bar1= [go.Bar(x=df.Country,
            y=df.HappinessS)]
 st.plotly_chart(bar1)
 st.markdown("Countries like Switzerland rank amongst the countries with the highest Happiness Score (7.6), whereas countries like Syria are on the other side of the spectrum, with a Happiness Score of about 3.")

if Nav == "Govermental factors of Happiness":

 
#Bar plot showing the effect of Governmental factors upon happiness in different countries
 st.header("4. Countries' Happiness in Relation to Govermental Factors")

 GDP_effect = go.Bar(x=df.Country,
                  y=df["Econ(GDP/C)"],
                  width=1,
                  name='GDP',
                  marker=dict(color='Red'))

 Freedom_effect = go.Bar(x=df.Country,
                y=df.Freedom,
                width=1,
                 name='Freedom',
                marker=dict(color='Blue'))

 Gov_effect = go.Bar(x=df.Country,
                y=df["TrustGov"],
                width=1,
                opacity=0.6,
                name='TrustGov',
                marker=dict(color='Yellow'))

 data = [GDP_effect,Freedom_effect,Gov_effect]

 layout = go.Layout(title="Countries Happiness based on GDP,Freedom, and Governmental Trust",
                xaxis=dict(title='Countries'),
                yaxis=dict(title='Governmental Effects'))

 bar2 = go.Figure(data=data, layout=layout)

 st.plotly_chart(bar2)
 st.markdown("""As shown, having a high GDP per capita (red) has the highest effect upon people's happiness among all countries almost.
Second comes the Freedom given by the government (blue), followed by the extent to which people trust their governments (yellow)""")
#Bar plot showing the effect of personal and life factors upon happiness in different countries
if Nav == "Life Quality factors of Happiness": 
 st.header("5 Countries' Happiness in Relation to Life Quality Indicators")
 Family_effect = go.Bar(x=df.Country,
                  y=df["Family"],
                  width=1,
                  name='Family',
                  marker=dict(color='red'))

 LifeExp_effect = go.Bar(x=df.Country,
                y=df["LifeExp"],
                width=1,
                 name='LifeExp',
                marker=dict(color='blue'))

 Generosity_effect = go.Bar(x=df.Country,
                y=df["Generos."],
                width=1,
                opacity=0.6,
                name='Generosity',
                marker=dict(color='yellow'))

 data = [Family_effect,LifeExp_effect,Generosity_effect]

 layout = go.Layout(title="Countries Happiness based on Family, Life Expectancy, and Generosity",
                xaxis=dict(title='Countries'),
                yaxis=dict(title='Life Quality Effects'))

 bar3 = go.Figure(data=data, layout=layout)
 st.plotly_chart(bar3)

 st.markdown("""As for the Life quality indicators,having a Family seems to have a high relevance to people's happiness, followed by the average life expectancy in each country.
Last comes the generosity amongst each country's people as an indicator of happiness.""")

if Nav ==  "Cultural Values Horizontal Bar":
 st.header("6. Visualizing What Each Culture/Region Value")
 bar4 = px.bar(df, x=["Econ(GDP/C)","Freedom","Family","TrustGov","LifeExp","Generos."], y="Region", title="The Effect of All Variables From a Cultural Point of View")
 st.plotly_chart(bar4)

 st.markdown("""Since each region have cultural similarities among its countries, we can display what each culture/region values in terms of affecting their happiness.
Although almost all regions value the same indicators with similar importance (proportionally with their happiness score), some have significant differences.Sub Saharan African region and Western Europe have very close happiness scores.However, it is noticeable that the Sub-Saharan African region considers family presence as the main indicator of Happiness, whereas Western Europe puts more value on the GDP/ capita """) 



if Nav== "Animated ScatterPlot":

 st.header("7. Animated scatter plot locating the countries of each region on the scale of GDP,LifeExp, and Freedom in Happiness Determination")

 fig2=px.scatter(df, x="Econ(GDP/C)", y="LifeExp", animation_frame="Region", animation_group="Country",
           size="HappinessS", color="Freedom", hover_name="Country", title="GDP, Life Expectancy,and Freedom in terms of Detecting Happiness",
           log_x=True, size_max=55, range_x=[0.1,1], range_y=[0.1,1])
 st.plotly_chart(fig2)
 st.markdown("""The above scatter displays the countries in each region (represented by a circle), and their position on the scales of GDP/capita and Life Expectancy. 
The color of the circle also represents an indicator, which is freedom.
Finally, the size of the circle represents the happiness score of the relative country.
This animation highly aids in vosualizing which indicator effects the happiness of a country the most.
For example, some countries are located at the top-right of the graph with a light color, indicating a high GDP/capita, high Life Expectancy, and high levels of Freedom. Typically, they also have a bigger size (a higher happiness score) """)

# A 3D model dispalying the scattering of countries based on different factors

if Nav == "3D Model":

 st.header("8. A 3D model displaying the scattering of countries based on GDP/capita and Freedom")

 x= df["Country"]
 y= df["Econ(GDP/C)"]
 z=df["Freedom"]

 trace=go.Scatter3d(x=x,y=y,z=z, mode='markers', marker=dict(size=12,color=df["HappinessS"], colorscale='aggrnyl'))
 data=[trace]
 layout=go.Layout(title="Where the Countries Lie in terms of GDP and Life Expectancy",margin=dict(l=0,r=0,b=0,t=0), scene = dict(
    xaxis = dict(
        title="Countries"),
    yaxis = dict(
        title='GDP'),
    zaxis = dict(
        title='Freedom')),

 )

 fig3=go.Figure(data=data, layout=layout)
 st.plotly_chart(fig3)

 st.markdown("""The above 3D model displays the designated countries and where they fall in terms of their GDP/capita and their freedom.
This model can clarify several direct/indirect findings.
To begin with, most of the countries place high value on its GDP/capita, as the majority falls on the right side of the Y-axis. 
It also displays that an inter-relation lies between having a high GDP and the degree of freedom given in a country.For example, most of the countries that have a high GDP are also located at the higher level of the Freedom axis.
Moreover, the countries that have a high level of both (top-right) are the ones with the lightest color too, indicating a higher happiness score.
On the other hand, the countries located at the bottom-left (low GDP/low Freedom) are all of a darker shade, revealing a low happiness score.
Lastly, as a country start to escelate on both axes (Freedom & GDP), the color becomes lighter.""")

#Detecting any Relation between GDP and LifeExpectancy and an overall effect on Happiness
if Nav == "ScatterPlot":


 st.header("9. GDP/capita and LifeExpectancy with overall effect on Happiness")
 fig4 = px.scatter(df, x=df["Econ(GDP/C)"], y=df["LifeExp"],color="HappinessS", title="Relation between GDP and Life Expectancy and Effect on Happiness")
 st.plotly_chart(fig4)
 st.markdown("""The above bargraph displays the association found between the importance of securing a high GDP and the importance of having a high life expectancy for different countries.
It is highly visible that countries that have a high GDP/capita tend to value life expectancy(health) more than those who dont.
  
  
  
  --> Implying that when monetary security is provided and life expenses are somehow covered, the people of a country will shift their attention to providing a healthier life.
    
As also expected, those countries with a higher GDP and a higher Life expectancy have a higher Happiness score as devoted by the light color of the countries on the top-right""")


from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
if Nav == "Freedom and GovTrust Histogram":

 st.header("10. A Histogram Displaying the Relation between Freedom and Trusting the Government")
 fig6=px.histogram(df, x="Freedom", y="TrustGov", color="Region")
 st.plotly_chart(fig6)

 st.markdown("""The above histogram explains the distribution and clustering of the regions in terms of Freedom levels and the trust that each region has in each cluster.
 What is clyster clear is that regions that have a higher degree of Freedom and value the latter usually trust their governments more than those that dont enjoy high freedom levels.
 
 Even those that are distributed along the X-axis (different Freedom levels) display the same correlation. For instance, Western Europe countries that have a freedom level of (0.4 on average) score their trust in their government as (0.06-0.2) at most. 
 
However, as we move down the scale, the same region with a (0.6-0.7) score in terms of Freedom scores its trust in the government as 2.2.


Given that the same region is chosen, which is the most reliable method to group countries while keeping other factors constant, we can clearly conclude that a higher level of freedom establishes peoples' trust in their governments. 

 That is because, a slight increase of 0.2 in terms of Freedom (from 0.4 to 0.6) led to an increase of 2 in terms of trusting the government.""")

if Nav == "Findings Summary":


 st.header("Summary of The Findings")

 st.markdown("""The performed graphs and analysis revealed several and interrelational associations among several indicators and overall happiness, and among the indicators themselves.
 
 Sweden has the highest Happiness Score, while Togo has the lowest
 
 GDP has the highest influence on Happiness among Govermental factors
 
 Family has the highest influence on Happiness among Life Quality factors
 
 Almost all regions consider GDP and Family as main indicators of Happiness, but some with different levels
 
 Countries with high GDP and high life expectancy tend to enjoy more freedom and happiness
 
 A positive relation exists between GDP levels and Freedom levels, and both have a positive effect on a country's happiness
 
 Countries with a high GDP tend to value life expectancy and health more, and of course increase the overall happiness score

 Enjoying a high level of Freedom greatly enhances the trust level that each country's people have with their government in a postive way.""")
 st.subheader("Reflecting")
 choose_again = st.multiselect("After this ride, re-choose your happiness source and see how your knowledge influences your choice!", ("Money","Family","Freedom","Goverm.Trust"))
 st.write("Now you chose:",choose_again)




 if st.button("Did you enjoy it? :)"):
    st.write("Of course !!")
 else:
    st.write("Yes !")
if Nav == "Dataset Visualizations":
 st.header('Feel free to switch between the columns to see the distribution of the valuation of each indicator (GDP,Family,Freedom ...')
 col,figg = pl.subplots()
 col = st.sidebar.selectbox("View Columns", df.columns)
 pl.hist(df[col])
 pl.xlim([0,2])
 st.pyplot(figg=pl)
 st.subheader("To view the Dataset Source")
 if st.button("View Dataset"):
     st.write("https://www.kaggle.com/unsdsn/world-happiness")
    

 st.set_option('deprecation.showPyplotGlobalUse', False)
