from selenium import webdriver
from selenium.webdriver.common.by import By


# event-197801688_odds_market-home_away_-_over_under_sign-OH
# event-197801688_odds_market-home_no_bet_sign-X
# event-197801688_odds_market-home_score_both_halves_sign-Y
# event-197801688_odds_market-highest_scoring_half_home_team_sign-1

def get_odd_group_and_name(event_id):
    event_list = event_id.split("-")
    group = event_list[2].replace("_sign", "")
    name = event_list[-1]
    # print(group)
    # print(name)

    return group, name


website = 'https://sports.bet9ja.com/event/197801688'
driver = webdriver.Chrome()
driver.get(website)
# driver.maximize_window()

driver.find_element(By.XPATH, "//*[.='Home / Away']").click()

odds_elements = driver.find_elements(By.CLASS_NAME, 'market-odd')

odds_list = []
for odds_element in odds_elements:
    event_id = odds_element.get_attribute('id')
    odd_group, odd_name = get_odd_group_and_name(event_id)
    odd_value = odds_element.text

    if odd_group == "home_away_":
        market_holder__label = odds_element.find_element(By.XPATH, "./../../../..")
        text_content = market_holder__label.find_element(By.TAG_NAME, 'div')
        text = text_content.text  # Then get the text inside the div
        odd_group += "Over/Under" + "_" + text


    odds_list.append((odd_group, odd_name, odd_value))

odds_dictionary = {}
for odds_tuple in odds_list:
    odd_group, odd_name, odd_value = odds_tuple

    if odd_group not in odds_dictionary:
        odds_dictionary[odd_group] = {}

    odds_dictionary[odd_group][odd_name] = odd_value

    print(odd_group, odd_name, odd_value)

print("\n\n")
print(odds_dictionary)

driver.quit()
