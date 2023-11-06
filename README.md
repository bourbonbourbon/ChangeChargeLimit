# ChangeChargeLimit

ChangeChargeLimit is a Python script designed to manage and modify the charging limits for your GHelper on specific days of the week. This project is intended to be run in administrator mode and requires a few configurations to work correctly.

**This Python script can be ran at user login using Window's built-in Task Scheduler.**

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

## Scheduling with Windows Task Scheduler

1. **Create a New Folder in Task Scheduler Library**:
   - In Windows Task Scheduler, it's a good practice to create a separate folder for your task. To do this, right-click on the "Task Scheduler Library" in the left panel and select "New Folder." Give the folder an appropriate name.

2. **Create a New Task**:
   - Inside the newly created folder, right-click and select "Create Task..." (not "Basic Task"). This will open the task creation window.

3. **General Tab**:
   - In the "General" tab of the task properties:
     - Name your task and provide an optional description.
     - Check the "Run with highest privileges" checkbox to ensure the task runs with administrator privileges.
     - In the "Security Options" section, ensure that "Run only when the user is logged on" is the only radio button selected.

4. **Triggers Tab**:
   - In the "Triggers" tab:
     - Create a new trigger by clicking "New...".
     - In the "Begin the task" drop-down menu, select "At log on." You can also choose the specific user, if necessary.
     - In the "Advanced Settings" section:
       - Toggle "Repeat task every" and select 1 hour.
       - For "for a duration of," select "Indefinitely."
       - Select "Stop task if it runs longer than" and set it to 4 hours.
     - Ensure that the "Enabled" checkbox is checked to enable the trigger.

5. **Actions Tab**:
   - In the "Actions" tab:
     - Create a new action by clicking "New...".
     - In the "Program/script" field, provide the full path to the Python executable (e.g., `C:\Users\Admin\AppData\Local\Programs\Python\python.exe` or wherever you might have installed it).
     - In the "Add arguments (optional)" field, set it to `main.py`.
     - In the "Start in (optional)" field, specify the path where your Git repository has been saved (for example, `C:\Users\Admin\git-projects\ChangeChargeLimit\`).

6. **Settings Tab**:
   - In the "Settings" tab:
     - Check the following fields:
       - "Allow task to be run on demand"
       - "Run task as soon as possible after a scheduled start is missed"
       - "If the task fails, restart every": Set this to 1 minute.
       - "Attempt to restart up to": Set this to 3.
       - "Stop the task if it runs longer than": Set this to 4 hours.
       - "If the running task does not end when requested, force it to stop."
       - Ensure that "If the task is already running, then the following rule applies" is set to "Do not start a new instance."

7. **Save and Exit**:
   - Click "OK" or "Save" to create the task with the specified settings.

8. Run the task once manually by right clicking on the newly created task and then clicking on "Run". Then click "Refresh" in the "Actions" panel on the right hand side.

With these configurations, the task will run the `main.py` script from your local Git repository every hour after a user logs on, ensuring that it has administrator privileges and handling task failures gracefully.

Make sure to review and adjust these settings as needed based on your specific use case and requirements.

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
