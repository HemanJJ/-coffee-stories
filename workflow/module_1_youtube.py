from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    parsed = urlparse(url)
    if parsed.hostname == 'youtu.be':
        return parsed.path[1:]
    if parsed.hostname in ('www.youtube.com', 'youtube.com'):
        if parsed.path == '/watch':
            return parse_qs(parsed.query)['v'][0]
    return url

def fetch_transcript(url):
    video_id = get_video_id(url)
    try:
        # 使用新版的 API 語法
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id)
        
        # 尋找可用的字幕 (優先順序: 繁體中文 > 簡體中文 > 英文)
        transcript = transcript_list.find_transcript(['zh-TW', 'zh-Hant', 'zh-CN', 'zh-Hans', 'zh', 'en'])
        
        # 取得字幕內容
        fetched = transcript.fetch()
        
        # 將所有字幕片段組合成一個大字串
        text_list = [snippet.text for snippet in fetched]
        full_text = " ".join(text_list)
        
        return full_text
    except Exception as e:
        print(f"❌ 無法抓取字幕: {e}")
        return None
