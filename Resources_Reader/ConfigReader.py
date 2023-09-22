import os


def read_configs(key):
    # Define the relative path to the config.properties file
    config_rel_path = r"Resources_holder\config.properties"

    # Get the absolute path to the project directory
    project_directory = os.path.dirname(os.path.abspath(__file__))

    # Combine the project directory path with the relative path
    configpath = os.path.join(project_directory, "..", config_rel_path)

    get_config_data = {}
    print(f"config path is {configpath}")

    try:
        with open(configpath, 'r') as file:
            for line in file:
                data = line.strip().split("=")
                get_config_data[data[0].strip()] = data[1].strip()
    except IOError as e:
        print(e)
    print(f"Current path is ==> {get_config_data.get(key)}")
    return get_config_data.get(key)


