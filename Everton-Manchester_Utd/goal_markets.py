from selenium import webdriver
from selenium.webdriver.common.by import By


# event-197801688_odds_market-multi_goal_sign-1-2 [1, 2] (1-2)
# event-197801688_odds_market-home_goals_exact_sign-0
# event-197801688_odds_market-goal_no_goal_ht_goal_no_goal_2ht_sign-GGANDGG
# event-197801688_odds_market-total_goals_1st_+_2nd_half_sign-1-AND1-N

def get_odd_group_and_name(event_id):
    event_list = event_id.split("-")
    group = event_list[2].replace("_sign", "")
    name = '-'.join(event_list[3:])
    # print(group)
    # print(name)

    return group, name


website = 'https://sports.bet9ja.com/event/197801688'
driver = webdriver.Chrome()
driver.get(website)
# driver.maximize_window()

driver.find_element(By.XPATH, "//*[.='Goal Markets']").click()

odds_elements = driver.find_elements(By.CLASS_NAME, 'market-odd')

odds_list = []
for odds_element in odds_elements:
    event_id = odds_element.get_attribute('id')
    odd_group, odd_name = get_odd_group_and_name(event_id)
    odd_value = odds_element.text

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
