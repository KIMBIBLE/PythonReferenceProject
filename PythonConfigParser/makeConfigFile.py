import configparser

def createConfig(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "font", "Courier")
    config.set("Settings", "font_size", "10")
    config.set("Settings", "font_style", "Normal")
    config.set("Settings", "font_info",
               "You are using %(font)s at %(font_size)s pt")

    config.add_section("BYE")
    config.set("BYE", "byebye~", "20000")
    config.set("BYE", "name", "BBKIM")

    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    createConfig(path)
