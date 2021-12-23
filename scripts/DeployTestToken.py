from scripts.support.WEB3_getacc import get_account
from brownie import TestToken
from web3 import Web3


def deploy():
    # Contract requires initial supply input, currently 10 is chosen
    initSupply = Web3.toWei(10, "ether")
    account = get_account()
    Token = TestToken.deploy(initSupply, {"from": account})
    print("TestToken.sol succesfully deployed")
    return Token


def main():
    deploy()
