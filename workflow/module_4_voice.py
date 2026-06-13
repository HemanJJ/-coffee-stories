import edge_tts

async def generate_voice(text, output_file, voice_type="female"):
    if voice_type == "female":
        voice = "zh-TW-HsiaoChenNeural" # 溫暖女聲 (預設)
    else:
        voice = "zh-TW-YunJheNeural" # 沉穩男聲
        
    communicate = edge_tts.Communicate(text, voice, rate="-10%") 
    await communicate.save(output_file)
