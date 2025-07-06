from flask import Flask, render_template, request, jsonify
from flask import send_from_directory
import subprocess
import time
import re
import openai

app = Flask(__name__)

# 🔑 Your OpenAI API key for GPT voice search
openai.api_key = "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"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def command():
    data = request.get_json()
    action = data.get("action")

    if action == "home":
        subprocess.run(["adb", "shell", "input", "keyevent", "3"])
    elif action == "back":
        subprocess.run(["adb", "shell", "input", "keyevent", "4"])
    elif action == "ok":
        subprocess.run(["adb", "shell", "input", "keyevent", "23"])
    elif action == "up":
        subprocess.run(["adb", "shell", "input", "keyevent", "19"])
    elif action == "down":
        subprocess.run(["adb", "shell", "input", "keyevent", "20"])
    elif action == "left":
        subprocess.run(["adb", "shell", "input", "keyevent", "21"])
    elif action == "right":
        subprocess.run(["adb", "shell", "input", "keyevent", "22"])
    elif action == "power":
        subprocess.run(["adb", "shell", "input", "keyevent", "26"])
    elif action == "volume_up":
        subprocess.run(["adb", "shell", "input", "keyevent", "24"])
    elif action == "volume_down":
        subprocess.run(["adb", "shell", "input", "keyevent", "25"])
    elif action == "settings":
        subprocess.run(["adb", "shell", "am", "start", "-a", "android.settings.SETTINGS"])
    elif action == "keyboard":
        text = data.get("text", "")
        subprocess.run(["adb", "shell", "input", "text", text.replace(" ", "%s")])
    elif action == "voice_feedback":
        text = data.get("text", "")
        subprocess.run([
            "adb", "shell", "am", "broadcast",
            "-a", "com.android.intent.action.SHOW_TOAST",
            "--es", "msg", text
        ])
    elif action == "launch_youtube":
        subprocess.run(["adb", "shell", "monkey", "-p", "com.google.android.youtube.tv", "-c", "android.intent.category.LAUNCHER", "1"])
    elif action == "launch_netflix":
        subprocess.run(["adb", "shell", "monkey", "-p", "com.netflix.ninja", "-c", "android.intent.category.LAUNCHER", "1"])
    elif action == "launch_prime":
        subprocess.run(["adb", "shell", "monkey", "-p", "com.amazon.amazonvideo.livingroom", "-c", "android.intent.category.LAUNCHER", "1"])
    elif action == "launch_hotstar":
        subprocess.run(["adb", "shell", "monkey", "-p", "in.startv.hotstar", "-c", "android.intent.category.LAUNCHER", "1"])
    elif action == "open_tv_settings":
     subprocess.run([
        "adb", "shell", "am", "start", "-a", "android.settings.SETTINGS"
    ])
    elif action == "power":
     subprocess.run(["adb", "shell", "input", "keyevent", "26"])
    elif action == "num_0":
     subprocess.run(["adb", "shell", "input", "keyevent", "7"])
    elif action == "num_1":
     subprocess.run(["adb", "shell", "input", "keyevent", "8"])
    elif action == "num_2":
     subprocess.run(["adb", "shell", "input", "keyevent", "9"])
    elif action == "num_3":
     subprocess.run(["adb", "shell", "input", "keyevent", "10"])
    elif action == "num_4":
     subprocess.run(["adb", "shell", "input", "keyevent", "11"])
    elif action == "num_5":
     subprocess.run(["adb", "shell", "input", "keyevent", "12"])
    elif action == "num_6":
     subprocess.run(["adb", "shell", "input", "keyevent", "13"])
    elif action == "num_7":
     subprocess.run(["adb", "shell", "input", "keyevent", "14"])
    elif action == "num_8":
     subprocess.run(["adb", "shell", "input", "keyevent", "15"])
    elif action == "num_9":
     subprocess.run(["adb", "shell", "input", "keyevent", "16"])
    elif action == "vol_up":
     subprocess.run(["adb", "shell", "input", "keyevent", "24"])
    elif action == "vol_down":
     subprocess.run(["adb", "shell", "input", "keyevent", "25"])
    elif action == "mute":
     subprocess.run(["adb", "shell", "input", "keyevent", "164"])
    elif action == "voice_input":
     text = data.get("text", "")
     subprocess.run(["adb", "shell", "input", "text", text.replace(" ", "%s")])
    elif action == "launch_assistant":
     subprocess.run(["adb", "shell", "am", "start", "-a", "com.google.android.voiceinteraction.GOOGLE_VOICE_ASSIST"])
    elif action == "toggle_cursor":
     subprocess.run(["adb", "shell", "input", "keyevent", "82"])  # or your custom APK receiver
    elif action == "youtube_search":
     query = data.get("query", "")
     if query:
        # Open YouTube search input (if not already open)
        # Then type and press Enter
        subprocess.run(["adb", "shell", "input", "text", query.replace(" ", "%s")])
        time.sleep(1)
        subprocess.run(["adb", "shell", "input", "keyevent", "66"])  # Enter key

    elif action == "reminder":
        message = data.get("message")
        time_str = data.get("time")
        print(f"[Reminder] At {time_str}: {message}")
        # Optionally save or schedule reminder in backend
    elif action == "gpt_command":
        text = data.get("text", "")
        # Use OpenAI to interpret the command (optional extension)
        print("GPT command received:", text)
    elif action == "tap":
        x = str(data.get("x"))
        y = str(data.get("y"))
        subprocess.run(["adb", "shell", "input", "tap", x, y])
        subprocess.run([
            "adb", "shell", "am", "broadcast",
            "-a", "com.android.intent.action.SHOW_TOAST",
            "--es", "msg", f"👆 Tapped at {x}, {y}"])
    elif action == "swipe":
        x1 = str(data.get("x1"))
        y1 = str(data.get("y1"))
        x2 = str(data.get("x2"))
        y2 = str(data.get("y2"))
        subprocess.run(["adb", "shell", "input", "swipe", x1, y1, x2, y2, "100"])
    elif action == "youtube_search":
     query = data.get("query", "")

    if query:
        # Step 1: Launch YouTube app on TV
        subprocess.run([
            "adb", "shell", "monkey", "-p", "com.google.android.youtube.tv",
            "-c", "android.intent.category.LAUNCHER", "1"
        ])
        time.sleep(2)

        # Step 2: (Optional GPT clean)
        import openai
        openai.api_key = "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"

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a voice assistant that reformats user speech into short YouTube search keywords."},
                    {"role": "user", "content": f"User said: '{query}'"}
                ]
            )
            cleaned_query = response['choices'][0]['message']['content'].strip()
        except Exception as e:
            cleaned_query = query  # fallback if GPT fails

        # Step 3: Send cleaned query to TV
        # subprocess.run(["adb", "she])  # Removed invalid/incomplete line


        try:
            gpt_response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Turn user voice into a clean search query for Android TV."},
                    {"role": "user", "content": query}
                ]
            )
            clean_query = gpt_response.choices[0].message.content.strip()
        except Exception as e:
            print("GPT error:", e)
            return jsonify({"status": "GPT failed"})

        subprocess.run(["adb", "shell", "input", "text", clean_query.replace(" ", "%s")])
        time.sleep(0.5)
        subprocess.run(["adb", "shell", "input", "keyevent", "66"])  # Enter key
        return jsonify({"status": f"Typed: {clean_query}"})

    return jsonify({"status": "ok"})

@app.route('/screen', methods=['GET'])
def screen_size():
    result = subprocess.run(["adb", "shell", "wm", "size"], capture_output=True, text=True)
    match = re.search(r"Physical size: (\d+)x(\d+)", result.stdout)
    if match:
        return jsonify({"width": int(match.group(1)), "height": int(match.group(2))})
    return jsonify({"width": 1920, "height": 1080})

@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

