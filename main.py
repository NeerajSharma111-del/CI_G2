import os

# Train model if not exists
if not os.path.exists("src/model.pkl"):
    import src.train

import src.predict