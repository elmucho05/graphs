# graphs and algos
Commands to do:

git clone "url della repo"
cd graphutils

python3 -m pip install --upgrade build
python3 -m build
cd dist
python3 -m pip install graphutils-0.0.7-py3-none-any.whl 

################
# Now we can import our modules

from graph import Graph
from algos import *

# We can use the algorithms like this:
disjktra(graph, graph.get_vertex("a"))

