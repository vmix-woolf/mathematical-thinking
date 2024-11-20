import plotly.graph_objects as go
import numpy as np

# points generation
num_points = 10
points_x = np.random.randint(-10, 10, num_points)
points_y = np.zeros(num_points)

# create Figure object for the graph
fig = go.Figure()

# add horizontal axis X
fig.add_trace(go.Scatter(x=[-10, 10], y=[0, 0], mode='lines', name='X-axis'))

# add points on coordinates
fig.add_trace(go.Scatter(x=points_x, y=points_y, mode='markers', name='Points'))

# graph view settings
fig.update_layout(
    title='Coordinate line with the points',
    xaxis=dict(title='Axis X'),
    yaxis=dict(title='Axis Y'),
    showlegend=True
)

# Output of the graph
fig.show()