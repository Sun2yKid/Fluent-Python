"""
function decorators are executed as soon as the module is imported
Note: `import time` vs `runtime`
"""
import sys
import registration
from dis import dis

print(f"sys.path: {sys.path}")
print(f"registration.registry: {registration.registry}")
