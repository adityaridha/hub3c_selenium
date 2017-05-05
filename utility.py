import os
import  sys
from pathlib import Path


root = Path(__file__).parents[0]
root_model = os.path.join(str(root),'model')
sys.path.append(root_model)




