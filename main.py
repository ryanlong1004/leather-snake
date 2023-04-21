from src.view import View

import json
import requests
import logging

# logging.basicConfig(filename="leather-snake.log", encoding="utf-8", level=logging.INFO)

if __name__ == "__main__":
    url = "https://www.google.com/async/lr_mt_h?ei=FbdBZKCvOvjV5NoPneS-IA&client=firefox-b-1-d&yv=3&p3=1&cs=0&async=sp:4,lmid:%2Fm%2F09p14,emid:%2Fg%2F11sd4nylc8,itoefe:true,ct:US,hl:en,tz:America%2FNew_York,_fmt:jspb"

    response = requests.get(url).text.split("\n", 1)[1]
    obj = json.loads(response)
    team_a, team_b = obj["match_for_header"][1], obj["match_for_header"][2]

    team_a_name, team_a_score = team_a[0][0], team_a[9]
    team_b_name, team_b_score = team_b[0][0], team_b[9]
    print(f"{team_a_name}: {team_a_score} vs. {team_b_name}, {team_b_score}")
