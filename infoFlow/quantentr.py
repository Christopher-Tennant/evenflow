import numpy as np
from infoflow import quantize as qtz


def quantentr(x,quantlvl):

    """
    :param x: vector containing a data series
    :param quantlvl: number of quantization levels
    :return: indices of quantization levels for the data series
    """
    
    xmin = np.amin(x)
    xmax = np.amax(x)
    quantstep = (xmax - xmin)/quantlvl
    if quantstep == 0:
        xquant = np.zeros(shape=np.shape(x))
    else:
        partition = list(range(xmin+quantstep,xmax-quantstep+1,quantstep))
        xquant = qtz.quantize(x,partition,range(0,quantlvl-1),1)

        assert isinstance(xquant, np.array)
        return xquant