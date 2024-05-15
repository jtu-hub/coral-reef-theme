import torch
from torch import nn

#TODO: test if this works :')
def setup_device():
    return "cuda" if torch.cuda.is_available() else "cpu"

def print_progressbar(i,iter,pb_len=50,load_array=["","\\","|","/","="],load_str="=",not_load_str="-"):
    """
    Just me being bored
    i               current iteration
    iter            total number of iterations
    pb_len          char count of progress bar
    load_array      symbols for fine loading, first string must be empty!
    load_str        progress done
    not_load_str    progress that has not been done yet
    """
    intermediat_load=len(load_array)-1
    progress=(i+1)/iter*pb_len
    print("progress: [%s%s%s] %.2f%s" % (load_str*int(np.floor(progress)), load_array[int(np.ceil(intermediat_load*(progress-np.floor(progress))))], not_load_str*(pb_len-int(np.ceil(progress))), ((i+1)/iter*100), "%"),end="\r")
    if(i+1==iter):
        print(end="\n")
