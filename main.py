class Phone:
    def __init__(self, brand, memory):
        self.brand = brand
        self.memory = memory

    def info(self):
        print(f"Brand: {self.brand}")
        print(f"Xotira: {self.memory} GB")

p = Phone("Samsung", 128)
p.info()
