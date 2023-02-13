class ClassBased():
    def __init__(self) -> None:
        
        # List
        self.all_customer = [
            {"id": 1, "nama": "nibras"}
        ]

    def call_all_customer(self) -> None:
        for cus in self.all_customer:
            print(cus['nama'])
