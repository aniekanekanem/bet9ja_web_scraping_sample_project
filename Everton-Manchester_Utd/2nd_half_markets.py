from selenium import webdriver
from selenium.webdriver.common.by import By

# reference point code
def get_odd_group_and_name(event_id):
    event_list = event_id.split("-")  # 'event' '195698782_odds_market' '1st_half_' '_1x2_sign' '1'
    group1 = event_list[2].split("_")
    group11 = group1[0] + "_" + group1[1]
    group111 = event_list[3]
    group_iv = group111.replace("_sign", "")
    group_v = group_iv.replace(group_iv[0], "")
    group = group11 + "-" + group_v

    name = event_list[-1]

    return group, name


website = 'https://sports.bet9ja.com/event/197801688'
driver = webdriver.Chrome()
driver.get(website)
# driver.maximize_window()

driver.find_element(By.XPATH, "//*[.='2nd Half Markets']").click()


odds_elements = driver.find_elements(By.CLASS_NAME, 'market-odd')


odds_list = []
for odds_element in odds_elements:
    event_id = odds_element.get_attribute('id')
    odd_group, odd_name = get_odd_group_and_name(event_id)
    odd_value = odds_element.text

    if odd_group == "2nd_half-overunder":
        market_row = odds_element.find_element(By.XPATH, "./../..")  # Get the parent "market-row" class
        market_item = market_row.find_element(By.CLASS_NAME, 'market-item') # Then get the first "market-item" and the div inside it
        text = market_item.text  # Then get the text inside the div
        odd_group += "_" + text  # append the text inside the div to the odd_group

    if odd_group == "european_h-":
        market_row = odds_element.find_element(By.XPATH, "./../..")  # Get the parent "market-row" class
        market_item = market_row.find_element(By.CLASS_NAME, 'market-item') # Then get the first "market-item" and the div inside it
        text = market_item.text  # Then get the text inside the div
        odd_group += "1st Half" + "_" + text  # append the text inside the div to the odd_group

    if odd_group == "2nd_half-homeawayoverunder":
        market_holder__label = odds_element.find_element(By.XPATH, "./../../../..")  # This carries the div text we want.  So we get the parent "market-holder" class (e.g (starting point)2.07-->market-item(1)-->market-row(2)-->market-container market-container--right(3)-->market-holder(4)
        print('market_holder__label', market_holder__label.get_attribute('class'))  # getting the parent class which determines the no. of steps needed to get to it from the starting point which is "market-holder".  From the starting point to market-holder is 4 steps
        text_content = market_holder__label.find_element(By.TAG_NAME, 'div')
        text = text_content.text
        odd_group += "_" + text  # append the text inside the div to the odd_group


    odds_list.append((odd_group, odd_name, odd_value))


# print(odds_list)

# odds_list = [('2nd_half-1x2', '1', '4.30'), ('2nd_half-1x2', 'X', '2.51'), ('2nd_half-1x2', '2', '2.13'), ('2nd_half-doublechance', '1X', '1.59'), ('2nd_half-doublechance', '12', '1.42'), ('2nd_half-doublechance', 'X2', '1.15'), ('2nd_half-overunder', 'O', '1.21'), ('2nd_half-overunder', 'U', '3.95'), ('2nd_half-overunder', 'O', '2.02'), ('2nd_half-overunder', 'U', '1.68'), ('2nd_half-overunder', 'O', '4.20'), ('2nd_half-overunder', 'U', '1.17'), ('2nd_half-goalnogoal', 'Y', '3.20'), ('2nd_half-goalnogoal', 'N', '1.30'), ('2nd_half-correctscore', '1:0', '6.60'), ('2nd_half-correctscore', '0:0', '3.95'), ('2nd_half-correctscore', '0:1', '3.95'), ('2nd_half-correctscore', '2:0', '19.00'), ('2nd_half-correctscore', '1:1', '6.40'), ('2nd_half-correctscore', '0:2', '8.10'), ('2nd_half-correctscore', '2:1', '18.00'), ('2nd_half-correctscore', '2:2', '29.00'), ('2nd_half-correctscore', '1:2', '11.75'), ('2nd_half-correctscore', 'OTH', '8.20'), ('2nd_half-totalgoals', '1', '2.76'), ('2nd_half-totalgoals', '2', '3.55'), ('2nd_half-totalgoals', '3', '6.30'), ('2nd_half-multigoal', '12', '1.52'), ('2nd_half-multigoal', '13', '1.24'), ('2nd_half-multigoal', '23', '2.28'), ('2nd_half-oddeven', 'OD', '1.94'), ('2nd_half-oddeven', 'EV', '1.74'), ('2nd_half-drawnobet', '1', '2.80'), ('2nd_half-drawnobet', '2', '1.36'), ('away_score-', 'Y', '1.50'), ('away_score-', 'N', '2.41'), ('european_h-', '1', '13.75'), ('european_h-', 'X', '5.50'), ('european_h-', '2', '1.15'), ('european_h-', '1', '1.59'), ('european_h-', 'X', '3.35'), ('european_h-', '2', '5.20'), ('european_h-', '1', '1.08'), ('european_h-', 'X', '8.00'), ('european_h-', '2', '14.50'), ('home_score-', 'Y', '2.11'), ('home_score-', 'N', '1.65'), ('home_win-', 'Y', '5.30'), ('home_win-', 'N', '1.09'), ('away_win-', 'Y', '2.65'), ('away_win-', 'N', '1.38'), ('2nd_half-homeawayoverunder', 'HO', '2.11'), ('2nd_half-homeawayoverunder', 'AO', '1.50'), ('2nd_half-homeawayoverunder', 'HU', '1.65'), ('2nd_half-homeawayoverunder', 'AU', '2.41'), ('2nd_half-homeawayoverunder', 'HO', '7.20'), ('2nd_half-homeawayoverunder', 'AO', '3.55'), ('2nd_half-homeawayoverunder', 'HU', '1.06'), ('2nd_half-homeawayoverunder', 'AU', '1.25')]



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