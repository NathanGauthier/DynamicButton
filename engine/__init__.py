import sys

def getEngine():


    if 'maya' in sys.executable:
        from engine import engine_maya as em
        return em.Maya_engine()

    elif 'hou' in sys.executable:
        from engine import engine_hou as eh
        return eh.Houdini_engine()

    else:
        from engine import engine_base as eb
        return eb.Engine()



if __name__ == '__main__':
    test = getEngine()
    print(test)

