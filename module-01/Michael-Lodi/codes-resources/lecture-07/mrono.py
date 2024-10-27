class CC:
    pass
class DD:
    pass
class AA(CC,DD):
    pass
class BB(DD,CC):    #consistent if we swap DD,CC
    pass
class EE(AA,BB):
    pass 