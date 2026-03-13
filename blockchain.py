
import datetime

import json

import hashlib



class Transaction:

    def __init__(self, sender, recipient, amount):

        self.sender = sender

        self.recipient = recipient

        self.amount = amount



    def to_dict(self):

        return {

            "sender": self.sender,

            "recipient": self.recipient,

            "amount": self.amount

        }

    

    def print(self):

        print(self.to_dict())



class Block:

    def __init__(self, index, transactions, previous_hash):

        self.index = index

        self.timestamp = str(datetime.datetime.now())

        self.transactions = transactions

        self.nonce = 0

        self.previous_hash = previous_hash

        self.hash = self.calculate_hash()



    def calculate_hash(self):

        block = {

            "index": self.index,

            "timestamp": self.timestamp,

            "transactions": [tx.to_dict() for tx in self.transactions],

            "nonce": self.nonce,

            "previous_hash": self.previous_hash

        }

        block_string = json.dumps(block)

        generatedHash = hashlib.sha256(block_string.encode()).hexdigest()

        return generatedHash

    

    def print_hash(self):

        print(self.calculate_hash())



    def mine_block(self, difficulty):

        startTime = datetime.datetime.now()



        while self.hash[:difficulty] != "0" * difficulty:

            self.nonce += 1

            self.hash = self.calculate_hash()

        print("Block mined: " + self.hash + " with nonce: " + str(self.nonce) + " in " + str((datetime.datetime.now() - startTime).total_seconds()) + " seconds")



class Blockchain:

    def __init__(self):

        self.chain = [self.create_genesis_block()]

        self.difficulty = 5

        self.pending_transactions = []

    

    def create_genesis_block(self):

        return Block(0, [], "0")

    

    def add_transaction(self, transaction):

        self.pending_transactions.append(transaction)



    # def get_last_block(self):

    #     return self.chain[-1]



    def mine_pending_transactions(self):

        index = len(self.chain)

        previous_hash = self.chain[-1].hash

        new_block = Block(index, self.pending_transactions, previous_hash)

        new_block.mine_block(self.difficulty)

        self.pending_transactions = []



    def is_valid(self):

        for i in range(1, len(self.chain)):

            current_block = self.chain[i]

            previous_block = self.chain[i - 1]



            if current_block.hash != current_block.calculate_hash():

                return False

            if current_block.previous_hash != previous_block.hash:

                return False

        return True

        



if __name__ == "__main__":

    transaction1 = Transaction("Alice", "Bob", 10)

    transaction1.print()



    Block1 = Block(1, [transaction1], "0")

    Block1.print_hash()



    blockchain = Blockchain()

    blockchain.add_transaction(transaction1)

    blockchain.mine_pending_transactions()



    print("is Valid?", blockchain.is_valid())
