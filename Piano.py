import keyboard
import time
import re

shift_chars = {
    '!': ('1', True),
    '@': ('2', True),
    '$': ('4', True),
    '%': ('5', True),
    '^': ('6', True),
    '*': ('8', True),
    '(': ('9', True),
}

special_keys = {
    '^': 'ctrl',
    '%': '%',
    '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
    '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',
}

input_sequence = """
Music Code!
"""

def parse_input(seq):
    parts = re.split(r'(-)', seq)
    return [p.strip() for p in parts if p.strip() != '']

def clean_keys(s):
    s = s.strip()
    if s.startswith('[') and s.endswith(']'):
        s = s[1:-1]
    return s.replace(' ', '').lower()

sequence_parts = parse_input(input_sequence)

print("Starting...")
time.sleep(3)

for part in sequence_parts:
    if part == '-':
        time.sleep(0.2)
    else:
        if part.startswith('[') and part.endswith(']'):
            keys = clean_keys(part)

            for k in keys:
                key_to_press = special_keys.get(k, k)
                keyboard.press(key_to_press)

            for k in keys:
                key_to_release = special_keys.get(k, k)
                time.sleep(0.05)
                keyboard.release(key_to_release)
        else:
            for original_k in part.replace(' ', ''):
                if original_k in shift_chars:
                    base_key, need_shift = shift_chars[original_k]

                    if need_shift:
                        keyboard.press('shift')

                    keyboard.press(base_key)
                    time.sleep(0.2)
                    keyboard.release(base_key)

                    if need_shift:
                        keyboard.release('shift')
                else:
                    k = original_k.lower()
                    key_to_press = special_keys.get(k, k)

                    if original_k.isupper():
                        keyboard.press('shift')
                    keyboard.press(key_to_press)
                    time.sleep(0.1)
                    try:
                        keyboard.release(key_to_press)
                    except Exception:
                        print(f"")

                    if original_k.isupper():
                        keyboard.release('shift')

print("Done!")
