##############################
# Author:   Josh West        #
# Discord:  Pigeon#2628      #
# Date:     14-06-2023       #
# Version:  1.0              #
##############################


import requests
import yaml
import os


def unfollow_channel(headers, channel_id):
    unfollow_payload = [
        {
            "operationName": "FollowButton_UnfollowUser",
            "variables": {
                "input": {
                    "targetID": channel_id
                }
            },
            "extensions": {
                "persistedQuery": {
                    "version": 1,
                    "sha256Hash": "f7dae976ebf41c755ae2d758546bfd176b4eeb856656098bb40e0a672ca0d880"
                }
            }
        }
    ]

    resp = requests.post('https://gql.twitch.tv/gql', headers=headers, json=unfollow_payload)
    if resp.status_code != 200:
        print(f"Error unfollowing: {channel_id}")
        print(resp.status_code)
        print(resp.text)
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Error unfollowing: {channel_id}\n")
            log_file.write(f"Response status code: {resp.status_code}\n")
            log_file.write(f"Response text: {resp.text}\n")
        exit(1)

    json_resp = resp.json()

    if json_resp[0]['data']['unfollowUser']['follow'] is None:
        print(f"Already unfollowed: {channel_id}")
    else:
        display_name = json_resp[0]['data']['unfollowUser']['follow']['user']['displayName']
        print(f"Unfollowed: {display_name}")
        with open('log.txt', 'a') as log_file:
            log_file.write(f"Unfollowed: {display_name}\n")


def main():
    try:
        with open('config.yml', 'r') as config_file:
            config = yaml.safe_load(config_file)
    except FileNotFoundError:
        print("Failed to read config.yml, have you created the file?")
        exit(1)

    necessary_headers = ['Authorization', 'Client-Id', 'Client-Integrity', 'X-Device-Id', 'Content-Type']
    headers = {header: config.get(header) for header in necessary_headers}

    if None in headers.values():
        print("Missing headers in config.yml")
        exit(1)

    # Whitelist = config.get('Whitelist', [])

    done = False
    while not done:
        get_channels_payload = [
            {
                "operationName": "ChannelFollows",
                "variables": {
                    "limit": 100,
                    "order": "DESC"
                },
                "extensions": {
                    "persistedQuery": {
                        "version": 1,
                        "sha256Hash": "eecf815273d3d949e5cf0085cc5084cd8a1b5b7b6f7990cf43cb0beadf546907"
                    }
                }
            }
        ]
        channels_resp = requests.post('https://gql.twitch.tv/gql', headers=headers, json=get_channels_payload)
        if channels_resp.status_code != 200:
            print("Error getting followed channels")
            print(channels_resp.status_code)
            print(channels_resp.text)
            with open('log.txt', 'a') as log_file:
                log_file.write("Error getting followed channels\n")
                log_file.write(f"Response status code: {channels_resp.status_code}\n")
                log_file.write(f"Response text: {channels_resp.text}\n")
            exit(1)

        channels_json_resp = channels_resp.json()
        channel_edges = channels_json_resp[0]['data']['user']['follows']['edges']
        channel_ids = set([c['node']['id'] for c in channel_edges])
        if len(channel_ids) == 0:
            done = True
            continue

        for channel in channel_edges:
            channel_id = channel['node']['id']
            # display_name = channel['node']['displayName']
            # if display_name in Whitelist:
            #     print(f"Skipping whitelisted channel: {display_name}")
            #     continue

            unfollow_channel(headers, channel_id)


if __name__ == '__main__':
    if not os.path.exists('log.txt'):
        open('log.txt', 'w').close()  # Create the log file if it doesn't exist
    else:
        open('log.txt', 'w').close()  # Clear the log file if it exists

    main()