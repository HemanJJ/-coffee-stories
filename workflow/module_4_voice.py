import edge_tts

async def generate_voice(text, output_file, voice_type="female"):
    if voice_type == "female":
        voice = "zh-TW-HsiaoChenNeural" # 溫暖女聲 (預設)
    else:
        voice = "zh-TW-YunJheNeural" # 沉穩男聲
        
    communicate = edge_tts.Communicate(text, voice, rate="-10%") 
    await communicate.save(output_file)
    return output_file


async def generate_voice_with_fallback(text, output_file, voice_type="female"):
    output_path = __import__("pathlib").Path(output_file)
    temp_path = output_path.with_suffix(".tmp.mp3")
    fallback_order = [voice_type]
    if voice_type != "female":
        fallback_order.append("female")

    last_error = None
    for candidate in fallback_order:
        try:
            if temp_path.exists():
                temp_path.unlink()
            await generate_voice(text, str(temp_path), candidate)
            if temp_path.exists() and temp_path.stat().st_size > 0:
                temp_path.replace(output_path)
                return True, candidate, ""
            last_error = RuntimeError("TTS produced an empty audio file.")
        except Exception as exc:
            last_error = exc

    if temp_path.exists():
        temp_path.unlink()
    return False, "", str(last_error)


async def generate_dialogue_voice(turns, output_dir):
    output_dir.mkdir(parents=True, exist_ok=True)
    audio_paths = []
    for index, turn in enumerate(turns, start=1):
        speaker = turn.get("speaker", "female")
        text = turn.get("text", "").strip()
        if not text:
            continue
        output_file = output_dir / f"dialogue_{index:02d}_{speaker}.mp3"
        await generate_voice(text, str(output_file), speaker)
        audio_paths.append(output_file)
    return audio_paths
