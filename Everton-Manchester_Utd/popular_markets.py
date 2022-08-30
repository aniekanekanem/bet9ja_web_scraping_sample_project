from selenium import webdriver
from selenium.webdriver.common.by import By


def get_odd_group_and_name(event_id):
    event_list = event_id.split("-")
    group = event_list[2].replace("_sign", "")
    name = event_list[3]

    return group, name


website = 'https://sports.bet9ja.com/event/197801688'
driver = webdriver.Chrome()
driver.get(website)
# driver.maximize_window()

odds_elements = driver.find_elements(By.CLASS_NAME, 'market-odd')


odds_list = []
for odds_element in odds_elements:
    event_id = odds_element.get_attribute('id')
    odd_group, odd_name = get_odd_group_and_name(event_id)
    odd_value = odds_element.text

    if odd_group == "over_under":
        market_row = odds_element.find_element(
            By.XPATH, "./../..")  # Get the parent "market-row" class
        # Then get the first "market-item" and the div inside it
        market_item = market_row.find_element(By.CLASS_NAME, 'market-item')
        text = market_item.text  # Then get the text inside the div
        odd_group += "_" + text  # append the text inside the div to the odd_group

    if odd_group == "handicap":
        market_item = odds_element.find_element(
            By.XPATH, "./..")  # Get the parent "market-item" class
        print("Parent class attribute: " + market_item.get_attribute("class"))
        # Then get the first "market-item" and the div inside it
        text_div = market_item.find_element(By.TAG_NAME, 'div')
        text = text_div.text  # Then get the text inside the div
        text = text.split("(")  # Split the text
        text = "(" + text[1]
        print("Text: " + text)
        odd_group += "_" + text  # append the text inside the div to the odd_group

    odds_list.append((odd_group, odd_name, odd_value))


print(odds_list)

odds_list = [('1x2', '1', '4.50'), ('1x2', 'X', '3.80'), ('1x2', '2', '1.80'), ('double_chance', '1X', '1.98'), ('double_chance', '12', '1.25'), ('double_chance', 'X2', '1.19'), ('over_under', 'O', '1.04'), ('over_under', 'U', '10.25'), ('over_under', 'O', '1.26'), ('over_under', 'U', '3.45'), ('over_under', 'O', '1.84'), ('over_under', 'U', '1.93'), ('over_under', 'O', '3.00'), ('over_under', 'U', '1.35'), ('over_under', 'O', '5.30'), ('over_under', 'U', '1.12'), ('over_under', 'O', '9.90'), ('over_under', 'U', '1.00'), ('over_under', 'O', '17.00'), ('over_under', 'U', '1.00'), ('goal_no_goal', 'Y', '1.74'), ('goal_no_goal', 'N', '2.04'), ('odd_even', 'OD', '1.89'), ('odd_even', 'EV', '1.88'), ('correct_score', '1:0', '12.50'), ('correct_score', '0:0', '10.25'), ('correct_score', '0:1', '7.00'), ('correct_score', '2:0', '27.00'), ('correct_score', '1:1', '7.40'), ('correct_score', '0:2', '9.20'), ('correct_score', '2:1', '14.75'), ('correct_score', '2:2', '15.00'), ('correct_score', '0:3', '17.00'), ('correct_score', '3:0', '69.00'), ('correct_score', '3:3', '58.00'), ('correct_score', '0:4', '38.00'), ('correct_score', '3:1', '40.00'), ('correct_score', '4:4', '185.00'), ('correct_score', '1:2', '8.30'), ('correct_score', '3:2', '40.00'), ('correct_score', '1:3', '14.25'), ('correct_score', '4:0', '154.00'), ('correct_score', 'OTH', '22.00'), ('correct_score', '1:4', '31.00'), ('correct_score', '4:1', '109.00'), ('correct_score', '2:3', '23.00'), ('correct_score', '4:2', '108.00'), ('correct_score', '2:4', '48.00'), ('correct_score', '4:3', '136.00'), ('correct_score', '3:4', '99.00'), ('half_time_full_time', '1/1', '7.30'), ('half_time_full_time', '1/X', '16.00'), ('half_time_full_time', '1/2', '25.00'), ('half_time_full_time', 'X/1', '10.00'), ('half_time_full_time', 'X/X', '5.50'), ('half_time_full_time', 'X/2', '4.80'), ('half_time_full_time',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   '2/1', '39.00'), ('half_time_full_time', '2/X', '16.00'), ('half_time_full_time', '2/2', '2.73'), ('handicap', '1H', '11.50'), ('handicap', 'XH', '5.10'), ('handicap', '2H', '1.19'), ('handicap', '1H', '1.98'), ('handicap', 'XH', '3.30'), ('handicap', '2H', '3.20'), ('handicap', '1H', '1.25'), ('handicap', 'XH', '5.60'), ('handicap', '2H', '6.60'), ('handicap', '1H', '1.02'), ('handicap', 'XH', '11.75'), ('handicap', '2H', '15.00'), ('draw_no_bet', '1', '3.20'), ('draw_no_bet', '2', '1.32'), ('multi_c_score_(1)', '0011', '4.70'), ('multi_c_score_(1)', '223344', '10.75'), ('multi_c_score_(1)', '102021', '5.30'), ('multi_c_score_(1)', '010212', '2.66'), ('multi_c_score_(1)', '303132', '14.25'), ('multi_c_score_(1)', '031323', '5.60'), ('multi_c_score_(1)', '414243', '31.00'), ('multi_c_score_(1)', '142434', '14.50'), ('multi_c_score_(1)', '4004O', '12.00'), ('multi_c_score(2)', '00110110', '2.21'), ('multi_c_score(2)', '20213031', '6.80'), ('multi_c_score(2)', '02120313', '2.76'), ('multi_c_score(2)', '22233233', '6.60'), ('multi_c_score(2)', '40414243', '28.00'), ('multi_c_score(2)', '04142434', '10.75'), ('multi_c_score(2)', '44O', '16.00'), ('score_5_minutes', 'YF5M', '7.80'), ('score_5_minutes', 'NF5M', '1.02'), ('score_10_minutes', 'YS10M', '4.80'), ('score_10_minutes', 'NS10M', '1.11'), ('score_20_minutes', 'YS20M', '2.32'), ('score_20_minutes', 'NS20M', '1.47'), ('score_30_minutes', 'YS30M', '1.73'), ('score_30_minutes', 'NS30M', '1.88'), ('gg_ng_2+', 'GG', '6.10'), ('gg_ng_2+', 'NG', '1.09'), ('total_goals_(exact)', '1', '4.70'), ('total_goals_(exact)', '2', '3.80'), ('total_goals_(exact)', '3', '4.15'), ('total_goals_(exact)', '4', '5.60'), ('total_goals_(exact)', '5', '8.90'), ('total_goals_(exact)', '6', '15.00'), ('first_team_to_score', '1', '2.68'), ('first_team_to_score', 'X', '10.25'), ('first_team_to_score', '2', '1.59')]

odds_dictionary = {}
for odds_tuple in odds_list:
    odd_group, odd_name, odd_value = odds_tuple

    if odd_group not in odds_dictionary:
        odds_dictionary[odd_group] = {}
    odds_dictionary[odd_group][odd_name] = odd_value
    print(odd_group, odd_name, odd_value)

print("\n\n")
print(odds_dictionary)

# working
