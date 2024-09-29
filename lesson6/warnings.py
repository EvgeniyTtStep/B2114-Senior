import _warnings

try:
    _warnings.warn("text for warning is deprecated", SyntaxWarning)
except:
    print("Warning for warning is deprecated")

print("Code end")