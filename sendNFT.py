from web3 import Web3
import json

alchemy_url="https://eth-goerli.g.alchemy.com/v2/_xtvbx98H0BR4y_GsXc8uqwtiGVKJgGL"
web3=Web3(Web3.HTTPProvider(alchemy_url))

with open("jsonabi.json") as f:
    info_json = json.load(f)
abi = info_json["abi"]
  
address_from={
    # "private_key":"e0cc301683cf0037f584a272c9baa1bf215b94964553512319dec064ee39efaf"
    "private_key":"",
    # "address":"0x632001efcf13AEbBCB59E66ADF4f3490313d5482"
    "address":""
}
address_to="0x58ca721Bf1F9cE29C516735da55F257963c23DC4"
tokenId=1
contractAddress="0x0f2497CD1125Cb8e0Bbfbcb6010d25Ffd0bC1B4a"


tokenContract=web3.eth.contract(address=contractAddress, abi=abi)

NFT_tx=tokenContract.functions.safeTransferFrom(address_from["address"], address_to, tokenId).buildTransaction(
    {
        'from': address_from['address'],
        'nonce': web3.eth.get_transaction_count(address_from['address']),
    }
)
tx_create = web3.eth.account.sign_transaction(NFT_tx, address_from['private_key'])

tx_hash = web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

print(f'Tx successful with hash: { tx_receipt.transactionHash.hex() }')