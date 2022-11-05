from web3 import Web3

alchemy_url="https://eth-goerli.g.alchemy.com/v2/_xtvbx98H0BR4y_GsXc8uqwtiGVKJgGL"
web3=Web3(Web3.HTTPProvider(alchemy_url))

address_from="0x632001efcf13AEbBCB59E66ADF4f3490313d5482"
address_to="0x58ca721Bf1F9cE29C516735da55F257963c23DC4"

balance_from=web3.fromWei(web3.eth.get_balance(address_from),"ether")
balance_to=web3.fromWei(web3.eth.get_balance(address_to), "ether")

print(f"The balance of {address_from} is : {balance_from} ETH")
print(f"The balance of {address_to} is : {balance_to} ETH")