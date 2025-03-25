import sys
import os
import importlib
import pkgutil

# Get the absolute path of the 'src' directory
src_path = os.path.join(os.path.dirname(__file__), "src")

# Add 'src' to the module search path (for relative imports)
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Automatically import all modules from 'src' and expose them under 'dltmeta'
for _, module_name, _ in pkgutil.iter_modules([src_path]):
    module = importlib.import_module(f"src.{module_name}")  # Import from 'src'
    globals()[module_name] = module  # Expose under 'dlt-meta'
