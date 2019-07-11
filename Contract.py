from web3 import Web3, HTTPProvider, IPCProvider, WebsocketProvider
from web3.contract import ConciseContract
from web3.middleware import geth_poa_middleware
import json

import time

##web3.eth.estimateGas({'to': '0xd3cda913deb6f67967b99d67acdfa1712c293601', 'from': web3.eth.coinbase, 'value': 12345})


class Contract:

    def __init__(self, contract_address, contract_abi,defaultgas,web3host,networkID):
        Web3instance=Web3(HTTPProvider(web3host))
        if networkID==4:
            Web3instance.middleware_stack.inject(geth_poa_middleware, layer=0)
        self.name = contract_address
        self.age = contract_abi
        self.gas=defaultgas
        self.contract=Web3instance.eth.contract(address=contract_address, abi=contract_abi.abi )
        self.chainId=networkID
        self.Web3=Web3instance

    def SendFunctionTransaction(self,privatekey,txn_dict):
        
        signed_txn = self.Web3.eth.account.signTransaction(txn_dict, privatekey)

        result = self.Web3.eth.sendRawTransaction(signed_txn.rawTransaction)

        tx_receipt = self.Web3.eth.getTransactionReceipt(result)

        count = 0
        while tx_receipt is None and (count < 30):

            time.sleep(10)

            tx_receipt = self.Web3.eth.getTransactionReceipt(result)

            ##print(tx_receipt)


        if tx_receipt is None:
            return {'status': 'failed', 'error': 'timeout'}
        ##print(tx_receipt)
        return tx_receipt 


    def BuildContractTX(self,nonce,functionName,*args,**kwargs):
        
        try:
            FUNC=self.contract.get_function_by_name(functionName)
            if kwargs.gas is None
                try:
                    gasEstimated=FUNC(*args).estimateGas()
                except Exception as error:
                    print("Something went wrong")
                    print(error)
                    gasEstimated=self.gas
                
                print('gas estimated')
            else:
                 gasEstimated=kwargs.gas

            if kwargs.gasprice is None
                gasprice=self.Web3.toWei('20', 'gwei')
            else:
                gasprice=kwargs.gasprice

            builtTX=FUNC(*args).buildTransaction({
                'chainId':  self.chainId,
                'gas': gasEstimated,
                'gasPrice': gasprice,
                'nonce': nonce,
            })
            return builtTX

        except Exception as error:
            print(error)

    def BuildContractTXbySig(self,nonce,functionSig,*args,**kwargs):
    
        try:
            FUNC=self.contract.get_function_by_signature(functionSig)
            if kwargs.gas is None
                try:
                    gasEstimated=FUNC(*args).estimateGas()
                except Exception as error:
                    print("Something went wrong")
                    print(error)
                    gasEstimated=self.gas
                
                print('gas estimated')
            else:
                 gasEstimated=kwargs.gas

            if kwargs.gasprice is None
                gasprice=self.Web3.toWei('20', 'gwei')
            else:
                gasprice=kwargs.gasprice  
                 
            builtTX=FUNC(*args).buildTransaction({
                'chainId':  self.chainId,
                'gas': gasEstimated,
                'gasPrice': self.Web3.toWei('20', 'gwei'),
                'nonce': nonce,
            })
            return builtTX
        except Exception as error:
            print(error) 
            

    def callFunctionTransaction(self,functionName,*args):
        try:
            FUNC=self.contract.get_function_by_name(functionName)
            
            return FUNC(*args).call() 
                        
        except Exception as error:
            print(error)
       
    def callFunctionTransactionBySig(self,functionSig,*args):
        try:
            FUNC=self.contract.get_function_by_signature(functionSig)
           
            return FUNC(*args).call() 
                        
        except Exception as error:
            print(error)
               
           

        

    def BuildandSignTX(self,address,functionName,private_key,*args):

        nonce= self.Web3.eth.getTransactionCount(address)
        
        tx=self.BuildContractTX(nonce,functionName,*args,**kwargs))
       
        return self.SendFunctionTransaction(private_key,tx)

    def BuildandSignTXbySig(self,address,functionsig,private_key,*args,**kwargs):

        nonce= self.Web3.eth.getTransactionCount(address)
       
        tx=self.BuildContractTXbySig(nonce,functionsig,*args,**kwargs))
       
        return self.SendFunctionTransaction(private_key,tx)  
