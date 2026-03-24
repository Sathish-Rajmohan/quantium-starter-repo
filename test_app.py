from app2 import app, update_graph

def test_header():
    header = app.layout.children[0]
    assert header.children == "Pink Morsel sales visualiser"

def test_visualisation():
    graph = app.layout.children[2]
    assert graph.id == "sales_graph"

def test_region_picker():
    radio = app.layout.children[1].children[0]
    assert radio.id == "region_filter"

def test_update_graph_all():
    fig = update_graph("all")
    assert fig is not None

def test_update_graph_region():
    fig = update_graph("north")
    assert len(fig.data) > 0