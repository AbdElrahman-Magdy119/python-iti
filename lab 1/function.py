pi=3.14
def shap(*var):
    if(var[0]=='t'):
        print("area",0.5*var[1]*var[2])
    elif(var[0]=='s'):
        print("area",var[1]*var[1])
    elif(var[0]=='r'):
        print("area",var[1]*var[2])
    elif(var[0]=='c'):
        print("area",pi*var[1]*var[1])
    else:
        print("please enter kind of shape")
