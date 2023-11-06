# ChangeChargeLimit

ChangeChargeLimit is a Python script designed to manage and modify the charging limits for your GHelper on specific days of the week. This project is intended to be run in administrator mode and requires a few configurations to work correctly.

## Prerequisites

Before using this script, make sure you have the following prerequisites in place:

1. **GHelper Installed**: Ensure you have GHelper installed on your system. You need to specify the installation location in a configuration file.

2. **Python Environment**: Make sure you have Python installed on your system.

3. **Administrator Privileges**: Run the script with administrator privileges.

4. **Configuration Files**:
    - **.env File**: Create a `.env` file with a single variable `gh_installed_location` that specifies the installation location of GHelper. Use double backward slashes in the path. For example:
      ```
      gh_installed_location="C:\\Users\\Admin\\bin\\GHelper"
      ```

    - **ChangeChargeLimit Config**: A directory named "ChangeChargeLimit" should exist in the `%AppData%` folder. Inside this directory, there should be a `config.json` file with a schedule that defines the days and their corresponding charge limits. Here's an example of what the `config.json` might look like:
      ```json
      {
        "schedule": [
          {
            "day": "Monday",
            "charge": "60"
          },
          {
            "day": "Sunday",
            "charge": "70"
          }
        ]
      }
      ```

## How It Works

The `ChangeChargeLimit` script reads the `config.json` file in the "ChangeChargeLimit" directory, fetches the current day, and checks if there is a corresponding entry in the schedule. If a match is found, it will change the GHelper's charge limit according to the schedule. The script does this by modifying the `config.json` of GHelper and restarting it.

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/bourbonbourbon/ChangeChargeLimit.git
   ```

2. Set up the configuration files as described in the "Prerequisites" section.

3. Run the script in administrator mode:

   ```bash
   python main.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you want to contribute to this project, feel free to create issues or submit pull requests.

## Notes

* Please note that this README provides a general overview of the project. Be sure to check the script and make any necessary adjustments to suit your specific setup and requirements.

## Disclaimer

**Use this software at your own risk. The author assumes no responsibility for any adverse consequences resulting from the use of this code. By running this script, you acknowledge and agree to the following:**

- The author provides this software as-is, without any warranties or guarantees of any kind.
- It is your responsibility to ensure that the script is compatible with your system and that you have followed all the necessary setup instructions.
- Any modifications made to GHelper's configuration files are at your own risk. The author is not responsible for any data loss or system instability that may occur.
- Running scripts with administrator privileges can have significant consequences. Ensure that you fully understand the script's behavior before executing it with elevated privileges.
- It is your responsibility to back up any critical data or configurations before running this script.
- If you encounter issues or errors, you should seek assistance from the developer community or relevant support channels.

**By using this software, you agree to accept all risks associated with it. The author is not liable for any damages, direct or indirect, resulting from the use or misuse of this code.**

**Always exercise caution and take necessary precautions when running code from unverified sources. If you are unsure about any part of this software or its usage, consult with a qualified professional before proceeding.**

Please take the time to review and understand this disclaimer before using this software.
