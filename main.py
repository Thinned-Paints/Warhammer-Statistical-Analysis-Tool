"""
Final Project V1-Harry Leng, hl17490


This is the main body of code that will be used to execute other code blocks from the various other classes I have setup.
It implements multithreading too, generating a thread for each of your logical processors, to help speed up execution time.

"""
#TODO: Fix multithreading by adding a threadpool

import Handlers
import multiprocessing


cores = (multiprocessing.cpu_count()-1)
samplesize = 10
threadruns = round(samplesize/cores)

test = Handlers.heavyweaponsgraph(samplesize)


