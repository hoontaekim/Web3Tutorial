from web3.gas_strategies.rpc import rpc_gas_price_strategy
from web3 import Web3

alchemy_url="https://eth-goerli.g.alchemy.com/v2/_xtvbx98H0BR4y_GsXc8uqwtiGVKJgGL"
web3=Web3(Web3.HTTPProvider(alchemy_url))

account_from={
    "private_key":"e0cc301683cf0037f584a272c9baa1bf215b94964553512319dec064ee39efaf",
    "address":"0x632001efcf13AEbBCB59E66ADF4f3490313d5482"
}

address_to="0x58ca721Bf1F9cE29C516735da55F257963c23DC4"

web3.eth.set_gas_price_strategy(rpc_gas_price_strategy)

tx_create=web3.eth.account.sign_transaction(
    {
        "nonce":web3.eth.get_transaction_count(account_from["address"]),
        "gasPrice":web3.eth.generate_gas_price(),
        "gas":21000,
        "to":address_to,
        "value":web3.toWei("0.0001","ether")
    },
    account_from["private_key"]
)

tx_hash=web3.eth.send_raw_transaction(tx_create.rawTransaction)
tx_receipt=web3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction successful with hash : {tx_receipt.transactionHash.hex()}")