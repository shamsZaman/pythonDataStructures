class dicTest:
    def __init__(self):
        self.data = "data"
def main():
    instance = dicTest() 
    d = {}
    d['object'] = instance
    print(d['object'].data)
    for key in d:
        print("key",key)
    for key,value in d.items():
        print("this",value.data)

main()