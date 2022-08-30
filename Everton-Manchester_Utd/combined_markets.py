from selenium import webdriver
from selenium.webdriver.common.by import By


# event-197801688_odds_market-1x2_+_over_under_sign-1O [event-197801688_odds_market-, 1x2_+_over_under_sign-1O]
# 1x2_+_over_under_sign-1O => ['1x2_+_over_under_sign-', '1O']
# event-197801688_odds_market-1st_half_-_1x2_+_over_under_sign-1O1T [event-197801688_odds_market-, 1st_half_-_1x2_+_over_under_sign-1O1T]
# 1st_half_-_1x2_+_over_under_sign-1O1T => ['1st_half_-_1x2_+_over_under_sign-', '101T']
# event-197801688_odds_market-goal_no_goal_+_over_under_sign-GGOVER
# event-197801688_odds_market-1st_half_-_double_chance_over_under_sign-1XO
# event-197801688_odds_market-1st_half_-_double_chance_+_goal_no_goal_sign-1XGGHT

def get_odd_group_and_name(event_id):
    event_group_and_name = (event_id.split("odds_market-"))[1]
    event_group_and_name_delimiter = "_sign-"
    event_group_and_name_list = event_group_and_name.split(event_group_and_name_delimiter)
    group = event_group_and_name_list[0].replace(event_group_and_name_delimiter, '')
    name = event_group_and_name_list[1]

    return group, name


website = 'https://sports.bet9ja.com/event/197801688'
driver = webdriver.Chrome()
driver.get(website)
# driver.maximize_window()

driver.find_element(By.XPATH, "//*[.='Combined Markets']").click()

odds_elements = driver.find_elements(By.CLASS_NAME, 'market-odd')

odds_list = []
for odds_element in odds_elements:
    event_id = odds_element.get_attribute('id')
    odd_group, odd_name = get_odd_group_and_name(event_id)
    print('odd_group', odd_group)
    print('odd_name', odd_name)
    odd_value = odds_element.text
#
    if odd_group == "1x2_+_over_under":
        small = odds_element.find_element(By.XPATH, "./../..")
        text_content = small.find_element(By.TAG_NAME, 'div')
        text = text_content.text  # Then get the text inside the div
        odd_group += "_" + text

    if odd_group == "1st_half_-_1x2_+_over_under":
        small = odds_element.find_element(By.XPATH, "./../..")
        text_content = small.find_element(By.TAG_NAME, 'div')
        text = text_content.text
        odd_group += "_" + text

    if odd_group == "2nd_half_-_1x2_+_over_under":
        small = odds_element.find_element(By.XPATH, "./../..")
        text_content = small.find_element(By.TAG_NAME, 'div')
        text = text_content.text
        odd_group += "_" + text

    if odd_group == "goal_no_goal_+_over_under":
        small = odds_element.find_element(By.XPATH, "./../..")
        text_content = small.find_element(By.CLASS_NAME, 'small')
        text = text_content.text
        odd_group += "_" + text

    if odd_group == "double_chance_+_over_under_":
        small = odds_element.find_element(By.XPATH, "./../..")
        text_content = small.find_element(By.CLASS_NAME, 'small')
        text = text_content.text
        odd_group += "_" + text

    if odd_group == "1st_half_-_double_chance_over_under":
        small = odds_element.find_element(By.XPATH, './../..')
        text_content = small.find_element(By.CLASS_NAME, 'small')
        text = text_content.text
        odd_group += "_" + text

    if odd_group == "2nd_half_-_double_chance_over_under":
        small = odds_element.find_element(By.XPATH, './../..')
        text_content = small.find_element(By.CLASS_NAME, 'small')
        text = text_content.text
        odd_group += "_" + text

    if odd_group == "ht_ft_o_u":
        small = odds_element.find_element(By.XPATH, './../..')
        text_content = small.find_element(By.TAG_NAME, 'div')
        text = text_content.text
        odd_group += "_" + text

    if odd_group == "ht_ft_o_u_1,5_ht":
        small = odds_element.find_element(By.XPATH, './../..')
        text_content = small.find_element(By.TAG_NAME, 'div')
        text = text_content.text
        odd_group += "_" + text
#
#
    odds_list.append((odd_group, odd_name, odd_value))
#
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
