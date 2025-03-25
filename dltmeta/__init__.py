import sys
import os
import importlib
import pkgutil

# Define the src package name explicitly
SRC_PACKAGE = "src"

# Get the absolute path of the src directory
src_path = os.path.join(os.path.dirname(__file__), "..", "src")

# Add src to sys.path so Python can find modules inside it
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Create an explicit mapping to ensure submodules work
for _, module_name, _ in pkgutil.iter_modules([src_path]):
    full_module_name = f"{SRC_PACKAGE}.{module_name}"  # Import as `src.module`
    module = importlib.import_module(full_module_name)  # Import using package context

    # Explicitly register submodules under dltmeta
    sys.modules[f"dltmeta.{module_name}"] = module
    setattr(sys.modules[__name__], module_name, module)  # Expose under dltmeta
