import hashlib
import time

# Block Class
class Block:
    def init(self, index, previous_hash, timestamp, data, nonce=0):
        self.index = index  # Nomor dari blok
        self.previous_hash = previous_hash  # Hash dari blok sebelumnya
        self.timestamp = timestamp  # Waktu pembuatan blok
        self.data = data  # Data transaksi atau informasi lainnya
        self.nonce = nonce  # Angka yang digunakan untuk mencari hash yang valid (proof of work)
        self.hash = self.calculate_hash()  # Hash dari blok ini

    def calculate_hash(self):
        """
        Menghitung hash dari blok berdasarkan atribut-atribut blok tersebut.
        """
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def repr(self):
        return f"Block(index: {self.index}, hash: {self.hash}, previous_hash: {self.previous_hash}, " \
               f"timestamp: {self.timestamp}, data: {self.data}, nonce: {self.nonce})"

# Blockchain Class
class Blockchain:
    def init(self):
        self.chain = [self.create_genesis_block()]  # Memulai blockchain dengan blok genesis
        self.difficulty = 4  # Mengatur tingkat kesulitan (jumlah nol di depan hash)

    def create_genesis_block(self):
        """
        Blok pertama dalam blockchain, disebut sebagai blok genesis.
        """
        return Block(0, "0", time.time(), "Genesis Block")

    def get_latest_block(self):
        """
        Mengembalikan blok terakhir di dalam blockchain.
        """
        return self.chain[-1]

    def add_block(self, data):
        """
        Menambahkan blok baru ke dalam blockchain.
        """
        latest_block = self.get_latest_block()
        new_block = Block(index=latest_block.index + 1,
                          previous_hash=latest_block.hash,
                          timestamp=time.time(),
                          data=data)
        self.mine_block(new_block)
        self.chain.append(new_block)

    def mine_block(self, block):
        """
        Melakukan proses proof-of-work dengan mencari nonce yang menghasilkan hash yang valid.
        """
        while not block.hash.startswith('0' * self.difficulty):
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Block mined: {block}")

    def is_chain_valid(self):
        """
        Memvalidasi integritas dari seluruh blockchain.
        """
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True
    class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]  # Membuat blockchain dengan blok genesis
        self.difficulty = 4  # Mengatur tingkat kesulitan (jumlah nol di depan hash)

    def create_genesis_block(self):
        """
        Blok pertama dalam blockchain, disebut sebagai blok genesis.
        """
        return Block(0, str(time.time()), "Genesis Block")

    def get_latest_block(self):
        """
        Mengembalikan blok terakhir di dalam blockchain.
        """
        return self.chain[-1]
    
  def add_block(self, new_block):
    """
    Menambahkan blok baru ke dalam blockchain setelah memvalidasi proof of work.
    """
    new_block.previous_hash = self.get_latest_block().hash  # Mengatur hash dari blok sebelumnya
    new_block.hash = self.proof_of_work(new_block)  # Validasi proof of work sebelum menambah blok ke blockchain
    self.chain.append(new_block)  # Tambahkan blok baru ke dalam chain

def proof_of_work(self, block):
    """
    Proses penambangan sederhana yang mencoba menemukan hash yang valid (dengan kesulitan tertentu).
    """
    block.nonce = 0
    calculated_hash = block.calculate_hash()
    while not calculated_hash.startswith('0' * self.difficulty):
        block.nonce += 1
        calculated_hash = block.calculate_hash()
    return calculated_hash

# Membuat blockchain baru
my_blockchain = Blockchain()

# Menambah beberapa blok baru ke dalam blockchain
my_blockchain.add_block(Block(1, "", time.time(), "Transaksi 1"))
my_blockchain.add_block(Block(2, "", time.time(), "Transaksi 2"))
my_blockchain.add_block(Block(3, "", time.time(), "Transaksi 3"))

# Cetak seluruh blok di dalam blockchain
for block in my_blockchain.chain:
    print(block)

# Memeriksa apakah blockchain valid
print(f"Apakah blockchain valid? {my_blockchain.is_chain_valid()}")