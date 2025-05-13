# vocaroo-sniffer
Vocaroo Sniffer is a singular Python script which looks for valid Vocaroo.com links (compatible with its legacy URL system).

**You must be connected to the internet in order to run this script.**

**It is extremely unlikely that it'll find a valid link. Links expire if it's not been accessed for a few months.**

![image](https://github.com/user-attachments/assets/a5ec7a77-398b-4aaf-80c4-d0f900cdf69a)
## Features
- Scans URLs from its legacy and current URL systems.
  - Outputs clickable links.
- Easily usable in PyCharm and other IDEs.
- Specify how many attempts. The default value of attempts is 50.
- Specify how long to wait in seconds for each attempt. The default value of waiting is 3 to ensure accuracy.
## Dependencies
- pyppeteer 2.0.0
## Before Using
- Give it enough time to load the page, otherwise there will be false positives. It is generally recommended not to set the waiting value to less than 3 seconds. If your computer or your internet is slower at loading webpages, set it to higher.
- Please ensure you have Chrome installed. If not, change **EXECUTABLE_PATH** from its initial configuration to your browser's executable path, or install Chrome.
  - **Your browser must be Chromium-based, otherwise it won't work.**
## How it works
### Generation
The script generates **11 characters**, which matches Vocaroo's URL systems. On its new URL system, "1" is always at the start of it, which to the human eye it reads as 12 characters.
#### Post-Generation
If a valid Vocaroo.com is found, the Python script will create a new file called "**valid_links.txt**", essentially logging every valid Vocaroo.com link. It does this whilst the script is running, which means you don't need to close it.
#### URL Formats
- Current System: vocaroo.com/1**Ku8f1MGIBxt**
- Legacy System: vocaroo.com/**Ku8f1MGIBxt**
### Page Loading
The script will load generated vocaroo.com links. It scans for "*Sorry, the requested media could not be found. It may have expired or been deleted.*" via HTML code - if it sees that, it will automatically mark the link as **INVALID** otherwise if it can't then it will mark it as **VALID**.
