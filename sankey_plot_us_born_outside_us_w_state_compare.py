import pandas as pd
import plotly.graph_objects as go




# Read in data for nodes and for the links
links = pd.read_excel('us_born_outside_us_links_w_state_compare.xlsx')
nodes = pd.read_excel('us_born_outside_us_nodes_w_state_compare.xlsx')


# Go in and add color changes to the nodes and links



# Convert the DataFrames to a list
nodes_list = [nodes.columns.values.tolist()] + nodes.values.tolist()

links_list = [links.columns.values.tolist()] + links.values.tolist()
# Retrieve headers and build dataframes

nodes_headers = nodes_list.pop(0)
links_headers = links_list.pop(0)
df_nodes = pd.DataFrame(nodes_list, columns = nodes_headers)

df_links = pd.DataFrame(links_list, columns = links_headers)
# Sankey plot setup

data_trace = dict(
    type='sankey',                                              # Sankey Plot type
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",                                          # 'h' = horizontal sankey plot, 'v' = vertical sankey plot
    arrangement = "snap",
    valueformat = "{,}",                                       # Formats the value shown with a dollar sign out front (ex. value = 726 -> ouput = $726)
    node = dict(
      pad = 10,                                               # The bigger the number the more space between each line vertically
      thickness = 10,                                           # The width of the vertical lines/nodes
      line = dict(
        color = "black",
        width = 0
      ),
      label =  df_nodes['label'].dropna(axis=0, how='any'),     # Name of the node
      x = df_nodes['x'].dropna(axis=0, how='any'),              # Horizontal position of the node's center (from left to right)
      y = df_nodes['y'].dropna(axis=0, how='any'),              # Vertical position of the node's center (from top to bottom)
      color = df_nodes['color']                                 # Color of the node
    ),
    link = dict(
      source = df_links['source'].dropna(axis=0, how='any'),    # Link starting from this node
      target = df_links['target'].dropna(axis=0, how='any'),    # Link going to this node
      value = df_links['value'].dropna(axis=0, how='any'),
      color = df_links['color'].dropna(axis=0, how='any'),
      label = df_links['label'].dropna(axis=0, how='any'),
  )
)
# Option 1, with a "basic" layout with a Title and Subtitle with reference link.

layout = dict(
        title = "Number of individuals born outside of US, living in the US (2018)<br>Compared to those born in US for a few States<br><span style='font-size:0.6em;color:gray'>Link to data <a href='https://www.migrationpolicy.org/data/state-profiles/state/demographics/US'>here.</a></span><span style='font-size:0.6em;color:gray'> Hover over diagram for more info on each flow.</span>",
    height = 750,                                               # Height of the figure output
    width = 1200,                                               # Width of figure output
    font = dict(
      size = 12),)
# Option 2. A more advanced layout consisting of the Title and Subtitle with reference link and some additional button features.The buttons in this 
# layout run down the left side of the plot and allow the user to make some additional visual adjustments to the plot that are already programed
# into the plot. Included are just a few examples of buttons and plot adjustments that can be included in a Sankey plot. 

layout_w_buttons =  dict(
    title = "Number of individuals born outside of US, living in the US (2018)<br>Compared to those born in US for a few States<br><span style='font-size:0.6em;color:gray'>Link to data <a href='https://www.migrationpolicy.org/data/state-profiles/state/demographics/US'>here.</a></span><span style='font-size:0.6em;color:gray'> Hover over diagram for more info on each flow.</span>",
    font = dict(
      size = 12
    ),
    height=750,
    width = 1200,
    updatemenus= [
            dict(
                y=.95,
                buttons=[
                    dict(
                        label='Light',
                        method='relayout',
                        args=['paper_bgcolor', 'white']
                    ),
                    dict(
                        label='Dark',
                        method='relayout',
                        args=['paper_bgcolor', 'black']
                    )
                ]
            ),
            dict(
                y=0.85,
                buttons=[
                    dict(
                        label='Thin',
                        method='restyle',
                        args=['node.thickness', 7]
                    ),
                    dict(
                        label='Medium',
                        method='restyle',
                        args=['node.thickness', 12]
                    ),
                    dict(
                        label='Thick',
                        method='restyle',
                        args=['node.thickness', 20]
                    )     
                ]
            )
            # dict(
            #     y=0.8,
            #     buttons=[
            #         dict(
            #             label='Snap',
            #             method='restyle',
            #             args=['arrangement', 'snap']
            #         ),
            #         dict(
            #             label='Perpendicular',
            #             method='restyle',
            #             args=['arrangement', 'perpendicular']
            #         ),
            #         dict(
            #             label='Freeform',
            #             method='restyle',
            #             args=['arrangement', 'freeform']
            #         ),
            #         dict(
            #             label='Fixed',
            #             method='restyle',
            #             args=['arrangement', 'fixed']
            #         )       
            #     ]
            # ),
            # dict(
            #     y=0.7,
            #     buttons=[
            #         dict(
            #             label='Small gap',
            #             method='restyle',
            #             args=['node.pad', 10]
            #         ),
            #         dict(
            #             label='Medium gap',
            #             method='restyle',
            #             args=['node.pad', 20]
            #         ),
            #         dict(
            #             label='Large gap',
            #             method='restyle',
            #             args=['node.pad', 50]
            #         )
            #     ]
            # ),
            # dict(
            #     y=0.6,
            #     buttons=[             
            #         dict(
            #             label='Horizontal',
            #             method='restyle',
            #             args=['orientation', 'h']
            #         ),
            #         dict(
            #             label='Vertical',
            #             method='restyle',
            #             args=['orientation', 'v']
            #         )
            #     ]
            # )
        ]
)
# Here we join together the data that formats the basics of how the Sankey plot with look with the layout that customizes the figure's details.
# The layout function you can choose either the basic option "layout" or the advanced layout "layout_w_buttons" that includes the buttons with
# additional plot feature changes. 

fig1 = go.Figure(data=[data_trace], layout=layout_w_buttons)
fig1.show()


# Export plot to html
fig1.write_html("us_born_outside_us_compared_to_us_states.html")

