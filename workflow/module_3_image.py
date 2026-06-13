import urllib.parse
import requests

def generate_image(prompt):
    """
    因為 Pollinations 現在開始收費 (402 Error)，
    我們暫時改用 Picsum 產生隨機的高畫質圖片作為佔位符。
    未來您可以手動替換成自己喜歡的圖片，或接回付費的生圖服務。
    """
    # 2K 高畫質、微長方形 (適合 10x12) -> 1536x1920
    url = "https://picsum.photos/1536/1920"
    
    try:
        # allow_redirects=True 是必要的，因為 Picsum 會 302 重新導向
        response = requests.get(url, allow_redirects=True)
        if response.status_code == 200:
            return response.content
        else:
            print(f"❌ 圖片生成失敗: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"❌ 圖片生成發生錯誤: {e}")
        return None
