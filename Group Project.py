import pandas as pd
import plotly
from plotly.offline import plot
import plotly.graph_objs as go

df = pd.read_excel("GISdata.xlsx", sheet_name ="cancercases")

cancercases = go.Bar(x= df["CancerType"], y=df["Number"],


                marker = {"color": df["Number"], "colorscale": "Jet"}
                    )

titles = go.Layout(
            
                    title = "Cancer cases in women",
                    
                    xaxis=go.layout.XAxis(
                            title=go.layout.xaxis.Title(
                                    text="Cancer Type",
                                    )
                             ),
                        
                            yaxis=go.layout.YAxis(
                                    title=go.layout.yaxis.Title(
                                            text="Number",
                                          )
                           
                           )
                        )
                            
fig= go.Figure(data=[cancercases], layout = titles)

plot(fig)