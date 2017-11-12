import igraph as ig
import json
import plotly
from plotly.graph_objs import *

def displayGraph(data):
    """ nodes{keyname, name, size}, links{source, target, frequence}
    format: nodes: keynames
    nodes_thickness : occurrences
    edges : relation
    thickness_edges: frequence"""
    N=len(data['nodes']) # nombre de nodes

    L=len(data['links']) # nombre de edges
    Edges=[(data['links'][k]['source'], data['links'][k]['target']) for k in range(L)] # list of edges
    print Edges

    G=ig.Graph(Edges, directed=False)

    G=ig.Graph(Edges, directed=False)

    keynames=[]
    occurrences=[]
    lcolors=[]
    lwidth=[]
    lname=[]
    for node in data['nodes']:
        keynames.append(node['name'])
        occurrences.append(node['size']*2)
        lcolors.append(node['keyname']*2)
        lname.append(node['name'])
    for edge in data['links']:
        lwidth.append(edge['width'])



    layt=G.layout('kk', dim=3)
    Xn=[layt[k][0] for k in range(N)]# x-coordinates of nodes
    Yn=[layt[k][1] for k in range(N)]# y-coordinates
    Zn=[layt[k][2] for k in range(N)]# z-coordinates
    Xe=[]
    Ye=[]
    Ze=[]
    for e in Edges:
        Xe+=[layt[e[0]][0],layt[e[1]][0], None]# x-coordinates of edge ends
        Ye+=[layt[e[0]][1],layt[e[1]][1], None]
        Ze+=[layt[e[0]][2],layt[e[1]][2], None]

    trace1=Scatter3d(x=Xe,
                   y=Ye,
                   z=Ze,
                   mode='lines',
                   name='sentence',
                   line=Line(color='rgb(125,125,125)', width=1),
                   text=lwidth,
                   hoverinfo='text'
                   )
    trace2=Scatter3d(x=Xn,
                   y=Yn,
                   z=Zn,
                   mode='markers',
                   name='keyword',
                   marker=Marker(symbol='dot',
                                 size=occurrences,
                                 color=lcolors,
                                 #color=group,
                                 colorscale='Viridis',
                                 line=Line(color='rgb(50,50,50)', width=0.5)
                                 ),
                   text=lname,
                   hoverinfo='text'
                   )
    axis=dict(showbackground=False,
              showline=False,
              zeroline=False,
              showgrid=False,
              showticklabels=False,
              title=''
              )

    layout = Layout(
             title="visualization of your text",
             width=1000,
             height=1000,
             showlegend=False,
             scene=Scene(
             xaxis=XAxis(axis),
             yaxis=YAxis(axis),
             zaxis=ZAxis(axis),
            ),
         margin=Margin(
            t=100
        ),
        hovermode='closest',
        annotations=Annotations([
               Annotation(
               showarrow=False,
                text="Data source: <a href='http://bost.ocks.org/mike/miserables/miserables.json'>[1] miserables.json</a>",
                xref='paper',
                yref='paper',
                x=0,
                y=0.1,
                xanchor='left',
                yanchor='bottom',
                font=Font(
                size=14
                )
                )
            ]),    )

    data=Data([trace1, trace2])
    plotly.offline.plot(data, layout)
    #py.iplot(fig, filename='Keyvalues')
