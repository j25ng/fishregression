import requests

def main():
    length = float(input("🐟 물고기의 길이를 입력하세요 (cm): "))
    weight = get_weight(length)
    fish = get_fish(length, weight)
    print(f"🐟 물고기는 {fish}로 예측됩니다.")

def get_weight(l, url="http://13.125.209.27:8080/how_weight/fish"):
    params = {
        'length': l 
    }

    r = requests.get(url, params=params).json()
    return r['weight']

def get_fish(l, w, url="http://13.125.209.27:8080/kind_fish/fish"):
    params = {
        'length': l,
        'weight': w
    }
    
    r = requests.get(url, params=params).json()
    return r
