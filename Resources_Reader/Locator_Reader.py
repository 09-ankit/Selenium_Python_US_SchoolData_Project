from selenium.webdriver.common.by import By


def locate_element(locator_name):
    element = None
    locator_file_path = "F:\\AnkitNewWorkSpace\\ResuableFramwork\\src\\main\\java\\Resources\\locatorReader.txt"
    get_locator = {}

    try:
        with open(locator_file_path, 'r') as file:
            for line in file:
                data = line.strip().split("==")
                get_locator[data[0].strip()] = data[1].strip()

        locator_info = get_locator.get(locator_name, "")
        locator_parts = locator_info.split('#')
        if len(locator_parts) == 2:
            locator_type, locator_value = locator_parts[0], locator_parts[1]

            # Map locator types to By methods
            locator_map = {
                "XPath": By.XPATH,
                "ID": By.ID,
                "ClassName": By.CLASS_NAME,
                "Name": By.NAME,
                # Add more as needed
            }

            if locator_type in locator_map:
                by = locator_map[locator_type]
                element = (by, locator_value)

    except IOError as e:
        print(e)

    return element

