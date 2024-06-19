class Menu:
    def __init__(self) :
        self.menuList = []
    
    def add_menu_item(self, item):
        self.menuList.append(item)
    
    def find_item(self, item_name):
        for item in self.menuList:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item :
            self.menuList.remove(item)
            print(f'\t{item_name} deleted')
        else:
            print(f'{item_name} not found')

    def show_menu(self):
        print('\t*****Our Menu*****')
        print('\tName\tPrice\tQuantity')
        for item in self.menuList:
            print(f'\t{item.name}\t${item.price}\t{item.quantity}')

