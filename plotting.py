import plotly
plotly.tools.set_credentials_file(username='bernstein', api_key='hptuy3m8z5')
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls


trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17])

trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9])

data = Data([trace0, trace1])

def get_url(data):
    url = py.plot(data, filename = 'basic-line', auto_open = False)
    return url

def get_html(url):
    return tls.get_embed(url)
