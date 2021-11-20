def fFullScreen():
    """Utilise full Jupyter Notebook screen.

Input:
Process: (IPython.core.display.display; IPython.core.display.HTML)
Output:
"""
    from IPython.core.display import display,HTML
    display(HTML("<style>.container { width:100% !important; }</style>"))
# --- END ---
if __name__=="__main__":
    pass
else:
    fFullScreen()
# --- END ---