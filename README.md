# Web3PYContractWrapper
A python class that simplifies use of Web3 python in making contract calls. Replicates the behaviour of web3.eth.Contract in Web3.js creating a contract as  a single object.
There are four different methods.

1. BuildandSignTX(self,address,functionName,private_key,*args,**kwargs):
Sends and generates an ethereum transaction for the contract by getting the method by name. Due to an issue with python web3 this will fail for methods with the same name but different inputs.
*args will be the contract function inputs
**kwargs can be used to specify gas limit and gasprice

2. BuildandSignTXbySig(self,address,functionsig,private_key,*args,**kwargs):
Sends and generates an ethereum transaction for the contract by getting the method by function signature. Will always get the correct function.
*args will be the contract function inputs
**kwargs can be used to specify gas limit and gasprice

3. callFunctionTransaction(self,functionName,*args):
Makes a web3 call to the contract by name. Has the same naming issues as BuildandSignTX.
*args will be the contract function inputs

4. callFunctionTransactionBySig(self,functionSig,*args):
Makes a web3 call to the contract by function signature
*args will be the contract function inputs

There is no support for events currently. 


import ContractClass

abi="""[
	{
		"inputs": [],
		"name": "retreive",
		"outputs": [
			{
				"internalType": "bytes32",
				"name": "",
				"type": "bytes32"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "num",
				"type": "bytes32"
			}
		],
		"name": "store",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]
"""
address ='0x298470895fa5647798e39fa601ee591309b79b69'

SECRET_KEY=""

owner="0xe1e043eb8c42776280941d090ff613183230e220"'

ENDPOINT ='HTTP://127.0.0.1:8545'

Getter=ContractClass.Contract(address,abi,100000,ENDPOINT,5777)

Getter.BuildandSignTX(owner,'store',SECRET_KEY,23423432)

value=Getter.callFunctionTransaction('retreive')