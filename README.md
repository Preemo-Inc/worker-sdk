# Preemo Worker SDK

## Manual Installations

### Homebrew

Download and install Homebrew from https://brew.sh/ and set it up for your environment.

## Scripted Installations

Run the following script to install widely used development dependencies:

```shell
worker-sdk$ ./setup.sh
```

### asdf

`asdf` is a tool version manager. It will use the nearest `.tool-versions` to your working directory to determine which versions of tools and language runtimes should be installed and used. `asdf` will keep poetry and python versions in sync.

To finish `asdf` setup, you will need to add some changes to your shell profile. **Follow the instructions here**: https://asdf-vm.com/guide/getting-started.html#_3-install-asdf

### Restart Shell

Once done, restart your shell so changes can take effect.

## Application Installations

### Visual Studio Code

Download and install Visual Studio Code from https://code.visualstudio.com/download.

#### Setup TODO Shortcut

To setup the TODO shortcut in VSCode:

1. Click `Code` > `Preferences` > `User Snippets`.
2. Select the global snippets file.
3. Copy and paste this into the existing object:
```
"TODO": {
  "prefix": "todo",
  "body": [
    "$LINE_COMMENT TODO(<your_email_address>, ${1:$CURRENT_MONTH}/${2:$CURRENT_DATE}/${3:$CURRENT_YEAR}): $0"
  ],
  "description": "Insert TODO comment with expected date of completion"
}
```
4. Replace `<your_email_address>` with your email address.
