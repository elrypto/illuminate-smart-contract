from boa.interop.Neo.Runtime import GetTrigger,CheckWitness
from boa.interop.Neo.Storage import Get,Put,Delete,GetContext
from boa.interop.Neo.TriggerType import Application, Verification

"""
Based on @deanpress' https://github.com/deanpress/neosense
"""


def Main(operation, args):

    """
    Main definition for the smart contracts

    :param operation: the operation to be performed
    :type operation: str

    :param args: list of arguments.
        args[0] is a key for a value (likely a key to ipfs)
        args[1] is the value to be stored (likely ipfs hash)
    :param type: str

    :return:
        byterarray: The result of the operation
    """

    #blockchain key, is the key stored for the data stored (probably ipfs)
    blockchain_key = args[0]

    if operation == 'Save':
        print("operation = Save()")
        blockchain_value = args[1]
        Put(GetContext(), blockchain_key, blockchain_value)
        return True
    if operation == 'Get':
        print("operation = Get()")
        stored_value = Get(GetContext(), blockchain_key)
        if stored_value:
            return stored_value

    return False
