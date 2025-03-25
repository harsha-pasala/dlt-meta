import sys
import os
import importlib
import pkgutil

# Alias dlt-meta as dltmeta so that `import dltmeta` works
sys.modules["dltmeta"] = sys.modules["dlt-meta"]

# Get the absolute path of the src directory
src_path = os.path.join(os.path.dirname(__file__), "src")

# Add src to sys.path so Python can find modules inside it
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Dynamically import and expose all modules in src as if they were inside dltmeta
for _, module_name, _ in pkgutil.iter_modules([src_path]):
    module = importlib.import_module(module_name)  # Import from src
    globals()[module_name] = module  # Expose under dltmeta
