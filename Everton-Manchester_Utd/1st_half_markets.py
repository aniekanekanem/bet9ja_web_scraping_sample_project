from selenium import webdriver
from selenium.webdriver.common.by import By

# event-195698782_odds_market-1st_half_-_1x2_sign-1
# event-195698782_odds_market-1st_half_-_double_chance_sign-1X
# event-195698782_odds_market-away_score_1st_half_sign-Y

def get_odd_group_and_name(event_id):
    event_list = event_id.split("-")  # 'event' '195698782_odds_market' '1st_half_' '_1x2_sign' '1'
    group1 = event_list[2].split("_")
    group11 = group1[0] + "_" + group1[1]
    group111 = event_list[3]
    group_iv = group111.replace("_sign", "")
    group_v = group_iv.replace(group_iv[0], "")
    group = group11 + "-" + group_v

    name = event_list[-1]


    # print(group_v)
    # print(group11)

    return group, name


website = 'https://sports.bet9ja.com/event/220963121'
driver = webdriver.Chrome()
driver.get(website)
# driver.maximize_window()


driver.find_element(By.XPATH, "//*[.='1st Half Markets']").click()

odds_elements = driver.find_elements(By.CLASS_NAME, 'market-odd')


odds_list = []
for odds_element in odds_elements:
    event_id = odds_element.get_attribute('id')
    odd_group, odd_name = get_odd_group_and_name(event_id)
    odd_value = odds_element.text

    if odd_group == "1st_half-overunder":
        market_row = odds_element.find_element(By.XPATH, "./../..")  # Get the parent "market-row" class
        market_item = market_row.find_element(By.CLASS_NAME, 'market-item') # Then get the first "market-item" and the div inside it
        text = market_item.text  # Then get the text inside the div
        odd_group += "_" + text  # append the text inside the div to the odd_group

    if odd_group == "european_h-":
        market_row = odds_element.find_element(By.XPATH, "./../..")  # Get the parent "market-row" class
        market_item = market_row.find_element(By.CLASS_NAME, 'market-item') # Then get the first "market-item" and the div inside it
        text = market_item.text  # Then get the text inside the div
        odd_group += "1st Half" + "_" + text  # append the text inside the div to the odd_group

    if odd_group == "1st_half-homeawayoverunder":
        market_holder__info = odds_element.find_element(By.XPATH, "./../../../..")  # Get the parent "market-row" class
        market_holder__label = market_holder__info.find_element(By.TAG_NAME, 'div') # Then get the first "market-item" and the div inside it
        text = market_holder__label.text  # Then get the text inside the div
        odd_group += "_" + text  # append the text inside the div to the odd_group

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

