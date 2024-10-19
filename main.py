import requests
import json
import time
from colorama import Fore, init
import random

# تفعيل الألوان في جميع الأنظمة
init(autoreset=True)

# قراءة query_id الكامل من ملف data.txt
def read_query_id_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            query_id = file.read().strip()
            return query_id
    except FileNotFoundError:
        print(Fore.RED + f"❌ File {file_path} not found!")
        return None

# قراءة query_id من ملف data.txt
query_id = read_query_id_from_file('data.txt')

# بعض الأشكال والرموز العشوائية للإخراج الجذاب
success_emoji = random.choice(['✅', '🎉', '✨', '👍', '✔️'])
loading_emoji = random.choice(['⏳', '🔄', '🔄', '🚀', '💫'])
error_emoji = random.choice(['❌', '⚠️', '🚫', '😔'])

if query_id:
    url_auth = "https://major.bot/api/auth/tg/"

    # استخدام query_id بالكامل كما هو
    init_data = query_id

    payload_auth = {
        "init_data": init_data
    }

    headers_auth = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        'Accept': "application/json, text/plain, */*",
        'Content-Type': "application/json",
        'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://major.bot",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://major.bot/",
        'accept-language': "en-US,en;q=0.9"
    }

    try:
        # إخراج جذاب عند إرسال الطلب الأول
        print(Fore.YELLOW + loading_emoji + " Sending Authentication Request...")

        response_auth = requests.post(url_auth, json=payload_auth, headers=headers_auth)
        
        if response_auth.status_code == 200:
            response_data = response_auth.json()
            access_token = response_data.get('access_token')
            user_data = response_data.get('user')

            if access_token and user_data:
                username = user_data.get('username', 'User')
                print(Fore.GREEN + success_emoji + " Welcome, "+ Fore.RED+ f" [{username}] " +Fore.GREEN +" ! Authentication Success! Waiting...⏳ ")
                time.sleep(15)
                # إرسال طلب Swipe Coin
                print(Fore.CYAN + loading_emoji + " Sending Swipe Coin Request...")

                url_swipe_coin = "https://major.bot/api/swipe_coin/"
                payload_swipe_coin = json.dumps({"coins": 2900})

                headers_swipe_coin = {
                    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
                    'Accept': "application/json, text/plain, */*",
                    'Content-Type': "application/json",
                    'authorization': f"Bearer {access_token}",
                    'origin': "https://major.bot",
                    'sec-fetch-site': "same-origin",
                    'sec-fetch-mode': "cors",
                    'sec-fetch-dest': "empty",
                    'referer': "https://major.bot/games/swipe-coin"
                }

                response_swipe_coin = requests.post(url_swipe_coin, data=payload_swipe_coin, headers=headers_swipe_coin)
                
                if response_swipe_coin.status_code == 201:
                    print(Fore.GREEN + success_emoji + " Swipe Coin Request Success!")
                else:
                    print(Fore.RED + error_emoji + f" Swipe Coin Error {response_swipe_coin.status_code}: {response_swipe_coin.text}")
                    print(Fore.YELLOW + "You have failed to receive the coins. Please try again after 7 hours.")

                # تأخير زمني لتجنب الحظر
                time.sleep(15)

                # إرسال طلب Bonuses Coins
                print(Fore.CYAN + loading_emoji + " Sending Bonuses Coins Request...")

                url_bonuses = "https://major.bot/api/bonuses/coins/"
                payload_bonuses = json.dumps({"coins": 915})

                headers_bonuses = {
                    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
                    'Accept': "application/json, text/plain, */*",
                    'Content-Type': "application/json",
                    'authorization': f"Bearer {access_token}",
                    'origin': "https://major.bot",
                    'sec-fetch-site': "same-origin",
                    'sec-fetch-mode': "cors",
                    'sec-fetch-dest': "empty",
                    'referer': "https://major.bot/games/hold-coin"
                }

                response_bonuses = requests.post(url_bonuses, data=payload_bonuses, headers=headers_bonuses)
                
                if response_bonuses.status_code == 201:
                    print(Fore.GREEN + success_emoji + " Bonuses Coins Request Success!")
                else:
                    print(Fore.RED + error_emoji + f" Bonuses Coins Error {response_bonuses.status_code}: {response_bonuses.text}")
                    print(Fore.YELLOW + "You have failed to receive the bonuses. Please try again after 7 hours.")

                # تأخير زمني لتجنب الحظر
                time.sleep(15)

                # إرسال طلب Roulette
                print(Fore.CYAN + loading_emoji + " Sending Roulette Request...")

                url_roulette = "https://major.bot/api/roulette/"
                payload_roulette = json.dumps({})

                headers_roulette = {
                    'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
                    'Accept': "application/json, text/plain, */*",
                    'Content-Type': "application/json",
                    'authorization': f"Bearer {access_token}",
                    'origin': "https://major.bot",
                    'sec-fetch-site': "same-origin",
                    'sec-fetch-mode': "cors",
                    'sec-fetch-dest': "empty",
                    'referer': "https://major.bot/games/roulette"
                }

                response_roulette = requests.post(url_roulette, data=payload_roulette, headers=headers_roulette)
                
                if response_roulette.status_code == 201:
                    print(Fore.GREEN + success_emoji + " Roulette Request Success!")
                else:
                    print(Fore.RED + error_emoji + f" Roulette Error {response_roulette.status_code}: {response_roulette.text}")
                    print(Fore.YELLOW + "You have failed to receive the roulette reward. Please try again after 7 hours.")

            else:
                print(Fore.RED + error_emoji + " Authentication Failed! Access Token or User data not found.")
        else:
            print(Fore.RED + error_emoji + f" Auth Error {response_auth.status_code}: {response_auth.text}")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + error_emoji + " An error occurred:", e)

else:
    print(Fore.RED + error_emoji + " Query ID not found in data.txt!")
