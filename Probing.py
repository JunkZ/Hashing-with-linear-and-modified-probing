import time
import random

def doubletest(length,max):
    i= probes= 0
    start_time = end_time = totaltime = 0
    A = [0] * length
    upcount= [0] * length
    downcount= [0] * length
    linprobes=probechain=linprobechain=0
    linstart_time = linend_time = lintotaltime = 0
    linA = [0] * length
    


        
    while i < length:
        x = (random.randrange(1, max)) #x to be inserted

        #<-------BELOW STARTS THE MODIFIED PROBING------->
        
        totaltime += end_time
        start_time = time.perf_counter()
        mod = x % len(A)    #hash value
        if not A[mod]:
            A[mod] = x
        elif downcount[mod] <= upcount[mod]:
            downcount[mod] +=1
            probestemp = probes
            while A[mod]:
                mod = (mod+1) %len(A)
                probes += 1
            A[mod] = x
            probestemp = probes - probestemp
            if probestemp > probechain:
                probechain = probestemp
        else:
            upcount[mod] +=1
            probestemp = probes
            while A[mod]:
                mod = (mod-1) %len(A) 
                probes += 1
            A[mod] = x
            probestemp = probes - probestemp
            if probestemp > probechain:
                probechain = probestemp
        end_time = time.perf_counter()- start_time
        
        #<-------BELOW STARTS THE NORMAL LINEAR PROBING------->
        
        lintotaltime += linend_time
        linstart_time = time.perf_counter()
        linmod = x % len(linA)    #hash value
        linprobestemp = linprobes
        while linA[linmod]:
                linprobes += 1
                linmod = (linmod+1) %len(linA)
        linA[linmod] = x
        linprobestemp = linprobes - linprobestemp
        if linprobestemp > linprobechain:
            linprobechain = linprobestemp

        linend_time = time.perf_counter()- linstart_time

        i += 1

    print("Mod: time",end_time, "probes:", probes, "Longest probechain:",probechain)
    print("Lin: time",linend_time,  "probes:", linprobes, "Longest probechain:", linprobechain)


doubletest(1000,100) #test with same random values

