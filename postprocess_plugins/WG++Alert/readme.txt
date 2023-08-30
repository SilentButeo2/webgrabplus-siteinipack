Advance WG++ license expiry date email warning .. Jan Van Straaten, Sept 2023
V1.3  requires WG 5.2 (5.1.0.1 or higher)

Without commandline argument sends email 7 days before any license component expires

Commandline arguments :
  ? or help .. displays this
  number between 0 and 30 .. sets advance to that number of days
  (this number argument, if used, must be the first argument, 
     and can be combined with the following):
  force  .. ingnores days, sends email with the expiry dates
  test   .. sends a test email

How to use:
in WebGrab++.config.xml for all platforms: 
  <postprocess run="y" grab="y or n">dotnet WG++Alert.dll [?|help][number 0-30]|[force]|[test]</postprocess>
windows only :
  <postprocess run="y" grab="y or n">WG++Alert.exe [?|help][number 0-30]|[force]|[test]</postprocess>