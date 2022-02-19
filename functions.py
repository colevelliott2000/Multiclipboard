import clipboard
import json

FILENAME = 'clipboard.json'

def display_clipboard_data(data):
    for key, value in data.items():
        print(key + ' : ' + value)

def save_clipboard_data(data, key):
    data[key] = clipboard.paste()
    with open(FILENAME, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))

def load_clipboard_data():
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except:
        return {}

def load_clipboard(data, key):
    if key in data:
        clipboard.copy(data[key])
        print('Data copied to clipboard')
    else:
        print('Invalid key')

def delete_clipboard_data(data, key):
    if key in data:
        data.pop(key)
        print('Data deleted')

        with open(FILENAME, 'w') as f:
            json.dump(data, f, sort_keys=True, indent=4, separators=(',', ': '))

    else:
        print('Invalid key')