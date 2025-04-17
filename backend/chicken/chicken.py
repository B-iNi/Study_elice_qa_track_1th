menu = {
    "후라이드" : 18000,
    "양념치킨" : 19000,
    "간장치킨" : 20000,

}

def get_menu():
    return menu

def order_chicken(name,quantity):
    if name not in menu:
        raise ValueError(f"{menu}는 메뉴에 없다")
    return menu[name] * quantity

print(order_chicken("후라이드", 2))
