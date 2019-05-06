try:
    import folder_working as FW
    import master as M
    import lessons as L
    import problems as P
except ImportError:
    from app.DB import folder_working as FW
    from app.DB import master as M
    from app.DB import lessons as L
    from app.DB import problems as P

FW.reinit()
M.init()
L.init()
P.init()