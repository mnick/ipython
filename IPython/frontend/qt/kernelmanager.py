""" Defines a KernelManager that provides signals and slots.
"""

# Local imports.
from IPython.utils.traitlets import Type
from IPython.zmq.kernelmanager import ShellSocketChannel, SubSocketChannel, \
    StdInSocketChannel, HBSocketChannel, KernelManager
from base_kernelmanager import QtShellChannelMixin, QtSubChannelMixin, \
    QtStdInChannelMixin, QtHBChannelMixin, QtKernelManagerMixin


class QtShellSocketChannel(QtShellChannelMixin, ShellSocketChannel):
    pass

class QtSubSocketChannel(QtSubChannelMixin, SubSocketChannel):
    pass

class QtStdInSocketChannel(QtStdInChannelMixin, StdInSocketChannel):
    pass

class QtHBSocketChannel(QtHBChannelMixin, HBSocketChannel):
    pass


class QtKernelManager(QtKernelManagerMixin, KernelManager):
    """ A KernelManager that provides signals and slots.
    """

    sub_channel_class = Type(QtSubSocketChannel)
    shell_channel_class = Type(QtShellSocketChannel)
    stdin_channel_class = Type(QtStdInSocketChannel)
    hb_channel_class = Type(QtHBSocketChannel)
