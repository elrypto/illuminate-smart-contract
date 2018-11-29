from boa.interop.Neo.Storage import Get,Put,Delete,GetContext

"""
Based on @deanpress' https://github.com/deanpress/neosense

Would be imported into neo with paramters 0710 05 True False False

0710 - String and array
05 - Byte array (returned)
True - Storage
False False - No dynamic invoke or Payment
"""

def Main(operation, args):
    print("illicontract.Main()")
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
        print("illicontract.Save()")
        blockchain_value = args[1]
        Put(GetContext(), blockchain_key, blockchain_value)
        return True
    if operation == 'Get':
        print("illicontract.Get()")
        stored_value = Get(GetContext(), blockchain_key)
        if stored_value:
            return stored_value

    return False
